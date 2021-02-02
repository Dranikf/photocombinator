from PIL import Image;
from get_image_strips import get_image_strips;
from combine_strips import combine_strips;
from combine_photo import combine_photo;

p = Image.open('examples/cuci.jpeg')

strips = get_image_strips(p, 3, dir = 0);

#for strip in strips:
#    strip.show();

res = combine_strips(strips,2, 0);

#for r in res:
#    r.show();


combine_photo('examples/elumin.jpeg', 20, 2,0);