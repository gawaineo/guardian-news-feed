from flask import render_template, request, url_for
import urllib2, urllib
import json
from datetime import datetime

from newsapp import app

# GO-news-feed 1.0 => User Agent string used for Faroo Search Engine

TRENDING_NEWS = 'http://www.faroo.com/api?q=%s&start=1&length=10&l=en&src=news&f=json&key=he0JQxvNk2m837QQMqHIOk8E3sg_'
NEWS_SEARCH = 'http://www.faroo.com/api?q=%s&start=1&length=20&l=en&src=news&f=json&key=he0JQxvNk2m837QQMqHIOk8E3sg_'

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index_page():

	search_bar_value = request.args.get('search_q')
	articles = []

	if search_bar_value is not None:
		search_bar_value = urllib.quote_plus(search_bar_value)
		search_req = urllib2.Request(NEWS_SEARCH % search_bar_value)
		search_response = urllib2.urlopen(search_req)
		search_content = json.loads(search_response.read())
	else:
		# default: get news/web results with no search term specified
		search_response = urllib2.urlopen(TRENDING_NEWS % search_bar_value)
		search_content = json.loads(search_response.read())

	for result in search_content['results']:
		result['date'] = datetime.fromtimestamp(int(result['date'])/1000).strftime('%b %d, %Y %I:%M %p %Z')
		if result['iurl'] == "":
			result['iurl'] = "http://cdn.jetcharters.com/bundles/jetcharterspublic/images/image-not-found.jpg"
		articles.append(result)


	return render_template('index.html', articles=articles)
