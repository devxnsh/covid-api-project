import requests
import json

def tracker(d_id,date):    
    link="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+d_id+"&date="+date
    #creates link from provided data
    response=requests.get(link)
    responsetext=response.text
    #acquires json object via requesting on created link
    if response.ok: #checks for permission or other errors
        with open("somefiles.json", "w") as fher:
            responsetexts=json.loads(responsetext)
            json.dump(responsetexts,fher,indent=2)
            fher.close()# writes acquired data in a json file, which is created automatically.
if __name__ == "__main__":
    dist_id=str(input("enter district id"))
    day=str(input("Enter date of month"))
    month=str(input("Enter month 01-12"))
    year=str(input("Enter year"))
    dates=day+"-"+month+"-"+year

