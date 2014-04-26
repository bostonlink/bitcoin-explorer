#!/usr/bin/env python

# Google Custom Search Engine Python Module coded specifically for the Bitcoin-Explorer Maltego transform pack project

import requests
import urllib
import json

__author__ = 'David Bressler (@bostonlink)'
__copyright__ = 'Copyright 2014, David Bressler'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'bostonlink'
__email__ = 'bostonlink@igetshells.io'
__status__ = 'Development'


def http_get(url):
	
	""" Standard HTTP GET request, accepts a url and returns the response
	ex: http_get("http://google.com")"""

	try:
		response = (requests.get(url))
 		return response.content
	except Exception as e:
		return e


def csequery(gapi, cseid, query):
	
	"""Google Custom Search Engine API query coded for the Bitcoin-explorer project"""

	query = urllib.urlencode({'q': query})
	url = "https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&%s" % (gapi, cseid, query)

	return http_get(url)


def cseq_nextp(gapi, cseid, startindex, query):
	
	"""Google Custom Search Engine API NextPage query coded for the Bitcoin-explorer project.
	Returns the results of the next page in a search by specifying the startindex"""

	query = urllib.urlencode({'q': query})
	start = urllib.urlencode({'start': startindex})
	url = "https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&%s&%s" % (gapi, cseid, query, start)

	return http_get(url)


# Dev shit and testing below - Delete before pushing!

#cseid = '004789283585187479137:bkw4vuae8n0'
#gapi = 'AIzaSyB1zoOKWsKnwWsLVzEglR7lKCx62S2ba0E'

# jsondata = json.loads(csequery(gapi, cseid, '1FfmbHfnpaZjKFvyi1okTjJJusN455paPH -site:blockchain.info -site:blockexplorer.com'))

#f = open('data', 'r').read()
#jsondata = json.loads(f)
#starti = jsondata['queries']['nextPage'][0]['startIndex']
#query = jsondata['queries']['nextPage'][0]['searchTerms']
#print cseq_nextp(gapi, cseid, starti, query)

# print csequery(gapi, cseid, '1FfmbHfnpaZjKFvyi1okTjJJusN455paPH -site:blockchain.info -site:blockexplorer.com')