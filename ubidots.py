import urequests as requests
import keys

TOKEN = keys.token #Import your key from key file

# Builds the JSON-object to send the POST HTTP request
def build_json(variable1, value1, variable2, value2, variable3, value3):
    try:
        lat = 56.029394
        lng = 14.156678
        data = {variable1: {"value": value1},
                variable2: {"value": value2, "context": {"lat": lat, "lng": lng}},
                variable3: {"value": value3}}
        return data
    except:
        return None


# Sends the POST HTTP request. Please reference the REST API reference https://ubidots.com/docs/api/
def sending_data_to_ubidots(device, value1, value2, value3):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json("temperature", value1, "position", value2, "pH", value3)
        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass
