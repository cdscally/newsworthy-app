from collections import Counter
import re

articles = ["Lorem Lorem ipsum dolor sit amet, consectetuer adipiscing elit.", "consectetuer adipiscing elit Lorem some some extra bollocks"]
word_library = {}
all_article_frequencies_table = []

def word_frequencies(string):
    return Counter(__parse_string(string))

def article_frequencies(word_frequencies):
    article_frequencies = []
    for word in word_library:
        article_frequencies.append(__already_in_word_library(word, word_frequencies))
    return article_frequencies

def all_articles_word_frequency_table(article_list):
    __build_word_library(article_list)
    for article in article_list:
        all_article_frequencies_table.append(article_frequencies(word_frequencies(article)))
    return all_article_frequencies_table

# Private methods

def __build_word_library(article_list):
    for article in article_list:
        __map_words_to_library(article)

def __map_words_to_library(string):
    words = __parse_string(string)
    i = 0
    while i < len(words):
        word_library[words[i]] = i
        i += 1
    return word_library

def __parse_string(string):
    new_words = []
    for word in string.split():
        new_word = re.sub(r'[\W]', '', word)
        new_words.append(new_word)
    return new_words

def __already_in_word_library(word, word_frequencies):
    if word in word_frequencies:
        return word_frequencies[word]
    else:
        return 0


print all_articles_word_frequency_table(articles)
