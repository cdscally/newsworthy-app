import newspaper
import requests

sources = ["http://www.snopes.com/tag/fake-news/",
           "https://www.infowars.com/news/",
           "http://nationalreport.net/",
           "http://bizstandardnews.com/",
           "http://abcnews.com.co",
           "http://www.YourNewsWire.com",
           "http://www.Now8News.com",
           "http://www.naturalnews.com",
           "http://www.Bloomberg.ma",
           "http://www.NBCNews.com.co"
          ]
output = []

for source in sources:
    response = requests.get(source)

    if (response.status_code == 200):
        print("%s: %s" % (source, response))
        source_paper = newspaper.build(source, memoize_articles=False)
        a = len(source.articles)
        for article in source_paper.articles:
            print(a)
            # article_response = requests.get(article.url)
            # if (article_response.status_code != 200):
            #     print('Article %s Error --> continuing' % (a))
            #     continue
            # else:
            #     print('%s - Article %s: %s' % (source, a, article)
            #     article.download()
            #     article.parse()
            #     output.append(article.text)
            # a -= 1
    else:
        print('Source Error --> continuing')
        continue

myfile =  open('fake_news.txt','w')

for article in output:
  myfile.write(article)
  myfile.write('\n\n~_~\n\n')
  myfile.close
