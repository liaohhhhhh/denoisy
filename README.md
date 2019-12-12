# 超声去噪
### 文件解析
#### 主模块
* 主模块包括`main.py`和`evaluation.py`，其余文件均为子模块
* `main.py`用于超声图像去噪并输出结果，`evaluation.py`用于生成对应的**PSNR**与**SSIM**测量标准
#### 子模块
* `loaddata.py`是一个自定义的数据库类型，用于读取噪声图片及输出结果
* `Detect.py`用于寻找超声图片中的人工标记，其返回的结果是一个对人工标记的mask，大小与图像本身一致
* `Method.py`含有去除人工标记所使用的插值算法，及各类在测试时用到的平滑滤波函数
* `PSNR.py`与`SSIM.py`为**PSNR**与**SSIM**的评估算法实现

### 编译环境
* 编译语言使用`Python 3.7.4`
* 编译环境已用Python写好`requirement.txt`,使用方法为：在`requirement.txt`的文件目录下输入命令行
```pip install -r requirements.txt```
    
 
### 代码运行
### main.py
* 执行`main.py`,要求输入输入文件夹与输出文件夹的名称
#### Input
    --input_dir: train_noise
    --output_dir: train_result
* 输出为正在处理后的文件名
#### Output
    BR 176 YUAN XIA F39Y_20160113_133403_image.jpg
    BRE HU YUQING F 74_20180608_104646_image.jpg
    BRE XU MINWEN F 62_20180604_153248_image.jpg
    ……

### evaluation.py
* 执行`evaluation.py`,要求输入目标文件夹与`main.py`中输出文件夹的名称
#### Input
    --target_dir: train_origin
    --output_dir: train_result
* 输出为正在处理后的文件名以及其**PSNR**与**SSIM**值，且将结果保存在与`.py`同目录下的`result.xls`中
#### Output
    NAME: BR 176 YUAN XIA F39Y_20160113_133403_image.jpg
    PSNR: 45.66860261509194
    SSIM: 0.9971477421850732
    NAME: BRE HU YUQING F 74_20180608_104646_image.jpg
    PSNR: 42.60963954842132
    SSIM: 0.9924067270353069
    ……
