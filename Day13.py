'''
Mapping --> Dictionary -->its a collection of key value pairs used to store related data
applicatons of dictionaries--> JSON,APIs,Database records
dict() ---> data = {}--> data = {key : value}
it is mutable , indexed through keys , ordered, heterogenous, key must be unique (int,strings,float values...)
'''
'''
details = {}
print(type(details))
details = {'Id' : 'CGH4025', 'Name' : 'Gayathri',
           'Gender' : 'F','Age' : 20,
           'Batch' : 'DA23', 'Place' : 'HYD' }
print(details)
print(len(details))

#Access the data from dictionary
#details[0] #keyError
print(details.keys()) #it retuns keys from dictionary
print(details['Id'], details['Name'])
#if key name not matching / invalid
#print(details['marks'])#KeyError as marks is not present
details['marks'] = []
print(details)
print(type(details['marks']))

details['marks'].append(20)
print(details)
details['marks'].extend([15,20,25,20,23])
print(details)
#create a key value pair of practice session
details['PS'] = ('Tuesday','Thursday', 'Saturday')
print(details.keys())
#Accessing 3rd day marks of student
print(details['marks'][2])
#Accessing 2nd day of practice session
print(details['PS'][1])
details['MI'] = ('Monday', 'Wednesday', 'Firday')
#operations --> mutable,indexing through keys,membership
print('Wednesday' in details)
print('MI' in details)#returns true as we have MI as key
for i in details:
    print(i)#returns keys one by one
for i in details.keys():
    print(f'Key = {i}')
    #print(details[i])
    print(f' value = {details[i]}')
#key()--> returns keys from the dictionary
for i in details.values(): #returns value from dictionary
    print(i)
for i in details.items():#returns a key-value pair in tuple
    print(i)
for key,value in details.items():
    print(f'key is {key}')
    print(f'Value is {value}')
#update()--->updating the dictionary with key-value pairs
details.update({'marks':[],'PS':('Tuesday','Thursday', 'Saturday')})
print(details)
details['marks'].extend([20,21,15,25])
print(details)
marks = list(map(int,input("enter the marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)

print(details.keys())
print(details.get('Name'))
print(details.get('Branch'))#it returns None as we dont have branch as key
print(details.keys())
details.setdefault('Branch')#if key is not present it inserts into dict
print(details)
details['Branch'] = 'CSE(AI&ML)'
print(details)
print(details.setdefault('Name'))
print(details.keys())
print(details.pop('Branch'))#we need to mention the key
print(details.keys())
print(details.popitem())#removes and return a key,value pair as a 2-tuple
print(details.popitem())
del details['Id']
print(details.keys())
details.clear()#removes all elements from dict
print(details)

#fromkeys()
data = ['gayathri','sai','data']
b = dict.fromkeys(data)#creates a dict but value set to None
print(b)
b['saketh']=31
print(b)
c = dict.fromkeys(['CGH4025','CGH4022'],['CODE','GNAN'])
print(c)
'''
#Task: create a dictionary with your personal details,similar to your codegnan profile
profile = {
    'Name':'Gayathri',
    'Education':'B.Tech',
    'Branch':'CSE',
    'Sepcialization':'AL&ML',
    'Skills':['python','SQL','Excel'],
    'Goal':'Data Analyst'
    }
print(profile)
profile.update({'Location': 'Hyderabad','insitute':'Codegnan'})
print(profile)
for i in profile.keys():
    print(f'Key = {i}')
    print(profile[i])
    print(f' value = {profile[i]}')
















    

