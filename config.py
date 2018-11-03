from array import *

#input file and ouput file
DATA_IN_PATH = "raw_dataset/first10Cleaned.json"
DATA_OUT_PATH = "data/data_out_full.csv"

#values to keep in the outfile
OBJECTS = [["door_outdoor", 1],["door_indoor", 1],["window_indoor", 2],["window_outdoor", 2]] #object mapped with label to be used on the output file
MEASURES = ["accel"] #accel, gyro, magnto, temp(which gets the tuple pressure, temp, light)