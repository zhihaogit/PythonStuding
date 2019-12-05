## 第四章:首次登陆与线上求助

### 4.1首次登录系统

#### 4.1.3 x window与文字模式的切换

- linux默认提供6个 terminal
- 切换方式为 [Ctrl] + [Alt] + [F1] ~ [F6]
- 系统将 [F1] ~ [F6]命令为 tty1 ~ tty6
- `startx`启动窗口界面，任何人都可以执行
- `systemctl setdefault graphical.target`将图形化界面设为默认
- `exit`登出系统

### 4.2 文字模式下指令的下达

#### 4.2.1 开始下达指令

```shell
# 格式
[linux@name ~]$ command [-options] parameter1 parameter2 ...
```

0. 一行指令中第一个输入的部分是  [指令 command] 或 [可执行档案 例: 可执行脚本 scrpit]
1. command为指令的名称
2. 中括号[]位置是加入选项设定，通常选项前会带 `-` 号，如 `-h`；也可以是完整指令，选项前带 `—`号，如 `--help`
3. parameter1 parameter2.. 为依附在选项后面的参数，或者是 command的参数
4. 指令，选项，参数之间用空格来区分，不论空几格shell都视为一格。空格是很重要的特殊字元
5. 按下 Enter按键后，该指令就立即执行。它代表着一行指令的开始启动
6. 指令太长，可以使用反斜杠 `/`来跳脱 Enter符号
7. linux系统区分 英文字母大小写

语系支持

- `locale`显示目前所支持的语系
- `LANG=en_US.utf8`、`export LC_ALL=en_US.utf8`，LANG只与输出信息有关系。若需要更改其他不同信息，还要同步更新LC_ALL

#### 4.2.2 基础指令的操作

- `date`显示日期与时间
- `cal` 显示日历
- `bc` 计算器

### 4.3 man page与 Info page

- man page

  | 代号 | 代表内容                                                     |
  | ---- | ------------------------------------------------------------ |
  | 1    | 用户可以在shell中操作的指令或可执行文件                      |
  | 2    | 系统核心可调用的函数与工具                                   |
  | 3    | 一些常用的函数(function)或函数库(library)，大部分为C的函数库(libc) |
  | 4    | 设备文件的说明，通常在/dev下的文件                           |
  | 5    | 配置文件或某些文件的格式                                     |
  | 6    | 游戏                                                         |
  | 7    | 惯例与协议，如Linux文件系统、网络协定、ASCII code            |
  | 8    | 系统管理员可用的管理指令                                     |
  | 9    | 跟 kernel有关的文件                                          |

### 4.4 文本编辑器：nano

`^`代表 `Ctrl`按键

### 4.5 正确关机方法

- `who` 查看目前有谁在线上
- `netsat -a` 查看网络的连线状态
- `ps -aux` 查看后台执行的程序
- `sync` 将数据同步写入硬盘中
- `shutdown` 常用关机指令
- `reboot、halt、poweroff` 重新开机，关机
- `shutdown` 在關機時會把系統的服務都關閉之後，才關閉電腦，而 `halt`、 `poweroff`指令則允許不管系統的狀態為何，直接停止電腦的運作
- `shutdown`、`reboot`、`halt`等指令均已经执行过 `sync`了
