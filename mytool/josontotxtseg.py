import json
from PIL import Image
import os

# 用于提取json文件中的数据标签，并存到txt文件里
if __name__=="__main__":

    #  数据集中annotations_all.json的路径
    jsonpath = "E:\\TranfficSign\\ObjectCheck\\seg\\tt100k_2021\\annotations_all.json"
    # 数据集路径
    imgpath = "E:\\TranfficSign\\ObjectCheck\\seg\\tt100k_2021\\"

    # listdic = {"w":1,"p":2,"pg":2,"ps":2,"i":}
    marks = os.listdir(imgpath+"marks")
    marksname = []
    for mark in marks:
        marksname.append(mark[0:-4])
    mark_dict = {element: index for index, element in enumerate(marksname)}
    print(mark_dict)

    with open(jsonpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # print(data["types"])
    j = 0
    for imgnum in data["imgs"]:
        # print(data["imgs"][i])
        # 获取图片尺寸
        # print("open:",imgpath + data["imgs"][imgnum]["path"])
        try:
            with Image.open(imgpath + data["imgs"][imgnum]["path"]) as img:
                Xsize, Ysize = img.size
        except:
            print(imgpath + data["imgs"][imgnum]["path"],"is none")
            continue
        esaydic = {"w":1,"p":2,"i":3}
        # print(Xsize,Ysize)
        # 以图片名字命名txt文件
        txtname = data["imgs"][imgnum]["id"]
        # print(txtname)
        textcontent = []
        for obj in data["imgs"][imgnum]["objects"]:
            templist = []
            # 标志类型，这里我只取了第一个字符，需要完整的标志类型名字可以自己修改
            labelimg = obj["category"]
            # 归一化
            # 四个点的坐标
            xb = obj["bbox"]["xmax"]
            yb = obj["bbox"]["ymax"]
            xs = obj["bbox"]["xmin"]
            ys = obj["bbox"]["ymin"]
            xc = xs + (xb - xs) / 2
            yc = ys + (yb - ys) / 2
            y1 = yc - (yb - ys) / 4
            y2 = yc + (yb - ys) / 4
            x1 = xc - (xb - xs) / 4
            x2 = xc + (xb - xs) / 4

            xb = xb/Xsize
            xs = xs/Xsize
            xc = xc/Xsize
            x1 = x1/Xsize
            x2 = x2/Xsize

            yb = yb/Ysize
            ys = ys/Ysize
            yc = yc/Ysize
            y1 = y1/Ysize
            y2 = y2/Ysize

            if labelimg == "ip":
                pointlist = [esaydic[labelimg[0]],xs, ys,xb,ys,xb,yb,xs,yb]
            elif labelimg == "pg":
                pointlist = [esaydic[labelimg[0]],xs,ys,xb,ys,xc,yb]
            elif labelimg == "ps":
                pointlist = [esaydic[labelimg[0]],x1,ys,x2,ys,xb,y1,xb,y2,x2,yb,x1,yb,xs,y2,xs,y1]
            # elif labelimg[0:2] in["pa","pm","pl",""]

            elif labelimg[0] == 'p' or labelimg[0] == 'i':
                pointlist = [esaydic[labelimg[0]],xc,ys,x2,y1,xc,yb,x2,y2,xc,yb,x1,y2,xs,yc,x1,y1]
            elif labelimg[0] == "w":
                pointlist = [esaydic[labelimg[0]],xc,ys,xb,yb,xs,yb]
            else:
                print("error.........",txtname)

            # # 标志根据类型计算其他的点
            # # print(pointlist)
            #
            #
            # witX = (obj["bbox"]["xmax"] - obj["bbox"]["xmin"])
            # witY = (obj["bbox"]["ymax"] - obj["bbox"]["ymin"])
            #
            # cenX = obj["bbox"]["xmin"]+witX/2
            # cenY = obj["bbox"]["ymin"]+witY/2
            #
            # templist.append(labelimg)
            #
            # templist.append(cenX)
            # templist.append(cenY)
            # templist.append(witX)
            # templist.append(witY)
            textcontent.append(pointlist)
            # break
            # print(templist)
        print(textcontent)
        # print(data["imgs"][imgnum]["path"].split("/")[0])

        # 确保文件夹存在【testlable，ortherlable，trainlable】
        os.makedirs(imgpath+data["imgs"][imgnum]["path"].split("/")[0]+"seglable", exist_ok=True)
        print(imgpath+data["imgs"][imgnum]["path"].split("/")[0]+"seglable")
        # 写入并保存txt文件
        with open(imgpath+data["imgs"][imgnum]["path"].split("/")[0]+"seglable\\"+f"{txtname}.txt", 'w', encoding='utf-8') as f:
            for row in textcontent:
                f.write(' '.join(map(str, row)) + '\n')


