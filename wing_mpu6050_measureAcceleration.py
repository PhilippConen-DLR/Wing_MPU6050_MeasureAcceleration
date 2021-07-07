import math
import time
from datetime import datetime
from time import sleep		 
import board
import adafruit_mpu6050
import adafruit_tca9548a

print("Welcome!")

currentDay = datetime.today()
currentTime = datetime.now()
fileDate = currentDay.strftime("%m%d")#("%y%m%d")
fileTime = currentTime.strftime("%H%M")#("%H%M%S")
file = open("Experiment_Gyro_Acc"+str(fileDate)+"_"+str(fileTime)+".csv", "a")
print("Entering: ", "Experiment_"+fileDate+"_"+fileTime)
file.write("T,AX1,AY1,AZ1,AX2,AY2,AZ2,AX3,AY3,AZ3,AX4,AY4,AZ4,AX5,AY5,AZ5,AX6,AY6,AZ6,AX7,AY7,AZ7,AX8,AY8,AZ8\n")

imus = 8

i2c = board.I2C()  # uses board.SCL and board.SDA
tca = adafruit_tca9548a.TCA9548A(i2c)
i = 0

print("Initializing ...")

if imus >= 1:
    print("1/" + str(imus) + " IMUS ...")
    mpu0 = adafruit_mpu6050.MPU6050(tca[0])
if imus >= 2:
    print("2/" + str(imus) + " IMUS ...")
    mpu1 = adafruit_mpu6050.MPU6050(tca[1])
if imus >= 3:
    print("3/" + str(imus) + " IMUS ...")
    mpu2 = adafruit_mpu6050.MPU6050(tca[2])
if imus >= 4:
    print("4/" + str(imus) + " IMUS ...")
    mpu3 = adafruit_mpu6050.MPU6050(tca[3])
if imus >= 5:
    print("5/" + str(imus) + " IMUS ...")
    mpu4 = adafruit_mpu6050.MPU6050(tca[4])
if imus >= 6:
    print("6/" + str(imus) + " IMUS ...")
    mpu5 = adafruit_mpu6050.MPU6050(tca[5])
if imus >= 7:
    print("7/" + str(imus) + " IMUS ...")
    mpu6 = adafruit_mpu6050.MPU6050(tca[6])
if imus >= 8:
    print("8/" + str(imus) + " IMUS ...")
    mpu7 = adafruit_mpu6050.MPU6050(tca[7])

print("Initializing done!\n")

print("Starting ..")
start = datetime.now()

print("T,AX1,AY1,AZ1,AX2,AY2,AZ2,AX3,AY3,AZ3,AX4,AY4,AZ4,AX5,AY5,AZ5,AX6,AY6,AZ6,AX7,AY7,AZ7,AX8,AY8,AZ8\n")

while True:
    end = datetime.now()
    delta = end-start
    dt = (delta.seconds+delta.microseconds/1000000)

    file.write("%.2f"%dt 
    + ",%.2f,%.2f,%.2f"%(mpu0.acceleration) 
    +",%.2f,%.2f,%.2f"%(mpu1.acceleration) 
    +",%.2f,%.2f,%.2f"%(mpu2.acceleration) 
    +",%.2f,%.2f,%.2f"%(mpu3.acceleration)
    +",%.2f,%.2f,%.2f"%(mpu4.acceleration)
    +",%.2f,%.2f,%.2f"%(mpu5.acceleration)
    +",%.2f,%.2f,%.2f"%(mpu6.acceleration)
    +",%.2f,%.2f,%.2f"%(mpu7.acceleration)
    + "\n")    
    #time.sleep(1)
