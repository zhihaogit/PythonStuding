##  第八章:文件与文件系统的压缩，打包与备份

### 8.1 压缩文件的用途与技术

- 目前计算机系统中是使用所谓的 Bytes单位来计量
- 1Bytes = 8bits
- WWW网站压缩技术

### 8.2 Linux系统常见的压缩指令

- 压缩文件拓展名
  - `*.z`  compress程序压缩的文件
  - `*.zip`  zip程序压缩的文件
  - `*.gz`  gzip程序压缩的文件
  - `*.bzz`  bzip2程序压缩的文件
  - `*.xz`  xz程序压缩的文件
  - `*.tar`  tar程序打包的数据
  - `*.tar.gz`  tar程序打包的文件，经过 gzip压缩
  - `*.tar.bzz`  tar程序打包的文件，经过 bzip2压缩
  - `*.tar.xz`  tar程序打包的文件，经过 xz压缩

#### 8.2.1 gzip,zcat/zmore/zless/zgrep

- gzip可以解开 compress,zip,gzip等软件压缩的文件
- `gzip [-cdtv#] 文件名`
  - -c 将压缩的数据输出到屏幕上，可通过数据流重导向来处理
  - -d 解压缩
  - gunzip 解压缩
  - -t 可以用来检验一下压缩文件的一致性，检查错误
  - -v 可以显示元文件/压缩文件的压缩比等信息
  - -# #是数字，代表压缩等级，1~9(压缩比最好)，默认为6
- gzip 压缩的文件可以在 window系统上被解压
- zcat/zmore/zless 可以读取纯文本文件压缩后的文件
- zgrep 来搜寻压缩文件中的关键字

#### 8.2.2 bzip2,bzcat/bzmore/bzless/bzgrep

- bzip2为了取代 gzip来提供更好的压缩比
- `bzip2 [-cdkzv#] 文件名`
  - -k  保留原始文件
  - -z  压缩的参数，默认值
  - 其他参数类似 gzip的参数
- bzcat/bzmore/bzless 可以读取纯文本文件压缩后的文件
- bzgrep来搜寻压缩文件中的关键字

#### 8.2.3 xz,xzcat/xzmore/xzless/xzgrep

- xz比 bzip2的压缩比要更高，但时间更久
- `xz [-dtlkc#] 文件名`
  - -l 列出压缩文件的相关信息
  - 其他参数类似 gzip, bzip2的参数

### 8.3 打包指令: tar

将多个文件或目录包成一个大文件的指令功能就是打包指令

#### 8.3.1 tar

- 常用 tar命令及参数
  - `tar [-z | -j | -J] [cv] [-f 待创建的新文件名] filename`  打包
  - `tar [-z | -j | -J] [tv] [-f 既有的 tar文件名]`  察看
  - `tar [-z | -j | -J] [xv] [-f 既有的 tar文件名] [-C 目录]`  解压
  - `-c`  创建打包文件，可搭配 -v来查看过程中的被打包文件名
  - `-t`  查看打包文件的内容有哪些文件名
  - `-x`  解打包或解压缩，搭配 -C在特定目录解开
  - `-c, -t, -x` 不可同时出现在一行命令中
  - `-z`  通过 gzip来压缩或解压，文件名：*.tar.gz
  - `-j`  通过 bzip2来压缩或解压，文件名：*.tar.bz2
  - `-J`  通过 xz来压缩或解压，文件名：*.tar.xz
  - `-z, -j, -J` 不可同时出现在一行命令中
  - `-v`  在压缩或解压过程中，将正在处理的文件名显示出来
  - `-f filename`  -f后面直接接要被处理的文件名
  - `-C 目录`  在特定目录进行解压
  - `-p`  保留备份数据的原本权限与属性
  - `-P`  保留绝对路径，允许备份数据包含根目录
- 简单的使用方式
  - `tar -jcv -f filename.tar.bz2 要被压缩的目录或目录名称`  压缩
  - `tar -jtv -f filename.tar.bz2`  查询
  - `tar -jxv -f filename.tar.bz2 -C 欲解压的目录`  解压
- 打包某目录，但不包含该目录下的某些文件
  - `--exclude`  不包含
  - eg: `tar -jcv -f /root/system.tar.bz2 --exclude=/root/etc*`
- 仅备份比某个时刻还要新的文件
  - `--newer-mtime`  后续日期只包含 mtime
  - `--newer`  后续日期包含 mtime和 ctime
  - eg: `tar -jcv -f /root/etc.newer.then.passwd.tar.bz2 --newer-mtime="2019/08/13" /etc/*`
- 基本名称 tarfile, tarball
  - tar打包出来的文件没有进行压缩，叫作 tarfile
  - tar打包出来的文件有进行压缩，叫作 tarball
- 特殊应用: 利用管线命令与数据流
  - eg: `tar -cvf - /etc | tar -xvf -` 将 /etc的数据压缩并解压到 当前所在目录

### 8.4 XFS文件系统的备份与还原

xfs文件系统中，xfsdump和 xfsrestore

#### 8.4.1 XFS文件系统备份 xfsdump

- xfsdump 可以进行文件系统的完整备份(full backup)，还可以进行累积备份(Incremental backup)，备份有变化的文件
- 限制
  - xfsdump只备份已挂载的文件系统
  - 只有 root权限才能操作
  - 只能备份 XFS文件系统
  - 备份下来的数据只能通过 xfsrestore解析
  - 可以通过文件系统的 UUID来分辨备份文件，不能备份两个相同 UUID的文件系统
- 指令
  - `xfsdump [-L S_label] [-M M_label] [-l #] [-f 备份文件] 待备份数据`
  - `xfsdump -I` 从 /var/lib/xfsdump/inventory 列出目前备份的信息状态

#### 8.4.2 XFS文件系统还原 xfsrestore

- xfsdump的复原使用的是 xfsrestore指令
- `xfsrestore -I`  查看备份文件数据
  - xfsfdump和 xfsrestore都会从 /var/lib/xfsdump/inventory/里面取数据
- `xfsrestore [-f 备份文件] [-L S_label] [-s] 待复原项目` 
  - 需要被复原的那个文件
  - 该文件的 session label name
  - eg: `xfsrestore -f /srv/boot.dump -L boot_all /boot`
  - 只想要复原某个目录或文件，直接加上 `-s 目录`
- `xfsrestore [-f 备份文件] -r 待复原文件`  通过累积备份文件来复原系统
  - 如果备份数据是由 level0 -> level1 -> level2...去进行的
  - 复原也需要相同的流程
- `xfsrestore [-f 备份文件] -i 待复原文件`  进入互动模式
  - `-s` 可以接部分数据还原
  - `-i` 可以以互动的形式来还原

### 8.5 光盘写入工具

文字模式的烧录行为的通常做法

- 利用 mkisofs指令先将文件创建成为 镜像文件(iso)
- 利用 cdrecord指令来将镜像文件烧录至光盘或DVD

#### 8.5.1 mkisofs: 创建镜像文件

#### 8.5.2 cdrecord: 光盘烧录工具

### 8.6 其他常见的压缩与备份工具

#### 8.6.1 dd

- dd 不只是制作一个文件，更重要的是在 备份
- 可以读取磁盘设备的内容（几乎是直接读取扇区 sector）
- 没有用到的扇区也会写入备份文件，xfsdump只会备份使用到的部分
- 做出来的文件跟原本的数据大小一样
- 新分区的 partition不需要格式化，因为 dd直接将 sector表面的数据都复制来了

#### 8.6.2 cpio

- cpio可以备份任何东西，包括设备文件
- 不会主动的去找文件备份
- 配合 find等可以找到文件名的指令来使用
- `cpio -ovcB > [file|device]`  备份
- `cpio -ivcdu < [file|device]`  还原
- `cpio -ivct < [file|device]`  查看
- eg: `find boot | cpio -ocvB > /tmp/boot.cpio` 
