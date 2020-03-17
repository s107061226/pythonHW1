# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================
# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061226.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================
# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
target_data_0 = list(filter(lambda item: item['station_id'] == 'C0A880', data))
target_data_1 = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
target_data_2 = list(filter(lambda item: item['station_id'] == 'C0G640', data))
target_data_3 = list(filter(lambda item: item['station_id'] == 'C0R190', data))
target_data_4 = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# Retrive ten data points from the beginning.
#target_data = data[:10]
#=======================================
# Part. 4
#=======================================
# Print result
humidity = 0
ans = []
for i in range(len(target_data_0)):
    if (float(target_data_0[i]['HUMD']) != -99 and float(target_data_0[i]['HUMD']) != -999):
        humidity += float(target_data_0[i]['HUMD'])
ans.append(['C0A880', humidity])

humidity = 0
for i in range(len(target_data_1)):
    if (float(target_data_1[i]['HUMD']) != -99 and float(target_data_1[i]['HUMD']) != -999):
        humidity += float(target_data_1[i]['HUMD'])
ans.append(['C0F9A0', humidity])

humidity = 0
for i in range(len(target_data_2)):
    if (float(target_data_2[i]['HUMD']) != -99 and float(target_data_2[i]['HUMD']) != -999):
        humidity += float(target_data_2[i]['HUMD'])
ans.append(['C0G640', humidity])

humidity = 0
for i in range(len(target_data_3)):
    if (float(target_data_3[i]['HUMD']) != -99 and float(target_data_3[i]['HUMD']) != -999):
        humidity += float(target_data_3[i]['HUMD'])
ans.append(['C0R190', humidity])

humidity = 0
for i in range(len(target_data_4)):
    if (float(target_data_4[i]['HUMD']) != -99 and float(target_data_4[i]['HUMD']) != -999):
        humidity += float(target_data_4[i]['HUMD'])
ans.append(['C0X260', humidity])

print(ans)
#========================================