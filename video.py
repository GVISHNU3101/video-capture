import cv2
import time

#for video names
i =0

#video length in sec
capture_time = 3
#video intervals in sec
delay_time = 10
while True:

    cam = cv2.VideoCapture(0)

    frame_width = int(cam.get(3))
    frame_height = int(cam.get(4))
    size = (frame_width, frame_height)

    video = cv2.VideoWriter(str(i)+'.avi',cv2.VideoWriter_fourcc(*'MJPG'),10,size)

    start_time = time.time()

    while (int(time.time() - start_time) < capture_time):
        ret, frame = cam.read()
    
        if ret == True:
            video.write(frame)
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    cam.release()
    video.release()
    cv2.destroyAllWindows()

    start_time=time.time()

    while (int(time.time()-start_time)<delay_time):
        try:
            raise KeyboardInterrupt
        except KeyboardInterrupt:
            break
    i=i+1
    
    
