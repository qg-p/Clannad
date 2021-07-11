# 基于docker1镜像
FROM docker2
 
# 工作目录
WORKDIR /code
 
# 拷贝py文件和requirements.txt文件
ADD . /code
# 也可使用以下两句实现
#COPY test.py /code/
#COPY requirements.txt /code/
 
# 更新pip
#RUN pip install --upgrade pip --index-url https://pypi.douban.com/simple
 
# pip安装依赖包
#RUN pip install -r requirements.txt
 
# 执行python文件
CMD ["docker2","app.py"]