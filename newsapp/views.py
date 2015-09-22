from flask import render_template
import urllib2
import json

from goose import Goose
from newsapp import app

req = urllib2.Request('http://content.guardianapis.com/search?q=trump&api-key=uzrj7hgs927dg7qx8s2bqp8q')
response = urllib2.urlopen(req)
the_page = json.loads(response.read())

articles = []

for result in the_page['response']['results']:
	articles.append(result)

#print len(articles)
"""
for article in articles:
	g = Goose()
	news = g.extract(url=article['webUrl'])
	print "Title: ", news.title, "\nSummary:",news.meta_description
	#print news.cleaned_text
	print 
"""

@app.route('/')
def report_news():
	return render_template('index.html')



