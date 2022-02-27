#! /usr/bin/env python

from os import listdir
import requests

SOURCE_PATH = "./percobaan/"
EXTERNAL_IP = "34.134.223.149"


def upload_files(source_path, external_ip):
    filenames = listdir(source_path)
    for file in filenames:
        feedback = {}
        with open(source_path + file, "r") as f:
            feedback['title'] = f.readline().strip()
            feedback['name'] = f.readline().strip()
            feedback['date'] = f.readline().strip()
            feedback['feedback'] = ' '.join(f.readlines())
            response = requests.post(
                'http://' + external_ip + '/feedback/', feedback)
            status_code = response.status_code
            if status_code in range(200, 300):
                print("Status code : {}".format(status_code))
            else:
                print("Request fail with status code : {}".format(status_code))


if __name__ == "__main__":
    upload_files(SOURCE_PATH, EXTERNAL_IP)
