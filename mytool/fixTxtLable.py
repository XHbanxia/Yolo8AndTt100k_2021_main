import os
import shutil


# 用于清理没有标签的图片
if __name__ == '__main__':

    # 指定文件夹路径
    folder_path = "E:\\TranfficSign\\ObjectCheck\\tt100k_2021\\"
    lablelist = ["otherlable","testlable","trainlable"]
    # targetlist = ["otherimage","testimage","trainimage"]
    imglist = ["other","test","train"]
    dic = {"p":"0","w":"1","i":"2","0":"0","1":"1","2":"2"}

    # 获取文件夹中所有文件的文件名
    for num in range(3):
        namenum = 0

        file_names = [f[0:-4] for f in os.listdir(folder_path + imglist[num])]
        # file_names = ["testfile"]
        for fn in file_names:
            with open(folder_path+lablelist[num]+"\\"+fn+".txt") as f:
                data = f.readlines()
                # print(data)
            for line in range(len(data)):
                # print(len(data))
                # if data[line][0] == " ":
                #     break
                data[line] = dic[data[line][0:1]]+data[line][1:]
                # print(data[line][0],"===>",dic[data[line][0]])
            with open(folder_path+lablelist[num]+"\\"+fn+".txt","w") as f:
                f.writelines(data)
            # print(data)
            # break
            newname = "000000"+str(namenum)
            if len(newname)>7:
                newname = newname[-7:]
            # print(newname)
            oldtable = folder_path+lablelist[num]+"\\"+fn+".txt"
            newtable = folder_path+lablelist[num]+"\\"+newname+".txt"
            # print(oldtable,"===>",newtable)
            os.rename(oldtable, newtable)
            oldimg = folder_path + imglist[num] + "\\" + fn + ".jpg"
            newimg = folder_path + imglist[num] + "\\" + newname + ".jpg"
            os.rename(oldimg, newimg)
            # print(oldimg,"===>",newimg)
            namenum+=1
        # break