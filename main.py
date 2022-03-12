from PIL import Image

# region Open a file and save it under a new graphic format.
Img = Image.open(r’Media\nasa-earth-as-art-3.png’)
Img.save(r’Media\nasa-earth-as-art-3.gif’, ‘GIF’)
# endregion
# region Create a thumbnail of the image and save it under a new name.
thumbnailSize = (100, 100)
Img_thumbnail = Img.copy()
Img_thumbnail.thumbnail(thumbnailSize)
# endregion
# region Flip the original image from top to bottom.
Img_FlipLR = Img.transpose(Image.FLIP_TOP_BOTTOM)
# endregion
# region Rotate the original image 270 degrees.
Img_Rot270 = Img.transpose(Image.ROTATE_270)
# endregion
# region Scale the original image by 75% and save it.
Scale = 0.75
sizeX, sizeY = Img.size
Img_Resized = Img.resize((int(sizeX*Scale), int(sizeY*Scale)))
# endregion
# region Save all image manipulation results and display the original image.
Img_thumbnail.save(r’Media\nasaearth-as-art-3_thumbnail.png’)
Img_FlipLR.save(r’Media\nasa-earthas-art-3_flippedLR.png’)
Img_Rot270.save(r’Media\nasaearth-as-art-3_rot270.png’)
Img_Resized.save(r’Media\nasaearth-as-art-3_resized.png’)
Img.show()
# endregion
