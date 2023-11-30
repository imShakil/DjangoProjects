
#!/usr/bin/env python3

#############################   
## author: imShakil@github ##   
#############################  

import os
import glob
import json
import requests

path = 'data/feedback/'
req_url = 'http://127.0.0.1:8000/feedback/'

def post_data(data):
    print(type(data))
    print(data["title"])
    pass
    try:
        response = requests.post(url=req_url, json=data)
        print(response)
    except Exception as e:
        return e
    return "success"

def do():
    for file in os.listdir(path):
        abs_file = os.path.join(path, file)
        print(abs_file)
        lines = open(abs_file, 'r').read().split('\n')
        data = dict()
        data["title"] = lines[0]
        data['name'] = lines[1]
        data['date'] = lines[2]
        data['feedback'] = lines[3]
        print(data)
        print(post_data(data))

do()


#test = {"title": "Experienced salespeople", "name": "Alex H.", "date": "2020-02-02", "feedback": "It was great to talk to the salespeople in the team, they understood my needs and were able to guide me in the right direction"}
#post_data(test)
