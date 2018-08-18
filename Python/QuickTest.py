from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models
from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
import os
import time

# Replace with a valid key
training_key = "<YOUR_TRAINING_KEY>"
prediction_key = "<YOUR_PREDICITON_KEY>"

predictor = prediction_endpoint.PredictionEndpoint(prediction_key)
trainer = training_api.TrainingApi(training_key)

trainer = training_api.TrainingApi(training_key)
project = trainer.create_project("AZ2Object-CodeRED")
iteration = trainer.train_project(project.id)

base_image_url = "https://raw.githubusercontent.com/insung3511/A2ZObject-Data/"

# Now there is a trained endpoint that can be used to make a prediction

predictor = prediction_endpoint.PredictionEndpoint(prediction_key)

test_img_url = base_image_url + "master/opencv888.png"
results = predictor.predict_image_url(project.id, iteration.id, url=test_img_url)

# Alternatively, if the images were on disk in a folder called Images alongside the sample.py, then
# they can be added by using the following.
#
# Open the sample image and get back the prediction results.
# with open("Images\\test\\test_image.jpg", mode="rb") as test_data:
#     results = predictor.predict_image(project.id, test_data, iteration.id)

# Display the results.
for prediction in results.predictions:
    print ("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))