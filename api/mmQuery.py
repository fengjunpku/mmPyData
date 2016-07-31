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
      return render.jsframe(3)
    else:
      return data['page']


class mmDraw:
  def GET(self):
    content = '''
    <script src="https://root.cern.ch/js/latest/scripts/JSRootCore.min.js"></script>
    <script type='text/javascript'>
     // absolute file path can be used as well
     var filename = "../data/hist.root";
     JSROOT.OpenFile(filename, function(file) {
        file.ReadObject("h1;1", function(obj) {
           JSROOT.draw("drawing", obj, "");
        });
     });
    </script>
    <div id="drawing" style="width:100%; height:100%"></div>
    '''
    return content
    

application = web.application(urls, globals()).wsgifunc()

if __name__=="__main__":
  a = mmQuery()
  print a.mmtest()
