# cnmoderndata
本项目为中国式现代化可视化设计的数据处理项目
Python版本号为3.11
在项目路径下输入以下命令即可安装所有依赖
` pip install -r requirements.txt `
# 项目结构
- pulic: 存放数据以及结果
- src: 存放源代码
- requirements.txt: 项目依赖
- README.md: 项目说明
# 项目运行
打开src文件夹
按照文件夹的名称顺序依次执行即可
结果统一输出到public/data/result文件夹下，其中output文件夹为存储到数据库的文件
/source文件夹为原始的数据文件

# 源码说明
关于/src下的文件夹的功能，依次为以下操作
-01 原始数据的审查与合并
-02 数据的清洗与处理
-03 数据得分的计算
-04 数据得分百分制转化
-05 区域得分数据的计算
-06 数据字典的转化
-07 数据输出到MySql数据库