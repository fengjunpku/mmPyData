# -*- coding:utf-8 -*-
import os,sys
path = "/Users/fengjun/PySys27/lib/python2.7/site-packages"
sys.path.append(path)

import web

urls = ('/', 'hello',)

class hello:
  def POST(self):
    return "Hello, world."

application = web.application(urls, globals()).wsgifunc()