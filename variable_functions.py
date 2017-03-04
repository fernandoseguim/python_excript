# variable functions and multi returns
def list_function(*list):
    print(list)
    return list


def dict_function(**dict):
    print(dict)
    return dict.keys(), dict.values(), dict.items()

def list_dict_function(*list,**dict):
    print(list)
    print(dict)

list_function(1,2,3,4,5,6,7,8,9,0)
a,b,c = list_function(1,2,3)

print(a)
print(b)
print(c)
print(a,b,c)
print()

dict_function(a=1,b=2,c=3,d=4,e=5)
keys,values,items = dict_function(a=1,b=2,c=3)

print(keys)
print(values)
print(items)
print(keys,values,items)
print()

list_dict_function(1,2,3,4,5,6,7,8,9,0,a=1,b=2,c=3,d=4,e=5)


