# Alfbts
A simple python toolchest of algorithms, file-batches and functions

#2025-02-16modified
//新增特色功能：

/文件：
清空：清空控制台输出文本
图标：播放入场动画
库检测：检测当前python环境中的常用库

对于已编译文件则不需要库检测这个功能

/算法：
同分异构体数量：计算仅针对基团CnH2n+1
链表冒泡排序
最大环长度：求解oeis数列A002326
求解罗马数字

/批处理：
补齐缺失后缀：针对常用后缀缺失的文件
图片颜色替换
图片排序：图片明暗度排序，方便人工去重
图片加解密：采用对称加密
生成组合字符：生成看起来像乱码的复合文本
解unicode：解码部分用unicode加密的文本
视频重命名：按照时间重命名

因为jp(e)g格式有损压缩的特性，
本工具中所有图片处理均以png格式为准

/功能：
抽卡模拟器：原神抽卡模拟器
圣遗物强化：原神圣遗物强化模拟器
迷宫可视化：生成与求解迷宫
抽卡概率计算：原神抽卡概率计算器

抽卡相关功能已支持明光机制，
但尚未支持星辉兑换机制


//后续优化：

由于图片加解密和抽卡概率计算运行缓慢，
后续将考虑使用cython将相关功能预编译提速


//自定义：

如果要一行内输入多个内容，请用空格隔开
pulchrlibs.txt中存储了相关角色信息，
如果要实现崩铁或绝区零的卡池，请自行修改

#2025-02-16modified
//新增特色功能：

不想等待程序无响应？正好！
我们对于部分功能使用了进度条，
保证您等待的体验

新增了预编译的二进制文件，
Windows，macOS，Linux，压缩包的都有
