from scripts import tester, performance_sampler, parser
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
import own_algorithm

category1_training = []
category1_test = []
category2_training = []
category2_test = []

category1_training_files = ['fake_news_train.txt']
category1_test_files = ['fake_news_test.txt']
category2_training_files = ['real_train.txt']
category2_test_files = ['real_test.txt']

parser.parse_txt_into_lists(category1_training_files,category1_training,"~_~")
parser.parse_txt_into_lists(category1_test_files,category1_test,"~_~")
parser.parse_txt_into_lists(category2_training_files,category2_training,"~_~")
parser.parse_txt_into_lists(category2_test_files,category2_test,"~_~")

sample_size = performance_sampler.ask_user_for_sample_size()
sample_data = performance_sampler.sample_data(sample_size, category1_training, category2_training)

category1_training_target = []
category1_test_target = []
category2_training_target = []
category2_test_target = []

for i in sample_data[0]:
    category1_training_target.append(-1)
for i in sample_data[1]:
    category2_training_target.append(1)
for i in category1_test:
    category1_test_target.append(-1)
for i in category2_test:
    category2_test_target.append(1)

training_data = sample_data[0] + sample_data[1]
test_data = category1_test + category2_test

training_target = category1_training_target + category2_training_target
test_target = category1_test_target + category2_test_target

#Training data
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(training_data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf_array = X_train_tfidf.toarray()

#Test data
X_test_counts = count_vect.transform(test_data)

X_test_tfidf = tfidf_transformer.transform(X_test_counts)
X_test_tfidf_array = X_test_tfidf.toarray()


predicted = own_algorithm.classify_multiple_vectors(X_train_tfidf_array, X_test_tfidf_array, training_target))

tester.mean_accuracy(predicted, test_target)





#
#
# text_clf = Pipeline([('vect', CountVectorizer()),
# 					 ('tfidf', TfidfTransformer()),
# 					 ('clf', MultinomialNB()),
# ])
#
# SGD_text_clf = Pipeline([('vect', CountVectorizer()),
# 					 ('tfidf', TfidfTransformer()),
# 					 ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42)),
# ])
#
#
# text_clf = text_clf.fit(training_data,training_target)
# SGD_text_clf = SGD_text_clf.fit(training_data,training_target)
#


# predicted_test = tester.predict_with_test_data(text_clf,test_data)
# print("This is np mean accuracy for Naiive Bayes:")
# print(tester.mean_accuracy(predicted_test,test_target))
# print("this is the detailed accuracy table:")
# print(tester.detailed_accuracy(predicted_test,test_target,["Fake News","Solid Journalism"]))
#
# SGD_predicted_test = tester.predict_with_test_data(SGD_text_clf,test_data)
# print("This is np mean accuracy for Support Vector Machine:")
# print(tester.mean_accuracy(SGD_predicted_test,test_target))
# print("this is the detailed accuracy table:")
# print(tester.detailed_accuracy(SGD_predicted_test,test_target,["Fake News","Solid Journalism"]))
