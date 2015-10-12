from flask import render_template, request, url_for
import urllib2
import urllib
import json
from datetime import datetime

from newsapp import app

# GO-news-feed 1.0 => User Agent string used for Faroo Search Enginee

EDITIONS_URL = 'http://content.guardianapis.com/editions?q=%s&api-key=uzrj7hgs927dg7qx8s2bqp8q'
SECTIONS_URL = 'http://content.guardianapis.com/sections?&api-key=uzrj7hgs927dg7qx8s2bqp8q'
SEARCH_CONTENT_URL = "http://content.guardianapis.com/search?%s&api-key=uzrj7hgs927dg7qx8s2bqp8q"

TRENDING_NEWS = 'http://www.faroo.com/api?q=%s&start=1&length=10&l=en&src=news&f=json&key=he0JQxvNk2m837QQMqHIOk8E3sg_'
NEWS_SEARCH = 'http://www.faroo.com/api?q=%s&start=1&length=20&l=en&src=news&f=json&key=he0JQxvNk2m837QQMqHIOk8E3sg_'

@app.route('/', methods=['GET'])
def index_page():

	search_bar_value = request.args.get('search_q')
	articles = []
	print search_bar_value, "QQQQQ"

	if search_bar_value is not None:
		search_bar_value = urllib.quote_plus(search_bar_value)
		search_req = urllib2.Request(NEWS_SEARCH % search_bar_value)
		search_response = urllib2.urlopen(search_req)
		search_content = json.loads(search_response.read())
	else:
		# default: get news/web results with no search term specified
		#search_req = urllib2.Request(SEARCH_CONTENT_URL % '')
		search_response = urllib2.urlopen(TRENDING_NEWS % search_bar_value)
		search_content = json.loads(search_response.read())


	for result in search_content['results']:
		result['date'] = datetime.fromtimestamp(int(result['date'])/1000)
		if result['iurl'] == "":
			print result['iurl']
			result['iurl'] = "http://cdn.jetcharters.com/bundles/jetcharterspublic/images/image-not-found.jpg"
		articles.append(result)


	return render_template('index.html', articles=articles)
										#editions=editions_content['response']['results'])
