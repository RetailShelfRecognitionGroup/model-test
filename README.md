# model-test
some py and sh files to implement more features

## 主要功能
* 计算每一类AUC，默认AUC<0.0001不予加入平均AUC
* 计算平均AUC
* 计算每一类最佳阈值下Recall和Precision，可在pascal_voc.py文件313行处更改阈值计算精度，默认值为0.01
* 计算每类最佳阈值下的平均Recall和Precision
* 修复easy-pva的bug，可实现一键精度测试

## 使用方式
* git clone 该项目，覆盖easy-pva项目文件
* 在easy-pva根目录下，使用 `./tools/test_demo.sh` 命令即可
* 测试模型只需更改data路径和最后一行python --weights 参数
