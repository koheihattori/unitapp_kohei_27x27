import csv
import os
import numpy as np
from numpy.core.multiarray import ndarray

from common.logger import Logger
from image.distortion import MappedStarObservationsOnPlate
from image.large_frame_processor import LargeFrameProcessor


star_image_size = 9
dpixel = 2.5e-6
known_stars_neighborhood = 10
known_stars_ecliptic_neighborhood = known_stars_neighborhood * dpixel
star_center_matrix = np.load('starCenter.npy')
known_stars_path = "data1/one_frame_known_stars.csv"

known_star_params = np.empty((0, 6), float)
with open(known_stars_path) as fr:
    reader = csv.reader(fr)
    next(reader)
    for r in reader:
        known_star_params = np.append(known_star_params, np.array([[-1, float(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4])]]), axis=0)

mapped_star_positions = MappedStarObservationsOnPlate(star_center_matrix=star_center_matrix)

large_frame_processor = LargeFrameProcessor(
    plate_id_offset=1,
    directory="data1",
    dpixel=dpixel,
    star_image_size=star_image_size
)

if len(known_star_params) != 0 and known_star_params[0, 0] < 0:
    known_star_params = LargeFrameProcessor.map_known_stars(
        all_star_position=star_center_matrix,
        known_star_params=known_star_params,
        same_star_ecliptic_range=known_stars_ecliptic_neighborhood
    )

np.save('knownStarParams', known_star_params)
# np.savetxt('knownStars.csv', known_star_params, delimiter=',')
