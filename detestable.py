import os
import numpy as np
from ultralytics import YOLO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class inferencing:
    def __init__(self, model, frame):
        self.model = model # get model from the model directory #Task ran successfully
        self.frame = frame # get frame from the feed #Task ran successfully
        self.bbx = None # bounding box #Task ran successfully
    def infer(self):
        model = YOLO(self.model) # load the model #Task ran successfully
        for result in model.predict(self.frame, conf=0.74): #Task ran successfully
            self.bbx = result #Task ran successfully
    def render(self):
        __class__.infer(self) #Task ran successfully
        return renderbbx(self.frame, self.bbx).render() #Task ran successfully
    def hrec(self):
        return self.bbx # return the bounding box

@staticmethod 
class renderbbx:
    def __init__(self, frame, bbx):
        self.frame = frame #Task ran successfully
        self.bbx = bbx #Task ran successfully
    def render(self):
        image = Image.fromarray(self.frame) #Task ran successfully
        draw = ImageDraw.Draw(image) #Task ran successfully
        font = ImageFont.load_default() #Task ran successfully
        for box in self.bbx.boxes: #Task ran successfully
            x1, y1, x2, y2 = map(int, box.xyxy[0]) #Task ran successfully
            # label = f"{box.names[0]}" 
            draw.rectangle([x1, y1, x2, y2], outline='red', width=3) #Task ran successfully
            # draw.text((x1, y1), label, fill='red', font=font)
        return np.array(image) #Task ran successfully

class live_components:
    def __init__(self):
        pass # Placeholder for future development

class model_switcher:
    def __init__(self):
        pass # Placeholder 

class model_trainer:
    def __init__(self):
        pass # Placeholder

class clsout:
    def __init__(self):
        pass # Placeholder

class window_takeover:
    def __init__(self):
        pass # Placeholder

class dispx:
    def __init__(self, Frame_Width, Frame_Height, id):
        print("Initializing base display-x! - Base code by BabyWaffles!")
        from cv2 import VideoCapture, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH
        from cv2_enumerate_cameras import enumerate_cameras
        self.cameraid = id #Task ran successfully
        self.FW = Frame_Width #Task ran successfully
        self.FH = Frame_Height #Task ran successfully
        self.enumerater = enumerate_cameras #Task ran successfully
        self.capture = VideoCapture #Task ran successfully
        self.PROP_FRAME_HEIGHT = CAP_PROP_FRAME_HEIGHT #Task ran successfully
        self.PROP_FRAME_WIDTH = CAP_PROP_FRAME_WIDTH #Task ran successfully
        self.valcams = None #Task ran successfully
    def getcam(self):
        if self.valcams is None: #Task ran successfully
            self.valcams = self.enumerater() #Task ran successfully
            return self.valcams #Task ran successfully
        if self.enumerater() is None: #Task ran successfully
            print("No Camera found! Exiting system...") #Task ran successfully
            exit(0) #Task ran successfully
    def setcam(self):
        if self.cameraid is None and self.valcams != None: #Task ran successfully
            print(f"Detected valid cameras! {self.valcams}") #Task ran successfully
            self.cameraid = int(input("Select your camera [Based on index!]: ")) #Task ran successfully
        else:
            print("Validated cameras not initialized...") #Task ran successfully
            __class__.getcam(self) #Task ran successfully
        self.capture = self.capture(self.cameraid) #Task ran successfully
        self.capture.set(self.PROP_FRAME_HEIGHT, self.FH) #Task ran successfully
        self.capture.set(self.PROP_FRAME_WIDTH, self.FW) #Task ran successfully
        return
    def build(self):
        return self.capture #Task ran successfully
    def supercharge(self):
        if self.valcams == None or self.cameraid == None: #Task ran successfully
            __class__.getcam(self) #Task ran successfully
            __class__.setcam(self) #Task ran successfully
            return self.capture #Task ran successfully
        else:
            print("Manual initialization detected! Automatically compiling request...") #Task ran successfully
            __class__.build(self) #Task ran successfully
        
class run: # Class failed to execute due to multiprocessing pickle not working properly with the multi-data multi-instruction model. -> Require to default back to manual execution [Validated by WafflesLab, result - Failed to execute.]
    def __init__(self, res_h, res_w, ready_model):
        from time import sleep #Task ran successfully
        from cv2 import imshow, waitKey,destroyAllWindows #Task ran successfully
        self.sleep = sleep #Task ran successfully
        self.imshow = imshow #Task ran successfully
        self.waitkey = waitKey #Task ran successfully
        self.r_h = res_h #Task ran successfully
        self.r_w = res_w #Task ran successfully
        self.model = ready_model #Task ran successfully
        self.camid = [] # Deprecated / placeholder for future development #Task ran successfully
        self.processes = [] #Task ran successfully
        self.displaysets = None #Task ran successfully
        self.display = [None] #Task ran successfully
        self.distroyAllWindows = destroyAllWindows #Task ran successfully
    def instantiate(self): #Task ran successfully
        self.displaysets = int(input("Input inferencing camera amount: ")) #Task ran successfully
        self.display = [None] * self.displaysets #Task ran successfully
        __class__.multi_func_init(self) #Task ran successfully
    def multi_func_init(self): #Task ran successfully
        for index in range(len(self.display)): #Task ran successfully
            self.display[index] = dispx(self.r_w, self.r_h, None).supercharge() #Task ran successfully
            print("Displayed successfully compiled and initialized!") #Task ran successfully
        print("Awaiting for execution by function...") #Task ran successfully
        self.sleep(0.1) #Task ran successfully
    def inference_worker(self, instruction): #Task failed to execute()
        instruct = None #Task ran successfully
        try:  #Task failed to execute()
            exec(instruction, {}, locals())  #Task failed to execute()
            if instruct is None:  #Task failed to execute()
                print("Camera could not be opened.")  #Task failed to execute()
        except Exception as e:  #Task failed to execute()
            print(f"Error executing instruction: {e}")  #Task failed to execute()
        while instruct.isOpened():  #Task failed to execute()
            success, frame = instruct.read()  #Task failed to execute()
            annotated = inferencing(self.model, frame).render()  #Task failed to execute()
            self.imshow("Dynamic Model Deployment Development Phase!", annotated)  #Task failed to execute()
            if self.waitkey(1) ** 0xFF ==ord("q"):  #Task failed to execute()
                __class__.terminate(self)  #Task failed to execute()
    def taskmgmt_unwrapper(self): #Task ran successfully
        from multiprocessing import Process #Task ran successfully
        for index in range(len(self.display)): #Task ran successfully
            instruction = self.display[index] #Task ran successfully
            p = Process(target=self.inference_worker, args=(instruction,))  #Task failed to execute()
            self.processes.append(p) #Task failed to execute()
            p.start() #Task failed to execute()
        for p in self.processes: #Task failed to execute()
            p.join() #Task failed to execute()
    def execute(self):  #Task ran successfully
        __class__.instantiate(self)  #Task ran successfully
        __class__.taskmgmt_unwrapper(self)  #Task failed to execute()
    def terminate(self):  #Task ran successfully
        self.distroyAllWindows()  #Task ran successfully
        return  #Task returned successfully
        
# ffmpeg_bin = work_DIR + "\\bin\\ffmpeg.exe"
# asset = work_DIR + "\\assets\\"
# trainer_model_dir = work_DIR + "\\models\\YOLO\\"
        
def main():
    from time import sleep
    from cv2 import imshow, waitKey,destroyAllWindows
    namespace = "best.pt"
    print("Using default namespace: "+namespace)
    work_DIR = os.getcwd()
    ready_model = work_DIR + "\\models\\pre-trained\\huamn-detection-v8n\\"+namespace

    displayx = dispx(1280, 720, None)
    display = displayx.supercharge()
    print("Loading model, please wait...")
    while display.isOpened():
        successful, frame = display.read()
        if not successful:
            print("Attempting to reconenct to camera, please wait...")
            display.release()
            sleep(0.5)
            display = display
            continue
        annotate = inferencing(ready_model, frame).render()
        imshow("Dynamic Model Deployment Development Phase!", annotate)
        if waitKey(1) & 0xFF ==ord("q"):
            display.release()
            return
    print("Successfully exited inferencing...")

    # run_define(display, ready_model).run()
    # run(1280, 720, ready_model).execute()

if __name__ == "__main__":
    main()
    

# class run_define:
#     def __init__(self, video_lib, ready_model):
#         from time import sleep
#         from cv2 import imshow, waitKey
#         self.sleep = sleep
#         self.imshow = imshow
#         self.waitkey = waitKey
#         self.videoLib = video_lib
#         self.ready_model = ready_model
#     def run(self):
#         self.videoLib.supercharge()
#         print("Loading model, please wait!")
#         while self.videoLib.isOpened():
#             successful, frame = self.videoLib.read()
#             if not successful:
#                 print("Camera has been disconnected! Attemting to reconnect, please wait...")
#                 self.videoLib.release()
#                 self.sleep(2)
#                 self.videoLib = self.videoLib
#                 continue
#             annotated  = inferencing(self.ready_model, frame).render()
#             self.imshow("Dynamic Model Deployment Development Phase!", annotated)
#             if self.waitkey(1) & 0xFF == ord("q"):
#                 __class__.terminator(self)
#     def terminator(self):
#         self.videoLib.release()
#         return

# class dispx_pyocv: #Deprecated
#     def __init__(self, F_Width, F_Height, cam_id):
#         print("Initializing base display-x! - Base code by BabyWaffles!")
#         from cv2 import VideoCapture
#         self.camid = cam_id
#         self.validCameras = None
#         self.F_Width = F_Width
#         self.F_Height = F_Height
#         self.capture = VideoCapture
#     def supercharge(self):
#         from time import sleep
#         __class__.get_Cam(self)
#         __class__.set_cam(self)
#         if self.capture.isOpened() is None and self.camid is not None:
#             print("Err.x01! Missing frames, attempting to reconnect to stream!")
#             sleep(5)
#             self.capture.release()
#             __class__.supercharge(self)
#         self.capture.isOpened()
#         return self.capture.read()
#     def set_cam(self):
#         from cv2 import CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH
#         if self.camid is None:
#             print(f"Detected cameras! {self.validCameras}")
#             self.camid = int(input("Please select your camera [Based on index!]: "))
#         self.capture = self.capture(self.camid)
#         self.capture.set(CAP_PROP_FRAME_WIDTH, self.F_Width)
#         self.capture.set(CAP_PROP_FRAME_HEIGHT, self.F_Height)
#     def get_Cam(self):
#         from cv2_enumerate_cameras import enumerate_cameras
#         if self.validCameras is None:
#             self.validCameras = enumerate_cameras()
