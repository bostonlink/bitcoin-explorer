#!/usr/bin/env python

from canari.maltego.entities import Phrase
from canari.maltego.message import Label
from canari.framework import configure
from common.entities import BitcoinAddress
from common.blockexplorer import bitcoin_address

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
    label='To Bitcoin Address [Bitcoin-Explorer]',
    description='Returns a BitcoinAddress entity from a bitcoin wallet address',
    uuids=[ 'bitcoin-explorer.v2.PhraseToBitcoinAddress',
            'bitcoin-explorer.v2.BitcoinAddressToBitcoinAddress' ],
    inputs=[ ( 'Bitcoin Explorer', Phrase ),
             ( 'Bitcoin Explorer', BitcoinAddress) ],
    remote=False,
    debug=False
)

def dotransform(request, response, config):
    
    try:
        btc_add = bitcoin_address(request.value)
        e = BitcoinAddress(request.value)
        e += Label("Short URL", btc_add['short_link'])
        e += Label("Date First Seen", btc_add['first_seen_date'])
        e += Label("First Seen in Block", btc_add['first_seen_block'])
        e += Label("Total Transactions Received", btc_add['received_transactions'])
        e += Label("Total Bitcoins Received", btc_add['received_bitcoin_total'])
        e += Label("Total Sent Transactions", btc_add['sent_transactions'])
        e += Label("Total Bitcoins Sent", btc_add['sent_bitcoins'])
        e += Label("Hash", btc_add['hash160'])
        e += Label("PublicKey", btc_add['public_key'])
    
        response += e

        return response

    except:
        pass
