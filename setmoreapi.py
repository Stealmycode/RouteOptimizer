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
    return appointments.json()["data"]["appointments"]
print(appointmentGetter())