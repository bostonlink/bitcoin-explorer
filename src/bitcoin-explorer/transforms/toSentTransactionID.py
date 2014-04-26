#!/usr/bin/env python

from canari.maltego.message import Label, Field
from canari.framework import configure
from common.entities import BitcoinTransaction, BitcoinAddress
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
    label='To Sent Transactions [Bitcoin-Explorer]',
    description='Returns sent transactions as BitcoinTransaction entities',
    uuids=[ 'bitcoin-explorer.v2.BitcoinAddressToSentTransactionID' ],
    inputs=[ ( 'Bitcoin Explorer', BitcoinAddress) ],
    remote=False,
    debug=True
)

def dotransform(request, response, config):
    
    btc_add = bitcoin_address(request.value)
    
    for trans in btc_add['transactions']:

        if 'Sent' in trans['transaction_type']:
            e = BitcoinTransaction(trans['transaction_hash'],
                                   trans_type = trans['transaction_type'],
                                   amount = trans['transaction_amount'],
                                   trans_uri = trans['transaction_uri'],
                                   address = request.value)
            e += Field("date", trans['date'], displayname='Date')
            e += Label("Bitcoin Address", request.value)
            e += Label("Total Amount of Transaction", trans['transaction_amount'])
            e += Label("Transaction Type", trans['transaction_type'])
            e += Label("Transaction Date", trans['date'])
            e.linklabel = 'Sent'
            
            response += e

        else:
            pass

    return response
