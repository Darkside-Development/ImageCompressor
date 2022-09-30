from PIL import Image

img = input("What's your image's file name and extension?\n> ")

img = Image.open(img)
img = img.convert('RGB')
img.save("output.jpg", quality=30)