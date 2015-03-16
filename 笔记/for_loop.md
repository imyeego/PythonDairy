## Python的for循环

***

### 语法结构

```
for target in sequences:
	statements

```

### 可遍历对象(sequencens)

1. list
2. tuple
3. strings
4. files

### 代码实例

#### 遍历字符串

	str = 'apple watch is beautiful!'
	for c in str:
		print c
	else:
		print 'out for'
		
#### 遍历列表(list)

	list1 = [1 ,3, 5, 2.6, 'liu', 'c']
	i = 0
	for c in list1:
		print format(i, '2d'),c
		i = i + 1
	else:
		print 'out for'
		
#### 遍历元组(tuples)

	tup = (1, 2, 3, 6, 2.5, 'str')
	i = 0
	for t in tup:
		print format(i, '2d'), t
	else:
		print 'out for'
		
#### 遍历文件(files)

##### 1.文件读取

**所用函数：**

1. open('filename', 'mod').readline/readlines

		for r in open('filename', 'r').readlines:
			print r,
		

##### 2.文件写入

	for r in open('filename', 'r').readlines:
		open('toFilename', 'a+').write(r)




