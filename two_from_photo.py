from PIL import Image;
from get_image_strips import get_image_strips;
from combine_strips import combine_strips;

def two_from_photo(filename, str_count, photo_count, dir = 1):
    '''combines  get_image_strips and combine_strips
    for geven file
    input:
    filename - name of original photo
    str_count - number of strips
    photo_count - count of ouput photos
    dir - =1 - horizontal, =0 - vertical
    output:
    files with photos at the same directory with input photo'''
    photo = Image.open(filename);
    
    strips = get_image_strips(photo, str_count, dir);
    photos = combine_strips(strips, photo_count, dir);

    if not strips or not photos:
        print('exeption!');
        return; 

    point_pos = filename.index(".");

    for i, photo in enumerate(photos):
        photo.save(filename[:point_pos] + '_' + str(i) + filename[point_pos:]);