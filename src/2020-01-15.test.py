# encoding:utf-8
"""
author: wgc
version: 3.1
title: 玩转Linux操作系统
"""

# 获取登录信息 - w / who / last/ lastb。

# 查看自己使用的Shell - ps。

# 查看命令的说明和位置 - whatis / which / whereis。

# 清除屏幕上显示的内容 - clear。

# 查看帮助文档 - man / info / help / apropos。

# 查看系统和主机名 - uname / hostname。

# 时间和日期 - date / cal。

# 重启和关机 - reboot / shutdown。

# 退出登录 - exit / logout。

# 查看历史命令 - history。

# 创建/删除空目录 - mkdir / rmdir。
"""
[root ~]# mkdir abc
[root ~]# mkdir -p xyz/abc
[root ~]# rmdir abc
"""

# 创建/删除文件 - touch / rm。
"""
[root ~]# touch readme.txt
[root ~]# touch error.txt
[root ~]# rm error.txt
rm: remove regular empty file ‘error.txt’? y
[root ~]# rm -rf xyz
"""

# 切换和查看当前工作目录 - cd / pwd。

# 查看目录内容 - ls。

# 查看文件内容 - cat / tac / head / tail / more / less / rev / od。

# 拷贝/移动文件 - cp / mv。
"""
[root ~]# mkdir backup
[root ~]# cp sohu.html backup/
[root ~]# cd backup
[root backup]# ls
sohu.html
[root backup]# mv sohu.html sohu_index.html
[root backup]# ls
sohu_index.html
"""

# 件重命名 - rename。
"""
[root ~]# rename .htm .html *.htm
"""

# 查找文件和查找内容 - find / grep。

# 创建链接和查看链接 - ln / readlink。

# 压缩/解压缩和归档/解归档 - gzip / gunzip / xz。

# 归档和解归档 - tar。

# 管道和重定向
"""
# 例子：查找当前目录下文件个数。

[root ~]# find ./ | wc -l
6152


# 例子：列出当前路径下的文件和文件夹，给每一项加一个编号。

[root ~]# ls | cat -n
     1  dump.rdb
     2  mongodb-3.6.5
     3  Python-3.6.5
     4  redis-3.2.11
     5  redis.conf

# 多重定向 - tee。

# 下面的命令除了在终端显示命令ls的结果之外，还会追加输出到ls.txt文件中。

[root ~]# ls | tee -a ls.txt
"""

# 别名
# alias
"""


[root ~]# alias ll='ls -l'
[root ~]# alias frm='rm -rf'
[root ~]# ll
...
drwxr-xr-x  2 root       root   4096 Jun 20 12:52 abc
...
[root ~]# frm abc
"""
# unalias
"""
[root ~]# unalias frm
[root ~]# frm sohu.html
-bash: frm: command not found
"""

# 文本处理
# 字符流编辑器 - sed。
"""
# sed是操作、过滤和转换文本内容的工具。假设有一个名为fruit.txt的文件，内容如下所示。

[root ~]# cat -n fruit.txt 
     1  banana
     2  grape
     3  apple
     4  watermelon
     5  orange
    
# 删除第3行。

[root ~]# sed '3d' fruit.txt
banana
grape
watermelon
orange


# 删除第2行到第4行。

[root ~]# sed '2,4d' fruit.txt
banana
orange


# 将文本中的字符a替换为@。

[root ~]# sed 's#a#@#' fruit.txt 
b@nana
gr@pe
@pple
w@termelon
or@nge
"""

# 模式匹配和处理语言 - awk。
"""
# 假设有一个名为fruit2.txt的文件，内容如下所示。

[root ~]# cat fruit2.txt 
1       banana      120
2       grape       500
3       apple       1230
4       watermelon  80
5       orange      400

# 显示文件的第3行。

[root ~]# awk 'NR==3' fruit2.txt 
3       apple       1230

# 显示文件的第2列。

[root ~]# awk '{print $2}' fruit2.txt 
banana
grape
apple
watermelon
orange

# 显示文件的最后一列。

[root ~]# awk '{print $NF}' fruit2.txt 
120
500
1230
80
400
"""