# compare strings conform ASCII table
print('a' > 'b')
print('a' > 'c')
print('c' > '9')

# ASCII table
print('ASCII | Char')
for i in range(33,123):
    print('%d | %s' % (i,chr(i)))


#iterate a string with enumerate - return a dict
for k,v in enumerate('Interando String'):
    print('%d : %s ' %(k,v), end='\t')