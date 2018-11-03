from array import *

#input file and ouput file
DATA_IN_PATH = "data/data.json"
DATA_OUT_PATH = "data/data_out.csv"

#values to keep in the outfile
OBJECTS = [ ["window_outdoor", 1], ["chair-1", 2]] #object mapped with label to be used on the output file
MEASURES = ["temp"] #accel, gyro, magnto, temp(which gets the tuple pressure, temp, light)