import requests
import json

r = requests.get('http://127.0.0.1:8000/system/category/')
print(r, r.json())
print('-'*20)

garden_tools_type = {'name':'Garden tools'}
r = requests.post('http://127.0.0.1:8000/system/category/typeoftools/', data=json.dumps(garden_tools_type))
print(r, r.json())
kitchen_tools_type = {'name':'Kitchen tools'}
r = requests.post('http://127.0.0.1:8000/system/category/typeoftools/', data=json.dumps(kitchen_tools_type))
print(r, r.json())
print('-'*20)

r = requests.get('http://127.0.0.1:8000/system/category/')
print(r, r.json())
print('-'*20)

hammers_type = {'name':'Hammers', 'type':'Hand tools'}
r = requests.post('http://127.0.0.1:8000/system/category/subtypeoftools/', data=json.dumps(hammers_type))
print(r, r.json())

watering_type = {'name':'Watering', 'type':'Garden tools'}
r = requests.post('http://127.0.0.1:8000/system/category/subtypeoftools/', data=json.dumps(watering_type))
print(r, r.json())

garden_forks_type = {'name':'Garden forks', 'type':'Garden tools'}
r = requests.post('http://127.0.0.1:8000/system/category/subtypeoftools/', data=json.dumps(garden_forks_type))
print(r, r.json())

pots_type = {'name':'Pots', 'type':'Garden tools'}
r = requests.post('http://127.0.0.1:8000/system/category/subtypeoftools/', data=json.dumps(pots_type))
print(r, r.json())
print('-'*20)

r = requests.get('http://127.0.0.1:8000/system/category?search=d')
print(r, r.json())
print('-'*20)

saw_2 = {'code':'02x', 'name':'see saw', 'description':'da-da', 'brand':'idk', 
         'amount':12, 'image':None, 'price':1000.00, 'type_of_tool':'Saws'}
r = requests.post('http://127.0.0.1:8000/system/category/subtype/tools/', data=json.dumps(saw_2))
print(r, r.json())

hammer_1 = {'code':'01x', 'name':'Testing hammer', 'description':'bang bang', 'brand':'idk', 
            'amount':10, 'image':None, 'price':200.00, 'type_of_tool':'Hammers'}
r = requests.post('http://127.0.0.1:8000/system/category/subtype/tools/', data=json.dumps(hammer_1))
print(r, r.json())

hammer_2 = {'code':'02x', 'name':'toob hammer', 'description':'bang bang', 'brand':'idk', 
            'amount':12, 'image':None, 'price':100.00, 'type_of_tool':'Hammers'}
r = requests.post('http://127.0.0.1:8000/system/category/subtype/tools/', data=json.dumps(hammer_2))
print(r, r.json())

watering_1 = {'code':'01x', 'name':'Testing watering can', 'description':'WET', 'brand':'idk', 
              'amount':10, 'image':None, 'price':50.00, 'type_of_tool':'Watering'}
r = requests.post('http://127.0.0.1:8000/system/category/subtype/tools/', data=json.dumps(watering_1))
print(r, r.json())

watering_2 = {'code':'02x', 'name':'Shower watering', 'description':'WET', 'brand':'idk', 
              'amount':12, 'image':None, 'price':100.00, 'type_of_tool':'Watering'}
r = requests.post('http://127.0.0.1:8000/system/category/subtype/tools/', data=json.dumps(watering_2))
print(r, r.json())
print('-'*20)

r = requests.get('http://127.0.0.1:8000/system/category/subtype/tools?search=t')
print(r, r.json())
print('-'*20)