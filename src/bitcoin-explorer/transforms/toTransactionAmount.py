#!/usr/bin/env python

from canari.maltego.message import Label, Field
from canari.framework import configure
from common.entities import BitcoinTransaction, BitcoinAmount
from canari.maltego.message import MaltegoException

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
    label='To Transaction Amount [Bitcoin-Explorer]',
    description='Returns transaction amount of a transaction',
    uuids=[ 'bitcoin-explorer.v2.BitcoinTransactionToTransactionAmount' ],
    inputs=[ ( 'Bitcoin Explorer', BitcoinTransaction) ],
    remote=False,
    debug=False
)

def dotransform(request, response, config):
    
    try:
        e = BitcoinAmount(request.fields['amount'])
        e += Field("date", request.fields['date'], displayname='Date')
        e += Field("trans_type", request.fields['trans_type'], displayname='Transaction Type')
        e += Field("trans_hash", request.value, displayname="Transaction Hash")
        e += Label("Transaction Type", request.fields['trans_type'])
        e += Label("Transaction Date", request.fields['date'])
        response += e

        return response

    except Exception as e:
        raise MaltegoException('An error occured: %s' % e)