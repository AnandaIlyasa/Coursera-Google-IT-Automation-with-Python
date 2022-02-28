#!/usr/bin/env python3

import glob
import requests
from os import path

url = "http://34.67.126.191/fruits/"
source_path = "./supplier-data/descriptions/"
fruit_descriptions = glob.glob("./supplier-data/descriptions/" + "*")
for desc_file in fruit_descriptions:
    fruit_desc = {}
    with open(desc_file, 'r') as file:
        name = file.readline()
        weight, _ = file.readline().split()
        description = file.read()
        fruit_desc['name'] = name
        fruit_desc['weight'] = weight
        fruit_desc['description'] = description
        fruit_desc['image_name'] = path.basename(desc_file).split(".")[0] + ".jpeg"
        r = requests.post(url, json=fruit_desc)
        if not r.status_code in range(200,300):
            print("Request failed with status code : {}".format(r.status_code))
        file.close()