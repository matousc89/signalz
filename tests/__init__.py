import unittest
import sys
import numpy as np

sys.path.append('..')
import signalz

class TestFunctions(unittest.TestCase):

    def test_autoregressive_model(self):
        np.random.seed(101)
        a = [-0.41, 1.27, -1.85, 1.79]
        N = 1000
        x = signalz.autoregressive_model(N, a, noise="white")
        self.assertAlmostEqual(x.sum(), 105.196, places=3)

    def test_gaussian_white_noise(self):
        np.random.seed(101)
        N = 1000
        x = signalz.gaussian_white_noise(N, 1, 1)
        self.assertAlmostEqual(x.sum(), 1026.433, places=3)
    
    def test_uniform_white_noise(self):
        np.random.seed(101)
        N = 10000
        x = signalz.uniform_white_noise(N, minimum=5, maximum=15)
        self.assertAlmostEqual(x.mean(), 10, places=1)
    
    def test_brownian_noise(self):
        np.random.seed(101)
        N = 10000
        x = signalz.brownian_noise(N, leak=0.5, std=5, source="uniform")
        self.assertAlmostEqual(x.mean(), 0, places=1)
    
    def test_mackey_glass(self):
        np.random.seed(101)
        N = 1000
        x = signalz.mackey_glass(N, a=0.2, b=0.8, c=0.9,
            d=23, e=10, initial=0.1)
        self.assertAlmostEqual(x.sum(), 845.613, places=3)
        
    def test_sinus(self):
        """
        First value should be one if the offset is 25% of period.
        """
        N = 200
        x = signalz.sinus(N, period=100, delay=25)
        self.assertEqual(x[0], 1.)
        
    def test_cosinus(self):
        """
        First value should be 1, if the ofset is 0.
        """
        N = 200
        x = signalz.cosinus(N, period=100, delay=0)
        self.assertEqual(x[0], 1.)
        
    def test_logistic_map(self):
        x = signalz.logistic_map(50, r=3)
        self.assertAlmostEqual(x.sum(), 33.04268063384672)
        
    def test_levy_noise(self):
        np.random.seed(101)
        x = signalz.levy_noise(1000, alpha=1.5, beta=0.5, sigma=1., position=-2)
        self.assertAlmostEqual(x.sum(), -1716.38225692)
        
    def test_levy_walk(self):
        np.random.seed(101)
        x = signalz.levy_walk(1000, ns=100, alpha=1.5,
            beta=0.5, sigma=1., position=-2)            
        self.assertAlmostEqual(x.sum(), -102548.26745083061, 4)
        
    def test_levy_flight(self):
        np.random.seed(101)
        x = signalz.levy_flight(1000, alpha=1.5,
            beta=0.5, sigma=1., position=-2)            
        self.assertAlmostEqual(x.sum(), -1002644.5419602607, 4)
        
    def test_lorem_ipsum_get_sentence(self):
        """
        Function should return string.
        The function output should contain given number of words.
        """
        out = signalz.lorem_ipsum.get_sentence(words=10)
        count = len(out.split(" "))
        self.assertIs(type(out), str)
        self.assertEqual(count, 10)
        
    def test_lorem_ipsum_get_text(self):
        """
        Function should return string.
        The function output should contain given number of words.
        """
        out = signalz.lorem_ipsum.get_text(words=30)
        count = len(out.split(" "))
        self.assertIs(type(out), str)
        self.assertEqual(count, 30)
        
    def test_lorem_ipsum_get_paragraphs(self):
        """
        Function should return string.
        The function output should contain given number of words.
        the function output should contane given number of newlines (paragraphs).
        """
        out = signalz.lorem_ipsum.get_paragraphs(words=123, paragraphs=3)
        count = len(out.replace("\n", " ").split(" "))
        newlines_count = out.count("\n")
        self.assertIs(type(out), str)
        self.assertEqual(count, 123)
        self.assertEqual(newlines_count, 3-1)

    def test_card_dealer_output_size(self):
        """
        Check if the output has a correct size.
        """
        x, y = 2, 3
        data = signalz.card_dealer(y, x, deck="standard+wild", decks_number=1)
        self.assertEqual(len(data), x)
        self.assertEqual(len(data[0]), y)


