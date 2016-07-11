# -*- coding:utf-8 -*-
import os,sys
path = "/Users/fengjun/PySys27/lib/python2.7/site-packages"
sys.path.append(path)

import web
import json

urls = ('/', 'mmQuery',)

class mmQuery:
  def POST(self):
    data = web.input()
    return data['page']

application = web.application(urls, globals()).wsgifunc()