import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


if __name__=="__main__":
    image_folder = "E:\\TranfficSign\\ultralytics-main\\ultralytics\\cfg\\datasets\\images\\train"

    # 读取图片
    image_path = image_folder + '\\00000.jpg'  # 请替换为实际图片文件名
    image = Image.open(image_path)