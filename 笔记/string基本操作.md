## String基本操作

---

1. +连接
2. *重复
3. s[i] 索引
4. s[i:j]切片  slice
5. for循环遍历

### 连接

#### 代码示例

	s1 = 'liuzhao'
	s2 = '.com'
	print s1 + s2
	
	i = 25
	print s1 +s2 + str(1)  //str(int) 整型转换成字符串
	
### 索引和切片

	s1 = 'liuzhao' * 3
	print s1[2]    //索引，正数从左数，负数从右数
	print s1[-1]
	print s1[2:6]   //切片，s[i:j] 等价于[i,j)，i≤j，否则无法切出，注意：但不报错
	print s1[2:10:2] //2为步数，代表间隔切片
	print s1[10:2:-1] -1切片方向反向
	print s1[-1::-1]  //利用切片实现字符串逆序