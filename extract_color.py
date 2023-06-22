import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
import extcolors

# from colormap import rgb2hex
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def extract_color(input_image, resize):
    output_width = resize
    img = Image.open("./uploads/"+input_image)
    if img.size[0] >= resize:
        width_per_c = (output_width / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(width_per_c)))
        img = img.resize((output_width, hsize), Image.ANTIALIAS)
        resize_name = 'resize_' + input_image
        img.save("./uploads/"+resize_name)

        return "./uploads/"+resize_name
    else:
        resize_name = input_image