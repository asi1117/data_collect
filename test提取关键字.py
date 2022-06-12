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
# filepath = 'D:/dataset/Steam/iteam_reviews'
# id_list = os.listdir(filepath)
id_list = ['1009850.csv', '1012790.csv', '1019550.csv', '1032430.csv', '1039880.csv', '1068820.csv', '1079800.csv', '1092430.csv', '1094390.csv', '1094410.csv', '1099500.csv', '1104380.csv', '1125240.csv', '1133580.csv', '1173510.csv', '1178780.csv', '1215270.csv', '1227160.csv', '1248270.csv', '1292040.csv', '1294760.csv', '1345820.csv', '1363430.csv', '1402020.csv', '1402320.csv', '1403370.csv', '1408230.csv', '1413020.csv', '1465070.csv', '1484280.csv', '1533390.csv', '1733890.csv', '322770.csv', '327140.csv', '342180.csv', '348250.csv', '382110.csv', '392190.csv', '400940.csv', '446750.csv', '448280.csv', '450390.csv', '450540.csv', '457320.csv', '469610.csv', '488310.csv', '493790.csv', '494150.csv', '495030.csv', '496240.csv', '502820.csv', '503580.csv', '518920.csv', '520010.csv', '526140.csv', '546560.csv', '551370.csv', '555160.csv', '555880.csv', '559330.csv', '578620.csv', '586210.csv', '587220.csv', '587430.csv', '587470.csv', '594370.csv', '605450.csv', '611120.csv', '611670.csv', '617830.csv', '618920.csv', '620980.csv', '629730.csv', '643590.csv', '653930.csv', '667970.csv', '669290.csv', '682140.csv', '691160.csv', '691260.csv', '700620.csv', '722180.csv', '722230.csv', '726830.csv', '746930.csv', '752480.csv', '771310.csv', '823500.csv', '858260.csv', '859640.csv', '877200.csv', '885000.csv', '885080.csv', '886250.csv', '908520.csv', '916840.csv', '951330.csv', '963930.csv', '998660.csv']

savepath = 'C:/Users/Owner/Desktop/HDMs/Steam/'
read_worry = []
write_worry = []
for id in id_list:
    df2 = pd.DataFrame()
    try:
        df = pd.read_csv('D:/dataset/Steam/iteam_reviews/'+id, sep=',', error_bad_lines=False, encoding='utf-8_sig')
    except:
        print("读取文本错误",id)
        read_worry.append(id)
    try:

        df2 = df[df['review'].str.contains(pat='Oculus|Rift|Rift S|rift|QUEST|quest|Quest|vr|VR|HTC|htc|Htc|vive|VIVE|Vive|HDMs|HDM|hdm|Pimax|pimax|Index|index|gear|Gear|Go|go|head|windowsMR|windows|Valve|valve|realy|equipment|device|control',regex=True,case =False)]
        print('这一步没问题')
        df2.to_csv(savepath + id, sep=',', encoding='utf-8_sig')
    except:
        print("写入有问题",id)
        write_worry.append(id)
    print(df2)
    #df3 = df[df['one_reviews_text'].str.contains(pat='Worth the money',regex=False)] #regex=True则pat是一个正则表达式，regex=False表示pat是一个字符串
    #df2.to_csv(savepath+id, index=True, sep=',', mode='w+', encoding='utf-8_sig')
    #print(df2)
print(read_worry,'读的错误的')
print(write_worry, '写的错误的')