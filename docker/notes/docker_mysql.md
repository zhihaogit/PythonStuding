# docker run mysql相关
```shell
docker volume create testmysql
# 创建一个 Docker Volume，这里用来储存状态，存储数据，数据持久化，移除了 mysql容器，数据依然会保留下来

docker run \
    -d \
    --name test_mysql \
    -p 13306:3306 \
    -v testmysql:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=123456789 \
    -e MYSQL_DATABASE=testmysql \
    -e MYSQL_USER=testuser \
    -e MYSQL_PASSWORD=1234567890 \
    mysql:8.0.22 \
    --default-authentication-plugin=mysql_native_password

# -d 后台运行容器，并运行容器 ID
# -v 挂载文件
# -e 设置环境变量
# MYSQL_ROOT_PASSWORD 根用户密码
# MYSQL_DATABASE 首次启动后创建数据库的名称
# MYSQL_USER 用户名
# MYSQL_PASSWORD 用户密码
# --default-authentication-plugin mysql8.0.4之后开始默认采用 caching_sha2_password， 使用与老版本兼容的密码插件 mysql_native_password，解决客户端与 mysql版本不兼容问题
```
