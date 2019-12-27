# Email的历史比 Web还要久远
# MUA (mail user agent 邮件用户代理) 发送的邮件
# MTA (mail transfer agent 邮件传输代理) email服务提供商
# MDA (mail delivery agent 邮件投递代理) 邮件到达的目的地

# 流程
# 发件人 -> MUA -> MTA -> MTA -> 若干MTA -> MDA <- MUA <- 收件人

# 发邮件时 MUA到 MTA，MTA到 MTA使用的协议是 SMTP (simple mail transfer protocol)
# 收邮件时 MUA和 MDA使用的协议有两种：
'''
pop (post office protocol)，当前版本是 3，俗称 POP3
IMAP (internet message access protocol)，当前版本是 4，优点是不但能取邮件，还可以直接操作 MDA上存储的邮件，如从收件箱移到垃圾箱
'''