# 为防止通过彩虹表根据哈希值反推原始口令，在计算哈希时，需要加 salt
# salt可以看做是一个 口令，加 salt的哈希就是：计算一段 message的哈希时，根据不同口令计算出不同的哈希，要验证哈希值，必须同时提供正确的口令
# Hmac算法：Keyed-Hashing for Message Authentication，通过标准的算法，在计算哈希的过程中，把 key混入计算过程中
# Hmac对所有哈希算法都通用，无论是 md5还是 sha-1
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod = 'MD5')
# 消息过长，可以调用 h.update(msg)
result = h.hexdigest()
print (result)
# fa4ee7d173f2d97ee79022d1a7355bcf

# hmac和 hash算法类似，输出长度和原始哈希算法的长度一致

import hmac, random
def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')