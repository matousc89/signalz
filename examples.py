import signalz

content = signalz.lorem_ipsum.get_sentence(words=10)


d = ["mouse", "rat", "shark", "sheep", "cat", "dog"]
content = signalz.lorem_ipsum.get_sentence(dictionary=d)

# content = signalz.lorem_ipsum.get_text()

content = signalz.lorem_ipsum.get_text(words=50, words_per_sentence=4)

content = signalz.lorem_ipsum.get_paragraphs()


content = signalz.lorem_ipsum.get_sentence(dictionary="english")


print(content)