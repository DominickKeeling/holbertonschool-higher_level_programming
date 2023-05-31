#!/usr/bin/python3
"""add item module"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

listp = []
try:
    listp = load_from_json_file("add_item.json")
except:
    pass
for i in range(1, len(sys.argv)):
    listp.append(sys.argv[i])
save_to_json_file(listp, "add_item.json")
