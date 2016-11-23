#!/usr/bin/env python3

"""
Post to telegra.ph

MIT License

Copyright (c) 2016 bvanrijn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import sys
import random

def random_uuid():
    b64 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    tmp = []

    for i in range(42):
        tmp.append(random.choice(b64))
    
    tmp = ''.join(tmp)

    return "tph_uuid=" + tmp

headers = {
    'Host': 'edit.telegra.ph',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'multipart/form-data; boundary=---------------------------TelegraPhBoundary21',
    'Referer': 'http://telegra.ph/',
    'Content-Length': '687',
    'Origin': 'http://telegra.ph',
    'Cookie': None,
    'Connection': 'keep-alive'
}


if headers['Cookie'] == None:
    try:
        cookieval = sys.argv[1]

        if not cookieval.startswith("tph_uuid"):
            cookieval = "tph_uuid" + cookieval
        
        headers['Cookie'] = cookieval
    except IndexError:
        headers['Cookie'] = random_uuid()
        print("I chose a random tph_uuid for you. Save it if you want to edit this post later.\n%s" % headers['Cookie'])

    
data = """-----------------------------TelegraPhBoundary21
Content-Disposition: form-data; name="Data";filename="content.html"
Content-type: plain/text

[
  {
    "_": "p",
    "c": [
      {
        "t": "Greetings,"
      }
    ]
  },
  {
    "_": "p",
    "c": [
      {
        "t": "Can we have a Telegraph API?"
      }
    ]
  },
  {
    "_": "p",
    "c": [
      {
        "t": "User "
      }
    ]
  },
  {
    "_": "p",
    "c": [
      {
        "_": "br"
      }
    ]
  }
]
-----------------------------TelegraPhBoundary21
Content-Disposition: form-data; name="title"

Let's make a post 
-----------------------------TelegraPhBoundary21
Content-Disposition: form-data; name="author"

For a Telegraph API 
-----------------------------TelegraPhBoundary21
Content-Disposition: form-data; name="page_id"

0
-----------------------------TelegraPhBoundary21--"""

print(requests.post("https://edit.telegra.ph/save", headers=headers, data=data).text)
