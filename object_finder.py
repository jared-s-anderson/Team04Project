#from io import BytesIO
#import PIL
#from PIL import Image
#import math

from GAME_VARIABLES import X, Y



class ObjectFinder:
    def __init__(self, image): 
        self.objects = {}
        #self.image = Image.open((image))
    
    def find_objects(self):
        coordinates = []
        for y in range(self.image.height):
            curr_row = []
            for x in range(self.image.width):  
                rgb = self.image.getpixel((x, y))
                curr_row.append((rgb, (x, y)))
        
            for i in range(len(curr_row) - 1):
                if i == 0:
                    pass
                elif i == len(curr_row) -1:
                    pass
                else:
                    prev_rgb = curr_row[i - 1][0]
                    curr_rbg = curr_row[i][0]

                    prev_r = prev_rgb[0]
                    prev_g = prev_rgb[1]
                    prev_b = prev_rgb[2]

                    curr_r = curr_rbg[0]
                    curr_g = curr_rbg[1]
                    curr_b = curr_rbg[2]

                    if curr_g > curr_r + 50 and curr_g > curr_b + 50:                                                         # (abs(prev_r - curr_r) >= 68) or (abs(prev_g - curr_g) >= 68) or (abs(prev_b - curr_b) >= 68):
                        x_rounded = round(curr_row[i][1][0] + 5.1, -1)
                        y_rounded = round(curr_row[i][1][1] + 5.1, -1)
                        coordinates.append([x_rounded, y_rounded])
                        print(curr_row[i], self.colored(curr_r, curr_g, curr_b, "COLOR"))
        return coordinates

    def colored(self, r, g, b, text):
           return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)