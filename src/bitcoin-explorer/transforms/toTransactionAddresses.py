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
    label='To Bitcoin Addresses [Bitcoin-Explorer]',
    description='Returns Received transactions as BitcoinTransaction entities',
    uuids=[ 'bitcoin-explorer.v2.BitcoinTransactionToAddresses' ],
    inputs=[ ( 'Bitcoin Explorer', BitcoinTransaction) ],
    remote=False,
    debug=True
)

def dotransform(request, response, config):
    
    try:
        
        btc_add = bitcoin_address(request.fields['address'])
    
        for trans in btc_add['transactions']:
            if request.value == trans['transaction_hash']:
                for address in trans['addresses']:
                    e = BitcoinAddress(address)
                    e += Field("date", trans['date'], displayname='Date')
                    e += Field("trans_uri", trans['transaction_uri'], displayname='Transaction URI')
                    e += Field("recieved_address", request.fields['address'], displayname='Recieved Address')
                    e += Label("Bitcoin Address", address)
                    e += Label("Bitcoin Recieved Address", request.fields['address'])
                    e += Label("Transaction Type", trans['transaction_type'])
                    e += Label("Transaction Hash", trans['transaction_hash'])
                    e += Label("Transaction Date", trans['date'])
                    
                    response += e

            else:
                pass

        return response

    except:
        pass
