#!/usr/bin/python

import requests
 
 
def consumePOSTRequestSync():
 params = {'test1':'param1','test2':'param2'}
 url = 'http://httpbin.org/post'
 headers = {"Accept": "application/json"}
 # call post service with headers and params
 response = requests.post(url,headers= headers,data = params)
 print "code:"+ str(response.status_code)
 print "******************"
 print "headers:"+ str(response.headers)
 print "******************"
 print "content:"+ str(response.text)
  
# call 
consumePOSTRequestSync()
