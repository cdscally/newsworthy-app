from scripts import tester, performance_sampler, parser
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

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
category2_training_target = []

for i in sample_data[0]:
    category1_training_target.append(0)
for i in sample_data[1]:
    category2_training_target.append(1)

training_data = sample_data[0] + sample_data[1]

training_target = category1_training_target + category2_training_target

print(training_target)
print(len(training_data))
print(len(training_target))
