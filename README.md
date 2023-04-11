# deeplabv3plus_re
semantic segmentation on ros  
## 0410:  
1. 学习CityScapes数据集的使用；  
2. 尝试将Citycapes中的图片以ROS格式发布；  
## 0411：  
1. 将Cityscapes数据集下载好后，使用官方的scripts脚本进行处理，之后整理好train和val文件夹；  
2. 组织了半天Cityscapes数据集的文件夹，，，应该将下载好的数据集，解压之后，从文件夹里把子文件夹取出来。  
![](https://github.com/XxxuLimei/deeplabv3plus_re/blob/main/pictures/WeChat%20Image_20230411185142.png)  
3. 下载resnet101的权重文件，注意下载好的.pth.tar无需解压，提示解压错误后就说明这本身就是一个权重文件，可以直接使用。  
4. 运行main.py脚本`python main.py --model deeplabv3plus_resnet101 --gpu_id 0 --lr 0.1 --crop_size 768 --batch_size 16 --output_stride 16 --ckpt ./result/best_deeplabv3plus_resnet101_cityscapes_os16.pth.tar --test_only --save_val_results --data_root /home/xilm/Cityscapes/ --dataset cityscapes`  
```
Device: cuda
Dataset: cityscapes, Train set: 2975, Val set: 500
Downloading: "https://download.pytorch.org/models/resnet101-5d3b4d8f.pth" to /home/xilm/.cache/torch/hub/checkpoints/resnet101-5d3b4d8f.pth
100%|████████████████████████████████████████████████████████████████████| 170M/170M [01:07<00:00, 2.64MB/s]
Model restored from ./result/best_deeplabv3plus_resnet101_cityscapes_os16.pth.tar
125it [12:46,  6.13s/it]

Overall Acc: 0.958689
Mean Acc: 0.837516
FreqW Acc: 0.923537
Mean IoU: 0.762100
```  
运行之后，获得了许多分割结果，这些结果都保存在`./results`文件夹下。  
![](https://github.com/XxxuLimei/deeplabv3plus_re/blob/main/pictures/7_image.png)  
![](https://github.com/XxxuLimei/deeplabv3plus_re/blob/main/pictures/7_overlay.png)  
![](https://github.com/XxxuLimei/deeplabv3plus_re/blob/main/pictures/7_pred.png)  
![](https://github.com/XxxuLimei/deeplabv3plus_re/blob/main/pictures/7_target.png)  
5. 运行`predict.py`脚本：`python predict.py --model deeplabv3plus_resnet101 --gpu_id 0 --crop_size 768 --output_stride 16 --ckpt ./result/best_deeplabv3plus_resnet101_cityscapes_os16.pth.tar --save_val_results_to ./result/ --dataset cityscapes --input /home/xilm/Cityscapes/leftImg8bit/test/berlin/berlin_000001_000019_leftImg8bit.png`  
```
(base) xilm@xilm-MS-7D17:~/fuxian/deeplabv3plus/DeepLabV3Plus-Pytorch-master$ python predict.py --model deeplabv3plus_resnet101 --gpu_id 0 --crop_size 768 --output_stride 16 --ckpt ./result/best_deeplabv3plus_resnet101_cityscapes_os16.pth.tar --save_val_results_to ./result/ --dataset cityscapes --input /home/xilm/Cityscapes/leftImg8bit/test/berlin/berlin_000001_000019_leftImg8bit.png
Device: cuda
Resume model from ./result/best_deeplabv3plus_resnet101_cityscapes_os16.pth.tar
100%|█████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.12it/s]
```  
运行结束后获得了分割结果。  
![](https://github.com/XxxuLimei/deeplabv3plus_re/blob/main/pictures/berlin_000001_000019_leftImg8bit.png)  
![](https://github.com/XxxuLimei/deeplabv3plus_re/blob/main/pictures/berlin_000001_000019_leftImg8bit_predict.png)  
