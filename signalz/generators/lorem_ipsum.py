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

DICTIONARY_DEFAULT = ENGLISH_WORDS

def get_sentence(words=7, dictionary=DICTIONARY_DEFAULT):
    sentence = list(np.random.choice(dictionary, words))
    return " ".join(sentence).capitalize() + "."

# def get_paragraph(sentences=5, words_per_sentence=False)
#     if words_per_sentence:
#         for sentence in words





