#this is a python code
[in]             
list2=[[1, 1, 'yes'],
[1, 1, 'yes'],
[1, 0, 'no'],
 [0, 1, 'no'],
[0, 1, 'no']]
[in] list2[-1]
[out][0, 1, 'no']   
[in]for fea in list2:
	print(fea[-1])
[out]
yes
yes
no
no
no
[in] for fea in list2:
	print(fea[0])
[out]
1
1
1
0
0
>>> L = ['a','b','c','d']
>>> for i in L:
	print(i[-1])

	
a
b
c
d
 for i in L:
	print(i[0])

	
a
b
c
d
>>> L[0]
'a'
[in] list2 [0][1]='maybe'
list2
[out]
[[1, 'maybe', 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
[in] type(list2)
[out]<class 'list'>
[in]list2[0][2]='where'
list2
[out][[1, 'maybe', 'where'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
#list型的数据，可以修改已有位置的数据。对于矩阵形式的list[i][j] i代表第i行，j代表第j列
