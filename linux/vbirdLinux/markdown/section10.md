## 第十章:认识与学习 BASH

### 10.1 认识 BASH这个 Shell

#### 10.1.1 硬件、核心与Shell

用户 --->  使用者界面(Shell, KDE, application)  --->  核心(kernel)  --->  硬件(Hardware)

#### 10.1.2 为何要学命令行的shell

- 各家 distributions使用的 bash都一样
- 远端管理：命令行的传输速度比较快

#### 10.1.3 系统的合法shell与/etc/shells功能

- Shell版本
  - Bourne Shell(sh)
  - Sun的 C Shell
  - 商业上的 K Shell
  - TCSH
  - Bourne Again Shell(bash)
- /etc/shells 可以看到可用的 shells 

#### 10.1.4 Bash shell的功能

- 命令编修能力(history)
  - 默认记录 1000个
  - 在 .bash_history中存储
  - 这一次的命令行会暂存在内存中
- 命令与文件补全功能( [tab]按键的好处)
  - 命令补全
  - 文件补齐
- 命令别名设置功能(alias)
  - `alias lm='ls -a'`
- 工作控制、前景背景控制(job control, foreground, background)
- 程序化脚本(shell scripts)
- 万用字符(Wildcard)

#### 10.1.5 查询指令是否为Bash shell的内置命名: type

- 查看某个指令是来自于外部指令(指非 bash所提供的命令)，还是内置 bash的指令
- `type [-tpa] name`
- 也可以作为类似 which指令的用途，找指令用的

#### 10.1.6 指令的下达与快速编辑按钮

- `\[Enter]` 换行输入

- | 组合键            | 功能与示范                                 |
  | ----------------- | ------------------------------------------ |
  | [ctrl]+u/[ctrl]+k | 分别是从光标处 向前删除或 向后删除指令串   |
  | [ctrl]+a/[ctrl]+e | 分别是让光标移动到指令串的 最前面或 最后面 |

### 10.2 Shell的变量功能

变量对于 bash非常重要

#### 10.2.1 什么是变量

- 让一个特定字符串代表不固定的内容
- 变量的可变性与方便性
- 影响 bash环境操作的变量
- 脚本程序设计(shell script) 的好帮手

#### 10.2.2 变量的取用与设置:echo,变量设置规则,unset

- 变量的取用
  - `echo $variable`
  - `echo $PATH`
  - `echo ${PATH}`
- 设置
  - `myname=abc`
  - `echo ${myname}`
- 变量的设置规则
  - 变量与变量内容以一个等号"="来链接
  - 等号两边不能直接接空白字符
  - 变量名称只能是英文字母与数字，但是开头字符不能是数字
  - 变量内容若有空白字符可使用双引号或 单引号将变量内容结合起来
    - 双引号中可识别变量
    - 单引号中仅为一般字符串
  - 可用跳脱字符`\`将特殊字符变成一般字符（转义字符）
  - 在一串指令中的执行中，还需要由其他额外的指令所提供的信息，可以使用 反单引号或 $(指令)
  - 若该变量为扩增变量内容时，可用 `$变量名称` 或 `${变量}`累加内容
  - 若该变量需要在其他子程序执行，则需要以 export来使变量变成环境变量
  - 通常大写字符为系统默认变量，自行设置变量可使用小写字符
  - 取消变量的方法是使用 unset: `unset 变量名称`

#### 10.2.3 环境变量的功能

- 用 `env`观察环境变量与常见环境变量说明
  - `env`
  - 列出所有的环境变量
  - 包括 export导出的变量
- 用 `set`观察所有变量(含环境变量与 自订变量)
- `PS1` 观察字符的设置
- `$` 关于本shell的PID
- `?` 关于上个执行命令的回传值
- OSTYPE,HOSTTYPE,MACHTYPE 主机硬件与核心的等级
- `export` 自订变量转成环境变量

#### 10.2.4 影响显示结果的语系变量(locale)

- 查询 linux支持的语系
  - `locale -a`
- 整体系统的默认语系定义在 locale.conf

#### 10.2.5 变量的有效范围

- 环境变量=全域变量
- 自订变量=区域变量

#### 10.2.6 变量键盘的读取、阵列与宣告: read,array,declare

- `read`
  - 读取来自键盘输入的变量
  - `read [-pt] variable`
- `declare/typeset`
  - 宣告变量的类型
  - `declare -x sum` 将 sum变成环境变量
  - `declare -r sum` 将 sum变成只读属性
  - `declare +x sum` 将 sum取消环境变量
  - `declare -p sum` 单独列出变量的类型
- bash对变量的定义
  - 变量类型默认为 字符串
  - bash环境中的数值运算，默认最多仅能达到整数形态，1/3 = 0
- 阵列(array) 变量类型
  - `var[index]=content` 设置阵列的每一个 item
  - `echo "${var[1]},${var[2]},${var[3]}"`

#### 10.2.7 与文件系统及程序的限制关系: ulimit

- `ulimit [-SHacdfltu] [配额]`
- 限制使用者的某些系统资源
- `ulimit -a` 列出目前身份的所有限制数据数值
- `ulimit -f 10240` 限制使用者仅能创建 10M以下容量的文件

#### 10.2.8 变量内容的删除、取代与替换

- `path=${PATH}`

- `echo ${path}`

- `echo ${path#/*local/bin:}`  删除 path变量中的 local/bin

- `#` 代表从前面开始删除，仅删除最短的那个，`*` 来取代 0到无穷多个字符

- `##` 代表删除最长的那个

- `:` 代表截止位置

- `%` 代表从后面向前删除变量内容

- | 变量设置方式                                  | 说明                                                         |
  | --------------------------------------------- | ------------------------------------------------------------ |
  | ${变量#关键字} \${变量##关键字}               | 若变量内容从头开始的数据符合“关键字”，则将符合的最短数据删除，若变量内容从头开始的数据符合“关键字”，则将符合的最长数据删除 |
  | ${变量%关键字} \${变量%%关键字}               | 若变量内容从尾向前的数据符合“关键字”，则将符合的最短数据删除，若变量内容从未向前的数据符合“关键字”，则将符合的最长数据删除 |
  | ${变量/旧字串/新字串} \${变量//旧字串/新字串} | 若变量内容符合“旧字串”则第一个旧字串会被新字串取代，若变量内容符合“旧字串”则全部的旧字串会被新字串取代 |

- 变量的测试与内容替换

  - `echo ${username} `  -->  ''

  - `username=${username-root}`

  - `echo ${username}`  -->  root

  - `username="test"`

  - `username=${username-root}`   -->  test

	### 10.3 命令别名与历史命令

#### 10.3.1 命令别名设置:alias,unalias

- `alias lm='ls -al | more'`
- `alias rm='rm -i'`
- `alias`
- `unalias lm`

#### 10.3.2 历史命令:history

- `alias h='history'`
- `history [n]` 列出最近 n条命令
- `history [-c]` 清除所有 history
- `history [-raw] hisfiles`
- 历史命令的读取与记录过程
  - 以 bash登录主机，会从 ~/.bash_history读取命令，条数跟 HISTFILESIZE有关
  - 登出时，会将历史记录更新到 ~/.bash_history
  - `history -w`强制写入
- 同一账号同时多次登录的 history写入问题
  - 会记录最后登出的那个 bash
  - 其他 bash命令也会被记录，但是会被最后一个覆盖更新
- 无法记录时间
  - 可以通过 ~/.bash_logout来进行 history的记录，并加上 date来增加时间参数


### 10.4 Bash Shell的操作环境

#### 10.4.1 路径与指令搜寻顺序

- 指令运行的顺序
  1. 以相对/绝对路径执行指令，eg: `/bin/ls` 或 `./ls`
  2. 由 alias找到该指令来执行
  3. 由 bash内置的(builtin)指令来执行
  4. 通过 $PATH这个变量的顺序搜寻到的第一个指令来执行
  5. 先 alias再 builtin再由 $PATH找到 /bin/echo

#### 10.4.2 bash的进站与欢迎讯息: /etc/issue, /etc/motd

-  终端机接口(tty1~tty6)登录时所提示的文字在 ` /etc/issue`中
- `/etc/issue.net`是提供给 telnet这个远端登录程序用的
- `/etc/motd` 记录着 当登陆后，告诉登录者的消息

#### 10.4.3 bash的环境配置文件

- login与 non-login shell
  - login shell
    - 取得 bash时需要完整的登录流程
    - login shell会读取两个配置文件
      1. `/etc/profile` 系统整体的设置
         - 利用使用者的 UID来决定很多重要的变量数据
         - 设置的变量还有 PATH, MAIL, USER, HOSTNAME, HISTSIZE, umask
         - 调用外部的数据
         - `/etc/profile.d/*.sh` 所有拓展名为 .sh的，并且用户有 r权限，那么该文件都会被 /etc/profile调用进来
         - `/etc/locale.conf` 由 /etc/profile.d/lang.sh调用进来，最重要的是 LANG/LC_ALL
         - `/usr/share/bash-comletion/completions/*` 由 /etc/profile.d/bash_completion.sh载入，主要是命令补齐，文件名补齐
      2. `~/.bash_profile或 ~/.bash_login或 ~/.profile` 属于使用者个人设置
         - bash在读完 /etc/profile，再依次读取个人配置文件 ~/.bash_profile, ~/.bash_login, ~/.profile
         - bash的 login shell设置只会读取 其中一个文件，顺序如上所述
         - `~/.bash_profile` 通过 sourse指令来读取，最后会读取 `~/.bashrc`的内容
    - source 读入环境配置文件的指令
      - 修改配置文件之后，不需要先登出再登录来生效设置
      - 直接读取配置文件到当前的环境中
  - non-login shell: 取得 bash接口的方法不需要重复登录
    - 仅会读取 `~/.bashrc`
    - 还会主动调用`/etc/bashrc`，其内容：
      - 依据不同的 UID规范出 umask的值
      - 依据不同的 UID规范出提示字符（S1变量）
      - 调用 /etc/profile.d/*.sh的设置
    - 是 RedHat系统特有的，其他 distributions可能有不同的文件名
  - 其他配置文件
    - `/etc/man_db.conf` 规范使用 man
    - `~/.bash_history` 与 HISTFIOESIZE变量有关
    - `~/.bash_logout` 记录了 登出bash需要做的动作

#### 10.4.4 终端机的环境设置: stty,set

- linux distributions已经提供了 使用者环境

- 某些 Unix like的机器中，需要自己来配置一些 按键

- stty (setting tty终端机的意思)可以帮助设置终端机的输入按键代表意义

- `stty [-a]` 将目前所有的 stty参数列出来

  - intr: interrupt中断的讯号给正在 run的程序
  - quit: quit的讯号给正在 run的程序
  - erase: 向后删除字符
  - kill: 删除在目前命令行上的文字
  - eof: End of file，结束输入
  - start: 在某个程序停止后，重新启动它的 output
  - stop: 停止目前屏幕的输出
  - susp: terminal stop的讯号给正在 run的程序

- set 除了来显示一些 变量，还可以设置这个指令输出/输入的环境

  - `set [-uvCHhmBx]`
  - `echo $-` $-变量内容就是 set的所有设置

- bash的默认组合键

  | 组合按键 | 执行结果                     |
  | -------- | ---------------------------- |
  | Ctrl + C | 终止目前命令                 |
  | Ctrl + D | 输入结束 EOF                 |
  | Ctrl + M | Enter                        |
  | Ctrl + S | 暂停屏幕的输出               |
  | Ctrl + Q | 恢复屏幕的输出               |
  | Ctrl + U | 在提示字符下，将整列命令删除 |
  | Ctrl + Z | 暂停目前的命令               |

#### 10.4.5 万用字符与特殊字符

- 万用字符（wildcard）

  | 符号 | 意义 |
  | ---- | ---- |
  | *    |      |
  | ?    |      |
  | []   |      |
  | [-]  |      |
  | [^]  |      |

- 特殊符合

  | 符号  | 意义                                        |
  | ----- | ------------------------------------------- |
  | #     |                                             |
  | \     |                                             |
  | \|    | 管线（pipe）:分隔两个管线命令的界定         |
  | ;     |                                             |
  | ~     |                                             |
  | $     |                                             |
  | &     |                                             |
  | !     |                                             |
  | /     |                                             |
  | >, >> | 数据流重导向：输出导向，分别是 取代 和 累加 |
  | <, << | 数据流重导向：输入导向                      |
  | ''    |                                             |
  | ""    |                                             |
  | ``    |                                             |
  | ()    | 在中间的为 子shell的起始与结束              |
  | {}    | 在中间为命令区块的组合                      |
