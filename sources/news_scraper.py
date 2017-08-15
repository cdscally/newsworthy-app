import newspaper
import requests

sources = [#"https://apnews.com//",
#           "https://www.thetimes.co.uk/",
#           "http://www.telegraph.co.uk/",
        #    "https://www.theguardian.com/uk/",
          "http://www.independent.co.uk/",
          "http://www.theweek.co.uk/"
          ]
output = []
file_name = 'real_news.txt'

for source in sources:
    response = requests.get(source)

    if (response.status_code == 200):
        print("%s: %s" % (source, response))
        source_paper = newspaper.build(source, memoize_articles=False)
        number_of_articles = source_paper.articles
        for article in source_paper.articles:
            article_response = requests.get(article.url)
            if (article_response.status_code != 200):
                print('Article %s Error: --> continuing' % (article))
                continue
            else:
                print('%s - Article: %s' % (source, article.url))
                article.download()
                article.parse()
                output.append(article.text)
    else:
        print('Source Error --> continuing')
        continue

myfile =  open(file_name,'w')

for article in output:
  myfile.write(article)
  myfile.write('\n\n~_~\n\n')
  myfile.close
