import os
import sys
import json
import csv
import flask
from flask import Flask,  url_for
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask import send_file
import glob

from misc_functions import haversine, bearing

base_path = '/Users/Delly/Desktop/NewEnv/5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/'

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
    return None
"""
---------------------------------------------------------------------------------------------------------------
---------------------------------------DATA BACKEND-----------------------------------------------------------
---------------------------------------------------------------------------------------------------------------

"""

"""
BIG GLOBALS --> KIND OF ACTING LIKE DATABASE
"""

"""
HELPER FUNCTIONS 

"""
STATES = load_data("/Users/Delly/Desktop/NewEnv/5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/states.json")

STATES_BBOXS = load_data("/Users/Delly/Desktop/NewEnv/5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/us_states_bbox.csv")


# with open("/Users/Delly/Desktop/NewEnv/5443-Spatial-DS-Augustine/Assignments/A04/assets/api/data/states.json") as f:
#     data = f.read()
# STATES = json.loads(data)  

# data = open(os.path.join(base_path,"color.names.json"),'r').read()
# COLORS = json.loads(data)

# data = open(os.path.join(base_path,'states.json'),'r').read()
# STATES = json.loads(data)

crash_files = glob.glob(os.path.join(base_path,"plane_crashes/crash_data/*.json"))


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

@app.route('/state_bbox', methods=["GET"])
def state_bbox():
    """
    Description: return a bounding box for a us state
    Params: None
    Example: http://localhost:8080/state_bbox?<statename>
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

# @app.route('/color/hex/<string:name>', methods=["GET"])
# def rgb(name):
#     """ Description: return hex value for a color
#         Params: 
#             name (string) : color name
#         Example: http://localhost:8080/color/hex/blue
#     """
#     data = []

#     for color in COLORS:
#         if color["name"] == name:
#             data = color["hex"]

#     return handle_response(data)



# @app.route('/crashes', methods=["GET"])
# def crashes():
#     """ Description: return menu for front end
#         Params: 
#             None
#         Example: http://localhost:8080/states
#     """
#     state = request.args.get('state',None)
    
#     if state:
#         results = []
#         for state in STATES:
#             if filter.lower() == state['name'][:len(filter)].lower():
#                 results.append(state)
#     else:
#         results = STATES

#     return handle_response(results)

"""
-----------------------------PRIVATE --------------------------------------------------
"""

def handle_response(data,params=None,error=None):
    """ handle_response
    """
    success = True
    if data:
        if not isinstance(data,list):
            data = [data]
        count = len(data)
    else:
        count = 0
        error = "Data variable is empty!"

    
    result = {"success":success,"count":count,"results":data,"params":params}

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


        
if __name__ == '__main__':
      app.run(host='localhost', port=8080,debug=True)