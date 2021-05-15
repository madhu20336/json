import json
def complex_number(object):
    if "complex" in object:
        return complex(object['real'], object['img'])
    return object
complex_object =json.loads('{ "real": 4, "img": 5}')
print(complex_number(complex_object))