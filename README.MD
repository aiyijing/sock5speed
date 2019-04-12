# 简单Sock5 代理测试工具
### 依赖
python3.5 requests pysocks
* 安装依赖
```shell
pip install -r deployment.text
```
### 使用
python Speed.py --args
* 参数详解
--proxy=127.0.0.1:1080  (代理服务器)  
--url=http://www.baidu.com  (访问网址)  
--time=5 (每次间隔)
--verb  (显示下载内容)  
--loop  (是否循环)  
--help  (帮助)  
* example  
python Speed.py --proxy=127.0.0.1:1080 --url=http://www.baidu.com --loop --time=3  
