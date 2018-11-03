import re
import config

with open(config.DATA_IN_PATH, "r") as infile, open(config.DATA_OUT_PATH, "w") as outfile:
	for line in infile:
		for measure in config.MEASURES:
			if measure in line: 
				outputLine = re.sub(r'(")([a-zA-Z1-3_-]+)(":{"timestamp":")(\d+)','', line)
				if measure == "temp":
					outputLine = outputLine.replace('","pressure":"','')
					outputLine = outputLine.replace('","temp":"',',')
					outputLine = outputLine.replace('","light":"',',')
				else:
					outputLine = outputLine.replace('","' + measure + '":{"x":"','')
					outputLine = outputLine.replace('","y":"',',')
					outputLine = outputLine.replace('","z":"',',')
				for obj in config.OBJECTS:
					if obj[0] in line:
						outputLine = re.sub(r'("(})+,),*',',' + `obj[1]`, outputLine)
						outfile.write(outputLine)
						continue
				
		  #       if "window_outdoor" in line: 
				#   outputLine = re.sub(r'("}},),*',',1', outputLine)
				# elif "door_indoor" in line: 
				#   outputLine = re.sub(r'("}},),*',',2', outputLine)
				# elif "chair-1" in line: 
				#   outputLine = re.sub(r'("}},),*',',3', outputLine)
				# else:
				#   continue
				