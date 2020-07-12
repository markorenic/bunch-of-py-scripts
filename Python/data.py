# /*
# Script write by Moz for YouTube changel logMaker360 for this video: https://www.youtube.com/watch?v=PNbsyHocM2U

# Script to read temperature data from the DHT11:
# # Importeer Adafruit DHT bibliotheek.
import Adafruit_DHT
import time
als = True
while als: 
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4) #on gpio pin 4 or pin 7
    if humidity is not None and temperature is not None:
      humidity = round(humidity, 2)
      temperature = round(temperature, 2)
      print ('Temperature = {0:0.1f}*C  Humidity = {1:0.1f}%'.format(temperature, humidity))
    else:
      print 'can not connect to the sensor!'
    time.sleep(60) # read data every minute
    
Update from the Script above with modification of writing the data to a CSV.file:
# Importeer Adafruit DHT bibliotheek.
#time.strftime("%I:%M:%S")
import Adafruit_DHT
import time
import csv
import sys
csvfile = "temp.csv"
als = True
while als: 
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4) # gpio pin 4 or pin number 7
    if humidity is not None and temperature is not None:
      humidity = round(humidity, 2)
      temperature = round(temperature, 2)
      print 'Temperature = {0:0.1f}*C  Humidity = {1:0.1f}%'.format(temperature, humidity)
    else:
      print 'can not connect to the sensor!'
    timeC = time.strftime("%I")+':' +time.strftime("%M")+':'+time.strftime("%S")
    data = [temperature, timeC]

    with open(csvfile, "a")as output:
        writer = csv.writer(output, delimiter=",", lineterminator = '\n')
        writer.writerow(data)
    time.sleep(6) # update script every 60 seconds
    
Script to read data from the CSV and display it in a graph:

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.animation as animation
from datetime import datetime

fig = plt.figure()
rect = fig.patch
rect.set_facecolor('#0079E7')
def animate(i):
    ftemp = 'temp.csv'
    fh = open(ftemp)
    temp = list()
    timeC = list()
    for line in fh:
        pieces = line.split(',')
        degree = pieces[0]
        timeB=  pieces[1]
        timeA= timeB[:8]
            #print timeA
        time_string = datetime.strptime(timeA,'%H:%M:%S')
        #print time_string
        try:
            temp.append(float(degree))
            timeC.append(time_string)
        except:
            print "dont know"
        

        ax1 = fig.add_subplot(1,1,1,axisbg='white')
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        ax1.clear()
        ax1.plot(timeC,temp, 'c', linewidth = 3.3)
        plt.title('Temperature')
        plt.xlabel('Time')
        
ani = animation.FuncAnimation(fig, animate, interval = 6000)   
plt.show()


*/

void setup() {
    
}

void loop() {
    
}
