# -*- coding:utf-8 -*-
import os,sys
path = "/Users/fengjun/PySys27/lib/python2.7/site-packages"
sys.path.append(path)

import web
import json

urls = ('/', 'mmQuery',
        '/draw','mmDraw',)

class mmQuery:
  def __init__(self):
    self.__frame = '''
    <iframe width="100%" height="400" src="http://thismac/query/draw">
    </iframe>
    '''
    self.__grid_head = '''
    <div class="row">
    '''
    self.__row_head = '''
    <div class="col-md-6">
    '''
  def POST(self):
    data = web.input()
    if data['page']=='home':
      return self.mmGrid(4)
    else:
      return data['page']

  def mmGrid(self,num):
    if num==1:
      return self.__frame
    else:
      sgrid = self.__grid_head
      for x in range(num):
        sgrid += self.__row_head
        sgrid += self.__frame
        sgrid += "<h3>"+str(x+1)+"</h3>"
        sgrid += "</div>"
      sgrid += "</div>"
      return sgrid

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