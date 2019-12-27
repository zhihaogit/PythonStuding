# SMTP是发送邮件的协议
# python对 SMTP支持有 smtplib和 email两个模块，email负责构造邮件，smtplib负责发送邮件
# from email.mime.text import MIMEText
# msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
# 第一个参数是邮件正文
# 第二个参数是 MIME的 subtype，传入 plain表示纯文本，最终的 MIME是 text/plain
# 第三个参数是 编码格式

# 输入 email地址和密码
from_addr = input('From: ')
password = input('Password: ')

# 输入收件人地址
to_addr = input('To: ')
# 输入 SMTP服务器地址
smtp_server = input('SMTP server: ')
smtp_server_port = input('SMTP server port: ')
image_src = input('Image absolute path: ')

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

# 邮件主题、如何显示发件人、收件人等信息并不是通过 SMTP协议发送给 MTA，而是包含在 MTA的文本中
# 需要在 MIMEText中加入 From, To和 Subject

import smtplib

def _format_addr_(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# msg = MIMEText('hello, send by python...', 'plain', 'utf-8')

# 添加附件
# 同时支持 HTML和 Plain，需要指定 subtype是 alternative
msg = MIMEMultipart('alternative')

msg['From'] = _format_addr_('Python爱好者<%s>' % from_addr)
# 接收的是字符串，而不是 list，如果有多个邮件地址，用 ,分隔
msg['To'] = _format_addr_('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自 SMTP的问候...', 'utf-8').encode()

msg.attach(MIMEText('plain text', 'plain', 'utf-8'))

# 添加附件就是加上一个 MIMEBase，从本地读取一个图片
with open(image_src, 'rb') as f:
    # 设置附件的 MIME和文件名
    mime = MIMEBase('image', 'jpg', filename = 'test.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename = 'test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用 base64编码
    encoders.encode_base64(mime)
    # 添加到 MIMEMultipart
    msg.attach(mime)

# 发送 HTML
# img的 src="cid:0" 表示引用第一个附件
# 达到发送图片的目的
htmlText = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '<img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8')
msg.attach(htmlText)

server = smtplib.SMTP(smtp_server, smtp_server_port) # SMTP协议默认端口是 25
# 加密 SMTP会话，先创建 SSL安全连接，在使用 SMTP协议发送邮件
server.starttls()
# 打印出和 SMTP服务器交互的所有信息
server.set_debuglevel(1)
server.login(from_addr, password)
# 可以一次发给多个人，所以参数是个 list
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
