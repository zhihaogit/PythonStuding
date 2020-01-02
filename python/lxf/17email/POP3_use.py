# 收取邮件就是编写一个 MUA作为客户端，从 MDA把邮件获取到用户的设备上
# 收取邮件最常用的是 POP协议，目前版本号是 3，俗称 POP3
# 内置 poplib模块，实现 POP3协议，直接用来收邮件
# 收取的不是可直接阅读的邮件本身，而是邮件的原始文本
# 基本步骤
# 1. 用 poplib把邮件的原始文本下载到本地
# 2. 用 email解析原始文本，还原为邮件对象

# 通过 POP3下载邮件
import poplib

# 输入邮件地址，口令和 POP3服务器地址
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

# 连接到 POP3服务器
server = poplib.pop3(pop3_server)
# 打开调试信息
server.set_debuglevel(1)
# 打印 POP3服务器的欢迎文字
print (server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间
print ('Message: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号
resp, mails, octets = server.list()
# 可以查看返回的列表
print (mails)

# 获取最新一封邮件，索引从 1开始
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行
# 可以获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 解析出邮件
msg = Parser().parsestr(msg_content)

# 可以根据邮件索引直接从服务器删除邮件
server.dele(index)
# 关闭连接
server.quit()


# 解析邮件
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib
msg = Parser().parsestr(msg_content)
# Message对象可能有一个 MIMEMultipart对象，包含嵌套的其他 MIMEBase对象，嵌套可能不止一层
# indent用于缩进显示
def print_info(msg, indent = 0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value: 
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s<%s>' % (name, addr)
            print ('%s%s: %s' % ('    ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print ('%spart %s' % ('    ' * indent, n))
            print ('%s--------------------' % ('    ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type = 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode = True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print ('%s Text: %s' % ('    ' * indent, content + '...'))
        else:
            print ('%sAttachment: %s' % ('    ' * indent, content_type))


# 意见的 Subject或者 Email中包含的名字都是经过编码后的 str，要正常显示，就需要 decode
def decode_str(s):
    # 目前只取了第一个元素
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# 文本邮件的内容也是 str，还需要检测编码，否则，非 utf-8编码的邮件都无法正常显示
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
