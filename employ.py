import json
list_1=["neelam","programer","24","2400",]
list_2=["komal","trainer","24","20000"]
list_3=["anuradha","HR","25","40000"]
list_4=["Abhishek","manager","29","63000"]  
emp_1={}
emp_2={}
emp_3={}
emp_4={}
dict1={"emp1":emp_1,"emp2":emp_2,"emp3":emp_3,"emp4":emp_4}
for i in list_1:
    emp_1["name"]=list_1[0]
    emp_1["designation"]=list_1[1]
    emp_1["age"]=list_1[2]
    emp_1["salary"]=list_1[3]

for i in list_1:
    emp_2["name"]=list_2[0]
    emp_2["designation"]=list_2[1]
    emp_2["age"]=list_2[2]
    emp_2["salary"]=list_2[3]

for i in list_1:
    emp_3["name"]=list_3[0]
    emp_3["designation"]=list_3[1]
    emp_3["age"]=list_3[2]
    emp_3["salary"]=list_3[3]

for i in list_1:
    emp_4["name"]=list_4[0]
    emp_4["designation"]=list_4[1]
    emp_4["age"]=list_4[2]
    emp_4["salary"]=list_4[3]

with open("employ.json","w+") as saral:
    json.dump(dict1,saral,indent=4)
    saral.close()