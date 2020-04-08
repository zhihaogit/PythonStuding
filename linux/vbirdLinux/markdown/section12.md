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

### 12.3 善用判断式

#### 12.3.1 利用 test指令的测试功能

- `test`指令
  - 检测系统上面某些文件或者是相关的属性

  - `test -e /dmtsai && echo 'exist' || echo 'no exist'`

    - 判断某个文件名的文件类型判断 `test -e filename`
    -  `-e`文件名是否存在
    - `-f`是否为文件
    - `-d`是否为目录

  - 关于文件的权限侦测 `test -r filename`

    - `-r` 是否具有 可读权限
    - `-w` 是否具有 可写权限
    - `-x` 是否具有 可执行权限

  - 两个文件之间的比较 `test file1 -nt file2`

    - `-nt` 判断 file1比 file2新
    - `-ot` 判断 file1比 file2旧
    - `-ef` 判断 是否为同一个文件，是否指向同一个 inode

  - 关于两个整数之间的判断 `test n1 -eq n2`

    - `-eq` 两数值相等（equal）
    - `-ne` 两数值不等（not equal）
    - `-gt` n1大于 n2（greater than）
    - `-lt` n1小于 n2（less than）
    - `-ge` n1大于等于 n2（greater than or equal）
    - `-le` n1小于等于 n2（less than or equal）

  - 判定字符串的数据

    - `test -z string` 判断字串是否为0？空字串为 true
    - `test -n string` 判断字串是否非为0？空字串为 false，可省略
    - `test str1 == str2`
    - `test str1 != str2`

  - 多重条件判断

    - `test -r file -a -x file` and判断

    - `test -r file -o -x file` or判断
    - `test ! -x file` 反相状态

- eg

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  # 提示输入，并判断是否有输入字串
  echo -e "Please input a filename, I will check the filename's type and permission. \n\n"
  read -p "Input a filename: " filename
  test -z ${filename} && echo "You Must input a filename." && exit 0
  # 判断文件是否存在？不存在则显示提示并结束脚本
  test ! -e ${filename} && echo "The filename '${filename}' DO NOT exist" && exit 0
  # 开始判断文件类型与属性
  test -f ${filename} && filetype="regulare file"
  test -d ${filename} && filetype="directory"
  test -r ${filename} && perm="readable"
  test -w ${filename} && perm="${perm} writable"
  test -x ${filename} && perm="${perm} executable"
  # 开始输出信息
  echo "The filename: ${filename} is a ${filetype}"
  echo "And the permissions for you are: ${perm}"
  ```

#### 12.3.2 利用判断符号 []

- `[ -z "${HOME}" ] ; echo $?` 判断这个变量是否为空

- 在 bash中，使用一个等号和两个等号的结果是一样的，推荐两等

- 在中括号内的每个元件都需要有空白键来分隔

- 在中括号内的变量，最好都以双引号括号起来

- 在中括号内的常数，最好都以单或双引号括号起来

- eg

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  read -p "Please input (Y/N): " yn
  [ "${yn}" == "Y" -o "${yn}" == "y" ] && echo "ok, continue" && exit 0
  [ "${yn}" == "N" -o "${yn}" == "n" ] && echo "oh, interrupt!" && exit 0
  echo "I don't know what your choice is" && exit 0
  ```

#### 12.3.3 shell script的默认变量（\$0, $1...）

- `$#` 代表后接的参数个数

- `$@` 代表 “"\$1" "\$2" "\$3" "\$4"”，每个变量都是独立的

- `$*` 代表 “ "$1<u>c</u>$2<u>c</u>$3<u>c</u>$4" ” 

- `shift` 会移动变量，后面可接数字，代表拿掉最前面几个参数

- eg

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  echo "The script name is ==> ${0}"
  echo "Total parameter number is ==> $#"
  [ "$#" -lt 2 ] && echo "The number of parameter is less than 2. stop here" && exit 0
  echo "Your whole parameter is ==> '$@'"
  shift # 第一次偏移
  echo "Total parameter number is ==> $#"
  echo "Your whole parameter is ==> '$@'"
  shift 3 # 第二次偏移 3个参数
  echo "Total parameter number is ==> $#"
  echo "Your whole parameter is ==> '$@'"
  echo "The 1st parameter ==> ${1}"
  echo "The 2nd parameter ==> ${2}"
  ```

### 12. 4 条件判断式

#### 12.4.1 利用 if...then

- 单层、简单条件判断式

  ```shell
  if [ 条件判断式 ]; then
  	statement # 条件成立时
  fi # 结束 if语句
  ```

- `&&`代表 AND

- `||`代表 or

- 多重、复杂条件判断式

  ```shell
  if [ 条件判断式1 ]; then
  	statement1
  elif [ 条件判断式2 ]; then
  	statement2
  else
  	statement3
  fi
  ```

- eg 判断输入

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  read -p 'Please input (Y/N): ' yn
  if [ "${yn}" == "Y" ] || [ "${yn}" == "y" ]; then
  	echo 'ok, continue'
  elif [ "${yn}" == 'N' ] || [ "${yn}" == "n" ]; then
  	echo 'Oh, interrupt!'
  else
  	echo 'I do not know what your choice is'
  fi
  ```

- eg 判断网络端口

  - 端口 80: WWW
  - 22: ssh
  - 21: ftp
  - 25: mail
  - 111: RPC(远端程序调用)
  - 631: CUPS(打印服务功能)

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  echo "Now, I will detect your linux server's services!"
  echo -e "The www, ftp, ssh and mail(smtp) will be detect! \n"
  
  testfile=/dev/shm/metstat_checking.txt
  netstat -tuln > ${testfile}
  testing=$(grep ":80" ${testfile})
  if [ "${testing}" != "" ]; then
    echo "WWW is running in your system."
  fi
  testing=$(grep ":22" ${testfile})
  if [ "${testing}" != "" ]; then
    echo "SSH is running in your system"
  fi
  testing=$(grep ":21" ${testfile})
  if [ "${testing}" != "" ]; then
    echo "FTP is running in your system"
  fi
  testing=$(grep ":25" ${testfile})
  if [ "${testing}" != "" ]; then
  	echo "Mail is running in your system"
  fi
  ```

- eg 判断退伍时间

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  echo "This program will try to calculate: "
  echo "How many days before your demobilization date..."
  read -p "Please input your demobilization date (YYYYMMDD ex> 20200716)" date2
  
  date_d=$(echo ${date2} | grep '[0-9]\{8\}')
  if [ "${date_d}" == "" ]; then
  	echo "You input the wrong date format......"
  	exit 1
  fi
  
  # date --date="YYYYMMDD"+%s 转换成秒数
  declare -i date_dem=$(date --date="${date2}" +%s)
  declare -i date_now=$(date +%s)
  declare -i date_total_s=$((${date_dem}-${date_now}))
  declare -i date_d=$((${date_total_s}/60/60/24))
  if [ "${date_total_s}" -lt "0" ]; then
  	echo "You had been demobilization before: " $((-1*${date_d})) "ago"
  else
  	declare -i date_h=$(($((${date_total_s}-${date_d}*60*60*24))/60/60))
  	echo "You will demobilize after ${date_d} days and ${date_h} hours."
  fi
  ```

#### 12.4.2 利用 case...esac判断

- eg

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  case ${1} in
    "hello") # 每个变量内容建议用双引号括起来，关键字则为小括号
      echo 'hello, how are you?'
      ;; # 每个类别的结尾使用两个连续的分号来处理
     "")
     	echo "You MUST input parameters, ex> {${0} someword}"
     	;;
     *) # 最后一个变量内容都用 *来代表所有其他值
     	echo "Usage ${0} {hello}"
     	;;
  esac
  ```

- eg

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  echo "This program will print your sellection!"
  read -p "Input your choice: " choice
  case ${choice} in
    "one")
    echo 'Your choice is ONE'
    ;;
    "two")
    echo 'Your choice is TWO'
    ;;
    'three')
    echo 'Your choice is THREE'
    ;;
    *)
    echo "Usage ${0} {one|two|three}"
    ;;
   esac
  ```

#### 12.4.3 利用 function功能

- function 后面可接参数

- function 内部也有  `${0}` -> 函数名，​`${1}` -> 一参...

- eg

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  function printit() {
  	echo -n 'Your choice is '
  }
  function printParams() {
  	echo ${1}
  }
  function toggleUpper() {
  	tr 'a-z' 'A-Z'
  }
  echo "This program will print your selection!"
  case ${1} in
  	"one")
  	printit ; printParams ${1} | toggleUpper
  	;;
  	"two")
  	printit ; printParams ${1} | toggleUpper
  	;;
  	"three")
  	printit ; printParams ${1} | toggleUpper
  	;;
  	*)
  	echo "Usage ${0} {one|two|three}"
  	;;
  esac
  ```

### 12.5 循环（loop）

#### 12.5.1 while do done, until do done（不定循环）

- eg `while`

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  while [ "${yn}" != "yes" -a "${yn}" != "YES" ] # while关键字后面跟中括号，中括号里面是判断条件
  do # do关键字，循环开始
  	read -p 'Please input yes/YES to stop this program: ' yn
  done # done关键字，循环结束
  echo 'OK! you input the correct answer.'
  ```

- eg `until`

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  until [ "${yn}" == "yes" -o "${yn}" == "YES" ]
  do
    read -p 'Please input yes/YES to stop this program: ' yn
  done
  echo 'OK! you input the correct answer.' 
  ```

- eg `累加`

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  s=0
  i=0
  while [ "${i}" != "100" ]
  do
  	i=$(($i+1))
  	s=$(($s+$i))
  done
  echo "The result is ==> $s" 
  ```

#### 12.5.2 for...do...done（固定循环）

- eg

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  for animal in dog cat elephant
  do
  	echo "There are ${animal}s..."
  done
  ```

- eg

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  users=$(cut -d ':' -f1 /etc/passwd) # 撷取账号名称
  for username in ${users}	# 开始循环进行
  do
  	id ${username}
  done
  ```

- eg `ping`

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  network="192.168.1"
  for sitenu in $(seq 1 100)
  do
    # 判断取得 ping的回值是正确的还是失败的
  	ping -c 1 -w 1 ${network}.${sitenu} &> /dev/null && result=0 || result=1
  	# 正确启动 UP，错误连通 DOEN
  	if [ "${result}" == 0 ]; then
  		echo "Server ${network}.${sitenu} is UP."
  	else
  		echo "Server ${network}.${sitenu} is DOWN."
  	fi
  done
  ```

- eg 检查目录文件权限

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  read -p 'Please input a directory: ' dir
  if [ "${dir}" == "" -o ! -d "${dir}" ]; then
  	echo "The ${dir} is NOT exist in your system."
  	exit 1
  fi
  filelist=$(ls ${dir})
  for filename in ${filelist}
  do
  	perm=""
  	test -r "${dir}/${filename}" && perm="${perm} readable"
  	test -w "${dir}/${filename}" && perm="${perm} writable"
  	test -x "${dir}/${filename}" && perm="${perm} executable"
  	echo "The file ${dir}/${filename}'s permission is ${perm}"
  done
  ```

#### 12.5.3 for...do...done的数值处理

- 格式

  ```shell
  for (( 初始值; 限制值; 执行步阶 ))
  do
  	statement
  done
  ```

- eg

  ```shell
  PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
  export PATH
  
  read -p 'Please input a number, I will count for 1+2+...+your_input: ' nu
  s = 0
  for (( i=1; i<=${nu}; i=i+1 ))
  do
  	s=$((${s}+${i}))
  done
  echo "The result is ==> ${s}"
  ```

#### 12.5.4 搭配乱数与陈列的实验

### 12.6 shell script的追踪与 debug

```shell
sh [-nvx] script.sh
-n: 不要执行 script，仅检查语法的问题
-v: 在执行 script前，先将 scripts的内容输出到屏幕上
-x: 将使用到的 script内容显示到屏幕上，列出执行步骤
```

