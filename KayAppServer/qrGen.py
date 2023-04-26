from PIL import Image;
import qrcode;
import os;
def get_qrs(data,filename):
    img = qrcode.make(data);
    img.save(filename+".png");
    im = Image.open(filename+".png")
    rgb_im = im.convert('RGB')
    rgb_im.save(filename+'.jpg')
    os.remove(filename+".png")