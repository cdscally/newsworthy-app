from collections import Counter
import re

test_articles = ["Lorem Lorem ipsum dolor sit amet, consectetuer adipiscing elit.", "consectetuer adipiscing elit Lorem some some extra bollocks"]
word_map = {}
word_frequency = []
total_word_frequency = {}

def map_words(string):
    words = __parse_string(string)
    i = 0
    while i < len(words):
        word_map[i] = words[i]
        i += 1
    return word_map

def counted_words(articles):
    for article in articles:
        map_words(article)
        word_frequency.append(Counter(__parse_string(article)))

def total_frequency_count(string):
    for article_count in word_frequency:
        for key in article_count:
            list_item = [word_map[i], counted_words(string)[i]]
            word_frequency.append(list_item)
    return word_frequency

def __parse_string(string):
    new_words = []
    for word in string.split():
        new_word = re.sub(r'[\W]', '', word)
        new_words.append(new_word)
    return new_words

counted_words(test_articles)
print ("---")
print (word_frequency)
print ("---")
print (word_map)
