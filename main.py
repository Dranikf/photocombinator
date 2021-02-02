from PIL import Image;
from get_image_strips import get_image_strips;
from combine_strips import combine_strips;

#sudo apt-get install imagemagick

p = Image.open('luka.jpeg');
k = Image.open('unnamed.jpeg');

sptis = 30;
while True:
    a = input();

    if a == "q":
        for i, photo in enumerate(photos):
            photo.save("test" + str(i) + ".jpeg");
    else:
        sptis += int(a);
        strips = get_image_strips(p, sptis, dir = 1);
        photos = combine_strips(strips, 3, dir = 1);
        for i, photo in enumerate(photos):
            photo.show()