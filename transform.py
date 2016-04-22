import json
import csv 
import urllib

chmu = urllib.urlopen("http://portal.chmi.cz/files/portal/docs/uoco/web_generator/aqindex_cze.json").read()
data = json.loads(chmu)

import codecs
fd = codecs.open("document.csv", "w", "utf-8")
#Add header
pollution = 'Name,Lon,Lat,Color,Alarm,DetailAlarm,Code,Int,Val'
fd.write(pollution + "\n")
for region in data['States'][0]['Regions']:
    for station in region['Stations']:
        if 'Components' in station.keys():
            pollutionline = []
            for component in station['Components']:                
                Name = station['Name']
                Lon = str(station['Lon'])
                Lat = str(station['Lat'])
                Alarm = station['Ix']
                if Alarm == 1:
                    Alarmcolor = 'C7EAFB'
                elif Alarm == 2:
                    Alarmcolor = '9BD3AE'
                elif Alarm == 3:
                    Alarmcolor = 'FFF200'
                elif Alarm == 4:
                    Alarmcolor = 'FAA61A'
                elif Alarm == 5:
                    Alarmcolor = 'FFFFFF'
                elif Alarm == 0:
                    Alarmcolor = '000000'
                DetailAlarm = str(component['Ix'])
                Code = str(component['Code'])
                Int = str(component['Int'])
                if 'Val' in component.keys():
                    Val = str(component['Val'])              
                pollution = Name + ',' + Lon + ',' + Lat + ',' + Alarmcolor + ',' + str(Alarm)+ ',' + DetailAlarm + ',' + Code + ' ' + Int + ',' + Val
                fd.write(pollution + "\n")

fd.close()
                    
                
