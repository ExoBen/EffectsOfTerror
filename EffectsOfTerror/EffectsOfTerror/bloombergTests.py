import BloombergData
import argparse
import json
import ssl
import sys
import urllib2

# Indexses of the dictionary are: migration, risk, stocks and bonds
dataLists = BloombergData.getData()

data = {
    "securities": [dataLists["migration"][0][0]],
    "fields": ["PX_LAST"],
    "startDate": "19700101",
    "endDate": "20120301"
}

def request():
    req = urllib2.Request('https://http-api.openbloomberg.com/request?ns=blp&service=refdata&type=HistoricalDataRequest')
    req.add_header('Content-Type', 'application/json')

    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_verify_locations('../../keys/bloomberg.crt')
    ctx.load_cert_chain('../../keys/stacshack_spring_2015_023.crt', '../../keys/stacshack_spring_2015_023.key')

    try:
        res = urllib2.urlopen(req, data=json.dumps(data), context=ctx)
        print res.read()
    except Exception as e:
        e
        print e
        return 1
    return 0
