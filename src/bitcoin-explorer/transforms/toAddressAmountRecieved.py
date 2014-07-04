#!/usr/bin/env python

from canari.maltego.message import Label
from canari.framework import configure
from common.entities import BitcoinAmount, BitcoinAddress
from common.blockexplorer import bitcoin_address
from canari.maltego.message import MaltegoException
# to add an exception : from canari.maltego.message import MaltegoException, UIMessage

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
    label='To Bitcoin Total Amount Received [Bitcoin-Explorer]',
    description='Returns a BitcoinAmount entity with the total amount of bitcoins the address holds from a BitcoinAddress entity',
    uuids=[ 'bitcoin-explorer.v2.BitcoinAddressToBitcoinAmountReceived' ],
    inputs=[ ( 'Bitcoin Explorer', BitcoinAddress) ],
    remote=False,
    debug=False
)

def dotransform(request, response, config):
    
    try:
        btc_add = bitcoin_address(request.value)
        e = BitcoinAmount(btc_add['received_bitcoin_total'],
                          address = request.value )
        e += Label("Bitcoin Address", request.value)
        e.linklabel = 'Received'
        response += e

        return response

    except Exception as e:
        raise MaltegoException('An error occured: %s' % e)
