## Python函数初涉
***

### 函数分类

1. 系统库提供的内部函数
2. 第三方提供的函数
3. 自定义函数

#### 系统提供的内部函数

- 字符函数库
- 数学函数库
- 网络编程库
- ……
- **函数的调用： 实参**

#### 字符函数库

1. 判断大小写：islower(),isupper()

	**使用方法：**
	
	```
	s = 'liuzhao';
	s.islower();
	
	```

2. 字符/串替换：replace('a','B')

	**使用方法：**

	```
	s = 'liuzhao';
	s.replace('a','b');
	
	```
	
	**使用说明**
	
	1. 该函数默认返回一个新的拷贝的字符串。
	2. 在原字符串中替换是无返回值
	3. 所以建议将其赋值给一个新的字符串。

#### 数学函数库

1. 三角函数和PI值:在使用数学函数库前需将其导入`import math`

	**使用方法：**
	
	```
	math.sin(math.pi/6);
	
	```
	
2. 指数函数：`math.pow(int ,int)`或者`a**b`

	**使用方法：**
	
	```
	math.pow(3,4)   ／*该函数返回一个浮点数*／
	
	```



#### 网络函数库

1. 导入socket:`import socket`
2. 获取网址的IP地址：

	```
	socket.gethostbyname('www.baidu.com');

	```


#### 操作系统库

1. 导入os:`import os`
2. 获取当前工作目录：`os.getcwd()`
3. 遍历并显示当前目录：`os.listdir(os.getcwd())`