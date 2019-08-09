## 第七章:Linux磁盘与文件系统的管理

### 7.1 认识Linux文件系统

#### 7.1.1 磁盘组成与分区的复习

- 磁盘组成
  - 原型的盒片（记录数据）
  - 机械手臂及磁头（读写盘片）
  - 主轴马达，转动盘片
- 磁盘的文件名
  - 所有的文件名被仿真为`/dev/sd[a-p]`，第一颗磁盘文件名为 `/dev/sda`
  - 分区的文件名为 `/dev/sda[1-128]`
  - 虚拟机的磁盘通常为 `/dev/vd[a-p]`
  - 软件磁盘阵列为 `/dev/md[0-128]`
  - 使用的是LVM时，文件名为 `/dev/VGNAME/LVNAME`等格式
  - `/dev/sd[a-p][1-128]`：为实体磁盘的磁盘文件名
  - `/dev/vd[a-d][1-128]`：为虚拟磁盘的磁盘文件名

#### 7.1.2 文件系统特性

- 磁盘分区，进行格式化之后，成为操作系统能够使用的 文件系统格式(filesystem)
  - LVM，软件磁盘阵列(software raid)将一个分区格式化为多个文件系统
  - LVM，PAID可以将多个分区合成一个文件系统
- 文件系统通常会将文件权限和文件属性分别到存放到不同的区块，权限与属性放置在 inode中,实际数据放置到 data block区块中，还有一个超级区块(superblock)会记录整个文件系统的整体信息
  - `superblock`：记录filesystem整体信息，包括inode/block的总量、使用量、剩余量，以及文本系统的格式与相关信息
  - `inode`：记录文件的属性，一个文件占用一个inode，同时记录此文件的数据所在的block号码
  - `block`：实际记录文件的内容，若文件太大时，会占用多个block
- 索引式文件系统（indexed allocation）
- 磁盘重组

#### 7.1.3 Linux的 EXT2文件系统(inode)

Ex2在格式化的时候基本上是区分为多个区块群组（block group）的，每个区块群组都有独立的 inode/block/superblock系统，每个区块群组有6个主要内容：

- `data block` 数据区块
  - 原则上，除了重新格式化，block的大小与数量在格式化完都不能改变了
  - 每个block内最多只能放一个文件的数据
  - 如果文件大于 block的大小，则一个文件会占用多个block
  - 若文件小于block，则剩余的容量不能再被使用
- `inode table` inode表格
  - inode记录的文件数据
    - 该文件的存取模式（read/write/excute）
    - 该文件的owner和group
    - 文件的容量
    - 文件的创建或状态改变的时间（ctime）
    - 最近一次的读取时间（atime）
    - 最近修改的时间（mtime）
    - 定义文件特性的flag，如SetUID...
    - 该文件真正内容的指向（pointer）
  - 特性
    - 每个 inode大小固定为 128Bytes(新的ext4和xfs可设置为 256B)
    - 每个文件仅占用一个 inode
    - 文件系统能够创建的文件数量与 inode的数量有关
    - 系统先找到 inode，分析inode中的权限是否符合使用者，符合的话，才开始实际读取block
- `Superblock` 超级区块
  - Superblock是记录整个filesystem相关信息的地方，记录的信息：
    - block与 inode的总量
    - 未使用与已使用的 block与 inode数量
    - block(1,2,4K)与 inode(128,256Bytes)的大小
    - filesystem的挂载时间、最近一次写入数据的时间、最近一次检验磁盘（fsck）的时间等
    - 一个 vaild bit数值，若文件系统被挂载，vaild bit为0，否则是1
  - 每个block group都可能有superblock，其他的是第一个的备份
- `Filesystem Descripition` 文件系统描述说明
  - 这个区段描述每个block group的开始和结束的block号码
  - 说明每个区段分别介于哪个block号码之间
- `block bitmap` 区块对照表
  - 得知哪个是空的 block
  - 删除文件后，相关block被释放，bitmap中的该block号码被标记为 未使用
- `inode bitmap` inode对照表
  - 记录使用与未使用的 inode号码
- `dumpe2fs`：查询 Ext家族 superblock信息的指令

#### 7.1.4 与目录树的关系

- 目录
  - 创建一个目录，文件系统会分配一个inode和一个block，其中 inode记录该目录的相关权限与属性及分配的block号码，而block中则是记录这个目录下的文件名与该文件名占用的inode号码数据
  - `ls -i` 来显示文件所占用的 inode号码
- 文件
  - inode 仅有12个直接指向
  - 一个间接
  - 一个双间接
  - 一个三间接记录区
- 目录树读取
  - 由于文件名的记录是在目录的block中，所以新增/删除/重命名与目录的w权限有关
  - 目录树由根目录开始读起

#### 7.1.5 EXT2/EXT3/EXT4 文件的存取与日志式文件系统的功能

- 新增文件的行为
  1. 确定使用者是否有 w和 x权限
  2. 根据inode bitmap找到没有使用的 inode号码，将新文件的权限/属性写入
  3. 根据block bitmap找到没有使用的 block号码，将实际数据写入block中，并将新的 inode的block指向数据
  4. 更新同步 inode bitmap, block bitmap, superblock
- 数据存放区域：inode table, data block
- 中介数据（metadata，涉及到操作，经常会变动）：superblock, block bitmap, inode bitmap
- 数据的不一致（inconsistent）状态
- 日志式文件系统(Journaling filesystem)
  - 预备：当系统要写入一个文件，会现在日志记录区块中记录某个文件准备写入的信息
  - 实际写入：开始写入文件的权限和数据，开始更新 metadata数据
  - 结束：完成数据与 metadata的更新，在日志记区块中完成该文件的记录

#### 7.1.6 Linux文件系统的运行

- 系统载入一个文件到内存后
- 该文件没有被更动过，被标记为 干净(clean)
- 被更动过，会被标记为 脏的(dirty)
- 所有动作暂不会被写入到磁盘
- 系统不定时将 dirty数据写回磁盘

#### 7.1.7 挂载点的意义(mount point)

- 挂载点一定是目录，该目录为进入该文件系统的入口
- 并不是任何文件系统都可以使用，必须挂载目录树的某个目录后，才能使用该文件系统

#### 7.1.8 其他Linux支持的文件系统与 VFS

- 常见支持的文件系统
  - 传统文件系统：ext2/minix/MS-DOS/FAT(用 vfat模块)/iso9960(光盘)
  - 日志式文件系统：ext3/ext4/ReiserFS/Window's NTFS/IBM's JFS/SGI's XFS/ZFS
  - 网络文件系统：NFS/SMBFS
- 查看linux支持和的文件系统，可查看这个目录
  - `ls -l /lib/modules/$(uname -r)/kernel/fs`
- 系统目前已载入内存中的文件系统
  - `cat /proc/filesystems`
- Linux VFS(Virtual Filesystem Switch)
  - 整个 Linux认识的 filesystem都是VFS 进行管理

#### 7.1.9 XFS 文件系统简介

- EXT家族当前：支持度最广，但格式化超慢
- XFS文件系统的配置
  - 数据区(data section)
    - 类似于 ext家族的 block group
    - block和inode有不同的容量进行设置
  - 文件系统活动登录区(log section)
    - 主要记录文件系统的变化
  - 实时运行区(realtime section)
    - 文件被创建时，xfs会在这个区段找到一/数个extent区块，将文件放置到这个区块后，等分配完，在写入到data section的 inode与 block
- XFS文件系统的描述数据观察
  - `xfs_info 挂载点 文件设备名` 

 ### 7.2 文件系统的简单操作

#### 7.2.1 磁盘与目录的容量

- `df` 列出文件系统的整体磁盘使用量
  - `df [-ahikHTm] [目录或文件名]`
  - 读取的范围主要是在 Superblock内的信息
  - 特别留意根目录的容量
- `du` 评估文件系统的磁盘使用量（常用在推估目录所占容量）
  - `du [-ahskm] 文件或目录名称`
  - 直接到文件系统内搜寻所有的文件数据

#### 7.2.2 实体链接与符号链接：ln

- Hard Link (实体链接，硬式链接或实际链接)
  - 只是在某个目录下新增一笔文件名链接到某 inode号码的关联记录
  - 一般情况下，使用hard link设置链接文件时，磁盘的空间与 inode的数目都不会改变
  - 不能跨 Filesystem
  - 不能 Link目录
- Symbolic Link (符号链接，亦即捷径)
  - 创建一个独立的文件，而这个文件会让数据的读取指向他link的那个文件的文件名
- `ln [-sf] 来源文件 目标文件`
- 关于目录的link数量

### 7.3 磁盘的分区、格式化、检验与挂载

新增磁盘步骤

1. 分区，创建可用的 partition
2. 对该 partition格式化(format)，创建可用的 filesystem
3. 可以选择对 filesystem进行检验
4. 创建挂载点(目录)，并挂载

#### 7.3.1 观察磁盘分区状态

- `lsblk` 列出系统中的所有磁盘列表
- `blkid` 列出设备的UUID等参数
- `parted` 列出磁盘的分区表类型与分区信息


### 7.3 磁盘的分区、格式化、检验与挂载

新增磁盘步骤

1. 分区，创建可用的 partition
2. 对该 partition格式化(format)，创建可用的 filesystem
3. 可以选择对 filesystem进行检验
4. 创建挂载点(目录)，并挂载

#### 7.3.1 观察磁盘分区状态

- `lsblk` 列出系统中的所有磁盘列表
  - `lsblk [-dfimpt] [device]`
  - `-f` 列出文件系统与设备的 UUID数据
  - `MAJ:MIN` 主要、次要设备代码
- `blkid` 列出设备的UUID等参数
  - UUID是全域单一识别码(universally unique identifier)
- `parted` 列出磁盘的分区表类型与分区信息
  - `parted device_name print`

#### 7.3.2 磁盘分区：gdisk/fdisk

MBR分区表使用 fdisk分区，GPT分区表使用 gdisk分区

- `gdisk`
  - `gdisk 设备名称`
  - `w` 立即执行
  - `q` 离开
  - `partprobe` 更新 Linux核心的分区表信息
  - `partprobe [-s]` -s打印信息
  - `cat /proc/partitions` 核心的分区资料
- `fdisk`
  - `fdisk 设备名称`
  - `m` 获得指令介绍

#### 7.3.3 磁盘格式化（创建文件系统）

- XFS文件系统 mkfs.xfs
  - `mkfs.xfs [-b bsize] [-d parms] [-i parms] [-l parms] [-L label] [-f] [-r parms] 设备名称`
  - eg: `mkfs.xfs /dev/vda4`
  - `grep 'processor' /proc/cpuinfo` 找出系统的cpu核数
  - `mkfs.xfs -f -d agcount=2 /dev/vda4` 设置 agcount数值
- XFS文件系统 for RAID性能优化（optional）
  - 磁盘阵列（RAID）
- EXT4文件系统mkfs.ext4
  - 格式化为 ext4的传统 linux文件
  - `mkfs.ext4 [-b size] [-L label] 设备名称`
- 其他文件系统 mkfs
  - mkfs(make filesystem)是个综合指令
  - `mkfs[tab][tab]` 查看支持的文件系统的格式化功能

#### 7.3.4 文件系统检验

- `xfs_repair` 处理 XFS文件系统
  - `xfs_repair [-find] 设备名称`
- `fsck.ext4` 处理 EXT4文件系统
  - `fsck.ext4 [-pf] [-b superblock] 设备名称`

#### 7.3.5 文件系统挂载与卸载

- 挂载点是目录，这个目录是进入磁盘分区（文件系统）的入口，挂载前的检查：
  - 单一文件系统不应该重复被挂载在不同的挂载点(目录)中
  - 单一目录不应该重复挂载多个文件系统
  - 要做为挂载点的目录，理论应该是空目录
- `mount` 挂载指令
  - `mount -a`  依照配置文件[/etc/fstab]将磁盘挂载
  - `mount [-l]` 显示Label名称
  - `mount [-t 文件系统] LABEL='' 挂载点`
  - `mount [-t 文件系统] UUID='' 挂载点`
  - `mount [-t 文件系统] 设备文件名 挂载点`
- 哪些类型的 filesystem需要进行挂载测试，参考：
  - `/etc/filesystems` 系统指定的测试挂载文件系统类型的优先顺序
  - `/proc/filesystems` linux系统已经载入的文件系统类型
- linux支持的文件系统之驱动程序所在目录
  - `/lib/moduels/$(uname -r)/kernel/fs/`
- 挂载 xfs/ext4/vfat等文件系统
  - `blkid /dev/vda5` 找出 /dev/vda5的UUID
  - `mount UUID="~~" /data/ext4`  挂载
- 挂载 CD或 DVD光盘
- 挂载 vfat中文U盘（USB磁盘）
- 重新挂载根目录与挂载不特定目录
- `umount` 将设备文件卸载
  - `umount [-fn] 设备文件名或挂载点`

#### 7.3.6 磁盘/文件系统参数修订

修改一下目前文件系统的一些相关信息

- mknod 

  - `mknod 设备文件名 [bcp] [Major] [Minor]`

- `xfs_admin` 修改 XFS文件系统的UUID与Label name

  - `xfs_admin [-lu] [-L label] [-U uuid] 设备文件名`

- `tune2fs` 修改 ext4的 label name与UUID

  - `tune2fs [-l] [-L label] [-U uuid] 设备文件名`
