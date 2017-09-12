#!/usr/bin/python

import requests
import pdb; pdb.set_trace()

response = requests.get("http://services.groupkt.com/country/get/iso2code/IN");

data = response.json()

#from requests.auth import HTTPBasicAuth
#requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
#<Response [200]>




