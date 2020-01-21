

which

```
which ls
```



chmod修改文件权限



字母法

r可读 w可写 x可执行

```
chmod u=rwx,g=r,o=x 123.txt
```

u 拥有者

g 同组者

o 其他人



数字法

r 4

w 2

x 1

```
chmod 666 123.txt
```



修改文件夹下所有文件的权限

```
chmod 777 a -R
```

