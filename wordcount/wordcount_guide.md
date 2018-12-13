## 伪分布运行wordcount

#### 首先要运行hadoop

``` shell
cd /usr/hadoop/sbin
./start-all.sh
jps
```

查看 **Java** 进程如下

![运行hadoop](/Users/yongxinxu/Documents/images/image-20181213195727518.jpg)



#### 创建file文件夹

创建名称为`file`的文件夹并向里面写点东西

``` shell
cd /usr/hadoop
mkdir file
cd file
echo "hello world, hadoop java" >> file1.txt 
echo "hello world, hadoop python" >> file2.txt
```

![创建结果](/Users/yongxinxu/Documents/images/image-20181213200428233.jpg)



#### 在HDFS上创建文件夹目录input

创建完后把本地硬盘上创建的文件传进`input`里面：

```shell
hadoop fs -mkdir /input
hadoop fs -put /usr/hadoop/file/file*.txt /input
```

可以用`hadoop fs -ls`查看结果

![image-20181213201103511](/Users/yongxinxu/Documents/images/image-20181213201103511.jpg)



#### 找到Hadoop自带运行的wordcount java包

![image-20181213201417863](/Users/yongxinxu/Documents/images/image-20181213201417863.jpg)

例子jar包就是这个`hadoop-mapreduce-examples-2.8.5.jar`

运行命令如下：（写到/output/wordcount1中)

``` shell
hadoop jar hadoop-mapreduce-examples-2.8.5.jar wordcount /input/ /output/wordcount1
```

看一下/output/wordcount1中有什么

```
hadoop fs -ls /output/wordcount1 
```

![查看内容](/Users/yongxinxu/Documents/images/image-20181213202255402.jpg)

发现新建了一个**_SUCCESS**文件和一个**part-r-00000**文件

内容存储在**part-r-00000**文件中，查看结果命令如下：

```
hadoop fs -cat /output/wordcount1/part-r-00000
```

![image-20181213202339727](/Users/yongxinxu/Documents/images/image-20181213202339727.jpg)