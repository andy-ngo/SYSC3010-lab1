from PIL import Image
import numpy as np

#Takes in image 1 and image 2 locations and t1
#returns a Boolean indicating if a "person" is in the image based on t1
def person_detected(image1_file,image2_file,t1):
    bg = Image.open(image1_file)
    buff = Image.open(image2_file)
    
    bg_asarray = np.asarray(bg)
    buff_asarray = np.asarray(buff)
    
    diff = np.absolute(bg_asarray - buff_asarray)
    
    """
    img1 = np.asarray(image1_file)
    img2 = np.asarray(image2_file)
    
    image1 = np.sum(img1)
    image2 = np.sum(img2)
    
    difference = np.subtract(image1,image2)
    final = np.abs(difference)
    """
    final = np.sum(diff)
    
    if (final > t1):
        return True
    else:
        return False