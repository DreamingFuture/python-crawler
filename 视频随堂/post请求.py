# 作者     ：孔庆杨
# 创建时间 ：2019/1/23 11:43
# 文件     ：post请求.py
# IDE      ：PyCharm

'''
post请求（主要用于登录）就是给Request（url， date） 加个date
date是用户名加密码
然后需要用 urlencode（）转码
然后把原有式子变成 request =Request(url, date=date.encode（）,headers=headers)
注意：date=(字节)
'''