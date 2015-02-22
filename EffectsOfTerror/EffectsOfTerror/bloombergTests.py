import BloombergData
import argparse
import json
import ssl
import sys
import urllib2
import re
import countries

# Data

# Indexses of the dictionary are: migration, risk, stocks and bonds
dataLists = BloombergData.getData()
# Dictionary of country codes
conuntryCode = countries.countries()

# Main Functions

data = getBloombergQueries(country, year, month, day)

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



# Helper Functions

def getBloombergQueries(country, year, month, day):
    dates = buildDates(year, month, day)

    securities = []

    for k in ["bonds", "stocks"]:
        for i in range(0..len(dataLists[k])):
            if dataLists[k][i][0] == countryCode[country]:
                securities.append(dataLists[k][i][2])

    for k in ["migration", "risk"]:
        for i in range(0..len(dataLists[k])):
            regex = re.compile(country, re.I)
            if regex.search(dataLists[k][i][0]) != None:
                securities.append(dataLists[k][i][2])

    # Possible future bug: what if more than one country entry is returned?
    return {
        "securities": securities,
        "fields": ["PX_LAST"],
        "startDate": dates[0],
        "endDate": dates[1]
    }


def buildDates(year, month, day):
    yea0 = str(int(year)-1)
    yea1 = str(int(year)+1)

    mon = ""
    if int(month) < 10:
        mon = "0" + month
    else:
        mon = month

    da = ""
    if int(day) < 10:
        da = "0" + day
    else:
        da = day

    return [yea0 + mon + da, yea1 + mon + da]

