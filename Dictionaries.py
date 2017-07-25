'''
Dictionaries are python specific
their like associative array in other
languages. Basic idea is unordered assortment(Collection)
of data & the data are always keys and values

SYNTAX:
 Dictionary_name = {key:value,key:value,...}
'''
exdict = {'Jack':25,'Joe':55,'Barry':26,'Steve':31}
print(exdict)
#Reference using 'Jack' as id
print(exdict['Jack'])
#Add to a Dictionaries
exdict['Tim'] = 14
print(exdict)
# Update value
exdict['Tim'] = 21
print(exdict)
# Delete Value
del exdict['Tim']
print(exdict)
'''
We can also create other Dictionaries and say 'Jack' = other Dictionaries
& create funtion any = to 'Jack'
'''
exdict2 = {'Jack':[25,'Blonde'],'Joe':[55,'Black'],'Barry':[26,'Red'],'Steve':[31,'Black']}
print(exdict2['Jack'])
print(exdict2['Jack'][1])
