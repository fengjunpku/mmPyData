# -*- coding:utf-8 -*-
""" Basic blog using webpy 0.3 """
import web
### Url mappings

urls = (
    '/', 'Index',
    '/query/', 'Query',
)


### Templates
t_globals = {
    'datestr': web.datestr,
    'static': '/'
}
render = web.template.render('./', globals=t_globals)


class Index:
    def GET(self):
        """ Show page """
        # for post in posts:
          # print post.posted_on.split(".")[0]
          # print web.datestr(datetime.datetime.strptime(post.posted_on.split(".")[0],"%Y-%m-%d %H:%M:%S"))
        return render.index()


class Query:
    def GET(self, id):
        """ View single post """
        return id


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()