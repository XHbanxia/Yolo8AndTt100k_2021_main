from ultralytics import YOLO
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw,ImageFont
import cv2



if __name__=="__main__":
    modul=YOLO("E:\\TranfficSign\\ultralytics-main\\runs\\detect\\train16\\weights\\best.pt")

    # 图片文件夹路径
    image_folder = "E:\\TranfficSign\\ultralytics-main\\ultralytics\\cfg\\datasets\\images\\train\\"
    # image_folder = "E:\\TranfficSign\\ultralytics-main\\ultralytics\\cfg\\datasets\\images\\test\\"

    # txt文件夹路径
    txt_folder = "E:\\TranfficSign\\ultralytics-main\\ultralytics\\cfg\\datasets\\labels\\train\\"
    for i in range(0,20):
        fliename = str(i)
        fliename = "0000"+fliename
        if len(fliename)>5:
            fliename = fliename[-5:]
        # print(fliename)

        # 合成文件路径
        image_path = image_folder + fliename +".jpg"
        txt_path = txt_folder + fliename + ".txt"

        # results = modul.predict(source=image_path)
        results = modul.predict(source=image_path,show=False,save=True,save_dir=True)

        print(results[0].boxes.data)





        # print(image_path)
        # print(txt_path)

        # 读取图片
        # image = Image.open(image_path)

        # 读取txt文件
        # with open(txt_path, 'r') as file:
        #     for line in file:
        #         # 解析数据
        #         data = line.strip().split()
        #         print(data)
        #         integer_part = int(data[0])
        #         float_parts = list(map(float, data[1:]))
        #
        #         width, height = image.size
        #
        #         # 在图片上绘制方形
        #         draw = ImageDraw.Draw(image)
        #
        #         cenx, ceny = float_parts[0]*width,float_parts[1]*height
        #         sizex, sizey = float_parts[2]*width/2,float_parts[3]*height/2
        #         left , top, right, bottom= cenx-sizex,ceny-sizey,cenx+sizex,ceny+sizey
        #         draw.rectangle([int(left), int(top), int(right), int(bottom)], outline='red', width=2)
        #         font = ImageFont.truetype('arial.ttf', size=45)
        #         draw.text((left, top-10), str(integer_part), fill='blue',font=font)
        #
        # # 显示图片
        # plt.imshow(image)
        # plt.axis('off')  # 不显示坐标轴
        # plt.show()
