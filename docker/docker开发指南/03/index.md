### 3.1 运行第一个镜像

```shell
docker run debian echo "Hello world"
# docker run启动容器
# debian参数是打算使用的镜像
# 本地没有该镜像，会从 docker hub下载，最后在容器运行 echo指令

docker run -i -t debian /bin/bash
# 提供一个命令行
# -t参数让 Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上
# -i参数让容器的标准输入保持打开
# bin/bash表示要一个 bash shell
```

### 3.2 基本命令

```shell
docker run -h container_name -i -t debian /bin/bash [--rm]
# -h参数设定一个新的主机名（hostname）
# -r参数的作用是当容器退出时，容器和相关的文件系统会一并删除

docker ps [-a]
# 目前运行中的容器的一些详细信息
# -a 列出所有容器，包括已停止的容器

docker inspect container_name
# 通过容器的名称和 ID来获取更多有关某个容器的信息

docker diff container_name
# 查看这个运行中的容器内，有哪些文件被改动过

docker logs container_name
# 该容器的日志

docker rm container_name
# 删除某个容器

docker rm -v $(docker ps -aq -f status=exited)
# 清理已停止的容器
# -v参数在这里意味着当所有由 Docker管理的数据卷已经没有和任何容器有关联时，都会一律删除
```

