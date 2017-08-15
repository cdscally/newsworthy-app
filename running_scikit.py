from scripts import tester, train_test_data_splitter, parser
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


category1 = []
category2 = []


category1_files = ['fake_combined.txt']
category2_files = ['real_combined.txt']

parser.parse_txt_into_lists(category1_files,category1,"~_~")
parser.parse_txt_into_lists(category2_files,category2,"~_~")


parser.remove_too_short_articles(category1)
parser.remove_too_short_articles(category2)

split = train_test_data_splitter.ask_user_for_split()
split_data = train_test_data_splitter.split_data(split, category1, category2)


category1_training_data = split_data[0][0]
category1_test_data = split_data[0][1]
category2_training_data = split_data[1][0]
category2_test_data = split_data[1][1]


category1_training_data_target = []
category1_test_data_target = []
category2_training_data_target = []
category2_test_data_target = []


for i in category1_training_data:
	category1_training_data_target.append(0)
for i in category1_test_data:
	category1_test_data_target.append(0)
for i in category2_training_data:
	category2_training_data_target.append(1)
for i in category2_test_data:
	category2_test_data_target.append(1)


training_data = category1_training_data + category2_training_data
training_target = category1_training_data_target + category2_training_data_target
test_data = category1_test_data + category2_test_data
test_target = category1_test_data_target + category2_test_data_target



text_clf = Pipeline([('vect', CountVectorizer()),
					 ('tfidf', TfidfTransformer()),
					 ('clf', MultinomialNB()),
])



text_clf = text_clf.fit(training_data,training_target)



input_string = input("Please paste the whole news story as one string: ")
print(input_string)
input_list = [input_string]
print(input_list)



predicted = text_clf.predict(input_list)
if predicted == 0:
    print("Fake News")
else:
    print("Real News")



predicted_test = tester.predict_with_test_data(text_clf,test_data)
print("This is np mean accuracy:")
print(tester.mean_accuracy(predicted_test,test_target))
print("this is the detailed accuracy table:")
print(tester.detailed_accuracy(predicted_test,test_target,["Fake News","Solid Journalism"]))
