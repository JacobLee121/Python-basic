import operator
mm={'a':"1",'c':"3",'f':"6",'e':"5"}
mmm=sorted(mm.items(),key=operator.itemgetter(1),reverse=True)
>>> mm
{'a': '1', 'c': '3', 'f': '6', 'e': '5'}
 mmm=sorted(mm.items(),key=operator.itemgetter(1),reverse=True)
>>> print(mmm)
[('f', '6'), ('e', '5'), ('c', '3'), ('a', '1')]
