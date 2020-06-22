import math
import os

import numpy as np
from PIL import Image
from imageai.Detection import ObjectDetection


def object_recognition(imageName, actual_size):
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(
        os.path.join(execution_path, "quickstart/recognition/object_recognition/resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(
        input_image=imageName,
        output_image_path=os.path.join(execution_path, "media/images/imagenew.jpg"))

    # opening the image and loading it into a
    # numpy array using PIL and numpy
    img = Image.open("media/images/imagenew.jpg")
    pixels = np.array(img)

    # dimensions of the image
    width, height, channels = pixels.shape

    detected_objects = {}
    for eachObject in detections:
        if eachObject["name"] not in detected_objects:
            detected_objects[eachObject["name"]] = []

    for eachObject in detections:
        detected_objects[eachObject["name"]].append(eachObject["box_points"])

    points = calculate_central_point_of_a_person(detected_objects)
    distance = calculate_distance_between_people(points, actual_size, width)
    nr_of_people = number_of_persons_with_less_than_2m(distance)

    return nr_of_people


def calculate_central_point_of_a_person(objects):
    central_points = []  # the list with a central point of each person

    for key in objects:
        print(key)
        if key == 'person':
            for data in objects[key]:  # evaluating all 4 coordinates of a person to find out the central point
                central_point_x = (data[0] + data[2]) / 2
                central_point_y = (data[1] + data[3]) / 2
                my_point = (central_point_x, central_point_y)
                central_points.append(my_point)  # adding the central point as a tuple inside a list

    return central_points


def calculate_distance_between_people(list_of_points, act_dist, width):
    """
    Calculate the real distance between people
    :param list_of_points:
    :param act_dist: the actual width of the place from the picture
    :param width: the width of the picture in pixels
    :return:
    """
    # act_dist=10
    distance = {}
    for point1 in list_of_points:
        x1, y1 = point1
        for point2 in list_of_points:
            ok = 0
            x2, y2 = point2
            if x1 != x2 and y1 != y2:
                dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                actual_dist = (dist / width) * act_dist
                for points in distance:
                    p1, p2 = points
                    if p1 == point2 and p2 == point1:
                        ok = 1
                if ok == 0:
                    distance[(point1, point2)] = actual_dist
    return distance


def number_of_persons_with_less_than_2m(distance_between):
    count = 0
    for elem in distance_between:
        print(distance_between[elem])
        if distance_between[elem] < 2:
            count = count + 1
    return count
