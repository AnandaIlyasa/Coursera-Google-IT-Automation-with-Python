#!/usr/bin/env python3
import operator
import re


def count_error_messages(log_file):
    error_messages = {}
    with open(log_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            result = re.search(r"ticky: ERROR ([\w' ]*) ", line)
            if result:
                message = result.group(1).strip()
                error_messages[message] = error_messages.get(message, 0) + 1
        f.close()

    sorted_error_messages = sorted(
        error_messages.items(), key=operator.itemgetter(1), reverse=True)
    with open("error_message.csv", "w") as f:
        f.write("Error, Count\n")
        for message, count in sorted_error_messages:
            f.write("{}, {}\n".format(message, count))
        f.close()


def count_user_entries(log_file):
    user_info_entries = {}
    user_error_entries = {}
    with open(log_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            info = re.search(r"ticky: INFO [\w\[\]\#' ]+ \(([\w\.]+)\)", line)
            error = re.search(
                r"ticky: ERROR [\w\[\]\#' ]+ \(([\w\.]+)\)", line)
            if info:
                username = info.group(1).strip()
                user_info_entries[username] = user_info_entries.get(
                    username, 0) + 1
            if error:
                username = error.group(1).strip()
                user_error_entries[username] = user_error_entries.get(
                    username, 0) + 1
        f.close

    users = sorted({**user_info_entries, **user_error_entries}.keys())
    with open("user_statistics.csv", "w") as f:
        f.write("Username, INFO, ERROR\n")
        for user in users:
            f.write("{}, {}, {}\n".format(user, user_info_entries.get(
                user, 0), user_error_entries.get(user, 0)))


if __name__ == "__main__":
    log_file = "syslog.log"
    count_error_messages(log_file)
    count_user_entries(log_file)
