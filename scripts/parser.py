def parse_txt_into_lists(category_files,category,splitter="~_~"):
    for file in category_files:
    	articles = open(file,'r').read().split(splitter)
    	for article in articles:
    		category.append(article)

def remove_too_short_articles(category):
    for article in category:
	       if len(article) < 50:
		             category.remove(article)
