# This script takes a string input in the form of Degrees Minutes Seconds
# or DDºMM'SS" and converts into decimal degrees for geopandas use.
# This will take both Lat and Long inputs and identify using 'N'/'S' and
# 'E'/'W'.

# Author: Mitchell Baum
# v0.1


def convert(latlong):
    new = latlong.replace(' ', '').replace(u'°', ' ').replace("\'", " ").replace('\"', ' ')
    deg, minutes, sec, direction = new.split(' ')
    dd = float(deg) + (float(minutes)/60) + (float(sec)/3600)
    if direction in ('S', 'W'):
        dd *= -1
    return dd
