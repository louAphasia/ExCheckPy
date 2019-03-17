from PIL import Image
from urllib.request import urlopen
import io

response=urlopen('http://img2.altcontroldelete.pl/covers/6ccedf44-066a-3d19-e5d8-63255bb841f3.jpg')
im_file=io.BytesIO(response.read())
im=Image.open(im_file)
#im=im.resize((800,600))
#im=im.rotate(90)
im.save("downpy.jpg","JPEG")