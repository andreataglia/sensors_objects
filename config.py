from array import *

#input file and ouput file
DATA_IN_PATH = "raw_dataset/cleanedAccelGyroFused2.json"
DATA_OUT_PATH = "prova.csv"

#values to keep in the outfile - objects mapped with label to be used on the output file
OBJECTS = [["door_apt_in", 0]] 
# OBJECTS = [["door_outdoor", 0], ["door_apt_in", 0], ["door_toilet_out", 0], 
# 			["chair-1", 1], ["chair", 1],
# 			["window_in", 2], ["window_outdoor", 2],
# 			["desk", 3],
# 			["person", 4]]
MEASURES = ["accelgyro"] #accel, gyro, magnto, temp(which gets the tuple pressure, temp, light)