# AgoraSdkPkg
agora sdk包体计算：标准版本&特殊版本
## 1.前提条件
Android:Android studio 4.2 及以上、JDK11

IOS:Xcode 13.0 或以上版本

## 2.使用参考help
python3 apk_pkg_stat.py -h

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
