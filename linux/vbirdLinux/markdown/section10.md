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

    | 符号 | 意义                                                |
    | ---- | --------------------------------------------------- |
    | *    | 代表 "0个到无穷多个"任意字符                        |
    | ?    | 代表 "一定有一个"任意字符                           |
    | []   | 同样代表 "一定有一个在括号内"的字符（非任意字符）   |
    | [-]  | 若有减号在中括号内时，代表 "在编码顺序内的所有字符" |
    | [^]  | 若中括号内的第一个字符为指数符号，表示 "反向选择"   |

  - 特殊符合

    | 符号  | 意义                                               |
    | ----- | -------------------------------------------------- |
    | #     | 注释符号                                           |
    | \     | 跳脱符号：将 特殊字符或万用字符还原成一般字符      |
    | \|    | 管线（pipe）:分隔两个管线命令的界定                |
    | ;     | 连续指令下达分隔符号：连续性命令的界定             |
    | ~     | 使用者的主目录                                     |
    | $     | 取用变量前置字符：亦即是变量之前需要加的变量取代值 |
    | &     | 工作控制（job control）：将指令变成背景下工作      |
    | !     | 逻辑运算意义上的非 not的意思                       |
    | /     | 目录符号：路径分隔的符号                           |
    | >, >> | 数据流重导向：输出导向，分别是 取代 和 累加        |
    | <, << | 数据流重导向：输入导向                             |
    | ''    | 单引号，不具有变量置换的功能（$变为纯文本）        |
    | ""    | 具有变量置换的功能（$可保留相关功能）              |
    | ``    | 中间为可执行的指令，亦可使用 $()                   |
    | ()    | 在中间的为 子shell的起始与结束                     |
    | {}    | 在中间为命令区块的组合                             |

  ### 10.5 数据流重导向

  redirect(数据流重导向)，就是将某个指令执行后应该要出现在屏幕上的数据，给他传输到其他的地方

  #### 10.5.1 什么是数据流重导向

  standard output和 standard error output分别代表 标准输出（STDOUT）与 标准错误输出（STDERR）。标准输出指的是 指令执行所回传的正确的讯息，而标准错误输出是 指令执行失败后，所回传的错误讯息

  - 数据流重导向可以将 standard output和 standard error output分别传送到其他的文件或设备去，而分别传送所用的特殊字符如下：
    - 标准输入（stdin）：代码为 0，使用 <或 <<
    - 标准输出（stdout）：代码为 1，使用 >或 >>
    - 标准错误输出（stderr）：代码为 2，使用 2>或 2>>

  - `ll / > ~/rootfile`

    - 该文件 rootfile若不存在，系统会自动的将它创建起来

    - 当这个文件存在的时候，那么系统就会先把这个文件内容清空，然后再将数据写入

    - 若以 `>`输出到一个已存在的文件中，那个文件将会被覆盖掉

    - 不想删除旧数据，可以使用 `>>`来累加数据，文件不存在就创建，存在就累加数据

    - `1>`：以覆盖的方法将正确的数据输出到指定的文件或设备上

    - `1>>`：以累加的方法将正确的数据输出到...

    - `2>`：以覆盖的方法将错误的数据输出到...

    - `2>>`：以累加的方法将错误的数据输出到...

      

  - 将正确的与错误的数据分别存入到不同的文件中

    `find /home -name .bashrc > list_right 2> list_error`

  - `/dev/null`垃圾桶黑洞设备和特殊写法

    /dev/null可以吃掉任何导向这个设备的信息，可以实现将错误讯息忽略掉而不显示或存储

    `find /home -name .bashrc 2> /dev/null`

  - 将正确和错误的数据写入同一个文件

    `find /home -name .bashrc > list 2>&1`

    `find /home -name .bashrc &> list`

  - standard input：<与 <<

    将原本需要由键盘输入的数据，改由文件内容来取代

    ```shell
    cat > catfile
      testing
      cat file test 
      < [ctrl] + d
    ```

    用某个文件的内容来取代键盘的敲击

    `cat > catfile < ~/.bashrc`

    `<<`表示结束的输入字符，eg: 用 cat直接将输入的信息输出到 catfile中，且当键盘输入 eof时，该次输入就结束

    ```shell
    cat > catfile << 'eof'
      this is a test
      ok now stop
      eof < 输入关键字，立刻结束而不需要输入 [ctrl] + d
    ```

  - `2>&1 1>&2`

  #### 10.5.2 命令执行的判断依据  ;   &&   || 

  - cmd;cmd 不考虑指令相关性的连续指令下达

    一次执行多个指令，分号前的指令执行完后就会立刻接着执行后面的指令

  -  $? （指令回传值）与 && 或 ||

    两个指令之间有相依性，而这个相依性主要判断的地方在于前一个指令执行的结果是否正确。若前一个指令执行的结果为正确，在 linux下面会回传一个 $? = 0的值

    - cmd1 && cmd2 ： 若 cmd1执行完毕且正确执行（`$?=0`），则开始执行 cmd2，若 cmd1执行完毕且为错误（`$?≠0`）,则 cm2不执行
    - cmd1 || cmd2：cmd1执行完毕且正确执行，cmd2不执行。若 cmd1执行完毕且为错误，则开始执行 cmd2

  - `ls /tmp/abc || mkdir /tmp/abc && touch /tmp/abc/hehe`

    如果某个目录不存在，就创建该目录，并且在目录下创建一个文件

  - `ls /tmp/abc && echo 'exist' || echo 'no exist'`

  - 假设判断式有三个

    `command1 && command2 || command3`

### 10.6 管线命令（pipe）

- `ls -al /etc | less`
- 管线命令前一个命令需要有 standard output，后一个命令需要接收 standard input
  - 管线命令仅会处理 standard output，对于 standard error output会忽略
  - 管线命令必须要能接受来自前一个指令的数据成为 standard input继续处理才行
- 硬要 standard error output被管线命令接收，可以使用数据流重导向，`2>&1`

#### 10.6.1 撷取命令：cut, grep

- `cut` 将一段信息切出来，操作的单位是行

  ```shell
  cut -d '分隔字符' -f fields # 用于特定分隔字符
  cut -c '字符区间'						# 用于排列整齐的信息
  -d # 后面接分隔字符，与 -f一起使用
  -f # 依据 -d的分隔字符讲一段信息分成几段，用 -f取出第几段
  -c # 以字符（characters）的单位取出固定字符区间
  
  echo ${PATH} | cut -d ':' -f 3,5
  export | cut -c 12- # export出的信息，取出 12行到末尾
  last | cut -d ' ' -f 1 # 显示登陆者的信息
  ```

- `grep` 分析一段信息，找出需要的

  ``````shell
  grep [-acinv] [--color=auto] '搜寻字段' filename
  -a # 将 binary文件以 text文件的方式搜寻数据
  -c # 计算找到 '搜寻字串'的次数
  -i # 忽略大小写的区别
  -n # 顺便输出行号
  -v # 反向选择，亦即显示出没有 '搜寻字串'内容的那一行
  --color=auto # 高亮关键字
  
  last | grep root
  last | grep -v root # 找出不是 root的用户
  last | grep root | cut -d ' ' -f1
  grep --color=auto 'MANPATH' /etc/man_db.conf
  ``````

#### 10.6.2 排序命令：sort, wc, uniq

- `sort` 排序

  ``````shell
  sort [-fbMnrtuk] [file or stdin]
  ``````

- `uniq` 去重

  ``````shell
  uniq [-ic]
  -i # 忽略大小写
  -c # 进行计数
  ``````

- `wc` 输出信息的整体数据

  ``````shell
  wc [-lwm]
  -l # 仅列出行
  -w # 仅列出多少字（英文单词）
  -m # 多少字符
  ``````

#### 10.6.3 双向重导向：tee

- `tee`指令会同时将数据流分送到文件和屏幕，输出到屏幕的是 stdout，就可以让下个指令继续处理

- `````shell
  tee [-a] file
  -a # 以累加的（append）的方式，将数据加入 file当中
  
  last | tee last.list | cut -d ' ' -f1 # 将 last的输出存一份到 last.list中
  ls -l /home | tee ~/homefile | more # 将 ls的数据存一份到 ~/homefile，同时输出到屏幕上
  ls -l / | tee -a ~/homefile | more # 不覆盖 homefile的内容，累加到里面
  `````

#### 10.6.4 字符转换命令：tr, col, join, paste, expand

- `tr` 用来删除一段信息中的文字，或者是进行文字信息的替换
- `col` 将 [tab]按键取代称为空白键
- `join` 处理两个文件，有相同数据的那一行，将它们加在一起，一般先将文件 sort处理，否则有些比对的项目会被略过
- `paste` 不对比两个文件的数据相关性，直接将两行贴在一起，中间用 [tab]键隔开
- `expand` 将 [tab]键转成空白键

#### 10.6.5 分区命令：split

``````shell
split [-bl] file PREFIX
-b # 后面可接欲分区成的文件大小，可加单位，如：b, k, m
-l # 以行数来进行分区
PREFIX # 代表前置字符的意思，可作为分区文件的前导文字

cd /tmp; split -b 300k /etc/services services # 拆文件
cat services* >> servicesback # 合并文件
ls -al / | split -l 10 - lsroot
``````

#### 10.6.6 参数代换：xargs

- `xargs`可以读入 stdin的数据，并且以空白字符或断行字符作为分辨，将 stdin的数据分隔成 arguments

- 因为是以空白字符作为分隔，有些文件名或语句内含有空白字符，`xargs`可能会误判

- ``````shell
  xargs [-øepn] command
  -ø # 如果输入的 stdin含有特殊字符，该参数可以将它还原成一般字符
  -e # 这个是 EOF（end of file），后面接一个字符，识别到字符后，将停止
  -p # 执行每个指令的 argument时，都会询问使用者的意思
  -n # 后面接次数，每次 command指令执行时，要使用几个参数
  ``````

- 很多指令不支持管线命令，可以通过 xargs来提供该指令引用 standard input

#### 10.6.7 关于减号-的用途

- 在管线命令中，会用到前一个指令的 stdout作为这次的 stdin，某些指令需要用到文件名称（如 tar）来进行处理，该 stdin与 stout可以利用减号-替代

- ``````shell
  mkdir /tmp/homeback
  tar -cvf - /home | tar -xvf - -C /tmp/homeback
  ``````

