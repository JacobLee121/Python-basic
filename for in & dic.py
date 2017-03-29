[in]
a={'name':"123",'name2':"333"}
for key in a:
	print(key, 'correspond', a[key])#a[key]取字典中的对应“key”这个“键” 的“值”
[out]
name correspond 123
name2 correspond 333
[in]
a.keys()#输出所有的键
[out]
dict_keys(['name', 'name2'])
