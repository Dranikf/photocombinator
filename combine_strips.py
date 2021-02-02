from PIL import Image;


def combine_strips(strips, count, dir = 1):
    '''function for gluing strips to count pictures
    input: 
    strips - (pillow images)
    count - count of photos
    dir - =1 - horizontal, =0 - vertical
    output: list of photos'''

    str_count = len(strips);

    if str_count < count:
        print('nor enought strips for ' + str(count) + ' photos')
        return None;

    result = [];
    pos = []
    active_mode = strips[0].mode;

    #images creating, and for every one create pos which will
    #describe where to insert strip
    for c in range(count):
        pos.append([0,0]);
        result.append(Image.new(active_mode, (0, 0)));

    new_size = [0,0];
  

    for c, strip in enumerate(strips):
        img_index = c%count;

        #compution new size of photo
        new_size = [result[img_index].size[0], result[img_index].size[1]]
        strip_size = strip.size

        new_size[dir] = new_size[dir] + strip_size[dir];
        if new_size[dir-1] < strip_size[dir-1]:
            new_size[dir-1] = strip_size[dir-1];


        #creating new photo and insert old photo and new part of it
        temp_image = Image.new(active_mode, new_size);
        temp_image.paste(result[img_index], (0,0));
        temp_image.paste(strip, [pos[img_index][0], pos[img_index][1]]); # [pos[img_index][0], pos[img_index][1]] no pos else funrciton will change pos 
        result[img_index] = temp_image;
        pos[img_index][dir] += strip_size[dir];


    return result;
