#!/usr/bin/env python

from canari.maltego.message import Label, Field
from canari.framework import configure
from common.entities import BitcoinAmount, BitcoinAddress
from common.blockexplorer import bitcoin_trans
from canari.maltego.message import UIMessage

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
    label='To Bitcoin Amount Sent in Transaction [Bitcoin-Explorer]',
    description='Returns a bitcoin amount sent per address per an associated transaction transaction',
    uuids=[ 'bitcoin-explorer.v2.BitcoinAddressToAmountSentInTransaction' ],
    inputs=[ ( 'Bitcoin Explorer', BitcoinAddress) ],
    remote=False,
    debug=True
)

def dotransform(request, response, config):
    
    if 'trans_uri' in request.fields:
        btc_trans = bitcoin_trans(request.fields['trans_uri'])
    else:
        UIMessage('No Transactions associated with address to lookup amount sent in the transaction.  Try Again!')
        pass

    for trans in btc_trans['outputs']:
        if trans['address'] == request.fields['recieved_address']:
            e = BitcoinAmount(trans['amount_sent'],
                              address=request.value)
            e += Label("Bitcoin Sent to Address", request.fields['recieved_address'])
            response += e
        else:
            UIMessage('No recieved transactions found')

    return response
