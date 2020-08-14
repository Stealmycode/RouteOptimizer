import datetime
import requests
from config import setmoreRefresh

def datestring(date):
    x = str(date).split("-")
    x.reverse()
    return "-".join(x)

def tokenGetter():
    accessResponse = requests.get("https://developer.setmore.com/api/v1/o/oauth2/token?refreshToken=" + setmoreRefresh)
    accessToken = accessResponse.json()["data"]["token"]["access_token"]
    return accessToken

def appointmentGetter():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days = 1)
    appointments = requests.get(
        "https://developer.setmore.com/api/v1/bookingapi/appointments?startDate=" 
        + datestring(today) 
        + "&endDate=" 
        + datestring(tomorrow) 
        + "&customerDetails=true",
        headers = {
            "Authorization": "Bearer "+ tokenGetter(),
            "Content-Type" : "application/json"})
    try:
        results = appointments.json()["data"]["appointments"]
    except:
        print("ERROR")
        results = "Error"
    return results

def appointmentParser(appointments):
    dailySchedule = []
    for aptInfo in appointments: #dictionary comprehension seemed too complicated with nested dictionaries
        appointment = {
            'date': aptInfo["start_time"][0:10], 
            'time': aptInfo["start_time"][11:],
            'duration': aptInfo["duration"], 
            'first': aptInfo["customer"]["first_name"],
            'last': aptInfo["customer"]["last_name"],
            'email': aptInfo["customer"]["email_id"],
            'phone': aptInfo["customer"]["cell_phone"],
            'address': aptInfo["customer"]["address"],
            'city': aptInfo["customer"]["city"],
            'state': aptInfo["customer"]["state"],
            'zip': aptInfo["customer"]["postal_code"],
            'dob': aptInfo["customer"]["additional_fields"]["Date of Birth"],
            'gender': aptInfo["customer"]["additional_fields"]["Gender"],
            'label': aptInfo["label"]}
        dailySchedule.append(appointment)
    return dailySchedule

print([list(apt.values()) for apt in appointmentParser(appointmentGetter())])
        
