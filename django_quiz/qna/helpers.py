
def generateresponse(status, modelobject, data):
    if status == 'Success':
        response = {
            "status": "Success",
            "data": {
                modelobject: data
            }
        }
    return response

def deleteEmptyOptions(**kwargs):
    for k, v in kwargs.items():
        if v == "":
            del kwargs[k]
    return kwargs