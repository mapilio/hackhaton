import csv
import os
from haversine import haversine


hackathon_file_path = 'Your Path'
gopro_360_file = 'GOpro360/gopro_360.csv'
absolute_path = os.path.join(hackathon_file_path, gopro_360_file)
with open(absolute_path) as fd:
    reader = csv.reader(fd)
    objects_which_is_ids_zero = [row for idx, row in enumerate(reader) if idx in (range(1, 5))]

ground_truth_object_zero = [float(objects_which_is_ids_zero[0][0]), float(objects_which_is_ids_zero[0][0])]
prediction = [41.088570138103435, 28.786196708679196]
distance = haversine(ground_truth_object_zero, prediction)
