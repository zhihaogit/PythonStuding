## 第五章:linux的文件权限与目录配置

- 文件的可存取身份：owner/group/others
- 三种身份各有 read/write/execute等权限

### 5.1 使用者与群组

linux使用者身份与群组记录的文件

- `/etc/passwd`这个文件中，记录着所有的系统上的账号与一般身份者及root的相关信息
- `/etc/shadow`记录着个人的密码
- `/etc/group` 记录着所有的群组名称

### 5.2 Linux 文件权限概念

#### 5.2.1 文件属性

```
					  连接数		 所属群组			创建时间或更新时间	
-rw-r--r--.  1  root  root  1864   May 4 18:01  initial-setup-ks.cfg
档案类型权限      owner			 档案容量										档案名字
```

```
	 -     r w x   	r w x  	---
档案类型 owner权限 群组权限 其他人的权限
r：可读     4
w: 可写     2
x: 可执行   1
```

- 第一栏是 文件的类型和权限
  - 第一字符代表文件的类型：目录[d]、文件[-]、链接文件[|]、设备文件里的可供储存的设备(可随机存取设备)[b]、设备文件里的序列埠设备(键盘等，一次性读取设备)[c]
  - 剩下的分别为 owner/group/others的权限
- 第二栏是 多少文件链接到此节点(i-node)
- 第三栏是 表示文件的owner
- 第四栏是 所属群组
- 第五栏是 文件size
- 第六栏是 文件的创建日期或 最近的修改日期
- 第七栏是 文件名

#### 5.2.2 如何改变文件属性与权限

- `chgrp` 改变文件所属群组
  - chgrp [ -R ] dirname/filename
  - -R 递归(recursive)执行
  - eg: chgrp users initial-setup-ks.cfg
- `chown` 改变文件拥有者
  - chown [ -R ] 账号名称  文件或目录 
  - chown [ -R ] 账号名称:群组名称  文件或目录
  - chown [ -R ] 账号名称.群组名称  文件或目录
  - eg: chown root:root initial-setup-ks.cfg
- `chmod` 改变文件的权限，SUID,SGID,SBIT等特性
  - chmod [ -R ] xyz  文件或目录。xyz为数字类型的权限属性(r: 4,w: 2,x: 1) 
  - chmod | u(user|owner) g(group) o(others) a(all) | + (加入) -(去除) =(设置) | r w x | 文件或目录
  - eg: 
    - chmod 777 .bashrc
    - chmod u=rwx,go=rx .bashrc
    - chmod a+w .bashrc
    - chmod a-x .bashrc

#### 5.2.3 目录与文件之权限意义

| 元件 | 内容          | 叠代物件   | r            | w            | x                     |
| ---- | ------------- | ---------- | ------------ | ------------ | --------------------- |
| 文件 | 详细数据 data | 文件数据夹 | 读到文件内容 | 修改文件内容 | 执行文件内容          |
| 目录 | 文件名        | 可分类抽屉 | 读到文件名   | 修改文件名   | 进入该目录的权限(key) |

#### 5.2.4 Linux文件种类与扩展名

- 文件种类
  - 正规文件(regular file)
    - 纯文本文件(ASCII)
    - 二进制(binary)
    - 数据格式文件(data)
  - 目录(directory)
  - 链接文件(link)
  - 设备与设备文件(device)
    - 区块(block)
    - 字符(character)
  - 数据接口文件(sockets)
  - 数据输送档(FIFO，pipe)
- 文件拓展名
  - 没有所谓的拓展名，全靠 权限的`x`来表示是否能执行
  - 常用拓展名
    - `.sh` 脚本或批处理文件(script)
    - `Z`，`.tar`，`.tar.gz`，`.zip` ，`.tgz` 经过打包的压缩文件
    - `.html`、`.php` 网页相关文件
- 文件长度限制
  - 单一文件或目录的最大容许文件名为 255 Bytes
  - 相当于 ASCII英文 255个字符
  - 相当于 中文(每个字符 2Bytes)，128个中文字
- 文件名称限制
  - 避免使用```?><;&![]|\'"`(){}```
  - `.`开头的文件为隐藏文件
  - 避免使用 `+ -`

### 5.3 Linux 目录配置

#### 5.3.1 目录配置的依据 — FHS

- FHS将目录分为四种交互作用的形态

  |                    | 可分享的(shareable)        | 不可分享的(unshareable) |
  | ------------------ | -------------------------- | ----------------------- |
  | 不变的(static)     | /usr (软件放置处)          | /etc (配置文件)         |
  |                    | /opt (第三方协力软件)      | /boot (开机与核心档)    |
  | 可变动的(variable) | /var/mail (使用者邮件信箱) | /var/run (程序相关)     |
  |                    | /var/spool/news (新闻群组) | /var/lock (程序相关)    |

- FHS定义的三个主目录

  - `/`(root，根目录)：与开机系统有关
    - 根目录是最重要的目录
    - 所有的目录都是由根目录衍生出来的
    - 与开机/还原/系统修复等有关
  - `/usr`(unix software resource): 与软件安装/执行有关
    - `/usr`放置的数据属于可分享与不可变动的(shareable, static)
    - 是 Unix Software Resource(Unix操作系统软件资源)所放置的目录
  - `/var`(variable): 与系统运行过程有关
    - `/var`目录主要针对常态性变动的文件，包括高速缓存(cache)、登录文件(log file)
    - 还有某些软件运行所产生的文件，包括程序文件(lock file, run file)，或者 MySQL数据库文件

#### 5.3.2 目录树 (directory tree)

- 目录树的起始点为根目录(/, root)
- 每一目录不止能使用本地端的 partition文件系统，可以用使用网络上的filesystem
- 每个文件在此目录树中的文件名(含完整路径)都是独一无二的
