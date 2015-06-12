#!/usr/bin/env python
#-*- coding: utf-8 -*-

'Get Data From JuMei'

__author__ = 'hulatang'

import urllib2
import json

baseURL = 'http://www.jumeiglobal.com/ajax_new/getDealsByPage?type=new&pagesize='
pageSize = 200
otherURL = '&index=0&page=global&callback=global_load_callback'
targetURL = baseURL + str(pageSize) + otherURL
dataJumei = ''

#get data of jumei global from JuMei server
def getHTML(url):
	data = ''
	tryTimes = 0
	targetURL = url

	while( data == '' and tryTimes < 5):
		try:
			data = urllib2.urlopen(targetURL).read()
		except urllib2.URLError as e:
			print e.reason
		else:
			print 'Get Jumei Data OK!!!'

		tryTimes += 1
	return data

#parse the data from jumei, using json
def parseHTML(html):
	html = html.replace('global_load_callback','')[1:-1]
	html = json.loads(html)

	items = html['list']
	return items
