from PIL import Image, ImageFilter

img= Image.open("./image_processing_python/pokedex/pokemon2.jpg")
print(img)
print(img.format)
print(img.size)
print(img.mode)

#to make picture blur (filters)
#filtered_image= img.filter(ImageFilter.BLUR)
#filtered_image= img.filter(ImageFilter.SMOOTH)
#filtered_image.save("blur1.png","png")
#filtered_image.save("smooth.png","png")
#filtered_image= img.convert("L")
#filtered_image.save("grayscale1.png","png")
#filtered_image.show()

# ROTATING IMAGES:
'''rotated_img=img.rotate(90)
rotated_img.save("rotatedimg1.png","png")
rotated_img.show()'''
# RESIZING IMAGES:
resizeimg=img.resize((1000,1000))
#resizeimg.show()
#img.show()
# CROPING IMAGES:
box= (100,100,400,400)
cropimg= img.crop(box)
cropimg.show()








