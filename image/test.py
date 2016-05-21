try:
     import Image
except ImportError:
     from PIL import Image
import pytesseract

def scale(image, max_size):
    """
    resize 'image' to 'max_size' keeping the aspect ratio 
    and place it in center of white 'max_size' image 
    """
    back = Image.new("RGB", max_size, (255,255,255,255))   ## luckily, this is already black!
    back.paste(image, ((max_size[0]-image.size[0])/2,
						(max_size[1]-image.size[1])/2))
    return back

img = Image.open('test2.png')
#img = scale(img, (640,480))
#img.save("test1.bmp")
print(pytesseract.image_to_string(img,config='-psm 10000'))
