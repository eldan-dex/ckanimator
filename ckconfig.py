# Output file name:
FILE_NAME = "output"

# Animation description:
DESCRIPTION = ""

# Animation starts if no keyboard input for IDLE_TIME minutes (max 10); 0 = infinite loop:
IDLE_TIME = 0

# Static RGB color to show during IDLE_TIME:
IDLE_COLOR = "000000"

# Each string must have the same number of HEX codes separated by commas in "" (<ColorPicture>):
COLOR_LIST = [
"3C3CF0,00FFFF,00FFFF,00FFFF,00FFFF,00FFFF,3C3CF0,00FFFF",
"703824,DF9CCC,DF9CCC,DF9CCC,DF9CCC,703824,8B42EA,703824",
"00FFFF,0080FF,0080FF,0080FF,0080FF,0080FF,00FFFF,0080FF",
"2900FF,6F4FFF,6F4FFF,6F4FFF,6F4FFF,6F4FFF,2A00FF,6F4FFF",
"0064FF,0000FF,00FF00,0000FF,00FF00,FFFF00,892F66,FFFF00",
"FF6400,FF0000,FF00FF,FF0000,FF00FF,00FFFF,662F89,00FFFF"
]

# Number and delay (seconds) of manually entered frames:
BASE_FRAME_COUNT = len(COLOR_LIST)
BASE_FRAME_TIME = 5

# Number and delay (seconds) of generated transition frames:
TRANSITION_FRAME_COUNT = 18
TRANSITION_FRAME_TIME = 0.025