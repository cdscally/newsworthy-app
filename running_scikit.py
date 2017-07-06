from scripts import tester
from scripts import train_test_data_splitter

category1 = []
category2 = []

category1_files = ['news_parse/guardian_sport.txt']
category2_files = ['news_parse/guardian_politics.txt', 'news_parse/guardian_business.txt', 'news_parse/guardian_world.txt', 'news_parse/bbc_world.txt', 'news_parse/guardian_technology.txt', 'news_parse/wapo_politics.txt', 'news_parse/wapo_business.txt', 'news_parse/bbc_ukpolitics.txt']


for file in category1_files:
	articles = open(file,'r').read().split('~~')
	for article in articles:
		category1.append(article)

for file in category2_files:
	articles = open(file,'r').read().split('ColinColin')
	for article in articles:
		category2.append(article)

for article in category1:
	if len(article) < 50:
		category1.remove(article)

for article in category2:
	if len(article) < 50:
		category2.remove(article)

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


category1_target=[]
for i in category1:
	category1_target.append(0)

category2_target=[]
for i in category2:
	category1_target.append(1)

training_data = category1_training_data + category2_training_data
training_target = category1_training_data_target + category2_training_data_target



print(training_target)
print(len(training_data))
print(len(training_target))

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(training_data)
print(X_train_counts.shape)

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, training_target)

input_string = input("Please paste the whole news story as one string: ")
print(input_string)
input_list = [input_string]
print(input_list)
X_new_counts = count_vect.transform(input_list)
print(X_new_counts.shape)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
print(X_new_tfidf.shape)

predicted = clf.predict(X_new_tfidf)
if predicted == 0:
    print("Sports")
else:
    print("Something else")
