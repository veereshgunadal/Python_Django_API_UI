import requests, json


url = 'http://127.0.0.1:8000/'

'''
r = requests.get(url+'student/')

print(r.status_code)
print(r.text)
print(r.json())'''

a = {'name':'Rohit', 'roll_no':2, 'age':35, 'addr':'Mumbai', 'ph_no':12345678, 'department':'Lazy'}
b = json.dumps(a)


r = requests.post(url+'student/create/', data = b)

print(r.status_code)
print(r.text)
print(r.json())

'''
r = requests.put(url+'student/update/3/', data = b)

print(r.status_code)
print(r.text)
print(r.json())'''

'''
r = requests.delete(url+'student/delete/2/')

print(r.status_code)
print(r.text)
#print(r.json())'''