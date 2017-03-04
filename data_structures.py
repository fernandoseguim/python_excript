# create simple numeric list
list = [1,2,3,4,5,6]
print(list)

# apppend a new element to list - list of list
x = [7,8,9,0]
list.append(x)
print(list)

print(type(list))

# remove an element from list
list.remove(x)
print(list)

# concatenate two or more list
new_list = list + x
print(new_list)
print(type(new_list))


# create a tuple NOTE: tuple don't append news elements - is a static data structure
t = (1, 'a', True, (10*18/32))
print(t)
print(type(t))

# create a dictionary
dic = {'nome':'fernando', 'idade':28, 'sexo':'masculino','cidade':'São paulo'}
print(dic)

print(type(dic))

# access a element from dictionary
print(dic["nome"])
print(dic["idade"])

# create matrix of dictionary or dictionary of dictionary
hortfrutti = {'maça':{'argentina':100,'gala':80,'fuji':30},'banana':{'nanica':150,'prata':90,'ouro':60}}

print(hortfrutti)
print(type(hortfrutti))

# input a new element to dictionary
hortfrutti['laranja'] = {'pera':40,'lima':90,'baiana':20}
print(hortfrutti)

# remover an element from dictionary
hortfrutti.pop('laranja')

print(hortfrutti)
print(type(hortfrutti))

# input a news elements to dictionary
hortfrutti['laranja'] = {'pera':40,'lima':90,'baiana':20}
hortfrutti['uva'] = {'crismon':200,'italiana':180,'rubi':120}

print(hortfrutti)
print(type(hortfrutti))
