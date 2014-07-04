#!/usr/bin/env python

from canari.framework import configure
from common.entities import BitcoinTransaction, BitcoinAmount, TransactionType
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
    label='To Transaction Type [Bitcoin-Explorer]',
    description='Returns transaction type of a BitcoinTransaction or BitcoinAmount entity for a specific transaction',
    uuids=[ 'bitcoin-explorer.v2.FromBitcoinAmountToTransactionType',
            'bitcoin-explorer.v2.FromBitcoinTransToTransactionType' ],
    inputs=[ ( 'Bitcoin Explorer', BitcoinAmount),
             ( 'Bitcoin Explorer', BitcoinTransaction) ],
    remote=False,
    debug=False
)

def dotransform(request, response, config):

    try:
        if 'trans_type' in request.fields:
            e = TransactionType(request.fields['trans_type'])
            response += e

            return response
    
        else:
            pass

    except Exception as e:
        raise MaltegoException('An error occured: %s' % e)
