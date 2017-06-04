#!/usr/bin/env python

__author__ = 'ryn'
from lxml import etree
import csv, sys

if len(sys.argv) == 2:
    out = "<!DOCTYPE NETSCAPE-Bookmark-file-1>\n" \
          "<TITLE>Bookmarks</TITLE>\n" \
          "<H1>Bookmarks</H1>\n" \
          "<DL><p>\n"
    with open(sys.argv[1], 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                a = etree.Element("A", HREF=row[1])
                a.text = row[0].decode("utf-8")
                out += "<DT>" + etree.tostring(a) + "\n"
                out += "<DD>" + row[1].decode("utf-8") + "\n"

    out += "</DL><p>"

    print out.encode("utf-8")
else:
    print "Nothing to convert"
