from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models
import time

# Replace with a valid key
training_key = "<YOUR_TRAINING_KEY>"
prediction_key = "<YOUR_PREDICITON_KEY>"

trainer = training_api.TrainingApi(training_key)

# Create a new project
print ("Creating project...")
project = trainer.create_project("CodeRed")

# Make two tags in the new project
top_tag = trainer.create_tag(project.id, "Top")
bottom_tag = trainer.create_tag(project.id, "Bottom")

base_image_url = "https://raw.githubusercontent.com/insung3511/A2ZObject-Data/"

print("Adding images...")
for image_num in range(1,10):
    image_url = base_image_url + "master/bottom/opencv{}.png".format(image_num)
    trainer.create_images_from_urls(project.id, [ ImageUrlCreateEntry(url=image_url, tag_ids=[ bottom_tag.id ] ) ])
    print("Image State Bottom : ", image_num)

for image_num in range(1,10):
    image_url = base_image_url + "master/top/opencv{}.png".format(image_num)
    trainer.create_images_from_urls(project.id, [ ImageUrlCreateEntry(url=image_url, tag_ids=[ top_tag.id ] ) ])
    print("Image State Top : ", image_num)

print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    time.sleep(1)

# The iteration is now trained. Make it the default project endpoint
trainer.update_iteration(project.id, iteration.id, is_default=True)
print ("Done!")


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