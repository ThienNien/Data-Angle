import csv
import os
import cv2
num_pic = 0 
data_path0 = r'C:\Users\tncup\Desktop\AI\car\Csv\class0'
data_path1 = r'C:\Users\tncup\Desktop\AI\car\Csv\class1'
data_path2 = r'C:\Users\tncup\Desktop\AI\car\Csv\class2'
data_path3 = r'C:\Users\tncup\Desktop\AI\car\Csv\class3'
data_path4 = r'C:\Users\tncup\Desktop\AI\car\Csv\class4'
data_path5 = r'C:\Users\tncup\Desktop\AI\car\Csv\class5'
data_path6 = r'C:\Users\tncup\Desktop\AI\car\Csv\class6'


def ReturnFolder(angle):
    if(angle >= -25.0 and angle <= -15.0):
        return data_path0 
    elif(angle >= -15.0 and angle <= -5.0):
        return data_path1
    elif(angle >= -5.0 and angle < 0.0):
        return data_path2
    elif(angle == 0.0):
        return data_path3
    elif(angle > 0.0 and angle <= 5.0):
        return data_path4
    elif(angle >= 5.0 and angle <= 15.0):
        return data_path5
    elif(angle >= 15.0 and angle <= 25.0):
        return data_path6

class_ID ={data_path0:0 , data_path1:1 , data_path2:2 , data_path3:3 , data_path4:4 , data_path5:5 , data_path6:6}
link_dir = r"C:\Users\tncup\Desktop\AI\car\Csv"
def CutImage(image,angle,classes = class_ID):
    global num_pic
    os.chdir(ReturnFolder(angle))
    cv2.imwrite(f'frame{num_pic}.jpg',image)
    print(num_pic)
    os.chdir(link_dir)
    with open('data_angle2.csv','a', newline='') as file:
        file_data = csv.writer(file)
        file_data.writerow([f'frame_{num_pic}.jpg',angle,classes[ReturnFolder(angle)]])
    num_pic += 1
    cv2.waitKey(30)