#!/usr/bin/env python3

with open('./band_names_edited_sorted.txt') as _in:
    lines = _in.read().split("\n")
    for line in lines:
        print(f"<li>{line}</li>")

