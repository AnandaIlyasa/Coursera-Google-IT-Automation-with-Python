#!/usr/bin/env python3

import glob
import requests


url = "http://localhost/upload/"
images = glob.glob("./supplier-data/images/" + "*.jpeg")
for im in images:
    with open(im, 'rb') as file:
        r = requests.post(url, files={'file': file})
        if not r.status_code in range(200,300):
            print("Request failed with status code : {}".format(r.status_code))
        file.close()