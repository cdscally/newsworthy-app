from scripts import tester, performance_sampler, parser
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# Create arrays to hold the article strings
category1_training = []
category1_test = []
category2_training = []
category2_test = []

# Gather the news sources
category1_training_files = ['./performance_testing/fake_news_train.txt']
category1_test_files = ['./performance_testing/fake_news_test.txt']
category2_training_files = ['./performance_testing/real_train.txt']
category2_test_files = ['./performance_testing/real_test.txt']

# Process strings into arrays
parser.parse_txt_into_lists(category1_training_files,category1_training,"~_~")
parser.parse_txt_into_lists(category1_test_files,category1_test,"~_~")
parser.parse_txt_into_lists(category2_training_files,category2_training,"~_~")
parser.parse_txt_into_lists(category2_test_files,category2_test,"~_~")

# Ask the user how much of the data should be used to train the algorithm. This is to try and show that larger amounts of training data should improve the result
sample_size = performance_sampler.ask_user_for_sample_size()
sample_data = performance_sampler.sample_data(sample_size, category1_training, category2_training)

# Generate arrays which hold corresponding binary values for categorisation
category1_training_target = []
category1_test_target = []
category2_training_target = []
category2_test_target = []

# Append 0/1 to the above arrays
for i in sample_data[0]:
    category1_training_target.append(0)
for i in sample_data[1]:
    category2_training_target.append(1)
for i in category1_test:
    category1_test_target.append(0)
for i in category2_test:
    category2_test_target.append(1)

# Brings together the above into four arrays
	# An array containing all training data
	# An array contianing the classification of training data
	# An array containing all test data
	# An array contianing the classiification of test data
training_data = sample_data[0] + sample_data[1]
test_data = category1_test + category2_test
training_target = category1_training_target + category2_training_target
test_target = category1_test_target + category2_test_target


# Transform data for model
text_clf = Pipeline([('vect', CountVectorizer()),
					 ('tfidf', TfidfTransformer()),
					 ('clf', MultinomialNB()),
])

SGD_text_clf = Pipeline([('vect', CountVectorizer()),
					 ('tfidf', TfidfTransformer()),
					 ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42)),
])

# Generate classification model
text_clf = text_clf.fit(training_data,training_target)
SGD_text_clf = SGD_text_clf.fit(training_data,training_target)

# Classify test data and test accuracy
predicted_test = tester.predict_with_test_data(text_clf,test_data)
print("This is np mean accuracy for Naiive Bayes:")
print(tester.mean_accuracy(predicted_test,test_target))
print("this is the detailed accuracy table:")
print(tester.detailed_accuracy(predicted_test,test_target,["Fake News","Solid Journalism"]))

SGD_predicted_test = tester.predict_with_test_data(SGD_text_clf,test_data)
print("This is np mean accuracy for Support Vector Machine:")
print(tester.mean_accuracy(SGD_predicted_test,test_target))
print("this is the detailed accuracy table:")
print(tester.detailed_accuracy(SGD_predicted_test,test_target,["Fake News","Solid Journalism"]))
