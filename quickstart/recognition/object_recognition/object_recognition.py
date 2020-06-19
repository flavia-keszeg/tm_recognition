import os

from imageai.Detection import ObjectDetection


def object_recognition(imageName):
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(
        os.path.join(execution_path, "quickstart/recognition/object_recognition/resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(
        # input_image=os.path.join(execution_path, "quickstart/recognition/object_recognition/test1.jpeg"),
        input_image=imageName,
        output_image_path=os.path.join(execution_path, "quickstart/recognition/object_recognition/imagenew.jpg"))

    detected_objects = {}
    for eachObject in detections:
        if eachObject["name"] not in detected_objects:
            detected_objects[eachObject["name"]] = []

    for eachObject in detections:
        detected_objects[eachObject["name"]].append(eachObject["percentage_probability"])
        detected_objects[eachObject["name"]].append(eachObject["box_points"])

    return detected_objects
