import json
from PIL import Image
import os

# 用于提取json文件中的数据标签，并存到txt文件里
if __name__=="__main__":

    #  数据集中annotations_all.json的路径
    jsonpath = "E:\\TranfficSign\\ObjectCheck\\tt100k_2021\\annotations_all.json"
    # 数据集路径
    imgpath = "E:\\TranfficSign\\ObjectCheck\\tt100k_2021\\"

    with open(jsonpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # print(data["types"])

    j = 0
    for imgnum in data["imgs"]:
        # print(data["imgs"][i])
        # 获取图片尺寸
        with Image.open(imgpath + data["imgs"][imgnum]["path"]) as img:
            Xsize, Ysize = img.size

        # 以图片名字命名txt文件
        txtname = data["imgs"][imgnum]["id"]
        # print(txtname)
        textcontent = []
        for obj in data["imgs"][imgnum]["objects"]:
            templist = []
            # 标志类型，这里我只取了第一个字符，需要完整的标志类型名字可以自己修改
            labelimg = obj["category"][0:1]
            # 归一化
            # 四个点的坐标
            pointlist = [[obj["bbox"]["xmin"],obj["bbox"]["ymin"]],
                         [obj["bbox"]["xmin"], obj["bbox"]["ymax"]],
                         [obj["bbox"]["xmax"], obj["bbox"]["ymin"]],
                         [obj["bbox"]["xmax"], obj["bbox"]["ymax"]]]
            # 标志根据类型计算其他的点
            print(pointlist)


            witX = (obj["bbox"]["xmax"] - obj["bbox"]["xmin"])
            witY = (obj["bbox"]["ymax"] - obj["bbox"]["ymin"])

            cenX = obj["bbox"]["xmin"]+witX/2
            cenY = obj["bbox"]["ymin"]+witY/2

            templist.append(labelimg)

            templist.append(cenX/Xsize)
            templist.append(cenY/Ysize)
            templist.append(witX/Xsize)
            templist.append(witY/Ysize)
            textcontent.append(templist)
            break
            # print(templist)
        # print(textcontent)
        # print(data["imgs"][imgnum]["path"].split("/")[0])

        # 确保文件夹存在【testlable，ortherlable，trainlable】
        os.makedirs(imgpath+data["imgs"][imgnum]["path"].split("/")[0]+"lable", exist_ok=True)

        # 写入并保存txt文件
        with open(imgpath+data["imgs"][imgnum]["path"].split("/")[0]+"lable\\"+f"{txtname}.txt", 'w', encoding='utf-8') as f:
            for row in textcontent:
                f.write(' '.join(map(str, row)) + '\n')
        #
        # j += 1
        # if j > 5:
        #     break
        break
