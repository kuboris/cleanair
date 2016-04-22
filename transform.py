import json
import csv 

f = open('polution.json')
data = json.load(f)
f.close()
data2 = json.dumps(data)
data3 = json.loads(data2)
import codecs
fd = codecs.open("document.csv", "a", "utf-8")

for region in data3['States'][0]['Regions']:
    for station in region['Stations']:
        if 'Components' in station.keys():
            for component in station['Components']:
                Name = station['Name']
                #print station
                Lon = station['Lon']
                Lat = station['Lat']
                Alarm = station['Ix']
                DetailAlarm = component['Ix']
                Code = component['Code']
                Int = component['Int']
                if 'Val' in component.keys():
                    Val = component['Val']
                fd.write(Name)

fd.close()
                    
                
