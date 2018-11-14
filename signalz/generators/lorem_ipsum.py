"""
.. versionadded:: 0.7

This function produces Lorem Ipsum - a placeholder text.

More information can be found at https://en.wikipedia.org/wiki/Lorem_ipsum

Example Usage
===============

Note: the output of Lorem Ipsum is random, thus you can see a slightly different output on your machine.

One sentence with 10 words:

.. code-block:: python

    >>> signalz.lorem_ipsum.get_sentence(words=10)
    Ultrices pulvinar nisl fringilla laoreet nostra eget enim elementum nibh.

One sentence with custom dictionary:

.. code-block:: python

    >>> d = ["mouse", "rat", "shark", "sheep", "cat", "dog"]
    >>> signalz.lorem_ipsum.get_sentence(dictionary=d)
    Shark mouse sheep mouse rat cat dog.


One sentence created with included english dictionary:

.. code-block:: python

    >>> d = ["mouse", "rat", "shark", "sheep", "cat", "dog"]
    >>> signalz.lorem_ipsum.get_sentence(dictionary=d)
    Went how here give after give there.

Text (one paragraph) with 50 words.

.. code-block:: python

    content = signalz.lorem_ipsum.get_text(words=50)


Text (one paragraph) with 50 words and custom sentence size - note that the last
sentence can have less words to match the given `words` count:

.. code-block:: python

    content = signalz.lorem_ipsum.get_text(words=50, words_per_sentence=4)

Text with paragraphs:

.. code-block:: python

    content = signalz.lorem_ipsum.get_paragraphs()

Fully customized text with paragraphs:

.. code-block:: python

    content = signalz.lorem_ipsum.get_paragraphs(words=1000, paragraphs=3, words_per_sentence=5, dictionary=my_custom_list_of_words)


Function Documentation
======================================
"""
import numpy as np

ENGLISH_WORDS = ("a", "about", "all", "also", "and", "because", "but", "by", "generators", "come", "could",
    "day", "do", "even", "find", "first", "for", "from", "get", "give", "go", "have", "he","her", "here", "him", "his",
    "how", "if", "documentation", "into", "it", "its", "just", "know", "like", "look", "make", "man", "many", "me", "more",
    "my", "distribution", "no", "not", "now", "of", "on", "one", "only", "or", "other", "our", "out", "people", "say", "see",
    "she", "so", "some", "take", "tell", "than", "that", "the", "their", "them", "then", "there", "these", "they", "thing",
    "think", "this", "those", "time", "to", "use", "very", "want", "approximately", "sufficient", "producer", "dictionary",
    "who", "will", "with", "would", "year", "you", "your", "new", "great", "put", "kind", "sound", "where", "and", "hand",
    "take", "help", "does", "picture", "only", "through", "another", "again", "little", "much", "well", "change", "work",
    "before", "large", "off", "know", "line", "must", "play", "place", "right", "big", "spell", "year", "too", "even", "air",
    "live", "mean", "such", "away", "me", "old", "because", "animal", "back", "any", "turn", "house", "give", "same", "here",
    "point", "most", "tell", "why", "page", "very", "boy", "installed", "letter", "after", "follow", "went", "mother", "thing",
    "came", "men", "answer", "our", "want", "read", "found", "just", "show", "need", "study", "name", "also", "land", "still",
    "good", "around", "different", "learn", "sentence", "form", "home", "should", "man", "three", "us", "America", "think",
    "small", "move", "world", "say", "set", "try", "high")

STANDARD_WORDS = (
    'enim', 'magna', 'quis', 'vel', 'lorem', 'litora', 'quam', 'id', 'viverra', 'dui', 'varius', 'aliquam', 'phasellus',
    'ornare', 'urna', 'conubia', 'suspendisse', 'consectetur', 'tempus', 'hac', 'natoque', 'est', 'parturient', 'condimentum',
    'sodales', 'eu', 'scelerisque', 'lacus', 'in', 'rutrum', 'turpis', 'consequat', 'aenean', 'posuere', 'pellentesque',
    'sociosqu', 'finibus', 'inceptos', 'facilisis', 'ullamcorper', 'ex', 'dis', 'magnis', 'libero', 'lacinia', 'quisque',
    'curabitur', 'augue', 'ut', 'sapien', 'massa', 'ante', 'nec', 'ridiculus', 'arcu', 'torquent', 'sollicitudin', 'cras',
    'purus', 'vulputate', 'interdum', 'pharetra', 'cursus', 'pulvinar', 'rhoncus', 'bibendum', 'sem', 'eros', 'blandit', 'nam',
    'hendrerit', 'proin', 'ac', 'laoreet', 'eget', 'et', 'sagittis', 'convallis', 'platea', 'orci', 'habitasse', 'neque',
    'metus', 'congue', 'dictum', 'nisl', 'a', 'mollis', 'dignissim', 'elementum', 'fames', 'tellus', 'etiam', 'non', 'vivamus',
    'nisi', 'penatibus', 'mi', 'nulla', 'eleifend', 'gravida', 'dictumst', 'mauris', 'praesent', 'lobortis', 'volutpat',
    'erat', 'integer', 'suscipit', 'auctor', 'imperdiet', 'nunc', 'adipiscing', 'nibh', 'porttitor', 'malesuada', 'ultrices',
    'sed', 'nascetur', 'donec', 'vitae', 'venenatis', 'taciti', 'maximus', 'justo', 'dapibus', 'tristique', 'commodo', 'luctus',
    'morbi', 'aptent', 'nostra', 'dolor', 'ligula', 'primis', 'lectus', 'vehicula', 'aliquet', 'feugiat', 'montes', 'fermentum',
    'fringilla', 'ad', 'molestie', 'egestas', 'tincidunt', 'faucibus', 'odio', 'felis', 'diam', 'mus', 'euismod', 'efficitur',
    'amet', 'tempor', 'himenaeos', 'placerat', 'accumsan', 'risus', 'tortor', 'ultricies', 'ipsum', 'pretium', 'at', 'elit',
    'class', 'sit', 'leo', 'per')

def get_dictionary(dictionary):
    """
    This function checks what word list is desired for Lorem Ipsum.

    Kwargs:

    * `dictionary` : options are:
        * "english" (str) for english words,
        * "standard" (str) for latin words,
        * any list obtaining strings (list) - for custom words

    Returns:

    * list of words
    """
    if type(dictionary) == str:
        if dictionary == "english":
            return ENGLISH_WORDS
        elif dictionary == "standard":
            return STANDARD_WORDS
        else:
            raise Exception('Provided Lorem Ipsum dictionary is not known')
    else:
        return dictionary
    

def get_sentence(words=7, dictionary="standard"):
    """
    This function returns one sentence of lorem ipsum.

    Kwargs:

    * `words` : number of desired words

    * `dictionary` : options are:
        * "english" (str) for english words,
        * "standard" (str) for latin words,
        * any list obtaining strings (list) - for custom words

    Returns:

    * sentence (str)
    """
    dictionary = get_dictionary(dictionary)
    sentence = list(np.random.choice(dictionary, words))
    return " ".join(sentence).capitalize() + "."

def get_text(words=150, words_per_sentence=7, dictionary="standard"):
    """
    This function generates text (paragraph).
    Last sentence can be shorter than requested if there is not enough words left.

    Kwargs:

    * `words` : number of desired words

    * `words_per_sentence` : prefered number of words in sentence

    * `dictionary` : options are:
        * "english" (str) for english words,
        * "standard" (str) for latin words,
        * any list obtaining strings (list) - for custom words

    Returns:

    * text made of multiple sentences (str)
    """
    dictionary = get_dictionary(dictionary)
    lenghts = (words_per_sentence, ) * (words // words_per_sentence) + (words % words_per_sentence, )
    list_of_sentences = [get_sentence(words=x, dictionary=dictionary) for x in lenghts]
    return " ".join(list_of_sentences)

def get_paragraphs(words=300, paragraphs=5, words_per_sentence=7, dictionary="standard"):
    """
    This function generates text with multiple paragraphs (newlines).
    The total number of words is divided between paragraphs as evenly as possible.

    Kwargs:

    * `words` : number of desired words

    * `paragraphs` : number of desired paragraphs

    * `words_per_sentence` : prefered number of words in sentence

    * `dictionary` : options are:
        * "english" (str) for english words,
        * "standard" (str) for latin words,
        * any list obtaining strings (list) - for custom words

    Returns:

    * text made of multiple sentences (str)
    """
    dictionary = get_dictionary(dictionary)
    lenghts = (words // paragraphs, ) * paragraphs
    if words % paragraphs:
        lenghts = [lenghts[_] + 1 if _ < words % paragraphs else lenghts[_] for _ in range(paragraphs)]
    texts = [get_text(words=x, words_per_sentence=words_per_sentence, dictionary=dictionary) for x in lenghts]
    return "\n".join(texts)





