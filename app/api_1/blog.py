# -*- coding: utf-8 -*-
'''
    博文类
'''
import re
import datetime
import json

from bson.objectid import ObjectId
import tornado.auth  # 用户认证
import tornado.web  # 基础 Web 框架
import tornado.escape  # 转义
import tornado.options  # 配置文件解析工具
from app.databases import db


class BlogHandler(tornado.web.RequestHandler):

    def get(self):
        # import ipdb; ipdb.set_trace()
        posts = db.posts
        # 查询一条数据
        blog = posts.find_one({'_id': ObjectId(self.get_cookie("blog_id"))})
        # 查看是存在数据
        if blog:
            # 渲染页面
            self.render(
                "blog.html",
                page_title=blog["title"],
                blog=blog,
            )
        else:
            # 没有查询到跳转主页
            self.redirect('/')


class MainHandler(tornado.web.RequestHandler):
    """主页"""

    def get(self):
        # 渲染主页
        self.render("index.html")

    def post(self):
        '''
                添加一页博客
        '''
        title = self.get_argument("title", None)
        author = self.get_argument("author", None)
        content = self.get_argument("content", None)
        tags = self.get_argument("tags", None)
        blog = dict()
        if title and content and tags:
            blog['title'] = title.strip()
            blog['author'] = author
            blog['content'] = content
            blog['tags'] = list(
                map(lambda item: item.strip(), re.split(r",|，", tags)))
            blog['date'] = datetime.datetime.now().strftime('%F %T')
            posts = db.posts
            # 添加到数据库
            # import ipdb; ipdb.set_trace()
            try:
                blog_id = posts.insert_one(blog).inserted_id
                if blog_id:
                    self.set_cookie('blog_id', str(blog_id))
                    # 添加成功直接跳转到博文页
                    self.write(json.dumps({'url': r'/blogs', 'code':200, 'message': '请输入消息'}))
                    # self.redirect('/blogs')
            except Exception as e:
                # 添加失败跳转到主页
                self.redirect('/')
