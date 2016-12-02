# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'l*****u@163.com'
password = '1*******m'

to_addr = '1********9@qq.com'

smtp_server = 'smtp.163.com'


msg = MIMEMultipart()
msg['From'] = _format_addr('Administrator <%s>' % from_addr)
msg['To'] = _format_addr('User <%s>' % to_addr)
msg['Subject'] = Header("Greeting from SMTP...", 'utf-8').encode()

msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

with open('/Users/yuxiaofei/img.png', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='img.png')

    mime.add_header('Content-Disposition', 'attachement', filename='img.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachement-Id', '0')

    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)

server.login(from_addr, password)

server.sendmail(from_addr, [to_addr], msg.as_string())

server.quit()


