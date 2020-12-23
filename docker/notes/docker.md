# Docker
## docker run相关指令
### 启动容器
```shell
docker run debian echo "Hello world"
# debian参数是打算使用的镜像
# 本地没有该镜像，会从 docker hub下载，最后在容器运行 echo指令
```

### 提供一个命令行
```shell
docker run -i -t debian /bin/bash
# -i参数让容器的标准输入保持打开
# -t参数让 Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上
# bin/bash表示要一个 bash shell
```

### 启动一个容器
```shell
docker run -h container_name -i -t debian /bin/bash [--rm]
# -h参数设定一个新的主机名（hostname）
# -r参数的作用是当容器退出时，容器和相关的文件系统会一并删除
```

### 挂载文件
```shell
docker run -it -v /test:soft centos /bin/bash
docker run -d --rm --name container_name -p 10007:80 -v `pwd`/nginx.conf:/etc/nginx/conf.d/nginx.conf image_id
# -d 后台运行容器，并返回容器 ID
# -v|--volume[=[[HOST-DIR:]CONTAINER-DIR[:OPTIONS]]] 创建一个文件挂载，路径为绝对路径
# --name 为容器指定一个名称
# -p 指定端口映射，格式为：主机(宿主)端口:容器端口。冒号左侧为机器实际端口，右侧容器中程序使用的端口
# --rm 容器停止后，自动删除容器
```

## docker build相关指令
### 使用当前目录的 Dockerfile创建镜像
```shell
docker build -t test/ubuntu:v1 ./
# -t,--tag 镜像的名字及标签，通常 name:tag或者 name格式。可以在一次构建中为一个镜像设置多个标签
# ./ 当前目录
```

### 指定 Dockerfile创建镜像
```shell
docker build -f /path/to/a/Dockerfile ./
```

## docker容器镜像管理指令
### 目前运行中的容器的一些详细信息
```shell
docker ps [-a]
# -a 列出所有容器，包括已停止的容器
```

### 列出本地的镜像
```shell
docker images
```

### 提供 bash并进入容器
```shell
docker exec -it container_name|container_id /bin/bash
```

### 通过容器的名称和 ID来获取更多有关某个容器的信息
```shell
docker inspect container_name
```

### 查看这个运行中的容器内，有哪些文件被改动过
```shell
docker diff container_name
```

### 该容器的日志
```shell
docker logs container_name
```

### 删除某个容器
```shell
docker rm container_name|container_id
```

### 删除某个镜像
```shell
docker rmi image_name|image_id
```

### 清理已停止的容器
```shell
docker rm -v $(docker ps -aq -f status=exited)
# -v参数在这里意味着当所有由 Docker管理的数据卷已经没有和任何容器有关联时，都会一律删除
```

### 重新生成一个新 tag的镜像
```shell
docker tag [OPTIONS] IMAGE[:TAG] [REGISTRYHOST/][USERNAME/]NAME[:TAG]
docker tag ubuntu:15.10 test/ubuntu:v3
# 标记本地镜像，并将其归入某一仓库
```

