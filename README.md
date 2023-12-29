# AgoraSdk计算包体工具
agora sdk包体计算：标准版本&特殊版本
## 1.前提条件
Android:Android studio 4.2 及以上、JDK11

IOS:Xcode 13.0及以上版本、Cocoapods（参考：https://guides.cocoapods.org/using/getting-started.html#getting-started）

## 2.使用参考help
python3 apk_pkg_stat.py -h

<img width="716" alt="image" src="https://github.com/chowen-zz/agorartc-pkg-size/assets/6028309/fea7cc92-6983-4e8d-8e85-8389a558fb5e">


## 3.脚本示例
#### 一.两版本对比：
python3 apk_pkg_stat.py 版本号1 版本号2 包类型[full/fullbasic/voicebasic/voicefull]
  
   例如：python3 apk_pkg_stat.py  4.2.0  4.2.3  full/fullbasic/voicebasic/voicefull
#### 二.单独版本：
python3 apk_pkg_stat.py 版本号 包类型[full/fullbasic/voicebasic/voicefull]
   
   例如：python3 apk_pkg_stat.py 4.2.0 full/fullbasic/voicebasic/voicefull
#### 三.特殊版本：
python3 apk_pkg_stat.py 版本号 包类型[specialfull/specialvoice]
  
   例如：python3 apk_pkg_stat.py 4.1.1.19 specialfull/specialvoice
