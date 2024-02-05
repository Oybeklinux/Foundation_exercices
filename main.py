from PIL import Image, ImageFont
text = """
print("Hello")
print("Hello")
"""
font_size = 36
font_filepath = "Roboto-Regular.ttf"
color = (255,255,255,255)
font = ImageFont.truetype(font_filepath, size=font_size)
mask_image = font.getmask(text=text, mode="L", anchor="lt",  direction="ttb")
img = Image.new("RGBA", mask_image.size)
img.im.paste(color, (0, 0) + mask_image.size, mask_image)  # need to use the inner `img.im.paste` due to `getmask` returning a core
img.save("yes.png")