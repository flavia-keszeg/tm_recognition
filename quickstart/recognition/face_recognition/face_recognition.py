from imageai.Prediction.Custom import CustomImagePrediction
import os

def face_recognition(imageName):

    execution_path = os.getcwd()

    prediction = CustomImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("./quickstart/recognition/face_recognition/model_ex-030_acc-1.000000.h5")
    prediction.setJsonPath("./quickstart/recognition/face_recognition/model_class.json")
    prediction.loadModel(num_objects=3)

    predictions, probabilities = prediction.predictImage(imageName, result_count=3)

    recognized_faces = {}
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        recognized_faces[eachPrediction] = eachProbability

    return recognized_faces
