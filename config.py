from array import *

#input file and ouput file
DATA_IN_PATH = "raw_dataset/andreaDataCleaned.json"
DATA_OUT_PATH = "data/data_val.csv"

#values to keep in the outfile
OBJECTS = [["door_apt_in", 1], ["door_room_in", 1]] #object mapped with label to be used on the output file
MEASURES = ["accel"] #accel, gyro, magnto, temp(which gets the tuple pressure, temp, light)