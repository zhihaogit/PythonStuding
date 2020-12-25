# Docker镜像导入导出
## Docker拷贝镜像文件
### docker save
```shell
docker save -o 要保存的文件名 要保存的镜像
docker save -o my_ubuntu_v3.tar myimages/ubuntu:v3
# -o 输出到的文件
# 保存镜像为文件
```

### docker load
```shell
docker load --input 文件名
docker load < 文件名
docker load < java8.tar
```

## 导出容器的快照
### docker export
```shell
docker export -o 文件名 容器ID
docker export -o mysql.tar a404c6c174a2
# -o 将输入内容写到文件
# 将文件系统作为一个tar归档文件导出到STDOUT
```

### docker import
```shell
docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]
docker import my_ubuntu_v3.tar myimages/ubuntu:v4
# -c 应用 docker指令创建镜像
# -m 提交时的说明文字
# 从归档文件中创建镜像
```

