# Discription
Data analysis with python

# Framework
* web server : apache+mod_wsgi+web.py
* data source : tushare
* data analysis : pyROOT
* data format : .root
* data viewer : jsROOT

# Deployment
1. apache2+mod_wsgi
   add `WSGIScriptAlias /query /where/your/mmPyData/api/mmQuery.py` to httpd conf
# Author
miaomiaoxiong

# History
* 20160706 Created

* 20160711 用ajax请求python处理，两条思路：

	1. apache处理静态页面，webpy直接处理动态请求；问题：占了80端口与apache冲突，不用80口有跨域问题。试着用php作为媒介。

	2. apache处理静态页面，web.py以mod_wsgi方式部署。

* 20160712 初步跑通流程：存root结果，经过apache+mod_wsgi+web.py+JSROOT展示
* 20160714 at gansu
* 20160724 at weihai
* 20160801 使用了webpy的模版
