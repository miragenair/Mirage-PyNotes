import json

data = '{"var1":30,"var2":41,"var3":56}'
print(data)


parsed = json.loads(data)

print(parsed['var1'])

data2 = {
    "channel_name": "codewithharry",
    "cars":["bmw","audi a8","ferrari"],
    "fridge": ('roti', 540),
    "condition": False
}

jscomp = json.dumps(data2)
print(jscomp)
