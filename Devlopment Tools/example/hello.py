import json

json_data = '''
[{"name":"Alice","age":28},{"name":"Bob","age":96},{"name":"Charlie","age":18},{"name":"David","age":98},{"name":"Emma","age":89},{"name":"Frank","age":94},{"name":"Grace","age":53},{"name":"Henry","age":99},{"name":"Ivy","age":16},{"name":"Jack","age":62},{"name":"Karen","age":4},{"name":"Liam","age":39},{"name":"Mary","age":15},{"name":"Nora","age":60},{"name":"Oscar","age":38},{"name":"Paul","age":70}]
'''

data = json.loads(json_data)
sorted_data = sorted(data, key=lambda x: (x['age'], x['name']))

result = json.dumps(sorted_data, separators=(',', ':'))
print(result)