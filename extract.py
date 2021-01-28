import sys, os
sys.path.append('../')


import numpy as np
from image.large_frame_processor import LargeFrameProcessor

binary_threshold = 1600
star_image_size = 9
# dpixel radian per pixel
large_frame_processor = LargeFrameProcessor(
    plate_id_offset=1,
    directory='/Users/kohei/JASMINE/from_kyoto/analysis_sandbox_kohei_distortion_at_kyoto/mksamplefits4_single_star/dataset/frame00000',
    dpixel=2.6e-6,
    star_image_size=star_image_size
)
# extract brighter stars and mapping
# brighter_star_position_in_pixel is list of
# (plate id, star id, x in ecliptic, y in ecliptic, x in pixel, y in pixel)
brighter_star_position_in_pixel, extracted_brighter_star_image_list = large_frame_processor.execute(
        same_star_ecliptic_range=0,
        binary_threshold=binary_threshold
)
n = brighter_star_position_in_pixel.shape[0]
print(str(n)+" star(s) is/are detected which is brighter than "+str(binary_threshold))

np.save('positionlist', brighter_star_position_in_pixel)
np.save('imagelist', extracted_brighter_star_image_list)

# np.savetxt('poslist.csv', brighter_star_position_in_pixel, delimiter=',')
# np.savetxt('imlist.csv', extracted_brighter_star_image_list.reshape(
#     [n * star_image_size, star_image_size]), delimiter=',')
