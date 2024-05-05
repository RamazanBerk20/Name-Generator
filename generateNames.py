# Description: This file creates txt files with 10000 names using api
# Use threading to create the files faster

import requests, threading

max_results = 5000

def t_M():
    with open("male_names.txt", "w", encoding='utf-16') as file:
        response = requests.get("https://randomuser.me/api/", params={"gender": "male", "results": max_results})
        data = response.json()

        for i in range(0, max_results):
            name = data["results"][i]["name"]["first"]
            surname = data["results"][i]["name"]["last"]
            nat = data["results"][i]["nat"]
            file.write(f"{name} {surname} -> {nat}\n")

def t_F():
    with open("female_names.txt", "w", encoding='utf-16') as file:
        response = requests.get("https://randomuser.me/api/", params={"gender": "female", "results": max_results})
        data = response.json()
        
        for i in range(0, max_results):
            name = data["results"][i]["name"]["first"]
            surname = data["results"][i]["name"]["last"]
            nat = data["results"][i]["nat"]
            file.write(f"{name} {surname} -> {nat}\n")

def create_txt():

    t1 = threading.Thread(target=t_M)
    t2 = threading.Thread(target=t_F)

    t1.start()
    t2.start()

    # Wait for the threads to finish
    t1.join()
    t2.join()

print("Generating Names...")
create_txt()