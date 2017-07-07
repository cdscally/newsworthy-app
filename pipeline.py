from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import frequency_counter

def sparse_frequencies(training_data):
    sparse_data = CountVectorizer().fit_transform(training_data)
    print(sparse_data.shape)
    return sparse_data
    # return frequency_counter.sparse_frequency(training_data)

def tf_transformer(training_data):
    transformed = TfidfTransformer().fit_transform(sparse_frequencies(training_data))
    print(transformed.shape)
    return transformed


def classifier(training_data, training_target):
    return MultinomialNB().fit(tf_transformer(training_data), training_target)
