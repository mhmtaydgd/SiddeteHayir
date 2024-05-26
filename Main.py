import cv2 
import mediapipe 

camera = cv2.VideoCapture(0)

mpHands = mediapipe.solutions.hands

hands = mpHands.Hands()

mpDraw = mediapipe.solutions.drawing_utils

while True :
    success, img = camera.read()
    
    img = cv2.flip(img, 1)
    
    imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    hlms = hands.process(imgRBG)
    
    height, width, channel = img.shape
    
    if hlms.multi_hand_landmarks:
        
        for handlandmarks in hlms.multi_hand_landmarks:
            
            for fingerNum, landmark in enumerate(handlandmarks.landmark):
                
                # x ve y noktalarının koordinatlarını belirtmemizi sağlıyor.
                positionX, positionY = int(landmark.x * width), int(landmark.y * height)
                
                #parmakların üstündeki numaraları ekranda parmakların üstünde gösteriyor.
                print(fingerNum,landmark)
                
                #parmakların x ve y koordinatlarını yazdırıyor
                cv2.putText(img, str(fingerNum), (positionX, positionY), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                
                #cond şağ elde baş parmağın içerde olması durumunu simgeliyor.
                cond = handlandmarks.landmark[5].x < handlandmarks.landmark[4].x and handlandmarks.landmark[4].x < handlandmarks.landmark[17].x 
                #cond2 baş parmak harici parmakların yumruk şeklinde kapanması durumunu simgeliyor.
                cond2 = handlandmarks.landmark[8].y > handlandmarks.landmark[3].y and handlandmarks.landmark[12].y > handlandmarks.landmark[3].y and handlandmarks.landmark[16].y > handlandmarks.landmark[3].y and handlandmarks.landmark[20].y > handlandmarks.landmark[3].y and handlandmarks.landmark[8].y < handlandmarks.landmark[0].y and handlandmarks.landmark[12].y < handlandmarks.landmark[0].y and handlandmarks.landmark[16].y < handlandmarks.landmark[0].y and handlandmarks.landmark[20].y < handlandmarks.landmark[0].y
                #cond3 sol elde baş parmağın içerde olması durumunu simgeliyor.
                cond3 = handlandmarks.landmark[5].x > handlandmarks.landmark[4].x and handlandmarks.landmark[4].x > handlandmarks.landmark[17].x
                
                #sol el için yapılan if yapısı
                if cond :
                        
                        if cond2 : 
                            print("The Police is being Called() !")
                #sağ el için yapılan if yapısı       
                elif  cond3 :  
                        if cond2 :
                           print("The Police is being Called() !")
            
            #ellerin üstündeki parmaklara nokta çizer   
            mpDraw.draw_landmarks(img, handlandmarks, mpHands.HAND_CONNECTIONS)
    
    #kameradan 1 milisaniyede görüntü almamızı sağlıyor // q tuşu ile kapanmamızı sağlıyor
    cv2.imshow("camera", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
