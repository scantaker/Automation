import requests
import json

#get
'''
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
print(strhtml.text)
'''

#post
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
form_data = {'i': 'aa',
'from': 'AUTO',
'to': 'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt': '15747583051720',
'sign': 'a2c08b1be0ab03f49bb1f2010b0ca56f',
'ts': '1574758305172',
'bv': '41ff9fc639f730385a8ab923c3ccf30b',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_CLICKBUTTION'}

response = requests.post(url, data=form_data)
content = json.loads(response.text)
print(content)