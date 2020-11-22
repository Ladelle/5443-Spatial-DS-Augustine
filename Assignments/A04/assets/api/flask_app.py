import os
import sys
import json
import csv
import geojson
import geopandas as gpd

from flask import Flask,  url_for
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask import send_file
import glob
from scipy.spatial import KDTree # added this 10/18/2020
from misc_functions import haversine, bearing

base_path = '5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data'

app = Flask(__name__)
CORS(app)

def isJson(data):
    """
    Helper method to test if val can be json 
    without throwing an actual error.

    """
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

def load_data(path):
    """
    Given a path, loads the file and handles it based on its extension type. 
    So far there is code for json and csv files.

    """
    _, ftype = os.path.splitext(path) # get fname(_), and extension

    if os.path.isfile(path):
        with open(path) as f:
            if ftype == ".json":   # handles json
                data = f.read()
                if isJson(data):
                    return json.loads(data)

            elif ftype == ".csv": # handles csv with csv reader
                with open(path, newline='') as csvfile:
                     data = csv.DictReader(csvfile)

                     return list(data)
            elif ftype == ".geojson":  # added this 10/18/2020 --> changed this 10/20/2020
                with open(path) as f:
                    if ftype == ".geojson":
                        data = f.read()
                        return json.loads(data)


    return None


#  ██╗  ██╗██████╗ ████████╗██████╗ ███████╗███████╗███████╗                                                                                                                                  
#  ██║ ██╔╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔════╝                                                                                                                                  
#  █████╔╝ ██║  ██║   ██║   ██████╔╝█████╗  █████╗  █████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
#  ██╔═██╗ ██║  ██║   ██║   ██╔══██╗██╔══╝  ██╔══╝  ██╔══╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
#  ██║  ██╗██████╔╝   ██║   ██║  ██║███████╗███████╗███████╗                                                                                                                                  
#  ╚═╝  ╚═╝╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝                                                                                                                                  
                                                                                                                                                                                            

def getTree():
    coords = []
    # with open ('Assignments/A04/assets/api/data/fixed_ufos.geojson', 'r') as f:
    #     data = json.load(f)
    
    for feature in UFO['features']:
        if type(feature['geometry']['coordinates'][0]) !=float or type(feature['geometry']['coordinates'][1]) !=float:
            pass
        else:
            coords.append(feature['geometry']['coordinates'])

    tree = KDTree(coords)
    print("This is tree: ",tree)
    return tree, coords

"""
---------------------------------------------------------------------------------------------------------------
---------------------------------------DATA BACKEND-----------------------------------------------------------
---------------------------------------------------------------------------------------------------------------

"""

"""
BIG GLOBALS --> KIND OF ACTING LIKE DATABASE
"""

# ██████╗  █████╗ ████████╗ █████╗     ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗     
# ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝     
# ██║  ██║███████║   ██║   ███████║    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗    
# ██║  ██║██╔══██║   ██║   ██╔══██║    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║    
# ██████╔╝██║  ██║   ██║   ██║  ██║    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝    
# ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     
                                                                                                

"""
DATA

"""
STATES = load_data("5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/states.json")
STATES_BBOXS = load_data("5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/us_states_bbox.csv")
UFO = load_data("5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/fixed_ufos.geojson")
CRASH =load_data("5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/plane_crashes/crash_data_1920-2020.json")
# EARTHQUAKE = load_data("/Users/Delly/Desktop/NewEnv/5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/earthquake_2020_7.json")
# RAILROADS = load_data("/Users/Delly/Desktop/NewEnv/5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/us_railroads.geojson")

# with open("/Users/Delly/Desktop/NewEnv/5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/states.json") as f:
#     data = f.read()
# STATES = json.loads(data)  

# data = open(os.path.join(base_path,"color.names.json"),'r').read()
# COLORS = json.loads(data)

# data = open(os.path.join(base_path,'states.json'),'r').read()
# STATES = json.loads(data)

# crash_files = glob.glob(os.path.join(base_path,"plane_crashes/crash_data/*.json"))

# ADDED 10/20/2020 @ 6:13PM ---------------------------------------------------------------------------
sid = -1
result_feature ={
    'type': 'FeatureCollection',
    'features':[],
}


# ██████╗  ██████╗ ██╗   ██╗████████╗███████╗███████╗
# ██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝
# ██████╔╝██║   ██║██║   ██║   ██║   █████╗  ███████╗
# ██╔══██╗██║   ██║██║   ██║   ██║   ██╔══╝  ╚════██║
# ██║  ██║╚██████╔╝╚██████╔╝   ██║   ███████╗███████║
# ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚══════╝
                                                   
"""
  ------------------------ ROUTES --------------------------------------------
"""

@app.route("/token", methods=["GET"])
def getToken():
    """ getToken: this gets mapbox token
    """
    with open("/Users/Delly/Desktop/NewEnv/mapboxtoken.txt") as f:
        tok = f.read()
    token = {'token':tok}
    return token

@app.route("/", methods=["GET"])
def getRoutes():
    """ getRoutes: this gets all the routes!
    """
    routes = {}
    for r in app.url_map._rules:
        
        routes[r.rule] = {}
        routes[r.rule]["functionName"] = r.endpoint
        routes[r.rule]["help"] = formatHelp(r.endpoint)
        routes[r.rule]["methods"] = list(r.methods)

    routes.pop("/static/<path:filename>")
    routes.pop("/")

    response = json.dumps(routes,indent=4,sort_keys=True)
    response = response.replace("\n","<br>")
    return "<pre>"+response+"</pre>"

#      ██╗███████╗ ██████╗ ███╗   ██╗    ███████╗ █████╗ ██╗   ██╗███████╗██████╗     ███████╗██████╗  ██████╗ ███╗   ██╗████████╗    ███████╗███╗   ██╗██████╗     ██╗███╗   ██╗███████╗ ██████╗ 
#      ██║██╔════╝██╔═══██╗████╗  ██║    ██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██╔════╝██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝    ██╔════╝████╗  ██║██╔══██╗    ██║████╗  ██║██╔════╝██╔═══██╗
#      ██║███████╗██║   ██║██╔██╗ ██║    ███████╗███████║██║   ██║█████╗  ██║  ██║    █████╗  ██████╔╝██║   ██║██╔██╗ ██║   ██║       █████╗  ██╔██╗ ██║██║  ██║    ██║██╔██╗ ██║█████╗  ██║   ██║
# ██   ██║╚════██║██║   ██║██║╚██╗██║    ╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  ██║  ██║    ██╔══╝  ██╔══██╗██║   ██║██║╚██╗██║   ██║       ██╔══╝  ██║╚██╗██║██║  ██║    ██║██║╚██╗██║██╔══╝  ██║   ██║
# ╚█████╔╝███████║╚██████╔╝██║ ╚████║    ███████║██║  ██║ ╚████╔╝ ███████╗██████╔╝    ██║     ██║  ██║╚██████╔╝██║ ╚████║   ██║       ███████╗██║ ╚████║██████╔╝    ██║██║ ╚████║██║     ╚██████╔╝
#  ╚════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝       ╚══════╝╚═╝  ╚═══╝╚═════╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                                                                                                                                                                
"""
THIS FILE HAS INFO FRON FRONT END SAVED TO JSON FILE
"""
@app.route('/jsonSavedFront')
def jsonSavedFront():
    with open('/Users/Delly/Desktop/NewEnv/5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/mapPoints.geojson','w') as out:
        json.dump(result_feature, out, indent = "   ")
    

    return "DONE"


# ██████╗ ███████╗██╗      ██████╗  █████╗ ██████╗          ██╗███████╗ ██████╗ ███╗   ██╗    ███████╗██╗██╗     ███████╗    
# ██╔══██╗██╔════╝██║     ██╔═══██╗██╔══██╗██╔══██╗         ██║██╔════╝██╔═══██╗████╗  ██║    ██╔════╝██║██║     ██╔════╝    
# ██████╔╝█████╗  ██║     ██║   ██║███████║██║  ██║         ██║███████╗██║   ██║██╔██╗ ██║    █████╗  ██║██║     █████╗      
# ██╔══██╗██╔══╝  ██║     ██║   ██║██╔══██║██║  ██║    ██   ██║╚════██║██║   ██║██║╚██╗██║    ██╔══╝  ██║██║     ██╔══╝      
# ██║  ██║███████╗███████╗╚██████╔╝██║  ██║██████╔╝    ╚█████╔╝███████║╚██████╔╝██║ ╚████║    ██║     ██║███████╗███████╗    
# ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚══════╝    
  
"""
THIS FILE takes the json file we created using the front end info and reloads it 
"""                                                                                                                         

@app.route('/reload')
def reloadJson():
    global sid, result_feature
    with open('/Users/Delly/Desktop/NewEnv/5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/mapPoints.geojson','r') as infile:
       result_feature= json.load(infile)
       coordinatesNum = len(result_feature['features'])
       sid = coordinatesNum
    

    return jsonify(coordinatesNum,result_feature['features'])

# ██████╗  ██████╗ ██╗███╗   ██╗████████╗███████╗ █████╗ ██╗   ██╗███████╗██████╗ 
# ██╔══██╗██╔═══██╗██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
# ██████╔╝██║   ██║██║██╔██╗ ██║   ██║   ███████╗███████║██║   ██║█████╗  ██║  ██║
# ██╔═══╝ ██║   ██║██║██║╚██╗██║   ██║   ╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  ██║  ██║
# ██║     ╚██████╔╝██║██║ ╚████║   ██║   ███████║██║  ██║ ╚████╔╝ ███████╗██████╔╝
# ╚═╝      ╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═════╝ 
                                                                                
"""
Saves The points where the lon lat was called into feautre collection
Example: http://localhost:8080/pointSaved?lon=-82.1888889&lat=36.595
"""
@app.route('/pointSaved')
def pointSaved():
    global sid, result_feature
    sid +=1
    lon = float(request.args.get('lon',None))
    lat = float(request.args.get('lat',None))
    # num = int(request.args.get('num',None))
    result_feature['features'].append({
        'type':'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [lon, lat]
        },
        'properties': {
            'source': str(sid)
        }
    })
    return (str(sid))  #saves the source id # and returns it


# ██████╗  ██████╗ ██╗███╗   ██╗████████╗███████╗    ███████╗██████╗  █████╗ ███████╗███████╗██████╗ 
# ██╔══██╗██╔═══██╗██║████╗  ██║╚══██╔══╝██╔════╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
# ██████╔╝██║   ██║██║██╔██╗ ██║   ██║   ███████╗    █████╗  ██████╔╝███████║███████╗█████╗  ██║  ██║
# ██╔═══╝ ██║   ██║██║██║╚██╗██║   ██║   ╚════██║    ██╔══╝  ██╔══██╗██╔══██║╚════██║██╔══╝  ██║  ██║
# ██║     ╚██████╔╝██║██║ ╚████║   ██║   ███████║    ███████╗██║  ██║██║  ██║███████║███████╗██████╔╝
# ╚═╝      ╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝ 
                                                                                                   
"""
Erases the points in feature collection in after done in html
"""

@app.route('/pointErased')
def pointErased():
    global sid, result_feature
    sid = -1
    coordinatesNum = len(result_feature['features'])
    coordsErasedFromFile = result_feature['features']
    result_feature['feature'] = []
    print("coordinate #:",coordinatesNum,"coords erased:", coordsErasedFromFile)
    return jsonify(coordinatesNum,coordsErasedFromFile)

# ██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗    ███╗   ███╗ █████╗ ██████╗     ██████╗  █████╗ ████████╗ █████╗ 
# ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝    ████╗ ████║██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
# ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝███████╗    ██╔████╔██║███████║██████╔╝    ██║  ██║███████║   ██║   ███████║
# ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗╚════██║    ██║╚██╔╝██║██╔══██║██╔═══╝     ██║  ██║██╔══██║   ██║   ██╔══██║
# ███████╗██║  ██║   ██║   ███████╗██║  ██║███████║    ██║ ╚═╝ ██║██║  ██║██║         ██████╔╝██║  ██║   ██║   ██║  ██║
# ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝         ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝


                                                                                                               


# ███╗   ██╗███████╗ █████╗ ██████╗ ███████╗███████╗████████╗    ███╗   ██╗███████╗██╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ██████╗      ██████╗ ██████╗ ██████╗ ███████╗
# ████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝    ████╗  ██║██╔════╝██║██╔════╝ ██║  ██║██╔══██╗██╔═══██╗██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
# ██╔██╗ ██║█████╗  ███████║██████╔╝█████╗  ███████╗   ██║       ██╔██╗ ██║█████╗  ██║██║  ███╗███████║██████╔╝██║   ██║██████╔╝    ██║     ██║   ██║██║  ██║█████╗  
# ██║╚██╗██║██╔══╝  ██╔══██║██╔══██╗██╔══╝  ╚════██║   ██║       ██║╚██╗██║██╔══╝  ██║██║   ██║██╔══██║██╔══██╗██║   ██║██╔══██╗    ██║     ██║   ██║██║  ██║██╔══╝  
# ██║ ╚████║███████╗██║  ██║██║  ██║███████╗███████║   ██║       ██║ ╚████║███████╗██║╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║    ╚██████╗╚██████╔╝██████╔╝███████╗
# ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝       ╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                                                                                                                   
"""
GETS THE NEAREST NEIGHBORS 
"""

nearNum = -1
neighborsFeatures = {
    'type':'FeatureCollection',
    'features':[]
}

@app.route('/neighbor', methods = ["GET"])
def findNearestNeigbors():
    """ Description: Return x nearest neigbhors for give lon lat coords
        Params: 
            None
        Example: http://localhost:8080/neighbor?lon=<longitude>&lat=<latitude>&num=<number of nearest neighbors to find>
        http://localhost:8080/neighbor?lon=-2.916667&lat=53.2&num=10
    """
    global tree 
    global coords
    global nearNum
    global neighbors
    global sid
   
    
    nearNum += 1

    lon = float(request.args.get('lon',None))
    lat = float(request.args.get('lat',None))
    num = int(request.args.get('num',None))
    sid += 1
    searchCoords=[lon,lat]     #[[98.581081, 29.38421],[98.581081, 29.38421]]

    
    # returns an array of distances and an array of indices for nearest neighbors
    distanceList, neighborList = tree.query(searchCoords,k=num,distance_upper_bound=180)
    
    # prints the results of the query to the console
   # prints the results of the query to the console
    if num > 1:
        for i in range(0,len(distanceList)):
            print(f"\nLng, Lat: {lon}, {lat}\nNearest neighbor: {coords[neighborList[i]]}\tDistance: {distanceList[i]}")
           
    else:
            print(f"\nLng, Lat: {lon}, {lat}\nNearest neighbor: {neighborList}\tDistance: {distanceList}")
     
   
    neighbors = []
  
    if num == 1:
        point = geojson.Point(coords[0])
        neighbors.append(geojson.Feature(geometry=point )) 
    else:
        for i in neighborList:
            # neighbors.append(coords[i])
    # neighbors = geojson.FeatureCollection(neighbors)
           
            point = geojson.Point(coords[i])
            neighbors.append(geojson.Feature(id=sid,geometry=point,properties = None ))
    neighbors = geojson.FeatureCollection(neighbors)
   
    
    return neighbors #(str(nearNum),neighbors) #result_feature #handle_response(neighbors)


 
"""
VIDEO PART 2: STATES
Dr. Griffin : https://www.youtube.com/watch?v=WX9OBH8Zv0M

"""
@app.route('/states', methods=["GET"])
def states():
    """ Description: returns a list of us states names
        Params: 
            None
        Example: http://localhost:8080/states?filter= 
        This will get all states that starts with tex 
        creates a results list loops through states then creates
        results. it will search from the beginning of list up to the 
        lenght of the text that passing in. if get match then 
        result . append state. if dont have filter then returns all states. 
    """
    filter = request.args.get('filter',None) 
    
    if filter:
        results = []
        for state in STATES:
            if filter.lower() == state['name'][:len(filter)].lower():
                results.append(state)
    else:
        results = STATES
    return handle_response(results)

# Testing 
@app.route('/ufo')
def datasetUFO():
    with open("/Users/Delly/Desktop/NewEnv/5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/fixed_ufos.geojson") as f:
        data = f.read()
        return json.loads(data)

@app.route('/state_bbox', methods=["GET"])
def state_bbox():
    """
    Description: return a bounding box for a us state
    Params: None
    Example: http://localhost:8080/state_bbox?state=<statename>
    """
    
    state = request.args.get('state',None)
    print(f'STATE {state}')

    if not state:
        results = STATES_BBOXS
        return handle_response(results)

    state = state.lower()

    results = []
   
    print(results)

    for row in STATES_BBOXS:

        if row ['name'].lower() == state or row['abbr'].lower() == state:
            row['xmax'] = float(row['xmax'])
            row['xmin'] = float(row['xmin'])
            row['ymin'] = float(row['ymin'])
            row['ymax'] = float(row['ymax'])
            results = row
    return handle_response(results)


@app.route('/image/<string:filename>')
def get_image(filename):
    """ Description: Return an image for display
        Params: 
            name (string)  : name of image to return
        Example: http://localhost:8080/image/battle_ship_1.png
    """

    image_dir= "./images/"

    image_path = os.path.join(image_dir,filename)

    if not os.path.isfile(image_path):
        return handle_response([],{'filename':filename,'imagepath':image_path},"Error: file did not exist!")

    return send_file(image_path, mimetype='image/png')

@app.route('/geo/direction/')
def get_direction():
    """ Description: Return the direction between two lat/lon points.
        Params: 
            lng1 (float) : point 1 lng
            lat1 (float) : point 1 lat
            lng2 (float) : point 1 lat
            lat2 (float) : point 1 lat
        Example: http://localhost:8080/geo/direction/?lng1=-98.4035194716&lat1=33.934640760&lng2=-98.245591004&lat2=34.0132220288
    """
    lng1 = request.args.get('lng1',None)
    lat1 = request.args.get('lat1',None)
    lng2 = request.args.get('lng2',None)
    lat2 = request.args.get('lat2',None)

    b = bearing((float(lng1),float(lat1)), (float(lng2),float(lat2)))

    return handle_response([{"bearing":b}],{'lat1':lat1,'lng1':lng1,'lat2':lat2,'lng2':lng2})


"""
-----------------------------PROJECT ------------------------------------
"""


# ██████╗ ██████╗ ██╗██╗   ██╗ █████╗ ████████╗███████╗    ███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
# ██╔══██╗██╔══██╗██║██║   ██║██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
# ██████╔╝██████╔╝██║██║   ██║███████║   ██║   █████╗      █████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
# ██╔═══╝ ██╔══██╗██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║
# ██║     ██║  ██║██║ ╚████╔╝ ██║  ██║   ██║   ███████╗    ██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                           

def handle_response(data,params=None,error=None):
    """ handle_response
    """
    success = True
    if data:
        if not isinstance(data,list):
            data = data
        count = len(data)
    else:
        count = 0
        error = "Data variable is empty!"
    
    result = {"success":success,"count":count, "FeatureCollection": data,"id": params}

    if error:
        success = False
        result['error'] = error
    

    return jsonify(result)

def formatHelp(route):
    """
    Gets the dock strings  for each methods and displays them
    """
    help = globals().get(str(route)).__doc__
    if help != None:
        help = help.split("\n")
        clean_help = []
        for i in range(len(help)):
            help[i] = help[i].rstrip()
            if len(help[i]) > 0:
                clean_help.append(help[i])
    else:
        clean_help = "No Help Provided."
    return clean_help

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# def dataSets(dataset):
#     global layers_mapdata
#     searchData =[]
#     for i in dataset:
#         if dataset[dataset]:
#             if not layers_mapdata[i]["loaded"]:
#                 loadedInfo = getTree(layers_mapdata[dataset]["path"])
#                 layers_mapdata[dataset]["loaded"] = True
#                 layers_mapdata[dataset]["kdtree"] = loadedInfo[0]
#                 layers_mapdata[dataset]["mapId"] = loadedInfo[1]
#             else:
#                 loadedInfo = (layers_mapdata[dataset]["kdtree"], layers_mapdata[dataset]["mapId"])
#             searchData.append(loadedInfo)
#     return searchData
if __name__ == '__main__':
      tree, coords = getTree()
      app.run(host='localhost', port=7878,debug=True)