#!/usr/bin/python3
import requests
import json, sys
from config import base64_api_key

company_name = input("\nCompany name: ")
company_number = input("\nCompany Number: ")

# Base64 your API and use it in Basic Authorization
headers = {"Authorization":	f"Basic {base64_api_key}"}

web_url = 'https://api.companieshouse.gov.uk'

def list_persons():
    url = f"{web_url}/company/{company_number}/officers"
    response = requests.get(url, headers=headers)
    data = json.loads(response.content)

    # {'error': 'Invalid Authorization', 'type': 'ch:service'}
    if data["error"] == "Invalid Authorization":
        print(f"\nError: {data['error']}\nCheck your authentication.")
        sys.exit()
    else:
        if data["items"]:
            people_names = [names["name"] for names in data["items"]]
            people_dob = [dob.get("date_of_birth", "Not Specified") for dob in data["items"]]
            people_occupation = [positions.get("occupation", "Not Specified") for positions in data["items"]]
        else:
            print("\nNo data found...\n")

    for names, dob, job in zip(people_names, people_dob, people_occupation):
        print(f"Name: {names} \nDoB: {dob} \nTitle: {job}\n")

print("\n")
list_persons()
