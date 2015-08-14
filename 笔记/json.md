### Python json模块

***

#### json简介

json是一种轻量级的数据交换格式，是JavaScript的一个子集，完全采用独立于语言的文本格式。

结构形式：

1. “名称/值”对的集合
2. 值的有序列表，大多数编程语言中被理解为数组。

#### python处理json的模块以及api

**模块：json**
**api:**json.dumps()和json.loads()

##### json.dumps无附加参数

json.dumps()接受简单数据类型和结构性数据类型，返回str类型

```
	import json
	obj = []
	encodedjson = json.dumps(obj)
	print encodedjson
	print type(encodedjson)

```

![](http://img.hb.aicdn.com/c7001b26c7171b61df2d1df1e277e55b23a02a32406e-AtdAoU_fw658)

从json到python的类型转化

![类型转化](http://images.cnblogs.com/cnblogs_com/coser/201112/201112141621146178.png)

json.dumps提供了很多很好的参数可供选择，比较常用的有sort_keys(对dict对象排序)，separators,indent等。

##### json.dumps附加参数

使用sort_keys对dict对象进行排序

```
	data1 = {'b':789,'c':123,'a':456}
	data2 = {'a':456,'b':789,'c':123}
	
	d1 = json.dumps(data1,sort_keys = True)
	d2 = json.dumps(data2)
	d3 = json.dumps(data2,sort_keys = True)

```

![](http://img.hb.aicdn.com/21f48dc3c4167ced1b946d5ef79ff074f948720c493b-nQxmmh_fw658)

使用indent进行缩进，使得输出更加美观。

```
	data1 = {'b':789,'c':123,'a':456}
	d1 = json.dumps(data1,indent = 4)
	print d1

```

![](http://img.hb.aicdn.com/8512146b5a8e418ae6756b5a3a32d2ce0b88926d3cec-clS8nL_fw658)

使用separator参数对数据进行压缩，该参数传递一个元组，包含分割对象的字符串。

```
	print len(json.dumps(data))
	print len(json.dumps(data,indent = 4))
	print len(json.dumps(data,separator(',',':')))

```

#### json.loads对json对象进行decode

```
	decodejson = json.loads(encodedjson)
	print type(decodejson)
	print decodejson[4]['key1']
	print decodejson

```

![](http://img.hb.aicdn.com/6e397fad5425b42f41562c567b6824ab8965eca399df-ICHehw_fw658)