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
    if data['page']=='home':
      urls=["?id=ma5","?id=close"]
      return render.jsframe(len(urls),urls)
    else:
      return data['page']

class mmDraw:
  def GET(self):
    url_data = web.input()
    return render.jsroot(url_data.id)

application = web.application(urls, globals()).wsgifunc()

if __name__=="__main__":
  a = mmQuery()
  print a.mmtest()
