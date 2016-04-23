import json
import csv 
import urllib
#Gets data from czech hydrometherologic bureau
chmu = urllib.urlopen("http://portal.chmi.cz/files/portal/docs/uoco/web_generator/aqindex_cze.json").read()
data = json.loads(chmu)
import codecs
fd = codecs.open("document.csv", "w", "utf-8")
#Add header
pollution = 'States__Regions__Stations__Name,States__Regions__Stations__Lon,States__Regions__Stations__Lat,Color,DetailAlarm,type,Val'
fd.write(pollution + "\n")
for region in data['States'][0]['Regions']:
    for station in region['Stations']:
        if 'Components' in station.keys():
            
            for component in station['Components']:                
                Name = station['Name'].replace(",", "")
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
                    Alarmcolor = 'ED1C24'
                elif Alarm == 0:
                    Alarmcolor = 'FFFFFF'
                DetailAlarm = component['Ix']
                if DetailAlarm == 1:
                    DAlarmcolor = 'C7EAFB'
                elif DetailAlarm == 2:
                    DAlarmcolor = '9BD3AE'
                elif DetailAlarm == 3:
                    DAlarmcolor = 'FFF200'
                elif DetailAlarm == 4:
                    DAlarmcolor = 'FAA61A'
                elif DetailAlarm == 5:
                    DAlarmcolor = 'ED1C24'
                elif DetailAlarm == -2:
                    DAlarmcolor = 'C7EAFB'
                elif DetailAlarm < 1:
                    DAlarmcolor = 'FFFFFF'
                Code = str(component['Code'])
                Int = str(component['Int'])
                if 'Val' in component.keys():
                    Val = str(component['Val'])
                else:
                    Val = ''
                pollution = Name + ',' + Lon + ',' + Lat + ',' + DAlarmcolor + ',' + str(DetailAlarm) + ',' + Code + ' ' + Int + ',' + Val
                fd.write(pollution + "\n")
            pollution = Name + ',' + Lon + ',' + Lat + ',' + Alarmcolor + ',' + str(Alarm) + ',' + 'General' + ','
            fd.write(pollution + "\n")

fd.close()
# gets a list of user pollution stations and adds them to the text

# gets a list of users that requested info and notifies them if needed.

# push new csv file to github
                    
                
