#!/usr/bin/env python3

import json
import requests

response = requests.get("https://map.internetintel.oracle.com/ixp/stats/ywg-prefixes.json")
data = json.loads(response.text)

prefixjson = data['prefixes']
for prefix in prefixjson:
    route = prefix['prefix']
    #print(route)
    origin = prefix['origin']
    rpki = prefix['rpki']
    irr = prefix['irr']
    bogon_prefix = prefix['bogon_prefix']
    bogon_asn = prefix['bogon_asn']
    spamhaus_prefix = prefix['spamhaus_prefix']
    spamhaus_asn = prefix['spamhaus_asn']
    if spamhaus_asn != None:
        for x in prefix:
            print("%s: %s" % (x, prefix[x]))
        print("-----")

