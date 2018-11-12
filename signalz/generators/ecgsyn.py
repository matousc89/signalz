"""
.. versionadded:: 0.6

This functions produces a synthesized ECG signal. User can control following
parameters: mean heart rate, number of beats, sampling frequency,
waveform morphology (P, Q, R, S, and T timing, amplitude,and duration),
standard deviation of the RR interval, LF/HF ratio.

Copyright (c) 2003 by Patrick McSharry & Gari Clifford, All Rights Reserved 
:cite:`mcsharry2003dynamical`.

More information can be found in PhysionNet https://www.physionet.org/physiotools/ecgsyn/

Example Usage
===============

Simple example follows

.. code-block:: python

    x, peaks = ecgsyn(n=10, hrmean=50, hrstd=3, sfecg=128)
    
The returned variable `x` contains the synthetic ECG series.   

References
============

.. bibliography:: ecgsyn.bib
    :style: plain

Function Documentation
======================================
"""
import numpy as np

from signalz.misc import check_type_or_raise, ode45, rem

def derfunc(t, x, rr, sfint, ti, ai, bi):
    """
    Derivations of the ECG function.
    """
    xi = np.cos(ti)
    yi = np.sin(ti)
    ta = np.arctan2(x[1], x[0])
    r0 = 1.
    a0 = 1. - np.sqrt((x[0]**2) + (x[1]**2)) / r0
    ip = int(np.floor(t * sfint))
    w0 = 2. * np.pi / rr[ip]
    fresp = 0.25
    zbase = 0.005 * np.sin(2 * np.pi * fresp * t)
    dx1dt = a0*x[0] - w0*x[1]
    dx2dt = a0*x[1] + w0*x[0]
    dti = rem(ta - ti, 2. * np.pi) 
    dx3dt = - np.sum(ai * dti * np.exp(-0.5*(dti / bi)**2)) - (x[2] - zbase)
    return np.array([dx1dt, dx2dt, dx3dt])

def rrprocess(flo, fhi, flostd, fhistd, lfhfratio, hrmean, hrstd, sfrr, n):
    w1 = 2. * np.pi * flo
    w2 = 2. * np.pi * fhi
    c1 = 2. * np.pi * flostd
    c2 = 2. * np.pi * fhistd
    sig2 = 1
    sig1 = lfhfratio
    rrmean = 60 / hrmean
    rrstd = 60 * hrstd / float(hrmean * hrmean)
    df = sfrr / float(n)
    w = np.arange(0,n) * 2 * np.pi * df 
    dw1 = w - w1
    dw2 = w - w2
    Hw1 = sig1 * np.exp(-0.5 * (dw1 / c1)**2) / np.sqrt(2.*np.pi*c1**2)
    Hw2 = sig2 * np.exp(-0.5 * (dw2 / c2)**2) / np.sqrt(2.*np.pi*c2**2)
    Hw = Hw1 + Hw2
    Hw0 = np.concatenate([Hw[0:int(n/2)], Hw[int(n/2):0:-1]])
    Sw = (sfrr / 2.) * np.sqrt(Hw0)
    ph0 = 2 * np.pi * np.random.uniform(0, 1, int(n/2)-1)
    ph = np.concatenate([[0], ph0, [0], -np.flipud(ph0)])
    SwC = Sw * np.exp(ph*1j)
    x = (1 / float(n)) * np.real(np.fft.ifft(SwC))
    xstd = np.std(x)
    ratio = rrstd / float(xstd)
    return rrmean + x * ratio

def annotate_peaks(x, thetap, sfecg):
    """
    This function annotates PQRST peaks (P=1, Q=2, R=3, S=4, T=5).
    """
    # find rough positions of peaks
    n = len(x)
    irpeaks = np.zeros(n)
    theta = np.arctan2(x[:,1], x[:,0])
    ind0 = np.zeros(n)
    for i in range(0, n-1):
        a = (theta[i] <= thetap) & (thetap <= theta[i+1])
        j = np.where(a==1)[0]
        if len(j) > 0:
            d1 = thetap[j] - theta[i]
            d2 = theta[i+1] - thetap[j]
            if d1[0] < d2[0]:
                ind0[i] = j[0]+1
            else:
                ind0[i+1] = j[0]+1
    # shift the peaks to correct position
    ind = np.zeros(n)
    z = x[:,2]
    extrema = np.array([np.argmax, np.argmin, np.argmax, np.argmin, np.argmax])
    for i in range(0,5):
        ind1 = np.where(ind0==i+1)[0]
        for j in ind1:
            if j:
                surrounding = z[j-3:j+3]
                correction = extrema[i](surrounding)
                ind[j-3+correction] = i+1
    return ind
   
def ecgsyn(sfecg=256, n=256, hrmean=60., hrstd=1,
        lfhfratio=0.5, sfint=512, ti=[-70, -15, 0, 15, 100],
        ai=[1.2, -5, 30, -7.5, 0.75], bi=[0.25, 0.1, 0.1, 0.1, 0.4]):
    """
    ECGSYN - realistic ecg generator.

    Kwargs:

    * `sfecg` : ECG sampling frequency (int), it Hz

    * `N` : approaximate number of heart beats (int)

    * `hrmean` : mean heart rate (float) in beats per minute

    * `hrstd` : standard deviation of heart rate (float) in beats per minute

    * 'lfhfration : LF/HF ratio (float)

    * `sfint` : internal sampling frequency (int) in Hz

    * `ti` : angles of PQRST extrema (1d array of size 5) in degrees

    * `ai` : z-position of PQRST extrema (1d array of size 5)

    * `bi` : Gaussian width of peaks (1d array of size 5)
        
    Returns:

    * `x` : ECG values in mV
    
    * `peaks`: labels for PQRST peaks (P=1, Q=2, R=3, S=4, T=5 and 0 elsewhere)
    
    """
    # check data types
    check_type_or_raise(sfecg, int, "sfecg")
    check_type_or_raise(n, int, "sfecg")
    check_type_or_raise(sfint, int, "sfint")
    # data cleaning
    ti = np.array(ti)
    hrmean = float(hrmean)
    ti = ti * np.pi / 180.
    ai = np.array(ai)
    bi = np.array(bi)
    # adjust extrema parameters for mean heart rate 
    hrfact =  np.sqrt(hrmean / 60.)
    hrfact2 = np.sqrt(hrfact)
    bi = hrfact * bi
    ti = np.array([hrfact2, hrfact, 1, hrfact, hrfact2]) * ti
    # check that sfint is an integer multiple of sfecg
    if sfint % sfecg != 0 or sfint < sfecg:        
        raise ValueError("Sfint must be an integer multiple of sfecg")
    # define frequency parameters for rr process, flo and fhi correspond
    # to the Mayer waves and respiratory rate respectively
    flo = 0.1
    fhi = 0.25
    flostd = 0.01
    fhistd = 0.01
    # calculate time scales for rr and total output
    sampfreqrr = 1
    trr = 1 / float(sampfreqrr) 
    tstep = 1 / float(sfecg)
    rrmean = 60 / hrmean	 
    Nrr = 2**(np.ceil(np.log2(n * rrmean / trr)))
    # compute rr process
    rr0 = rrprocess(flo, fhi, flostd, fhistd, lfhfratio, hrmean, hrstd, 
        sampfreqrr, Nrr)
    # upsample rr time series from 1 Hz to sfint Hz
    rrlin = np.arange(0, len(rr0)*sfint) / float(sfint) # upsample
    rr = np.interp(rrlin, np.arange(0, len(rr0)), rr0) # upsample
    # make the rrn time series
    dt = 1 / float(sfint)
    rrn = np.zeros(len(rr))
    tecg = 0
    i = 0
    while i <= len(rr):
       tecg = tecg + rr[i]
       ip = int(np.round(tecg / dt))
       rrn[i:ip+1] = rr[i] #+1?
       i = ip+1
    Nt = ip
    # integrate system using fourth order Runge-Kutta
    x0 = np.array([1,0,0.04])
    Tspan = np.arange(0, (Nt-1)*dt, dt)
    Tspan = Tspan[:len(rrn)]
    z = ode45(derfunc, Tspan, x0, rrn, sfint, ti, ai, bi)
    # resample (downsample)
    resample_factor = int(sfint / sfecg)
    x = z[::resample_factor]
    # annotate peaks
    ipeaks = annotate_peaks(x, ti, sfecg)
    # Scale signal to lie between -0.4 and 1.2 mV
    x = x[:,2]
    zmin = x.min()
    zmax = x.max()
    zrange = zmax - zmin
    out = (x - zmin) * 1.6 / zrange - 0.4
    return out, ipeaks

if __name__ == "__main__":
    x, peaks = ecgsyn(n=10, hrmean=50, hrstd=3, sfecg=128)
