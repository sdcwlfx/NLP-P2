# NLP-P2
基于1998人民日报语料库利用CRF++实现汉语命名实体自动识别程序

# 目录介绍
  1. corpusHandler.py文件读取人民日报语料库train2.txt文本，抽取20%作为测试集保存到test.txt，剩余80%作为训练集保存到train.txt中, 并对每个字使用          (B/M/E/S/W/O)其中之一进行标注.
  2. F1.py文件计算训练后的模型在测试集的正确率、召回率、F
  3. NER.py由于CRF++对应python接口安装出现版本问题，未能成功
  
# 步骤
  1. 运行corpusHandler.py文件，生成test.txt与train.txt文件
  2. 设计特征模版template文件
  3. 利用crf++对训练集train.txt训练得到模型model：crf_learn -f 4 -p 8 -c 3 template ./train.txt model
  4. 利用crf++利用模型model对测试集test.txt进行预测得到test.rst：crf_test -m model ./test.txt > ./test.rst，
      text.rst文件中包含三列数据，第一列是字，第二列是标签，第三列是模型model对第一列字做出的预测，利用test.rst文件即可得出正确率、召回率及F

