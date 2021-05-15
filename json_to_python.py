import json

dict1='{"Name":"Ram","Class":"IV","Age":"9"}'
dict2=json.loads(dict1)
print(dict2)