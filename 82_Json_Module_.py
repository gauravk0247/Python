import json

data = '{"var1":"gaurav", "var2":56}'
print(data)

parsed = json.loads(data)
# print(parsed['var1'])
print(type(parsed))

# Task - 1 json.load kya krta hai?
# json exposes an API familiar to users of the standard library marshal and pickle modules.

data2 = {
    "students_name":"Gaurav",
    "skill":['python', 'html', 'css', 'js', 'php'],
    "fridge":('fruit', 560),
    "isbad": False
}
jscomp = json.dumps(data2)
print(jscomp)

# Task - 2 what is sort keys parameter in dumps
#  Keys in key/value pairs of JSON are always of the type str. When a dictionary is converted into JSON, all the keys of the dictionary are coerced to strings. As a result of this, if a dictionary is converted into JSON and then back into a dictionary, the dictionary may not equal the original one. That is, loads(dumps(x)) != x if x has non-string keys.