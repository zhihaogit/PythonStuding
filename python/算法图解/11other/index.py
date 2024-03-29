'''
1. 树
二叉查找树（binary search tree）的数据结构
在二叉查找树中查找节点，平均运行时间为 O(log n)，最糟的情况所需时间为 O(n)
在有序数组中查找，最糟的情况所需时间是 O(log n)
        数组      二叉查找树
查找  O(log n)    O(log n)
插入  O(n)        O(log n)
删除  O(n)        O(log n)
二叉叉查找树不能随机访问，处于平衡状态时，平均访问时间是 O(log n)
树向左或向右倾斜的，性能不佳，也有一些平衡状态的特殊二叉查找树
B树，红黑树，堆，伸展树

2. 反向索引
一个散列表，将单词映射到包含它的页面，这种数据结构被称为反向索引（inverted index）

3. 傅里叶变换

4. 并行算法
并行性管理开销
负载均衡

5. Map Reduce（分布式算法）
可让算法在多台计算机上运行
映射（map）函数，归并（reduce）函数
5.1 映射函数
映射函数很简单，它接受一个数组，并对其中每个元素执行同样的处理
5.2 归并函数
将很多项归并为一项

6. 布隆过滤器和 HyperLogLog
6.1 布隆过滤器
是一种概率型数据结构，它提供的答案有可能不对，很可能是对的，优点在于占用的存储空间
可能出现错报的情况
不可能出现漏报的情况
6.2 HyperLogLog
近似地计算集合中不同的元素数，不能给出准确的答案，但也八九不离十，占用的内存空间少

7. SHA算法
散列算法的散列函数是来确定这个值放在数组的什么地方（数组索引）
7.1 比较文件
另一种是安全散列算法（secure hash algorithm, SHA），给定一个字符串，SHA返回其散列值（一个较短的字符串）
可以计算文件的散列值，从而比较是否是同一文件
7.2 检查密码
数据库中存储的密码是 SHA山截止，每次输入密码，都会计算其散列值，从而比较密码

8. 局部敏感的散列算法
SHA是局部不敏感，一个字符串，只改变其中的一个字符，生成SHA值都截然不同
有些算法是局部敏感的（如：Simhash），对字符串细微的修改，simhash生成的散列值只存在细微的差别
通过比较散列值来判断两个字符串的相似程度

9. Diffie-Hellman秘钥交换
双方无需知道加密算法，使用两个秘钥，公钥和私钥
发送消息时，使用已公布的公钥进行加密
接收消息时，使用私钥来解密加密后的消息

10. 线性规划
用于在给定约束条件下最大限度地改善指定的指标
线性规划使用 simplex算法
'''