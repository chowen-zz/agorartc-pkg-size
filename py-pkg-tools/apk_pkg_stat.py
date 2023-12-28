# !/usr/bin python3
# encoding    : utf-8 -*-
# @author     :   zhouwen
# @Time       :   2023/12/19 下午11:09

import time
import os
import sys
import datetime

base_path = os.path.dirname(__file__)
root_path = os.path.dirname(os.path.abspath(base_path))
sys.path.append(os.path.abspath(base_path))
sys.path.append(root_path)

def modify_sdk_version(sdk_version):
    global sdk_path
    gradle_file_path = f'{os.path.abspath(root_path)}/android/app/build.gradle'
    print(f'gradle_file_path={gradle_file_path}')
    gradle_file = open(gradle_file_path, 'r+')
    gradle_file_content = gradle_file.read()

    if 'full-sdk:' in gradle_file_content:
        print('current sdk version:io.agora.rtc:full-sdk:'+sdk_version+'')
        sdk_path = f'io.agora.rtc:full-sdk:{sdk_version}' 
        gradle_file_content = gradle_file_content.replace('full-sdk:', 'full-sdk:%s' % sdk_version)
        gradle_file.seek(0)
        gradle_file.write(gradle_file_content)
        gradle_file.close()
    elif 'full-rtc-basic:' in gradle_file_content:
        print('current sdk version:io.agora.rtc:full-rtc-basic:'+sdk_version+'')
        sdk_path = f'io.agora.rtc:full-rtc-basic:{sdk_version}'
        gradle_file_content = gradle_file_content.replace('full-rtc-basic:', 'full-rtc-basic:%s' % sdk_version)
        gradle_file.seek(0)
        gradle_file.write(gradle_file_content)
        gradle_file.close()
    elif 'voice-sdk:' in gradle_file_content:
        print('current sdk version:io.agora.rtc:voice-sdk:'+sdk_version+'')
        sdk_path = f'io.agora.rtc:voice-sdk:{sdk_version}'
        gradle_file_content = gradle_file_content.replace('voice-sdk:', 'voice-sdk:%s' % sdk_version)
        gradle_file.seek(0)
        gradle_file.write(gradle_file_content)
        gradle_file.close()
    elif 'voice-rtc-basic:' in gradle_file_content:
        print('current sdk version:io.agora.rtc:voice-rtc-basic:'+sdk_version+'')
        sdk_path = f'io.agora.rtc:voice-rtc-basic:{sdk_version}' 
        gradle_file_content = gradle_file_content.replace('voice-rtc-basic:', 'voice-rtc-basic:%s' % sdk_version)
        # print(f'chowen gradle_file_content: %s'% gradle_file_content)
        gradle_file.seek(0)
        gradle_file.write(gradle_file_content)
        gradle_file.close()
    elif 'agora-special-full:' in gradle_file_content:
        print('current sdk version:io.agora.rtc:agora-special-full:'+sdk_version+'')
        sdk_path = f'io.agora.rtc:agora-special-full:{sdk_version}' 
        gradle_file_content = gradle_file_content.replace('agora-special-full:', 'agora-special-full:%s' % sdk_version)
        # print(f'chowen gradle_file_content: %s'% gradle_file_content)
        gradle_file.seek(0)
        gradle_file.write(gradle_file_content)
        gradle_file.close()

    elif 'agora-special-voice:' in gradle_file_content:
        print('current sdk version:io.agora.rtc:agora-special-voice:'+sdk_version+'')
        sdk_path = f'io.agora.rtc:agora-special-voice:{sdk_version}' 
        gradle_file_content = gradle_file_content.replace('agora-special-voice:', 'agora-special-voice:%s' % sdk_version)
        # print(f'chowen gradle_file_content: %s'% gradle_file_content)
        gradle_file.seek(0)
        gradle_file.write(gradle_file_content)
        gradle_file.close()

    else:
        print('moudle type error! pls check it. --> python3 apk_pkg_stat.py -h')

def revert_gradle_content(origin_gradle_path, copy_gradle_path):
    with open(origin_gradle_path, 'w+', encoding='utf-8') as gradle_file, open(copy_gradle_path, 'r+', encoding='utf-8') as gradle_file_copy:
        replace_gradle = gradle_file_copy.read()
        # print(f'replace_gradle:{replace_gradle}')
        gradle_file.seek(0)
        gradle_file.write(replace_gradle)

def computer_aar_so_size(file_type, sdk_version):
    print('-' * 45)
    print(f'Execute Build assembleRelease--agorartc version:{sdk_version}')
    os.system(
        f'cd {os.path.abspath(root_path)}/android && {os.path.abspath(root_path)}/android/gradlew clean && {os.path.abspath(root_path)}/android/gradlew assembleRelease')

    print('\033[32m')
    # print('空工程 1.4M')
    date_now = datetime.datetime.now()
    print('-----agorartc calculate-----\n DataTime %s' % date_now)
    print('sdk_path:%s' % sdk_path)
    time.sleep(4)

    if file_type == 'so':
        v8_apk_size = os.path.getsize(
            f'{os.path.abspath(root_path)}/android/app/build/outputs/apk/release/app-arm64-v8a-release-unsigned.apk')
        v7_apk_size = os.path.getsize(
            f'{os.path.abspath(root_path)}/android/app/build/outputs/apk/release/app-armeabi-v7a-release-unsigned.apk')

        apk_v8_str = f'apk_v8_size:{v8_apk_size}--agorartc_so_v8_size:{round((v8_apk_size - origin_apk_size) / 1000.0 / 1000.0, 2)}M'
        apk_v7_str = f'apk_v7_size:{v7_apk_size}--agorartc_so_v7_size:{round((v7_apk_size - origin_apk_size) / 1000.0 / 1000.0 , 2)}M'
        # apk_v8_str = f'apk_v8_size:{v8_apk_size}M--agorartc_so_v8_size:{round((v8_apk_size - origin_apk_size) / 1000.0 / 1000.0, 2)}M'
        # apk_v7_str = f'apk_v7_size:{v8_apk_size}M--agorartc_so_v7_size:{round((v7_apk_size - origin_apk_size) / 1000.0 / 1000.0, 2)}M'
        print(f'agorartc sdk version:{sdk_version}')
        print(f'origin_apk_size:{origin_apk_size}')
        print(apk_v8_str)
        print(apk_v7_str)
        print(f'-----calculate done-----')
        print('\033[0m')
        save_file_for_so(sdk_version, apk_v7_str, apk_v8_str)
        return [v7_apk_size, v8_apk_size]

    elif file_type == 'aar':
        aar_apk_size = os.path.getsize(
            f'{os.path.abspath(root_path)}/android/app/build/outputs/apk/release/app-release-unsigned.apk')
        apk_aar_str = f'origin_apk_size:{origin_apk_size}M--agorartc_aar_size:{round((aar_apk_size - origin_apk_size) / 1000.0 / 1000.0, 5)}M'
        # apk_aar_str = f'origin_apk_size:{1.4}M--agorartc_aar_size:{round((aar_apk_size / 1000.0 / 1000.0) - 1.4 , 5)}M'

        print(f'agorartc sdk version:{sdk_version}')
        print(f'origin_apk_size:{origin_apk_size}')
        print(apk_aar_str)
        print(f'-----calculate done-----')
        save_file_for_aar(sdk_version, apk_aar_str)
        print('\033[0m')
        return [aar_apk_size]
    else:
        print('no pkg type, pls input pkg type')

 #计算包体 (so对比）
def computer_apk_size(sdk_type, sdk_version):
    print('-' * 45)
    print(f'Execute Build assembleRelease--agorartc version:{sdk_version}')
    os.system(
        f'cd {os.path.abspath(root_path)}/android && {os.path.abspath(root_path)}/android/gradlew clean && {os.path.abspath(root_path)}/android/gradlew assembleRelease')

    print('\033[32m')
    # print('空工程 1.4M')
    date_now = datetime.datetime.now()
    print('-----agorartc calculate-----\n DataTime %s' % date_now)
    print('sdk_path:%s' % sdk_path)
    time.sleep(4)

    v8_apk_size = os.path.getsize(
            f'{os.path.abspath(root_path)}/android/app/build/outputs/apk/release/app-arm64-v8a-release-unsigned.apk')
    v7_apk_size = os.path.getsize(
            f'{os.path.abspath(root_path)}/android/app/build/outputs/apk/release/app-armeabi-v7a-release-unsigned.apk')

    apk_v8_str = f'apk_v8_size:{round(v8_apk_size / 1000.0 / 1000.0, 2)}M--agorartc_so_v8_size:{round((v8_apk_size - origin_apk_size) / 1000.0 / 1000.0, 2)}M'
    apk_v7_str = f'apk_v7_size:{round(v7_apk_size / 1000.0 / 1000.0, 2)}M--agorartc_so_v7_size:{round((v7_apk_size - origin_apk_size) / 1000.0 / 1000.0 , 2)}M'
    print(f'agorartc sdk version:{sdk_version}')
    print(f'origin_apk_size:{origin_apk_size}')
    print(apk_v8_str)
    print(apk_v7_str)
    print(f'-----calculate done-----')
    print('\033[0m')
    save_file_for_so(sdk_type, sdk_version, apk_v7_str, apk_v8_str)
    return [v7_apk_size, v8_apk_size]

def calculate_origin_apk():
    gradle_path_copy = f'{os.path.abspath(root_path)}/android/app/build.gradle.copy'
    revert_gradle_content(gradle_path_origin, gradle_path_copy)  # 覆盖build.gradle

    os.system(
        f'cd {os.path.abspath(root_path)}/android && rm -rf build && rm -rf {os.path.abspath(root_path)}/app/build')
    os.system(f'cd {os.path.abspath(root_path)}/android && {os.path.abspath(root_path)}/android/gradlew assembleRelease')
    origin_apk_size = os.path.getsize(
        f'{os.path.abspath(root_path)}/android/app/build/outputs/apk/release/app-release-unsigned.apk')
    # print(f'origin_apk_size:{origin_apk_size}')

    return origin_apk_size

def save_file_for_so(file_type, sdk_version, apk_v7_str='', apk_v8_str=''):
    date_now = datetime.datetime.now()
    save_file = f'{os.path.abspath(base_path)}/apk_size_info'
    with open(save_file, 'a+', encoding='utf-8') as s_file, open('../user.txt') as user_info:
        text = user_info.read()
        user_name = text[text.find('username=') + 9: text.find('\n')]
        s_file.write('----Date:%s' %str(date_now) + '--Name:%s' %user_name)
        s_file.write('\n'+ 'agorartc SDK path:%s' % sdk_path)
        s_file.write('\n' + 'agorartc SDK Ver:%s' %sdk_version)
        s_file.write('\n' + f'origin_apk_size:{origin_apk_size}')
        s_file.write('\n' + apk_v7_str + '\n' + apk_v8_str + '\n')
        s_file.write(str('-' * 20))

def save_file_for_aar(sdk_version, apk_aar_str=''):
    date_now = datetime.datetime.now()
    save_file = f'{os.path.abspath(root_path)}/apksize/apk_size_info'
    with open(save_file, 'a+', encoding='utf-8') as s_file, open('../user.txt') as user_info:
        text = user_info.read()
        user_name = text[text.find('username=') + 9: text.find('\n')]
        s_file.write('\n' + 'agorartc Version:%s' %sdk_version + 'Date:%s' %str(date_now) + '--Name:%s' %user_name)
        s_file.write('\n' + f'origin_apk_size:{origin_apk_size}')
        s_file.write('\n' + apk_aar_str + '\n')
        s_file.write(str('-' * 20))

def modify_gradle(pkg_type, sdk_version):
    if pkg_type == 'full':
        gradle_path_full = f'{os.path.abspath(root_path)}/android/app/build.gradle.full' #替换文件
        revert_gradle_content(gradle_path_origin, gradle_path_full) # step 2
        modify_sdk_version(sdk_version) # 修改版本号
    elif pkg_type == 'fullbasic':
        gradle_path_basic = f'{os.path.abspath(root_path)}/android/app/build.gradle.basic'
        revert_gradle_content(gradle_path_origin, gradle_path_basic) # step 2
        modify_sdk_version(sdk_version) 
    elif pkg_type == 'voicefull':
        gradle_path_voice_full = f'{os.path.abspath(root_path)}/android/app/build.gradle.voicefull'
        revert_gradle_content(gradle_path_origin, gradle_path_voice_full) # step 2
        modify_sdk_version(sdk_version) 
    elif pkg_type == 'voicebasic':
        gradle_path_voicebasic = f'{os.path.abspath(root_path)}/android/app/build.gradle.voicebasic'
        revert_gradle_content(gradle_path_origin, gradle_path_voicebasic) # step 2
        modify_sdk_version(sdk_version) 
    elif pkg_type == 'specialfull':
        gradle_path_specialfull = f'{os.path.abspath(root_path)}/android/app/build.gradle.specialfull'
        revert_gradle_content(gradle_path_origin, gradle_path_specialfull) # step 2
        modify_sdk_version(sdk_version) 

    elif pkg_type == 'specialvoice':
        gradle_path_specialvoice = f'{os.path.abspath(root_path)}/android/app/build.gradle.specialvoice'
        revert_gradle_content(gradle_path_origin, gradle_path_specialvoice)
        modify_sdk_version(sdk_version)

if __name__ == '__main__':
    # cmd:
    # python3 apk_pkg_stat.py sdkver sdkver2 full/fullbasic/voicefull/voicebasic
    # python3 apk_pkg_stat.py sdkver full/fullbasic/voicefull/voicebasic
    
    # implementation 'io.agora.rtc:voice-sdk:4.2.3' 
    # implementation 'io.agora.rtc:voice-rtc-basic:4.2.3' 
    # implementation 'io.agora.rtc:full-sdk:4.2.3' 
    # implementation 'io.agora.rtc:full-rtc-basic:4.2.3' 
    
    # special
    # implementation 'io.agora.rtc:agora-special-voice:4.1.1.23'
    # implementation 'io.agora.rtc:agora-special-full:4.1.1.23'

    if sys.argv[1] == '-h':
        print('\033[32m')
        print('-'*80)
        print('一.两版本对比：python3 apk_pkg_stat.py 版本号1 版本号2 包类型[full/fullbasic/voicebasic/voicefull]')
        print('   例如：python3 apk_pkg_stat.py  4.2.0  4.2.3  full/fullbasic/voicebasic/voicefull')
        print('二.单独版本：python3 apk_pkg_stat.py 版本号 包类型[full/fullbasic/voicebasic/voicefull]')
        print('   例如：python3 apk_pkg_stat.py 4.2.0 full/fullbasic/voicebasic/voicefull')
        print('三.特殊版本：python3 apk_pkg_stat.py 版本号 包类型[specialfull/specialvoice]')
        print('   例如：python3 apk_pkg_stat.py 4.1.1.19 specialfull/specialvoice')
        print('-' * 80)
        print('\033[0m')
        exit()

    gradle_path_origin = f'{os.path.abspath(root_path)}/android/app/build.gradle'
    print(f'chow_path:{gradle_path_origin}')
    # 计算原始apk大小
    origin_apk_size = calculate_origin_apk()
    print(f'origin_apk_size:{origin_apk_size}')

    print(f'sys.argv:{len(sys.argv)}')

    if len(sys.argv) == 4:
        pkg_type = sys.argv[3]

        sdk_version = sys.argv[1]
        sdk_version2 = sys.argv[2]
        print(f'version compare:{sdk_version}--VS--{sdk_version2}')
        # sdk_version
        modify_gradle(pkg_type, sdk_version)  # step 1
        computer_apk_size(pkg_type, sdk_version) # step 4
        # sdk_version2
        modify_gradle(pkg_type, sdk_version2)
        computer_apk_size(pkg_type, sdk_version2)

    elif len(sys.argv) == 3:
        pkg_type = sys.argv[2]
        sdk_version = sys.argv[1]
        print(f"chowe pkg:{pkg_type}")
        print(f"chowen sdk_version:{sdk_version}")

        modify_gradle(pkg_type, sdk_version)
        computer_apk_size(pkg_type, sdk_version)
        pass
    else:
        print('input error, pls checkout it! --> python3 apk_pkg_stat.py -h')

    # clean build
    time.sleep(2)
    os.system(f'cd {os.path.abspath(root_path)}/android/ && {os.path.abspath(root_path)}/android/gradlew clean')

    # gradle revert
    gradle_path_copy = f'{os.path.abspath(root_path)}/android/app/build.gradle.copy'
    revert_gradle_content(gradle_path_origin, gradle_path_copy)  # 覆盖origin build.gradle