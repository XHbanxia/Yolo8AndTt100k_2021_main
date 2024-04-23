from ultralytics import YOLO

# 加载模型
model = YOLO(r"E:\TranfficSign\ultralytics-main\ultralytics\cfg\models\v8\my_yolov8n.yaml")  # 从头开始构建新模型
# model = YOLO("E:\\TranfficSign\\ultralytics-main\\yolov8n.pt")  # 加载预训练模型（建议用于训练）

if __name__=="__main__":
    # 训练模型
    # data是自己写的模型配置文件
    model.train(data="E:\\TranfficSign\\ultralytics-main\\ultralytics\\cfg\\datasets\\coco_trafficsig.yaml", epochs=50,batch=36)  # 训练模型
    metrics = model.val()  # 在验证集上评估模型性能
    results = model("E:\\TranfficSign\\ultralytics-main\\ultralytics\\cfg\\datasets\\images\\test\\18992.jpg")  # 对图像进行预测
    success = model.export(format="onnx")  # 将模型导出为 ONNX 格式