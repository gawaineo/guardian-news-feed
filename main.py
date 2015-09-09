#!/usr/bin/env python

from bottle import route,request,run,get
from bottle import static_file, url, redirect
from bottle import jinja2_template as template
from hackernews import HackerNews 


hn = HackerNews()

for story_id in hn.top_stories(limit=10):
	print hn.get_item(story_id).title
	#print type(hn.get_item(story_id))