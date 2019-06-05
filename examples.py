import signalz

# content = signalz.lorem_ipsum.get_sentence(words=10)


# d = ["mouse", "rat", "shark", "sheep", "cat", "dog"]
# content = signalz.lorem_ipsum.get_sentence(dictionary=d)

# # content = signalz.lorem_ipsum.get_text()

# content = signalz.lorem_ipsum.get_text(words=50, words_per_sentence=4)

# content = signalz.lorem_ipsum.get_paragraphs()


# content = signalz.lorem_ipsum.get_sentence(dictionary="english")


# print(content)

# my_deck = ["A1", "A2", "B1", "B2"]
# cards = signalz.card_dealer(2, deck=my_deck)
#
# print(cards)



# import random


# OPTIONS = {
#     "Visa": {
#         "prefix": "4",
#         "length": 16,
#     }
# }



# def get_credit_card_number(brand="Visa"):
#     n = 10
#     digits = [random.choice(range(10)) for _ in range(n-1)] + [0]
#     odd_sum = sum(digits[-1::-2])
#     even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
#     checksum_digit = (10 - (odd_sum + even_sum) % 10) % 10
#     all_digits = digits[:-1] + [checksum_digit]
#     cc "".join([str(_) for _ in all_digits])



# def checksum(string):
#     """
#     Compute the Luhn checksum for the provided string of digits. Note this
#     assumes the check digit is in place.
#     """
#     digits = list(map(int, string))
#     odd_sum = sum(digits[-1::-2])
#     even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
#     return (odd_sum + even_sum) % 10

# def verify(string):
#     """
#     Check if the provided string of digits satisfies the Luhn checksum.
#     >>> verify('356938035643809')
#     True
#     >>> verify('534618613411236')
#     False
#     """
#     return (checksum(string) == 0)

# def generate(string):
#     """
#     Generate the Luhn check digit to append to the provided string.
#     >>> generate('35693803564380')
#     9
#     >>> generate('53461861341123')
#     4
#     """
#     cksum = checksum(string + '0')
#     return (10 - cksum) % 10




# print(verify(cc))




