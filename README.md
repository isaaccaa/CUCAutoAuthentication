# CUCAutoAuthentication

## 思路来源

[nuanxinqing123/Srun_AutomaticAuthentication](https://github.com/nuanxinqing123/Srun_AutomaticAuthentication)

[ytf4425/Srun_login](https://github.com/ytf4425/Srun_login/)

## 用法

在 `login.py` 中的对应位置填写你的学号和密码, 如果你需要Bark推送服务, 就把链接替换成你的链接, 如果不需要就直接删除相关函数就行了...

然后用你喜欢的方式设置一个定时任务, 定时执行 `loginnet.sh` 脚本.

## 工作流程

* `loginnet.sh` 脚本会 ping 百度, 如果 ping 不通, 就调用python脚本去尝试做自动登录.
* python 会模拟游览器点击的方式登录校园网
