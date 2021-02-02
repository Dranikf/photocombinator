# photocombinator
functions for cutting a photo into strips and gluing back into multiple photos like represented here  https://youtu.be/ZL6jfM1ARQ8?t=394
# library Pillow
pillow library used https://github.com/python-pillow/Pillow 
# Examples

by using ``` get_image_strips```
you can get list of strips
```sh

strips = get_image_strips(p, 3, dir = 0);

for strip in strips:
    strip.show();

```

result

<img src = "https://raw.githubusercontent.com/Dranikf/photocombinator/main/examples/cuci.jpeg" height = "600">
<img src = "https://raw.githubusercontent.com/Dranikf/photocombinator/main/examples/example1.png" height = "600">

by using ```sh combine_strips```
you can combine strips in new pictures
```sh
res = combine_strips(strips,2, 0);

for r in res:
    r.show();
```

result

<img src = "https://raw.githubusercontent.com/Dranikf/photocombinator/main/examples/example2.png" height = "600">

```combine_photo```
uses previos functions for combining any file
```combine_photo('examples/cuci.jpeg', 40, 3,1);```

result

<img src = "https://raw.githubusercontent.com/Dranikf/photocombinator/main/examples/cuci_0.jpeg" height = "200">
<img src = "https://raw.githubusercontent.com/Dranikf/photocombinator/main/examples/cuci_1.jpeg" height = "200">
<img src = "https://raw.githubusercontent.com/Dranikf/photocombinator/main/examples/cuci_2.jpeg" height = "200">

for more examples look 'examples' folder