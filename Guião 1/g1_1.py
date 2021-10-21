#
# Guiao 1
#
#


def len_list(list_in):
		if list_in != []:
			return 1+len_list(list_in[1:])
		else:
			return 0

#print(len_list([1,2,3,7,8]))

def sum_list(list_in):
		if list_in ==[]:
			return 0
		else:
			return list_in[0]+sum_list(list_in[1:])

#print(sum_list([1,1,1,1]))

def isIN_list(list_in, e):
	if list_in == []:
		return	False
	else:
		if list_in[0] == e:
			return True
		else:
			return isIN_list(list_in[1:], e)

#print(isIN_list([1,1,1,1,2],2))
#print(isIN_list([1,1,1,1,1],2))
#print(isIN_list([0],2))

def concat_list(list_a, list_b):
	if list_a != []:
		return [list_a[0]]+concat_list(list_a[1:],list_b)
	elif list_b != []:
			return [list_b[0]]+concat_list(list_a,list_b[1:])
	else:
		return []

#print(concat_list([1,2,3,4],[5,6,7,8]))

def inv_list(list_in):
	if list_in == []:
		return []
	else:
		return [list_in[-1]]+inv_list(list_in[:-1])

#print(inv_list([1,2,3,4]))

def capicua_list(list_in):
	#if len_list(list_in) < 2:
	if list_in == []:
		return True
	elif list_in[0] == list_in[-1]:
		return capicua_list(list_in[1:-1])
	else:
		return False

#print(capicua_list(['1','2','3','2','1']))
#print(capicua_list([1,2,2,1]))
#print(capicua_list([1,2]))

def concat_lists(lists):
	if lists == []:
		return []
	else:
		return lists[0]+ concat_lists(lists[1:])

#print(concat_lists([[1,2,4],[5,6,7],[8,9,10]]))

def replace(list_in,x,y):
	if list_in == []:
		return []
	elif list_in[0]== x:
		return [y]+replace(list_in[1:],x,y)
	else:
		return [list_in[0]]+replace(list_in[1:],x,y)

#print(replace([1,2,3],2,3))

def sortUnion_lists(list_a,list_b):
	if list_a == [] and list_b == []:
		return []
	elif list_a == []:
		return list_b
	elif list_b == []:
		return list_a
	elif list_a[0]>list_b[0]:
		return [list_b[0]]+sortUnion_lists(list_a,list_b[1:])
	else:
		return [list_a[0]]+sortUnion_lists(list_a[1:],list_b)

#print(sortUnion_lists([1,3,5],[2,5,5]))
#print(sortUnion_lists([1,2],[]))
#print(sortUnion_lists([],[]))

def subsets(list_in):
	if list_in==[]:
		return [[]]

	t = subsets(list_in[1:])
	return t+[[list_in[0]]+e for e in t]

#print(subsets([1,2,3,4,5]))
