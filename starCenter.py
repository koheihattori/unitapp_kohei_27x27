import numpy as np
from image.large_frame_processor import LargeFrameProcessor
from image.distortion import MappedStarObservationsOnPlate

star_image_size = 9
star_pixel_position_with_errors = np.load('positionlist2.npy')
psf_coefficient = np.load('psfcoeff.npy')
large_frame_processor = LargeFrameProcessor(
    plate_id_offset=1,
    directory="data1",
    dpixel=2.5e-6,
    star_image_size=star_image_size
)
ecliptic_positions = large_frame_processor.convert_to_ecliptic(
    star_pixel_position_with_errors=star_pixel_position_with_errors)
star_center_matrix = np.concatenate([
    star_pixel_position_with_errors[:, 0:MappedStarObservationsOnPlate.LONGITUDE_INDEX],
    ecliptic_positions,
    star_pixel_position_with_errors[:, MappedStarObservationsOnPlate.LONGITUDE_INDEX:]
    ], axis=1)

np.save('eclipticPositions', ecliptic_positions)
np.save('starCenter',star_center_matrix)
# np.savetxt('eclipticPosition.csv', ecliptic_positions, delimiter=',')
# np.savetxt('starCenter.csv', star_center_matrix, delimiter=',')
