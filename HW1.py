# HW1: use python to analysis the data from Central Weather Branue

#=======================================
# Import module
# csv -- fileIO operation
#=======================================
import csv

#=======================================
# Read cwb weather data
#=======================================
cwb_filename = '107061226.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)

#=======================================
# analysis the data and print out the data I need
#=======================================
location = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
ans = [] 

for i in range (len(location)):
    target_data = list(filter(lambda item: item['station_id'] == location[i], data))
    humidity = 0
    for j in range (len(target_data)):
        if (target_data[j]['HUMD'] != -99 and target_data[j]['HUMD'] != -999):
            humidity += float(target_data[j]['HUMD'])
    if (humidity == 0):
        ans.append([location[i], 'NONE'])
    else :
        ans.append([location[i], humidity])

print(ans)
