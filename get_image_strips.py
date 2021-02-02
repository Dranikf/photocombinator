from PIL import Image;


def get_image_strips(image, count, dir = 1):
    '''function for cutting photos into small strips 
    input: 
    image - pillow image for transformation
    count - count of stripes
    dir - =1 - horizontal, =0 - vertical
    output: list of results'''

    orig_size = image.size


    step = int(orig_size[dir] / count);
    if step == 0: 
        print("too small resolution for so many stripes!!! chose count lower");
        return None;

    # cursor wich describe where top left coner of each strip
    pos = [0 , 0];

    box_size = [orig_size[0] , orig_size[1]];
    box_size[dir] = step;

    result = [];

    # getting each flat except the last
    for i in range(count-1):

        box = [pos[0], pos[1], pos[0] + box_size[0], pos[1] + box_size[1]];

        cropped = image.crop(box);
        result.append(cropped);
        pos[dir] += step;
    
    #the last stripe may differ in size, 
    #since the size of the photo is not always 
    #a multiple of the number of stripes 
    box[dir] += step;
    box[dir + 2] = box[dir] + orig_size[dir] % count + step;
    cropped = image.crop(box);
    result.append(cropped);

    return result;