import sys, os
sys.path.append('../')

import numpy as np
from app.calculate_center_position import CenterCalculator

brighter_star_position_in_pixel =np.load('positionlist.npy')
extracted_brighter_star_image_list = np.load('imagelist.npy')
# dpixel means radian / pixel
dpixel: float =2.6e-6

center_calculator = CenterCalculator(
    center_iteration=20,
    x_magnification=3,
    y_magnification=3,
    psf_brightness_threshold=100,
    max_iteration=20
)
brighter_star_position_in_pixel = brighter_star_position_in_pixel[:, [0, 1, 4, 5]]
star_pixel_position_with_errors, psf_coefficient = center_calculator.execute(
    star_positions_in_pixel=brighter_star_position_in_pixel,
    all_extracted_star_images=extracted_brighter_star_image_list
)
# np.savetxt('poslist2.csv', star_pixel_position_with_errors, delimiter=',')
errors = star_pixel_position_with_errors[:, CenterCalculator.X_ERROR_INDEX:CenterCalculator.Y_ERROR_INDEX + 1]
errors *= dpixel
star_pixel_position_with_errors[:, CenterCalculator.X_ERROR_INDEX:CenterCalculator.Y_ERROR_INDEX + 1] = errors

np.save('positionlist2', star_pixel_position_with_errors)
np.save('psfcoeff', psf_coefficient)

# np.savetxt('poslist3.csv', star_pixel_position_with_errors, delimiter=',')
# np.savetxt('psfcoeff.csv', psf_coefficient, delimiter=',')



