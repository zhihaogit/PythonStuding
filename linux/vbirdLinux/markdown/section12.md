## 第十二章:学习 Shell Script

shell script像早期的批处理文件，亦即将一些指令汇整起来一次执行，但是它可以进行类似程序（program）的撰写，并且不需要经过编译（compile）就能够执行

#### 12.1 什么是 Shell Script

Shell Script可以简单的看成是批处理文件，也可以看成是一个程序语言，且这个程序语言由于都是利用 shell与相关工具指令，所以不需要编译即可执行，且拥有不错的 debug工具

#### 12.1.1 干嘛学习 shell script

- 自动化管理的重要依据
- 追踪与管理系统的重要工作
- 简单入侵侦测功能
- 连续指令单一化
- 简易的数据处理
- 跨平台支持与学习历程较短

#### 12.1.2 第一支 script的撰写与执行

- 注意事项

  - 指令的执行是从上而下、从左而右的分析与执行
  - 指令的下达：指令、选项与参数间的多个空白都会被忽略掉
  - 空白行也将被忽略掉，并且 [tab]按键所推开的空白同样视为空白键
  - 如果读取到一个 Enter符号（CR），就尝试开始执行该行（或该串）命令
  - 使用 [Enter]将内容过多的行，延伸到下一行
  - `#`可做注解

- 执行文件

  - 直接指令下达：shell.sh文件必须要具备可读与可执行（rx）的权限
    - 绝对路径
    - 相对路径
    - 变量 PATH功能：将 shell.sh放到 PATH指定的目录内
  - 以 bash程序来执行，bash shell.sh或 sh shell.sh

- ``````shell
  # !/bin/bash
  # Program:
  #		This program shows 'hello world!' in your screen
  # History
  # 2020/03/24 HaHa First release
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  echo -e 'Hello world! \a \n'
  exit 0
  ``````

#### 12.1.3 撰写 shell script的良好习惯创建

每个 script的文件开始处记录

- script的功能
- script的版本信息
- script的作者与联络方式
- script的版权宣告方式
- script的 History（历史记录）
- script内较特殊的指令，使用 绝对路径的方式来下达
- script运行时需要的环境变量预先宣告与设置

### 12.2 简单的 shell script练习

#### 12.2.1 简单范例

- 对谈式脚本：变量内容由使用者决定

  ```shell
  # !/bin/bash
  # Program:
  #		User inputs his first name and last name. Program shows his full name.
  # History:
  # 2020/03/24 haha First release
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  read -p 'Please input your first name:' firstname
  read -p 'Please input your last name': lastname
  echo -e "\n Your full name is: ${firstname} ${lastname}"
  ```

- 随日期变化：利用 date进行文件的创建

  ```shell
  # !/bin/bash
  # Program:
  #		User inputs his first name and last name. Program shows his full name.
  # History:
  # 2020/03/24 haha First release
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  echo -e "I will use touch command to create 3 files."
  read -p "Please input your filename:" fileuser
  # 避免使用者随意按 Enter，利用变量功能
  filename=${fileuser:-"filename"} # 判断是否有配置文件名
  
  date1=$(date --date='2 days ago' + %Y%m%d)
  date2=$(date --date='1 days ago' + %Y%m%d)
  date3=$(date +%Y%m%d)
  file1=${filename}${date1}
  file2=${filename}${date2}
  file3=${filename}${date3}
  
  touch "${file1}"
  touch "${file2}"
  touch "${file3}"
  ```

- 数值运算：简单的加减乘除

  ```shell
  # !/bin/bash
  # Program:
  #		User inputs his first name and last name. Program shows his full name.
  # History:
  # 2020/03/24 haha First release
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  echo -e "You SHOULD input 2 numbers, I will multiplying them! \n"
  read -p 'first number: ' firstnu
  read -p 'second number: ' secnu
  total=$((${firstnu}*${secnu}))
  echo -e "\nThe result of ${firstnu} X ${secnu} is ==> ${total}"
  ```

- 数值运算：通过 bc计算 pi

  `bc`可协助计算含有小数点的数据

  `echo "123.123*55.9" | bc`

  ```shell
  # !/bin/bash
  # Program:
  #		User inputs his first name and last name. Program shows his full name.
  # History:
  # 2020/03/24 haha First release
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  echo -e "This program will calculate pi value. \n"
  echo -e "You should input a float number to calculate pi value. \n"
  read -p 'The scale number (10~10000)?' checking
  num=${checking:-"10"} # 开始判断是否有输入数值
  echo -e 'Starting calcuate pi value. Be patient.'
  time echo "scale=${num}; 4*a(1)" | bc -lq
  ```

#### 12.2.2 script的执行差异（source, sh script, ./script）

- 利用直接执行的方式来执行 script
  - 直接指令下达（不论是绝对路径，相对路径还是${PATH}内），或者是利用 bash(sh)来下达，该 script都会使用一个新的 bash环境来执行脚本内的指令
  - script是在子程序的 bash内执行
  - script中定义的变量，在 bash环境下是无效的
- 利用 source来执行脚本：在父程序中执行
  - `source sh.sh`
  - `source`对 script的执行是在原本的 bash中
  - 所以会有 `source ~/.bashrc`来使一些修改不用在登出系统的情况下生效