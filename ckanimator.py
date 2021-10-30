#!/usr/bin/env python3

from ckconfig import *

# Number of manually entered frames:
BASE_FRAME_COUNT = len(COLOR_LIST)

# Bloody6 RGB animation editor supports up to 99 frames only (crashes otherwise)!
TOTAL_FRAME_COUNT = BASE_FRAME_COUNT + BASE_FRAME_COUNT * TRANSITION_FRAME_COUNT

#########

def hexToRgb(hexString):
	return tuple(int(hexString[i:i+2], 16) for i in (0, 2 ,4))

def rgbToHex(rgbTuple):
	return "{:02X}{:02X}{:02X}".format(*map(int, rgbTuple))

def frame(frameNum, colors, dTime):
	sList = []
	sList.append("\t<Frame{}>\n\t\t<ColorPicture>".format(frameNum))
	sList.append(",".join(colors))
	sList.append("</ColorPicture>\n\t\t<DisplayTime>{0:.3f}</DisplayTime>\n\t</Frame{1}>\n".format(dTime, frameNum))
	return "".join(sList)

def rgbStep(rgb1, rgb2):
	return tuple([(x[1] - x[0]) / (TRANSITION_FRAME_COUNT + 1) for x in zip(rgb1, rgb2)])

def rgbSum(rgb1, rgb2):
	return [sum(z) for z in zip(rgb1, rgb2)]

def rgbListSum(rgbList1, rgbList2):
	return [rgbSum(*z) for z in zip(rgbList1, rgbList2)]

def transition(colors1, colors2, transFrameNum):
	current = list(map(hexToRgb, colors1))
	target = map(hexToRgb, colors2)
	stepList = []
	stepDiff = [rgbStep(*z) for z in zip(current, target)]
	
	for i in range(0, TRANSITION_FRAME_COUNT):
		current = rgbListSum(current, stepDiff)
		colors = tuple([rgbToHex(c) for c in current])
		stepList.append(frame(transFrameNum + i, colors, TRANSITION_FRAME_TIME))

	return stepList

def generateContent():
	sList = []
	sList.append("<Root>\n\t<Description>")
	sList.append(DESCRIPTION)
	sList.append("</Description>\n\t<Time>{}</Time>\n\t<BackgroundColor>".format(IDLE_TIME))
	sList.append(IDLE_COLOR)
	sList.append("</BackgroundColor>\n\t<FrameCount>{}</FrameCount>\n".format(TOTAL_FRAME_COUNT))
	colorList = list(map(lambda s: tuple(s.split(",")), COLOR_LIST))

	for i in range(0, BASE_FRAME_COUNT):
		frameNum = i * TRANSITION_FRAME_COUNT + i + 1
		sList.append(frame(frameNum, colorList[i], BASE_FRAME_TIME))
		sList.extend(transition(colorList[i], colorList[(i + 1) % BASE_FRAME_COUNT], frameNum + 1))

	sList.append("</Root>\n")
	return "".join(sList)

def main():
	if(IDLE_TIME < 0 or IDLE_TIME > 10):
		print("WARNING: IDLE_TIME ({}) is out of officially supported range (0-10).".format(IDLE_TIME))

	if(TOTAL_FRAME_COUNT > 99):
		print("WARNING: Total frame count exceeds officially supported range ({} > 99).".format(TOTAL_FRAME_COUNT))
		print("         Mouse support is possible but not guaranteed.")
		print("         Exceeding the frame limit may lead to memory access violation!")

	with open(FILE_NAME + ".ckAnimation", "w") as f:
		f.write(generateContent())

if __name__ == "__main__":
    main()