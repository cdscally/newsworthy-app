import newspaper

guardian = newspaper.build('https://www.theguardian.com/uk/sport', memoize_articles=False)

# # for category in bbc.category_urls():
# # 	print(category)

# print(bbc.category_urls()[2].articles)

# # for feed_url in bbc.feed_urls():
# # 	print(feed_url)

output = []
urls = []
print(guardian.articles)

for article in guardian.articles:
	if "/sport/" in article.url:
		urls.append(article.url)
		article.download()
		article.parse()
		output.append(article.text)

print(urls)


myfile =  open('guardian_sport.txt', 'w')
for article in output:
  myfile.write(article)
  myfile.write('\n')
  myfile.write('\n')
  myfile.write('ColinColin')
  myfile.write('\n')
  myfile.write('\n')

myfile.close
