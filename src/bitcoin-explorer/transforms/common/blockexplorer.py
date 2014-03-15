#!/usr/bin/env python

# Bitcoin blockexplorer.com python module
# modules: easy_install lxml, easy_install beautifulsoup4, easy_install requests

import requests
from bs4 import BeautifulSoup

__author__ = 'David Bressler (@bostonlink)'
__copyright__ = 'Copyright 2014, David Bressler'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'bostonlink'
__email__ = 'bostonlink@igetshells.io'
__status__ = 'Development'


def bitcoin_address(address):
    """Searches https://blockexplorer.com/address/[address] for the
    provided address, parses the data, and returns a dictionary of
    address information and all transactions associated with the
    wallet address."""

    url = "https://blockexplorer.com/address/%s" % address
    try:
        r = (requests.get(url))
    except Exception as e:
        print e

    soup = BeautifulSoup(r.content)
    sbody = soup.body
    stransactions = soup.body.table.find_all('tr')
    stransactions.pop(0)
    tr_bitcoins = sbody.ul.find_all('li')[2].contents[0].strip().split(":")
    tr_bitcoins = tr_bitcoins[1].lstrip().replace(" ", "")

    soup_dic = {"address": sbody.h1.contents[0].strip().split()[1],
                "short_link": sbody.div.a.contents[0],
                "first_seen_date": sbody.ul.find_all('li')[0].contents[4],
                "first_seen_block": sbody.ul.find_all('li')[0].find_all('a')[1].contents[0].strip().split()[1],
                "received_transactions": sbody.ul.find_all('li')[1].contents[0].strip().split()[2],
                "received_bitcoin_total": tr_bitcoins,
                "sent_transactions": sbody.ul.find_all('li')[3].contents[0].strip().split()[2],
                "sent_bitcoins": sbody.ul.find_all('li')[4].contents[0].strip().split()[2],
                "hash160": sbody.ul.find_all('li')[5].contents[2].lstrip(': '),
                "public_key": sbody.ul.find_all('li')[6].div.contents[0]
                }

    transactions = []
    for transaction in stransactions:
        trans_fields = transaction.find_all("td")
        trans_dic = {"transaction_hash": transaction.td.a['name'],
                     "transaction_uri": transaction.td.a['href'],
                     "block": trans_fields[1].a.contents[0].strip().split()[1],
                     "block_uri": trans_fields[1].a['href'],
                     "date": trans_fields[1].contents[1],
                     "transaction_amount": trans_fields[2].contents[0],
                     "transaction_type": trans_fields[3].contents[0],
                     "wallet_total": trans_fields[5].contents[0]
                     }

        addresses = []
        for line in trans_fields[4].find_all('li'):
            if line.a is None:
                pass
            else:
                addresses.append(line.a.contents[0])

        trans_dic['addresses'] = addresses
        transactions.append(trans_dic)

    soup_dic['transactions'] = transactions
    return soup_dic


def bitcoin_trans(trans_uri):
    """Parses https://blockexplorer.com/tx/[transaction hash] 
    """
    url = "https://blockexplorer.com/%s" % trans_uri
    try:
        r = (requests.get(url))
    except Exception as e:
        print e

    soup = BeautifulSoup(r.content)
    sbody = soup.body
    stables = soup.body.find_all('table')
    inputs = stables[0].find_all('tr')
    inputs.pop(0)
    outputs = stables[1].find_all('tr')
    outputs.pop(0)

    soup_dic = {"trans_url": url,
                "short_link": sbody.a.contents[0],
                "full_hash": sbody.ul.find_all('li')[0].contents[2].lstrip(': '),
                "block": sbody.ul.find_all('li')[1].a.contents[0],
                "block_uri": sbody.ul.find_all('li')[1].a['href'],
                "total_inputs": sbody.ul.find_all('li')[2].contents[2].lstrip(': ').rstrip(' ('),
                "btc_redeemed": sbody.ul.find_all('li')[3].contents[2].lstrip(': '),  # Total BTC in (Total BTC redeemed from previous transactions)
                "total_outputs": sbody.ul.find_all('li')[4].contents[0].split()[3],
                "btc_sent": sbody.ul.find_all('li')[5].contents[2].lstrip(': '),  # Total BTC out (Total BTC sent with this transaction.)
                "trans_size": sbody.ul.find_all('li')[6].contents[2].lstrip(': '),
                "block_fee": sbody.ul.find_all('li')[7].contents[2].lstrip(': '),
                "rawtx_uri": sbody.ul.find_all('li')[8].a['href']
                }

    # Inputs from a specific transaction are deposits to a wallet addess
    input_list = []
    for tran in inputs:
        tran_fields = tran.find_all('td')
        in_dic = {"output_index": tran_fields[0].a.contents[0],
                  "amount_received": tran_fields[1].contents[0],
                  "from_address": tran_fields[2].a.contents[0],
                  "trans_type": tran_fields[3].contents[0],
                  "script_sig": tran_fields[4].div.contents[0]
                 }

        input_list.append(in_dic)

    soup_dic["inputs"] = input_list

    # Outputs are withdrawals or sent bitcoins within the transaction
    output_list = []
    for tran in outputs:
        tran_fields = tran.find_all('td')
        out_dic = {"index": tran_fields[0].contents[0],
                   "redeemed": tran_fields[1].a.contents[0],  # indicates if reveived coins were spent yet
                   "amount_sent": tran_fields[2].contents[0],
                   "address": tran_fields[3].a.contents[0],
                   "type": tran_fields[4].contents[0],
                   "script_pubkey": tran_fields[5].div.contents[0]
                  }
        
        output_list.append(out_dic)

    soup_dic["outputs"] = output_list
    
    return soup_dic
    

def bitcoin_block(block_uri):
    """Parses https://blockexplorer.com/block/[block hash] that 
    is returned in the transactions from the bitcoin_address module for the
    provided block, parses the data, and returns a dictionary of
    block information and all transactions associated with the
    wallet address. """

    url = "https://blockexplorer.com/%s" % block_uri
    try:
        r = (requests.get(url))
    except Exception as e:
        print e

    soup = BeautifulSoup(r.content)
    sbody = soup.body
    trans = sbody.find_all('tr')
    trans.pop(0)

    block_dic = {"block_url": url,
                 "block": sbody.h1.contents[0].split()[1],
                 "short_link": sbody.div.a.contents[0],
                 "block_hash": sbody.ul.find_all('li')[0].contents[2].lstrip(': '),
                 "previous_block": sbody.ul.find_all('li')[1].find_all('a')[1].contents[0],
                 "next_block": sbody.ul.find_all('li')[2].find_all('a')[1].contents[0],
                 "block_time": sbody.ul.find_all('li')[3].contents[2].lstrip(': '),
                 "transactions": sbody.ul.find_all('li')[5].contents[2].lstrip(': '),
                 "block_btc_total": sbody.ul.find_all('li')[6].contents[2].lstrip(': '),
                 "block_size": sbody.ul.find_all('li')[7].contents[2].lstrip(': ')
                  }

    trans_list = []
    for tran in trans:
        tran_fields = tran.find_all('td')
        trans_dic = {"transaction": tran_fields[0].a.contents[0],
                     "tran_url": tran_fields[0].a['href'],
                     "fee": tran_fields[1].contents[0],
                     "size": tran_fields[2].contents[0]
                     }

        from_list = []
        for address in tran_fields[3].contents:
            if address.a is not None:
                add_dic = {"address_uri": address.a['href'],
                           "address": address.a.contents[0],
                           "amount": address.li.contents[1].lstrip(': ')
                          }
                
                from_list.append(add_dic)

            else:
                pass

        trans_dic["from_address"] = from_list
        

        to_list = []
        for address in tran_fields[4]:
            if address.a is not None:
                add_dic = {"address_uri": address.a['href'],
                           "address": address.a.contents[0],
                           "amount": address.li.contents[1].lstrip(': ')
                           }

                to_list.append(add_dic)
                
            else:
                pass

        trans_dic["to_address"] = to_list
        trans_list.append(trans_dic)

    block_dic['transactions'] = trans_list
        
    return block_dic

#  print bitcoin_address('1FfmbHfnpaZjKFvyi1okTjJJusN455paPH')
# print bitcoin_trans('/tx/3ae43bb0a8e4cc3a345a7a2a688217bcb8d9f7e9001263930cd23e9b3b7364c6#o0')
# print bitcoin_block('/block/000000000000000c417aad6743995662441875233a0a101bbcf6c5624bc87c34')