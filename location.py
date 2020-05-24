import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import os
import time
import math
import datetime

SETTINGS_FILE = "RTIMULib"
print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
  print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)
pressure = RTIMU.RTPressure(s)

print("IMU Name: " + imu.IMUName())
print("Pressure Name: " + pressure.pressureName())

if (not imu.IMUInit()):
    print("IMU Init Failed");
    sys.exit(1)
else:
    print("IMU Init Succeeded");

if (not pressure.pressureInit()):
    print("Pressure sensor Init Failed");
else:
    print("Pressure sensor Init Succeeded");

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)

raw_input("Press Enter when ready\n>")

while True:
  if imu.IMURead():
    (x, y, z) = imu.getFusionData()
    data = imu.getIMUData()
    (data["pressureValid"], data["pressure"], data["temperatureValid"], data["temperature"]) = pressure.pressureRead()
    fusionPose = data["fusionPose"]
    os.system('clear')

    print "timestamp: " + str(data["timestamp"])

    print "accelValid: " + str(data["accelValid"])
    print "accel: " + str(data["accel"])
    print "accel x: " + str(data["accel"][0])
    print "accel y: " + str(data["accel"][1])

    print "compassValid: " + str(data["compassValid"])
    print "compass: " + str(data["compass"])

    print "fusionPoseValid: " + str(data["fusionPoseValid"])
    print "fusionPose: " + str(data["fusionPose"])
    print("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]), math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))
    print("r: %i p: %i y: %i" % (int(math.degrees(fusionPose[0])), int(math.degrees(fusionPose[1])), int(math.degrees(fusionPose[2]))))
    print("x: %f y: %f z: %f" % (x,y,z))

    print "fusionQPoseValid: " + str(data["fusionQPoseValid"])
    print "fusionQPose: " + str(data["fusionQPose"])

    print "gyroValid: " + str(data["gyroValid"])
    print "gyro: " + str(data["gyro"])

    print "pressureValid: " + str(data["pressureValid"])
    print("Pressure: %f" % (data["pressure"]))

    print "temperatureValid: " + str(data["temperatureValid"])
    print("Temperature: %f" % (data["temperature"]))

    time.sleep(0.2)