import pipeline
from scripts import tester, performance_sampler, parser
from sklearn.pipeline import Pipeline
import numpy as np

category1_training = []
category1_test = []
category2_training = []
category2_test = []

category1_training_files = ['data/fake_news_train.txt']
category1_test_files = ['data/fake_news_test.txt']
category2_training_files = ['data/real_train.txt']
category2_test_files = ['data/real_test.txt']

parser.parse_txt_into_lists(category1_training_files,category1_training,"~_~")
parser.parse_txt_into_lists(category1_test_files,category1_test,"~_~")
parser.parse_txt_into_lists(category2_training_files,category2_training,"~_~")
parser.parse_txt_into_lists(category2_test_files,category2_test,"~_~")

# Target selection
sample_size = performance_sampler.ask_user_for_sample_size()
sample_data = performance_sampler.sample_data(sample_size, category1_training, category2_training)

category1_training_target = []
category1_test_target = []
category2_training_target = []
category2_test_target = []

for i in sample_data[0]:
    category1_training_target.append(0)
for i in sample_data[1]:
    category2_training_target.append(1)
for i in category1_test:
    category1_test_target.append(0)
for i in category2_test:
    category2_test_target.append(1)

training_data = sample_data[0] + sample_data[1]

test_data = category1_test + category2_test

training_target = category1_training_target + category2_training_target

test_target = category1_test_target + category2_test_target

text_clf = pipeline.classifier(training_data, training_target)

text_clf = text_clf.fit(training_data,training_target)
#
# predicted_test = tester.predict_with_test_data(text_clf,test_data)
# print("This is np mean accuracy for Naiive Bayes:")
# print(tester.mean_accuracy(predicted_test,test_target))
# print("this is the detailed accuracy table:")
# print(tester.detailed_accuracy(predicted_test,test_target,["Fake News","Solid Journalism"]))
