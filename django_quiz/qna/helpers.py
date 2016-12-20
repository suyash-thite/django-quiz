
def generateresponse(status, modelobject, data):
    if status == 'Success':
        response = {
            "status": "Success",
            "data": {
                modelobject: data
            }
        }

    return response