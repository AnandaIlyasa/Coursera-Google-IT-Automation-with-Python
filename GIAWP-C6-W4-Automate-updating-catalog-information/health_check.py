#!/usr/bin/env python3

import socket
import psutil
from emails import generate_email


def check_host_is_not_matched(name, expected_address):
    address = socket.gethostbyname(name)
    return address != expected_address

def check_cpu_is_high(interval):
    precentage = psutil.cpu_percent(interval=interval)
    return precentage > 80

def check_disk_space_is_low(path):
    _, percent_usage, _, _ = psutil.disk_usage(path)
    return percent_usage > 80

def check_memory_space_is_low():
    free_memory_b = psutil.virtual_memory().free
    free_memory_mb = free_memory_b / 1000000
    return free_memory_mb < 500

def main():
    if check_host_is_not_matched('localhost', '127.0.0.1'):
        generate_email(
            sender="automation@example.com",
            recipient="student-03-a317f892e602@example.com",
            subject="Error - localhost cannot be resolved to 127.0.0.1",
            body="Please check your system and resolve the issue as soon as possible.",
            smtp_server='localhost'
        )

    if check_cpu_is_high(10.0):
        generate_email(
            sender="automation@example.com",
            recipient="student-03-a317f892e602@example.com",
            subject="Error - CPU usage is over 80%",
            body="Please check your system and resolve the issue as soon as possible.",
            smtp_server='localhost'
        )

    if check_disk_space_is_low('/'):
        generate_email(
            sender="automation@example.com",
            recipient="student-03-a317f892e602@example.com",
            subject="Error - Available disk space is less than 20%",
            body="Please check your system and resolve the issue as soon as possible.",
            smtp_server='localhost'
        )

    if check_memory_space_is_low():
        generate_email(
            sender="automation@example.com",
            recipient="student-03-a317f892e602@example.com",
            subject="Error - Available memory is less than 500MB",
            body="Please check your system and resolve the issue as soon as possible.",
            smtp_server='localhost'
        )

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Health check error : {}".format(e))
