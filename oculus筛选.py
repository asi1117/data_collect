import csv
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as  pd
import numpy as np
import re
import os
#提取含有指定字符的行
# with open("4VR_Only_Game_Inf.csv",'rt',encoding='utf-8_sig') as f:
#     reader = csv.DictReader(f)
#     game_list = [row['Game_id'] for row in reader]
filepath = 'D:/dataset/Oculus/GearVR/Iteam_message'
id_list = os.listdir(filepath)

savepath = 'C:/Users/Owner/Desktop/HDMs/Oculusworry/'
read_worry = []
write_worry = []
for id in id_list:
    df2 = pd.DataFrame() 
    try:
        df = pd.read_csv('D:/dataset/Oculus/GearVR/Iteam_message/'+id, sep=',', error_bad_lines=False, encoding='utf-8_sig')
    except:
        print("读取文本错误",id)
        read_worry.append(id)
    try:
        print("到这一部")
        df3 = df[df['Game_Controllers'] == 'Apps']
        print(df3)
        #df3.fillna(value=False,inplace=True)
        #df4 =df[df3]
        #print(df4)
        df3.to_csv(savepath + "Apps.csv", sep=',', encoding='utf-8_sig')
        #print(df3)
        # if df3['review'] ==True:
        #     df4 = df3[df3]
        #     df4.to_csv(savepath + id, sep=',', encoding='utf-8_sig')
        # df2 = df[df['review'].str.contains(pat='Oculus|Rift|Rift S|rift|QUEST|quest|Quest|vr|VR|HTC|htc|Htc|vive|VIVE|Vive|HDMs|HDM|hdm|Pimax|pimax|Index|index|gear|Gear|Go|go|head|windowsMR|windows|Valve|valve|realy|equipment|device|control',regex=True,case =False)]
        # print('这一步没问题')
        # df2.to_csv(savepath + id, sep=',', encoding='utf-8_sig')
    except:
        print("写入有问题",id)
        write_worry.append(id)
    print(df2)
    #df3 = df[df['one_reviews_text'].str.contains(pat='Worth the money',regex=False)] #regex=True则pat是一个正则表达式，regex=False表示pat是一个字符串
    #df2.to_csv(savepath+id, index=True, sep=',', mode='w+', encoding='utf-8_sig')
    #print(df2)
print(read_worry,'读的错误的')
print(write_worry, '写的错误的')