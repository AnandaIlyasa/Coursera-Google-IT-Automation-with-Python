#!/usr/bin/env python3

from datetime import datetime
import glob
import reports
import emails


def generate_paraghraph_contents(src_path):
    fruit_descriptions = glob.glob(src_path)
    report_contents = []
    for desc_file in fruit_descriptions:
        with open(desc_file, 'r') as file:
            name = "name: {}".format(file.readline())
            weight = "weight: {}".format(file.readline())
            report_contents.append(name + "<br/>" + weight)
            file.close()

    report_contents_str = "<br/><br/>".join(report_contents)
    return report_contents_str

if __name__ == "__main__":

    #generat pdf report
    date_now = datetime.now().strftime('%B %d, %Y')
    report_attachment = "/tmp/processed.pdf"
    report_title = "Processed Update on {}".format(date_now)
    report_paragraph = generate_paraghraph_contents("./supplier-data/descriptions/*")
    reports.generate_report(report_attachment, report_title, report_paragraph)

    #send email
    emails.generate_email(
        sender="automation@example.com",
        recipient="student-03-a317f892e602@example.com",
        subject="Upload Completed - Online Fruit Store",
        body="All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        attachment="/tmp/processed.pdf",
        smtp_server='localhost'
    )