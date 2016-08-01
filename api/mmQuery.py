# -*- coding:utf-8 -*-
import os,sys
path = "/Users/fengjun/PySys27/lib/python2.7/site-packages"
sys.path.append(path)

import web
import json

urls = ('/', 'mmQuery',
        '/draw','mmDraw',)
##使用绝对路径！！！
root = os.path.dirname(__file__)   
render = web.template.render(os.path.join(root,'templates/'))
##
class mmQuery:
  def POST(self):
    data = web.input()
    ex_urls=["?id=ma5","?id=close"]
    if data['page']=='home':
      return render.jsframe(ex_urls)
    elif data['page']=='about':
      return render.about()
    else:
      return "Miao: Not Found!"

class mmDraw:
  def GET(self):
    url_data = web.input()
    return render.jsroot(url_data.id)

application = web.application(urls, globals()).wsgifunc()

if __name__=="__main__":
  pass
