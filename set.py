a={1,2,3,4,5,6}
print(a)
print(type(a))
b={'hi','hello',1,2,2.5,(5,8,9)}
print(b)

#add & update
print("After Adding operation")
a.add(10) #adds only one element once
print(a)

print("after update operation ")
a1={'python','c'}
a1.update('java') #unique values only
print(a1)

#discard
print("After discarding :")
c=a1.discard('java')
print(c)
