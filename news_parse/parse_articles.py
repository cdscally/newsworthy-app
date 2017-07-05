sport = []
rest = []

sport_files = ['guardian_sport.txt']
rest_files = ['guardian_politics.txt', 'guardian_business.txt', 'guardian_world.txt', 'bbc_world.txt', 'guardian_technology.txt', 'wapo_politics.txt', 'wapo_business.txt', 'bbc_ukpolitics.txt']


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