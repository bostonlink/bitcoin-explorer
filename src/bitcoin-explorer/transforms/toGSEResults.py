#!/usr/bin/env python

from canari.maltego.entities import URL
from canari.maltego.message import Label
from canari.framework import configure
from common.entities import BitcoinAddress
from common.pygcse import csequery
from canari.config import config
from canari.maltego.message import MaltegoException
import json

__author__ = 'bostonlink'
__copyright__ = 'Copyright 2014, Bitcoin-explorer Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'bostonlink'
__email__ = 'bostonlink@igetshells.io'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


@configure(
    label='To Google Custom Search Results [Bitcoin-Explorer]',
    description='Returns the first 10 results of a Google custom search for the bitcoin wallet address',
    uuids=[ 'bitcoin-explorer.v2.BitcoinAddressToGCSEResults' ],
    inputs=[ ( 'Bitcoin Explorer', BitcoinAddress) ],
    remote=False,
    debug=True
)

def dotransform(request, response, config):
    
    try:
        query = '%s -site:blockchain.info -site:blockexplorer.com' % request.value
        jsondata = json.loads(csequery(config['gcse/gapi'], config['gcse/gcseid'], query))
    except Exception as e:
        raise MaltegoException('An error occured: %s' % e)

    # parses the GCSE results

    if 'items' in jsondata:
        try:
            for item in jsondata['items']:
                e = URL(item['link'],
                    url=item['link'])

                e += Label("Title", item['title'].encode('ascii', 'ignore'))
                e += Label("Snippet", item['snippet'].encode('ascii', 'ignore'))
                e += Label("Google Query", jsondata['queries']['request'][0]['searchTerms'])

                response += e

        # TODO: Check to see if there are more than one page of results up to 100 results can be returned by the GCSE API
        # if 'nextPage' in jsondata['queries']
            return response

        except Exception as e:
            raise MaltegoException('An error occured: %s' % e)
    else:
        pass
