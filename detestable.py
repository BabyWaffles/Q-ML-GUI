import os
import numpy as np
import cv2
from ultralytics import YOLO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

work_DIR = os.getcwd()
asset = work_DIR + "\\assets\\"
trainer_model_dir = work_DIR + "\\models\\YOLO\\"
ready_model = work_DIR + "\\models\\pre-trained\\huamn-detection-v8n\\best.pt"
ffmpeg_bin = work_DIR + "\\bin\\ffmpeg.exe"
camera_id = 1


class inferencing:
    def __init__(self, model, frame):
        self.model = model # get model from the model directory
        self.frame = frame # get frame from the feed
        if self.frame is None:
            return None
        self.bbx = None # bounding box
    def infer(self):
        model = YOLO(self.model) # load the model
        for result in model.predict(self.frame, conf=0.8):
            self.bbx = result
    def render(self):
        __class__.infer(self) # Calls infer automatically
        return renderbbx(self.frame, self.bbx).render()
    def hrec(self):
        return self.bbx # return the bounding box


@staticmethod 
class renderbbx:
    def __init__(self, frame, bbx):
        self.frame = frame
        self.bbx = bbx
    def render(self):
        image = Image.fromarray(self.frame)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        for box in self.bbx.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # label = f"{box.names[0]}"
            draw.rectangle([x1, y1, x2, y2], outline='red', width=2)
            # draw.text((x1, y1), label, fill='red', font=font)
        return np.array(image)
    
class dispx:
    def __init__(self, camera_id):
        self.camid = camera_id
        self.capture = cv2.VideoCapture
    def supercharge(self):
        if self.capture(self.camid).isOpened():
            pass
        
    
def main():
    cap = cv2.VideoCapture(camera_id)
    while cap.isOpened():
        success, frame = cap.read() #Read frames from cameraid or streaming protocols
        
        if frame is None:
            print("Attempting to reconnect to >Stream<! Errx0, missing frames!")
            cap.release()
            cap = cv2.VideoCapture(camera_id)
            continue
        
        annotated = inferencing(ready_model, frame).render()
        cv2.imshow("Dynamic Model Deployment Development Phase", annotated)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    



if __name__ == "__main__":
    main()
