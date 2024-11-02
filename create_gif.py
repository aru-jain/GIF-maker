from PIL import Image

images = []
for filename in ['cat1.png','cat2.png','cat3.png']:
    images.append(Image.open(filename))

images[0].save('cat.gif', save_all=True, append_images=images[1:], duration=500, loop=0, disposal=2)

