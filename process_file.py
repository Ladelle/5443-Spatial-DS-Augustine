"""
PROCESSES THE DATA TO CREATE EACH ZODIAC SIGN (12) AND THE FINAL ZODIAC.JSON HAS ALL 
THE ZODIAC COORDINATES ON THE MAP.
"""

# Import JSON module
import requests
import json
import geojson


#-------------------------------------------------------------------------------------------------

    
    # y = {"type":"Feature",
    #         "id": i,
    #         "properties":{
    #         "name": features,
    #         "rank": rank
    #         },
    #         "geometry":{
    #             "type": geotype2,
    #             "coordinates": features2
    #             }
    

#--------------------------------------------------------------------------------------------
def consta():
   
    #zodnam = ['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpius','Sagittarius','Capricornus','Aquarius','Pisces']
    with open('constellations.json', encoding="utf8") as f:         # constellation Name & Rank
        gn = geojson.load(f)
    with open('constellations.lines.json',encoding="utf8") as f:    # Gets the Lines that form the constellations
        gl = geojson.load(f)

    for i in range(1,89):
        features = gn['features'][i]['properties']['name'] 
        rank = gn['features'][i]['properties']['rank']
        # featuresC2 = gn['features'][i]['geometry']['coordinates']  # just two points --> for kd tree @7:53pm -- for ZCor.json
        features2 = gl['features'][i]['geometry']['coordinates']  #---> this is for Zodiac.json file
        geotype2 = gl['features'][i]['geometry']['type']
        
        #  consd = {   
            # "id": i,
            # "name": features,
            # "rank": rank,
            # "Type": geotype2,
            # "coordinates": features2
        #     }
        
        # json_object = json.dumps(dic, indent = 4)
        # with open("sample.json","w") as outfile:
        #     outfile.write(json_object)
        

            # "id": i,
            # "name": features,
            # "rank": rank,
            # "Type": geotype2,
            # "coordinates": features2

      #---------------------------------------- these are data sets for Zodiac.json --------------------------------------------------------- 
        if i == 6:
            dic = { "id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
            json_object = json.dumps(dic, indent = 4) 
            with open("Aries.json", "w") as outfile: 
                outfile.write(json_object) 
        if i == 3:
           dic2 = { "id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
           json_object = json.dumps(dic2, indent = 4) 
           with open("Aquarius.json", "w") as outfile: 
                outfile.write(json_object)  
        if i == 15:
            dic3 = {"id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
            json_object = json.dumps(dic3, indent = 4) 
            with open("Capricorn.json", "w") as outfile: 
                outfile.write(json_object) 
        if i == 11:
            dic4 = {"id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
            json_object = json.dumps(dic4, indent = 4) 
            with open("Cancer.json", "w") as outfile: 
                outfile.write(json_object)  
        if i == 37:
            dic5 = {"id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
            json_object = json.dumps(dic5, indent = 4) 
            with open("Gemini.json", "w") as outfile: 
                outfile.write(json_object) 
        if i == 45:
            dic6 = {"id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
            json_object = json.dumps(dic6, indent = 4) 
            with open("Leo.json", "w") as outfile: 
                outfile.write(json_object) 
        if i == 48:
            dic7 = {"id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
            json_object = json.dumps(dic7, indent = 4) 
            with open("Libra.json", "w") as outfile: 
                outfile.write(json_object)  
        if i == 65:
            dic8 = {"id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
            json_object = json.dumps(dic8, indent = 4) 
            with open("Pisces.json", "w") as outfile: 
                outfile.write(json_object)  
        if i == 71:
            dic9 = {"id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
            json_object = json.dumps(dic9, indent = 4) 
            with open("Sagittarius.json", "w") as outfile: 
                outfile.write(json_object)  
        if i == 72:
            dic10 = {"id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
            json_object = json.dumps(dic10, indent = 4) 
            with open("Scorpio.json", "w") as outfile: 
                outfile.write(json_object)  
        if i == 78:
            dic11 = {"id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
            json_object = json.dumps(dic11, indent = 4) 
            with open("Taurus.json", "w") as outfile: 
                outfile.write(json_object)   
        if i ==  86:
            dic12 = {"id": i,
            "name": features,
            "rank": rank,
            "Type": geotype2,
            "coordinates": features2}
            json_object = json.dumps(dic12, indent = 4) 
            with open("Virgo.json", "w") as outfile: 
                outfile.write(json_object)  

    print(dic)
    print(dic2)
          # ----------------------------------------these are data sets for ZCors.json ---------------------------------------------------------

        # if i == 6:
        #     dic = { "id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #     json_object = json.dumps(dic, indent = 4) 
        #     with open("AriesCor.json", "w") as outfile: 
        #         outfile.write(json_object) 
        # if i == 3:
        #    dic2 = { "id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #    json_object = json.dumps(dic2, indent = 4) 
        #    with open("AquariusCor.json", "w") as outfile: 
        #         outfile.write(json_object)  
        # if i == 15:
        #     dic3 = {"id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #     json_object = json.dumps(dic3, indent = 4) 
        #     with open("CapricornCor.json", "w") as outfile: 
        #         outfile.write(json_object) 
        # if i == 11:
        #     dic4 = {"id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #     json_object = json.dumps(dic4, indent = 4) 
        #     with open("CancerCor.json", "w") as outfile: 
        #         outfile.write(json_object)  
        # if i == 37:
        #     dic5 = {"id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #     json_object = json.dumps(dic5, indent = 4) 
        #     with open("GeminiCor.json", "w") as outfile: 
        #         outfile.write(json_object) 
        # if i == 45:
        #     dic6 = {"id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #     json_object = json.dumps(dic6, indent = 4) 
        #     with open("LeoCor.json", "w") as outfile: 
        #         outfile.write(json_object) 
        # if i == 48:
        #     dic7 = {"id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #     json_object = json.dumps(dic7, indent = 4) 
        #     with open("LibraCor.json", "w") as outfile: 
        #         outfile.write(json_object)  
        # if i == 65:
        #     dic8 = {"id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #     json_object = json.dumps(dic8, indent = 4) 
        #     with open("PiscesCor.json", "w") as outfile: 
        #         outfile.write(json_object)  
        # if i == 71:
        #     dic9 = {"id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #     json_object = json.dumps(dic9, indent = 4) 
        #     with open("SagittariusCor.json", "w") as outfile: 
        #         outfile.write(json_object)  
        # if i == 72:
        #     dic10 = {"id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #     json_object = json.dumps(dic10, indent = 4) 
        #     with open("ScorpioCor.json", "w") as outfile: 
        #         outfile.write(json_object)  
        # if i == 78:
        #     dic11 = {"id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #     json_object = json.dumps(dic11, indent = 4) 
        #     with open("TaurusCor.json", "w") as outfile: 
        #         outfile.write(json_object)   
        # if i ==  86:
        #     dic12 = {"id": i,
        #     "name": features,
        #     "rank": rank,
        #     "Type": geotype2,
        #     "coordinates": featuresC2}
        #     json_object = json.dumps(dic12, indent = 4) 
        #     with open("VirgoCors.json", "w") as outfile: 
        #         outfile.write(json_object)  
    # print(dic)
    # print(dic2)
   
       
       
        




if __name__ == '__main__':
    consta()
 