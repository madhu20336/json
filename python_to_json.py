import json
dict1={"name": "David",
     "class":"I",
     "age": 6 }
file_open=open("python_to_json.json","w")
json.dump(dict1,file_open,indent=1)
file_open.close()