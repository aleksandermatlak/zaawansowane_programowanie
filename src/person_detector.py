import torch
import cv2
import time


def detection_model():
    # set download directory for model
    torch.hub.set_dir('src/')
    # load up model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, verbose=False)
    # only person class
    model.classes = [0]
    # check if system supports cuda if it does apply it
    if torch.cuda.is_available():
        model.model.cuda
    return model


def analyze_images(image, model):
    # load image
    img = cv2.imread(image)
    # image conversion to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # time measurement start
    start = time.time()
    # load the image onto the model
    analysis_results = model(img_rgb)
    # time measurement end
    end = time.time()
    # duration of the process
    duration = end - start
    # convert results into pandas dataframe
    df = analysis_results.pandas().xyxy[0]
    # show duration
    print("Processing time of " + str(image) + " was: " + str(duration) + " seconds.")
    # show total number of people detected
    print("Total number people detected: " + str(df.shape[0]))
    # show analysis details
    print(analysis_results)
    # show processed image
    analysis_results.show()
    # show dataframe
    print(df)
    # save processed image
    analysis_results.save(save_dir='data_output/processed')







