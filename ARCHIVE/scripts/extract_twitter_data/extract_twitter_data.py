#!/usr/bin/env python3

import json
import re

with open('/Users/alan/Desktop/tweets.json') as _json:
    json_data = json.load(_json)
    band_lines = []
    for tweet in json_data:
        tweet_text = tweet['tweet']['full_text']
        if re.search('band', tweet_text, re.IGNORECASE):
            if re.search('new', tweet_text, re.IGNORECASE):
                band_lines.append(tweet_text)

    band_names_processed = []
    album_names = []
    for band_line in band_lines:
        band_line = re.sub(r'"', '', band_line)
        band_line = re.sub(r' is the name of my new band.', '', band_line)
        band_line = re.sub(r' is the name of my new band', '', band_line)
        if re.search(r'album', band_line):
            album_names.append(band_line)
        else:
            band_names_processed.append(band_line)

with open('band_names.txt', 'w') as _bn:
    for band_name in band_names_processed:
        _bn.write(band_name)
        _bn.write("\n")

with open('album_names', 'w') as _an:
    for album_name in album_names:
        _an.write(album_name)
        _an.write("\n")




