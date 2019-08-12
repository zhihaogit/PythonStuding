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
