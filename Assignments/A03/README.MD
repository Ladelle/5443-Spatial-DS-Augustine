## A03 - FLASK SPATIAL API
### LADELLE AUGUSTINE
### Description:

This assignment was to create a flask backend and a frontend Javascript application. The assignment uses a KDtree to find the nearest neighbors and display the five closest points to the location that the mouse clicked on the map. I created my own map, because my data point were constellations and Zodiac signs.


### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | flaskapp.py     | Main driver of my project that launches Flask.     |
|   2   | index.html      | HTML that has the map         |
|   3   | templates folder | Has the index.html file in it |
|   4   | constPoint.geojson | Data < capitalize the 'P' in point>    |
|   5   | const   | -------------                  |

### Dependencies < WINDOWS >
 1. Geopandas (LINK: https://geopandas.org/install.html )
    - branca
    - gdal
    - fiona
    - pyproj
 2. Flask
 3. Flask-CORS
 4. Scipy 
 5. Folium
 6. KDTree 
 
### Instructions

- Create a Virtual Environment if you dont have one. I used Anaconda. 
- Make sure all your dependencies are upto date. 
- Download the file save in a folder Assignments and A03. 
   `Assignments/A03/constPoint.geojson`
- In the Terminal in that folder run the flask app. 
- copy link `http://localhost:8080/` then type in `/click/`

