#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from datetime import datetime
import glob
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()


def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1, 20)
    report_contents_paragh = Paragraph(paragraph, styles["BodyText"])
    report.build([report_title, empty_line, report_contents_paragh])