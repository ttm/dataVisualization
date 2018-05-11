# from https://pillow.readthedocs.io/en/5.1.x/handbook/tutorial.html
# import pilfile, pilprint, pilfont, pildriver, pilconvert
from PIL import Image
# im = Image.open("../figs/rf.jpg")
im = Image.open("../figs/RitaWu_nomes.png")
# mode is number and names of bands of image, also pixel depth and hight
# table of modes: xxx
print('fmt: {}, (w, h): {}, mode: {}'.format(im.format, im.size, im.mode))

MS = 14
i = 0
def mshow(mid=im):
    global i
    if MS < i:
        mid.show()
    i += 1
# # ou:
# def mshow(mid=im):
#     mid.show()
mshow(im)
# mshow(im) is im.show(), but skips first 'MS' show()

im.save("./RitaWu_nomes.gif")
# im.save("./nobelLast.jpg")  # gives error, RGBA -> JPEG

box = (100, 100, 400, 400)
region = im.crop(box)

region_ = region.transpose(Image.ROTATE_180)
im.paste(region_, box)
mshow(im)

# file:///home/renato/repos/Pillow/docs/_build/html/handbook/tutorial.html#color-transforms

def roll(image, delta):
    """Roll an image sideways"""
    xsize, ysize = image.size

    delta = delta % xsize
    if delta != 0:
        part1 = image.crop((0, 0, delta, ysize))
        part2 = image.crop((delta, 0, xsize, ysize))
        part1.load(), part2.load()  # lazy
        image.paste(part2, (0, 0, xsize - delta, ysize), part2)
        image.paste(part1, (xsize - delta, 0, xsize, ysize), part1)
        return image

roll(im, 300)
mshow(im)

r, g, b, a = im.split()

im2 = Image.merge("RGBA", (a, b, g, r))
mshow(im2)

im3 = im2.resize((200, 200))
im4 = im2.rotate(45)
mshow(im3)
mshow(im4)

im5 = im.transpose(Image.FLIP_LEFT_RIGHT)
im6 = im.transpose(Image.FLIP_TOP_BOTTOM)

# these are the same as im.rotate(xxx, expand=true)
im7 = im.transpose(Image.ROTATE_90)
im8 = im.transpose(Image.ROTATE_180)
im9 = im.transpose(Image.ROTATE_270)

# see im.transform()

# every mode is convertable to RGB and L:
im10 = im.convert('L')
# other modes might need intermediady conversion
# what are the modes? What does 'L' mean?

#############
### Image enhancements

# Filters
from PIL import ImageFilter

im11 = im.filter(ImageFilter.DETAIL)
mshow(im)
mshow(im11)

im12 = im.point(lambda i: i * 1.2)
im13 = im.point(lambda i: i ** 2)
mshow(im12)
mshow(im13)

# bands
source = im.split()
lowred_mask = source[0].point(lambda i: i < 100 and 255)
newgreen = source[1].point(lambda i: i * 0.7)
source[2].paste(newgreen, None, lowred_mask)
im14 = Image.merge(im.mode, source)
mshow(im)
mshow(im14)

# Enhancement
from PIL import ImageEnhance

enh = ImageEnhance.Contrast(im)
# enh.enhance(1.3).show('30% more constrast')  # title not working TTM
mshow(enh.enhance(1.3))

# Sequences
from PIL import ImageSequence
im15 = Image.open('../figs/giphy.gif')

mshow(im15)
j = 0
rot = [0, Image.ROTATE_90), Image.ROTATE_180), Image.ROTATE_270]
for frame in ImageSequence.Iterator(im5):
    r = rot[j % 4]
    frame = frame.transpose(frame)


################ 
# check if import PIL yields all the functionalities:
#   - above; and
#   - in the official Reference:
# file:///home/renato/repos/Pillow/docs/_build/html/reference/index.html

# choose a color,
# varre o space RGB cada vez com os 0 fixos, 000, até 111 = mudando os 3.
# fazer isso em outros espaços.
# Ou seja, primeiro só o azul muda, depois só o verde, depois o verde e azul (cian),
# depois só o vermelho, depois o vermelho e o azul (magenta), depois o vermelho e o verde,
# depois as tres cores.
# mostra escrito no gif com postscrit. O que tá parado fica em vermelho, anda de y em y unidades (e.g. 16 em 16), 
# e a x passos (paces) por segundo (e.g. 5 p/s).

# why is the image itself used as the mask in Image().paste()?
# pymovie TTM
