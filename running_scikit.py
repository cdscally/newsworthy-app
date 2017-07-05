sport = []
rest = []

sport_files = ['news_parse/guardian_sport.txt']
rest_files = ['news_parse/guardian_politics.txt', 'news_parse/guardian_business.txt', 'news_parse/guardian_world.txt', 'news_parse/bbc_world.txt', 'news_parse/guardian_technology.txt', 'news_parse/wapo_politics.txt', 'news_parse/wapo_business.txt', 'news_parse/bbc_ukpolitics.txt']


for file in sport_files:
	articles = open(file,'r').read().split('~~')
	for article in articles:
		sport.append(article)

for file in rest_files:
	articles = open(file,'r').read().split('ColinColin')
	for article in articles:
		rest.append(article)

for article in sport:
	if len(article) < 50:
		sport.remove(article)

for article in rest:
	if len(article) < 50:
		rest.remove(article)

sport_target=[]
for i in sport:
	sport_target.append(0)

rest_target=[]
for i in rest:
	sport_target.append(1)

data = sport + rest
target = sport_target + rest_target

print(target)
print(len(data))
print(len(target))

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(data)
print(X_train_counts.shape)

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, target)

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

import numpy as np
print(np.mean(predicted == target))
print(sum(target)/len(target))
