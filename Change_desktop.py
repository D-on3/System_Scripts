import ctypes

# Change if nesesery
wallpaper_path = "G:\\7485710.jpg"

#To change the desctop background
ctypes.windll.user32.SystemParametersInfoW(20,0,wallpaper_path,3)