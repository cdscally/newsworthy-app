from collections import Counter
import re
lorem = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt."
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
print frequency_count(lorem)
