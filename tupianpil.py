from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance, ImageFilter  
image1 = Image.open('F:/python/PythonClimbInsect/1.jpg')  
image2 = Image.open('F:/python/PythonClimbInsect/2.jpg')  
def 图片大小(image):  
   w, h = image.size      #获得图片的大小（分辨率）  
   return w, h  
def 图片剪裁(image, p1, p2, p3, p4):  
    box = (p1, p2, p3, p4)  
    image = image.crop(box)  
    #crop() : 从图像中提取出某个矩形大小的图像。它接收一个四元素的元组作为参数，
    #各元素为（left, upper, right, lower），坐标系统的原点（0, 0）是左上角。
    image.show()  
    return image  
def 图片压缩(image, size1, size2):  
    image.thumbnail((size1, size2), Image.ANTIALIAS)  
    image.show()  
    return image  
def 图片旋转(image, jiaodu):  
    image = image.rotate(jiaodu)  
    image.show()  
    return image  
def 图片黑白转换1(image):  
    image = image.convert('L')   #(8-bit pixels, black and white)  
    image.show()  
    return image  
def 图片过滤(image):  
    image.filter(ImageFilter.DETAIL)  
def 图片写字(image, p1, p2, text):  
    draw = ImageDraw.Draw(image)  
    draw.text((p1, p2), text)  
    image.show()  
#w, h = image1.size  
#图片写字(image1, w-100, h-20, 'hello')  
def 图片拼接(image1, image2):  
    images = (image1, image2)  
    w, h = image1.size  
    target = Image.new('RGB', (w*2, h))  
    left = 0 
    right = w  
    for image in images:  
        temp = image.resize((w, h), Image.ANTIALIAS)  
        target.paste(temp, (left, 0, right, h))  
        left += w  
        right += w  
    target.show()  
#图片拼接(image1, image2)  
def 图片黑白转换2(image):  
    image = image.convert('1')   #(1-bit pixels, black and white, stored with one pixel per byte)  
    image.show()  
    return image  
def 图片虚化(image):  
    image = image.convert('P')   #(8-bit pixels, mapped to any other mode using a colour palette)  
    image.show()  
    return image  
def 图片转换怀旧(image):  
    image = image.convert('LA')  
    image.show()  
    return image  
def 图片锐化(image, qiangdu):  
    enhancer = ImageEnhance.Sharpness(image)  
    enhancer.enhance(qiangdu).show()  
def 图片色彩增强(image, qiangdu):  
    enhancer = ImageEnhance.Color(image)  
    enhancer.enhance(qiangdu).show()  
def 图片亮度增强(image, qiangdu):  
    enhancer = ImageEnhance.Brightness(image)  
    enhancer.enhance(qiangdu).show()  
def 图片对比度增强(image, qiangdu):  
    enhancer = ImageEnhance.Contrast(image)  
    enhancer.enhance(qiangdu).show()  
def 图片BlUR(image):  
    image = image.filter(ImageFilter.BLUR)  
    image.show()  
def 图片MinFilter(image):  
    image = image.filter(ImageFilter.MinFilter)  
    image.show()  
def 图片转换黑白线条(image):  
    image = image.filter(ImageFilter.CONTOUR)  
    image.show()  
def 图片EMBOSS(image):  
    image = image.filter(ImageFilter.EMBOSS)  
    image.show()  
def 图片FIND_EDGES(image):  
    image = image.filter(ImageFilter.FIND_EDGES)  
    image.show()
图片剪裁(image2,10,20,10,20)