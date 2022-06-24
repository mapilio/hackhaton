import csv
import os
from haversine import haversine


hackathon_file_path = 'Hackathon'
gopro_360_file = 'GOpro360/gopro_360.csv'
object_locations = 'object_locations.csv'
absolute_path = os.path.join(hackathon_file_path, gopro_360_file)

start_id, end_id = 1, 5  #####First object ids. For second object (6,10)
object_id = 0
objects_feature1, objects_feature2 = 7, 8   ###7 : Lat , ###8: Lon
with open(absolute_path) as fd:
    reader = csv.reader(fd)
    objects_which_is_ids_zero = [row for idx, row in enumerate(reader) if idx in (range(start_id, end_id))]
    print(objects_which_is_ids_zero)

ground_truth_object_zero = [float(objects_which_is_ids_zero[object_id][objects_feature1]),
                            float(objects_which_is_ids_zero[object_id][objects_feature2])]
prediction = [41.088570138103435, 28.786196708679196]
distance = haversine(ground_truth_object_zero, prediction)
print(f'{distance} meter')
