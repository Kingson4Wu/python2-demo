#!python
# encoding: utf-8

import urllib2
import json
url = "http://54.223.208.103:9999/A46eXW_ETfafqGaPzCjBMQ/frontend/get_view_match_list"
#url = "https://www.baidu.com/"
req = urllib2.Request(url)
req = ""
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res

json_str = json.dumps(res)

data = json.loads(json_str)

