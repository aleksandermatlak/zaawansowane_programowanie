from src.person_detector import detection_model, analyze_images
images = ['data_input/people1.jpg', 'data_input/people2.jpg', 'data_input/people3.jpg']

model = detection_model()

for image in images:
    analyze_images(image, model)





