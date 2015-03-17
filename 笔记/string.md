## Python字符串简介

---

### 1.表示

1. 用单引号
2. 用双引号
3. 用三重（单、双均可）引号

#### 代码示例

	s1 = 'liuzhao is smart!' //通常用于表示字符串中有双引号的
	s2 = "liuzhao is smart!" //表示字符串中有单引号的
	s3 = '''liuzhao is smart!''' //跨行
	
### 2.分类

1. 转义字符串
2. raw字符串
	* 关闭转义机制
	
3. Unicode字符串
4. 格式化字符串
	- 'your age %d,sex %s,score %f'%(12,'male',78.5)
	
#### 代码示例

	s1 = 'liuzha\no\tis\tsmart'
	s2 = r'liuzha\no\tis\tsmart' //原字符串