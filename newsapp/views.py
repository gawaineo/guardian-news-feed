from flask import render_template, request, url_for
import urllib2
import json

from goose import Goose
from newsapp import app


EDITIONS_URL = 'http://content.guardianapis.com/editions?q=%s&api-key=uzrj7hgs927dg7qx8s2bqp8q'
SECTIONS_URL = 'http://content.guardianapis.com/sections?&api-key=uzrj7hgs927dg7qx8s2bqp8q'
SEARCH_CONTENT_URL = "http://content.guardianapis.com/search?q=%s&api-key=uzrj7hgs927dg7qx8s2bqp8q"

@app.route('/', methods=['GET'])
def report_news():
	#editions_req = urllib2.Request(EDITIONS_URL % '')
	#sections_req = urllib2.Request(SECTIONS_URL)

	#editions_response = urllib2.urlopen(editions_req)
	#sections_response = urllib2.urlopen(sections_req)

	#editions_content = json.loads(editions_response.read())
	#sections_content = json.loads(sections_response.read())

	search_bar_value = request.args.get('search_q')

	articles = []

	if search_bar_value is not None:
		search_req = urllib2.Request(SEARCH_CONTENT_URL % search_bar_value)
		search_response = urllib2.urlopen(search_req)
		search_content = json.loads(search_response.read())
	else:
		search_req = urllib2.Request(SEARCH_CONTENT_URL % '')
		search_response = urllib2.urlopen(search_req)
		search_content = json.loads(search_response.read())

	g = Goose()

	for result in search_content['response']['results']:
		art = g.extract(url=result['webUrl'])

		result['meta_description'] = art.meta_description

		print result['webUrl']

		try:
			result['image'] = art.top_image.src
		except AttributeError, e:
			result['image'] = 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRj0YzDMrnC8kqGjvTH3tQ_VpVY4HbtcpGCNcJ_tR4WdiMKvjYc'

		articles.append(result)


	return render_template('index.html', articles=articles) 
										#editions=editions_content['response']['results'])



