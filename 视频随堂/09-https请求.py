# 作者     ：孔庆杨
# 创建时间 ：2019/1/23 14:02
# 文件     ：09-https请求.py
# IDE      ：PyCharm

# 证书问题
# 不验证证书
import ssl
contex = ssl._create_unverified_context()
# 放在urlopen里