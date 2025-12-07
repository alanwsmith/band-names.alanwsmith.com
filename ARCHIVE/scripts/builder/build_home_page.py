#!/usr/bin/env python3

from itertools import groupby
from string import Template

from pprint import pprint 

template_path = "template.html"
output_path = "../../site/index.html"

content = {}

data = []
names = []
keys = []

def primarysort(input):
    return input['sort_key']

def keymaker(input):
    return input['sort_key'][0].upper()

with open('data.txt') as _data:
    for line in _data:
        data.append({
            "sort_key": line.strip().lower().replace('the ', ''),
            "value": line.strip()
            })

data = sorted(data, key=primarysort)
# pprint(data)

for k, g in groupby(data, keymaker):
    names.append(list(g))
    keys.append(k)
the_stuff = []

for key_num in range(0, len(keys)):
    the_stuff.append(f"<h3>{keys[key_num]}</h3>")
    the_stuff.append("<ul>")
    for name in names[key_num]:
        the_stuff.append(f"<li>{name['value']}</li>")
    the_stuff.append("</ul>")
content['CONTENT'] = "".join(the_stuff)

with open(template_path) as _template:
    template = Template(_template.read())
    with open(output_path, 'w') as _output:
        _output.write(
            template.substitute(content)
        )

