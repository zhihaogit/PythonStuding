# 摘要算法
# 又称哈希算法，散列算法，通过一个函数将任意长度的数据转换为一个长度固定的数据串（通常用16进制字符串表示）

# MD5
# MD5是常用的摘要算法，速度快，生成结果是固定的 128bit字节，通常用一个32位的16进制字符表示
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5Str = md5.hexdigest()
print (md5Str)
# d26a53750bc40b38b65a520292f69306

# 数据量大，可以分块多次调用 update()
md5_2 = hashlib.md5()
md5_2.update('how to use md5 in '.encode('utf-8'))
md5_2.update('python hashlib?'.encode('utf-8'))
md5_2Str = md5_2.hexdigest()
print (md5_2Str)
# d26a53750bc40b38b65a520292f69306

# SHA1
# SHA1的结果是 160bit字节，通常用一个40位的16进制表示
# 还用 SHA256，SHA512，越安全的算法越慢，摘要长度更长
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use md5 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
sha1Str = sha1.hexdigest()
print (sha1Str)
# b752d34ce353e2916e943dc92501021c8f6bca8c