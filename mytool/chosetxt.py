import os
import shutil


# 用于清理没有标签的图片
if __name__ == '__main__':

    # 指定文件夹路径
    folder_path = "E:\\TranfficSign\\ObjectCheck\\tt100k_2021\\"
    namelist = ["otherlable","testlable","trainlable"]
    targetlist = ["otherimage","testimage","trainimage"]
    sorlist = ["other","test","train"]

    # 获取文件夹中所有文件的文件名
    for num in range(3):
        print(folder_path+namelist[num])
        file_names = [f[0:-4] for f in os.listdir(folder_path+namelist[num])]
        os.makedirs(folder_path+targetlist[num], exist_ok=True)
        sumnum = 0
        for file_name in os.listdir(folder_path+sorlist[num]):
            fname = file_name
            # print(sorted(file_name))
            # 如果文件不在列表中，则移动
            if fname[0:-4] not in file_names:
                print(fname[0:-4])
                source_path = os.path.join(folder_path+sorlist[num], fname)
                target_path = os.path.join(folder_path+targetlist[num], fname)
                print(source_path,target_path)
                sumnum += 1
                # 移动文件
                shutil.move(source_path, target_path)

        # 打印文件名列表
        print(sumnum)
        print(file_names)
        # break