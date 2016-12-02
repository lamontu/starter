# -*- coding: utf-8 -*-

import werobot
from werobot.reply import ArticlesReply, Article
import send_email
import re

import send_email


robot = werobot.WeRoBot(token='l**********0')


@robot.handler
def welcome(message):
    return "Follow shiyanlou, learn by doing."


@robot.image
def echo(message):
    reply = ArticlesReply(message=message)
    article = Article(
      title='Learn By Doing',
      description="Shiyanlou, learn by doing.",
      img="https://ws1.sinaimg.cn/large/005EFdvdgw1f88zx9nwevj30b4086wev.jpg",
      url="https://github.com/whtsky/WeRoBot"
    )
    reply.add_article(article)
    return reply


@robot.text
def emailreply(message):
    usermessage = message.content
    email_str = re.search('\s(\w{4,16}@.*.com)', usermessage)
    if email_str is not None:
        email = email_str.group(1) 
        index = usermessage.find('com')
        content = usermessage[index+4:]

        try:
            send_email.sendEmail(email, content)
        except:
            return 'False'
        return 'Success'
    else:
        return "Stay after school!"


robot.run(host='127.0.0.1', port=8080)


