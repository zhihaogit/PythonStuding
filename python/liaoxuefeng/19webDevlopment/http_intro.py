# 浏览器和服务器之间的传输协议是 HTTP
# HTTP是在网络上传输 HTML的协议

# HTTP请求
# 步骤一：浏览器首先向服务器发送 HTTP请求
# 步骤二：服务器向浏览器返回 HTTP响应
# 步骤三：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出 HTTP请求，重复步骤1，2

# HTTP格式
# 每个 HTTP请求和响应都遵循相同的格式
# 一个 HTTP包含 Header和 Body两部分，Body可选
# 每个 Header一行一个，换行符是 \r\n
# 当遇到连续两个 \r\n时，Header部分结束，后面的数据全部是 Body
# HTTP响应如果包含 body，通过 \r\n\r\n来分隔
# Body的数据类型有 Content-Type头来确定
# 当存在 Content-Encoding时，Body的数据是被压缩的，常见的是 gzip
# Content-Encoding: gzip时，需要先将 body数据解压缩，才能得到真正的数据