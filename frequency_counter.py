from collections import Counter
import re

articles = ["Lorem Lorem ipsum dolor sit amet, consectetuer adipiscing elit.", "consectetuer adipiscing elit Lorem some some extra bollocks"]
word_map = {}
word_frequency = []

def map_words(string):
    words = __parse_string(string)
    i = 0
    while i < len(words):
        word_map[words[i]] = i
        i += 1
    return word_map

def counted_words(string):
    return Counter(__parse_string(string))

def build_table(article_list):
    master_list = []
    for article in article_list:
        map_words(article)

    for article in article_list:
        word_frequencies = counted_words(article)
        article_frequencies = []
        for key in word_map:
            if key in word_frequencies:
                article_frequencies.append(word_frequencies[key])
            else:
                article_frequencies.append(0)
        master_list.append(article_frequencies)
    return master_list
    print "----"

def frequency_count(string):
    map_words(string)
    i = 0
    for i in counted_words(string):
        list_item = [word_map[i], counted_words(string)[i]]
        word_frequency.append(list_item)
    return word_frequency

def __parse_string(string):
    new_words = []
    for word in string.split():
        new_word = re.sub(r'[\W]', '', word)
        new_words.append(new_word)
    return new_words

print build_table(articles)
