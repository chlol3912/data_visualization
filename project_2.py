import csv
import json
from matplotlib import pyplot as plt
import numpy as np

#SOCCER PLOT
epl = open('project_data/EPL_20_21.csv')
reader = csv.reader(epl)
epl_data = list(reader)
positions={}
for player in epl_data:
    if player[3] not in positions:
        positions.update({player[3]: 1})
    else:
        positions[player[3]]+=1
pos_x=positions.keys()
indexes=np.arange(len(pos_x))
pos_y=positions.values()
width=0.5
plt.figure('# of Players at Position in the English Premier League')
plt.bar(pos_x,pos_y,color='#444444', width=width)
plt.title('# of Players at Position in the English Premier League\nDF=Defender, MF=Midfielder, FW=Forward')
plt.xlabel('Position')
plt.ylabel('# of Players')

#WEATHER PLOT
weather = open('project_data/1880-2016.json')
reader = weather.read()
weather_json=json.loads(reader)
weather_data=weather_json.get('data')
weather_x = range(17)
weather_y_1900 = []
weather_y_2000 = []
for year in weather_data:
    if (int(year)>=1900 and int(year)<=1916):
        weather_y_1900.append(weather_data[year])
    elif (int(year)>=2000 and int(year)<=2016):
        weather_y_2000.append(weather_data[year])
plt.figure('Change in Weather Anomalies Over a Century')
plt.plot(weather_x, weather_y_1900, 'b--', label='Weather Anomaly 1900-1916')
plt.plot(weather_x, weather_y_2000, 'k', label='Weather Anomaly 2000-2016')
plt.title('Change in Weather Anomalies Over a Century')
plt.xlabel('Years since 1900/2000')
plt.ylabel('Deviation from Long-term Average (°C)')
plt.legend()
plt.show()