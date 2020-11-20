"""
Ladelle Augustine
Data Spatial Course Practice
Fall 2020
Midwestern state University
----------------------------------------------------------------
 This is a program that test out Flask. 
 I did 'pip install Flask' in the command line ad it already was 
 installed, then iI went to  'http://127.0.0.1:5000/ in the URL
 And the code shoudl run  and say 'Hello World - Ladelle Augustine!
 Press CTRL +C  to quit 
"""
"""
*********************** WHAT IS FLASK ? ************************
Flask is a micro web framework written in Python.
It does not require particular tools or libraries.
flask supports extensions that can add application features as 
if they were implemented in flask itself. 
-- can use in terminal 'pip install Flask' , can use a virtual 
environment like conda so you can use different dependencies 
depending on what project your doing. 
- -- uses an URL to look at results sample code below. 
****************************************************************
********************** WHAT IS GEOPANDAS ? *********************
GeoPandas is an open source project to make working with
geospatial data in python easier. It extend the datatypes used 
by pandas to allow spatial operations on geometric types. 
              " Used for Reading & writing files"
****************************************************************
********************** WHAT IS PANDAS ? ************************
Pandas is a fast, powerful, flexible and easy to use open
source data analysis and manipulation tool, built on top of the
Python programming language. 
****************************************************************
********************** WHAT IS FOLIUM ? ************************
Folium is a powerful Python library that helps you create
several types of Leaflet maps (leaflet.js), by maniupulating
 data and visualizing it on Leaflet map via folium. 
****************************************************************
********************** WHAT IS BRANCA ? ************************
Branca is a spinoff Library from folium. It host the non-map-
specific features. It is based on Kinja2 only. There is no 
documentation.
****************************************************************
********************* WHAT IS REQUESTS ? ***********************
Requests allows you to send HTTP/1.1 requests extremely easily.
It is designed to be used by humans to interact with the
language. It can add content like headers, form data, multipart
files, and parameters via simple Python libraries. Also, it 
allows you to access the response data of python int he same way.  
No need to manually add query strings to your URLs, or to form-
encode your POST data.
*****************************************************************
********************* WHAT IS JSON ? ****************************
JSON (JavaScript Object Notation) is a lightweight data 
interchange  format inspired by JavaScript object literal syntax.
json exposes an API familiar to users of the standard library
'marshal' & 'pickle' modules. Json is a subset of YAML 1.2 
*****************************************************************
********************* WHAT IS JSONIFY ? *************************
JSONIFY -- jsonify() function in flask returns a flask.Response()
object that already has the appropriate content-type header
'application/json' for use with json responses.
jsonify() also handles kwargs or dictinaries. 
Usefule when your building an API someone would query & expect 
json in return. 
****************************************************************
****************** WHAT IS FEATURES ? ***************************
A feature is a spatially bounded entity.
A feature is an object that represents a spatially bounded thing. 
Every Feature object is a GeoJson object no matter where it occurs
in a GeoJson text. 
A feature object has a "type" member with the value "Feature"
A feature object has a member with the name "geometry". The value 
of the geometry member SHALL be either a Geometry object as 
defined above or, in the case that the Feature is unlocated, a 
JSON null value. 
A feature object has a member with the name "properties". The
value of the properties member is an object ( any JSONB object
or a JSON null value.)
*****************************************************************
********************* WHAT IS GEOJSON ? ************************
Examples: https://leafletjs.com/examples/geojson/
GEOJSON (geo JavaScript Object Notation) is an open standard
format designed for representing simple geographical feautres, 
along with their non-spaatial attributes. It is based on the 
JSON format. The features include points ex.addresses & locations,
line strings ex. streets, highways & boundaries, polydons ex. 
countries, provinces, tracts of land, and multi-part collections
of these types.
A noteable offspring of GeoJSON is TopoJson, and extension of
GeoJSON that encodes geospatial topology, typically provides
smaller file sizes. 
GeoJSON format differs from other GIS standars in that it was 
written & maintained not by formal standards organization, but
by an internet working group of developers. 
*****************************************************************
****************** WHAT IS GEOJSONTOOLTIP ? *********************
GeoJSONTooltip (GeoJavaScript Object Notation Tool Tip) - Displays
a text when hovering over the object.  
GeoJSONToolTip allows you to access the properties keys in each 
GeoJSon features with fields kwargs, while Tooltip will write 
the same text string as Tooltip content for each feature.
*****************************************************************
****************** WHAT IS GEOJSONPOPUP ? *********************
GeoJSONPopup (GeoJavaScript Object Notation POP UP) -- inputs
text or visualization for object displayed when clicking. 
Geojsonpopup can be attached to features when thay are clicked. 
Ex. feature.properties.popupContent 
*****************************************************************
****************** WHAT IS FOLIUM.PLUGINS ? *********************
leaflet external plugins
Ex. https://python-visualization.github.io/folium/plugins.html
******************* WHAT IS MOUSEPOSITION? *********************
MousePosition - adds a field that shows the coordinates of the
mouse position.
Ex. Syntax of plugin mouseposition
(
    position='bottomright', separator=' : ', empty_string=
    'Unavailable',lng_first=False, num_digits=5, prefix='', 
     lat_formatter=None, lng_formatter=None, **kwargs
)
****************************************************************
************** CORS(Cross Origin Resource Sharing) *************
This package by default, submission of cookies across domains is 
disabled due to the security implication. Helps do request 
locally and javascript wont have an issue.
****************************************************************
"""

"""
-------------------------- CODE BEGINS --------------------------
"""
# ************************* IMPORTS USED *************************
from json import loads
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json
from scipy import spatial
from scipy.spatial import KDTree
import kdtree as kd
from folium.features import GeoJson, GeoJsonTooltip, GeoJsonPopup
import geopandas as gpd
import pandas as pd
import folium
import branca
import requests
import geojson
import numpy as np
import os,sys
from flask import request, url_for, render_template,redirect
from flask import make_response  # justa THJISSSJKDJFNKNDFKJN

"""
********************************************FLASK APP *******************************************************
"""
app = Flask(__name__)
CORS(app)             

"""
********************************************  METHODS *******************************************************
def getPoints()              --->     get the constellation file to get coordinates and save variable data. 
def get_constellations()     --->     gets the Zodiac coordinates from file      *NOT USED YET*
def getTree(data)            --->     Stores the data points into KDTree --> takes in param <data>
def getZodiacFrame()         --->     gets the Constellation borders            *NOT USED YET* 
*************************************************************************************************************
"""

# Gets the list of longitude and latitude coordinates from  my constPoint.geojson file 
def getPoints():                                           # The name of the file 
    data_file = 'map(1).geojson'
    if os.path.isfile(data_file):
        with open(data_file,'r') as f:
            data = f.read()
    else:
        return jsonify({"Error":"map(1).geojsonnot there!!"})

    return json.loads(data)
    

# Gets the Zodiac coordinates ----- ******NOT USED YET*******. 
def get_constellations():
    with open('ZCors.json') as f:
        data = f.read()
    return loads(data)

# Places the Coordinates into the KDTree
def getTree(data):
    cor = []                                                                # Dictionary for cordinates 
    for feature in data['features']:                                        # Take the features and search for coordinates
        cor.append(feature['geometry']['coordinates'])
    tree = KDTree(cor)                                    
    return tree, cor                                                        # Returns tree and cor

# Gets the outline of the Constellation borders ---- *****NOT USED YET***.
def getZodiacFrame():
    data_file = 'constellations.lines.json'
    if os.path.isfile(data_file):
        with open(data_file,'r') as f:
            data = f.read()
    else:
        return jsonify({"Error":"constellations.lines.json not there!! "})
    return json.loads(data)

"""
*****************************************  ROUTES *********************************************************
@app.route('/', methods=['GET','POST'])
This app loads the map as soon as you get to the localhost. 
I used my mapbox_access_token and used a template folder that has my html file to showcase my map. 
@app.route('/click/')
This is used to take in the click arguments and store them in lng, lat. 
The information is then taken to check the 5 nearest neighbors and the distance from the click. 
using the KDTree <tree> query. I increased the distance upper bound because the data points are
not as much to have a closer range. 
**********************************************************************************************************
"""

@app.route('/', methods=['GET','POST'])
def index():
     # getting map uploaded to webpage
    mapbox_access_token = 'pk.eyJ1IjoibGFkZWxsZTk0IiwiYSI6ImNrZmQxMXRvazB3a3gyeHBkaDVlcjN0MWwifQ.wHkuN_fFX5p5muYQY6tIhQ'
    return render_template('index.html',mapbox_access_token=mapbox_access_token)

@app.route('/click/')
def click():
    global lnglatlist     # global variable
    lookcor = []
    lnglatlist = []
    lng,lat = request.args.get("lngLat",None).split(",")                           # Takes in the click arguments
    lookcor.append(float(lng))
    lookcor.append(float(lat))
   
    distanceList, neighborList = tree.query(lookcor,k=10,distance_upper_bound=190)  # Checks the 10 closes neighbord to point
    
    for i in range(0,len(distanceList)):
        print(f"\nLng, Lat: {lng}, {lat}\nNearest neighbor: {cor[neighborList[i]]}\tDistance: {distanceList[i]}")
    
    for i in neighborList:                                           # Prints out the (5) nearest coordinates and distances
        point = geojson.Point(cor[i])
        lnglatlist.append(geojson.Feature(geometry=point,properties = None))
    lnglatlist = geojson.FeatureCollection(lnglatlist)
    return "jsonify"

lnglatlist = []
@app.route('/neighbors')
def showNeighbors():
    global lnglatlist


    return lnglatlist
 
if __name__ == '__main__':  
    points = getPoints()
    tree, cor = getTree(points)
    app.run(host='localhost', port=8080)                                            # Runs the app
 