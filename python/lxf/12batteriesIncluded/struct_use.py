# struct模块解决 bytes和其他二进制数据类型的转换
# struct的 pack函数把任意数据类型变成 bytes
import struct
b1 = struct.pack('>I', 10240099)
print (b1)
# 第一参数是指令参数，'>I'的意思是：
# >表示字节顺序是 big-endian，也就是网络序，I表示 4字节无符号整数
# 后面的参数个数要和处理指令一致

b2 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print (b2)
# H表示 2字节无符合整数
