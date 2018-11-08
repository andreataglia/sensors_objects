import re
import config

with open(config.DATA_IN_PATH, "r") as infile, open(config.DATA_OUT_PATH, "w") as outfile:
	if len(config.OBJECTS) > 1:
		for line in infile:
			for measure in config.MEASURES:
				if measure in line: 
					for obj in config.OBJECTS:
						if obj[0] in line:
							outputLine = re.sub(r'(")([a-zA-Z1-3_-]+)(":{"timestamp":")(\d+)','', line)
							if measure == "temp":
								outputLine = outputLine.replace('","pressure":"','')
								outputLine = outputLine.replace('","temp":"',',')
								outputLine = outputLine.replace('","light":"',',')
							else:
								outputLine = outputLine.replace('","' + measure + '":{"x":"','')
								outputLine = outputLine.replace('","y":"',',')
								outputLine = outputLine.replace('","z":"',',')
								if measure == "accelgyro":
									outputLine = outputLine.replace('","x":"',',')
							outputLine = re.sub(r'("(})+,),*',',' + `obj[1]`, outputLine)
							outfile.write(outputLine)
							continue
	else:
		for line in infile:
			if config.OBJECTS[0][0] in line:
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
							if measure == "accelgyro":
								outputLine = outputLine.replace('","x":"',',')
						
						outputLine = re.sub(r'("(})+,),*',',' + `config.OBJECTS[0][1]`, outputLine)
						outfile.write(outputLine)
						continue			