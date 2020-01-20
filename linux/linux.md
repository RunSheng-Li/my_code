

linux





```
linux下的文件系统
linux没有盘符这个概念，只有一个根目录 / ,所有文件都在它下面
```



```
显示当前路径下的文件以及文件夹的名字
ls

还可以指定路径
ls /home/computer1/

ls -l

ls -l -h
显示隐藏文件
ls -l -h -a 等于 ls-alh
```



```
显示当前正在操作的路径
pwd
```



```
创建一个文件
touch 文件名
```



```
创建文件夹
mkdir 文件夹名
```



```
进入指定路径
cd 路径

跳到上一层目录
cd ..

快速回到上一次的路径
cd -

进入test文件夹 .表示当前路径
cd ./test

跳到上一层的上一层
cd ../../
```



```
清屏
clear
```



```
删除文件
rm 1.txt 

删除文件夹
rm -r 文件夹名
```



```
复制文件
cp hello.txt test1/

复制文件夹
cp -r data/ test1/
```



```
剪切文件
mv hello.txt test3/

剪切文件夹
mv test3/ test2/

重命名
mv data1/ my_data
```



```
以目录树的方式显示文件结构
tree
```



```
查看命令历史
history
```



```
查看命令文档
help --help

man ls
```

