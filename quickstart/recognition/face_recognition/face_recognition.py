import os

from imageai.Prediction.Custom import CustomImagePrediction


def face_recognition(imageName):
    execution_path = os.getcwd()

    prediction = CustomImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("./quickstart/recognition/face_recognition/model_ex-030_acc-1.000000.h5")
    prediction.setJsonPath("./quickstart/recognition/face_recognition/model_class.json")
    prediction.loadModel(num_objects=3)

    predictions, probabilities = prediction.predictImage(imageName, result_count=3)

    person = ''
    max = '0'
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        if eachProbability > max:
            max = eachProbability
            person = eachPrediction

    if max >= '80':
        return "It's " + person + "!"
    else:
        return "Didn't recognise anyone"
