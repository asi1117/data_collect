#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import warnings

import requests as requests

warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import time
import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import traceback

# %%% initialize chrome
# open website
time_star = time.time()
# %%% collect all reviews

count = 0
dataframe = pd.DataFrame()
# with open('VIVEPort_id.csv', 'rt', encoding='utf-8_sig') as f:
#     reader = csv.DictReader(f)
#     game_list = [row['iteam_id'] for row in reader]
id_list = ['c8060c87-aba2-4509-bfd2-288ee08061cb', '11b5ee56-0ef0-41e1-852d-f73646d3261a', '6df3c71d-1a3d-4d2e-b383-2668cd80c603', '3ce0c6cf-bd53-4813-845b-0dcd7eb69ac3', '779292a0-a146-47cc-aa3b-25aae7c473a3', '0ac3288f-8c2d-43c2-bd69-f0db2eee14d7', '25e40ce9-efc0-465b-9ae6-10b54f1e9b69', '11dbc545-8a46-4890-b5da-d93e8df1d983', '4c1cf314-2017-46fe-939a-724a77d7918e', 'ee24e838-9585-48a2-ac6c-2fb25a6afca9', '80f78a04-f726-404f-8140-5064c7ce86de', '3f8a371c-f36d-4759-b729-b4cc6ac6929a', '508c52ce-a49e-4130-8156-a608666dc004', '70755b3a-4397-46a8-a33b-5abb9f832f32', '10061f99-1e01-448a-9f90-30ad942850fa', 'bb98955b-7792-4ab1-baf1-320a824f0ce6', 'a58bb5cf-cbf4-4fd7-a2d6-7bdf7878b9ce', 'd1f89b95-788f-4e59-83a0-5d9ccf071c66', '90015ddd-309e-4095-96a0-d4e37afcf195', '297c5d39-57c8-4d1e-8479-dcf78d6017d0', '72209e3f-2304-422b-9b6f-4442a361db42', '9c8338db-5a6c-40e7-b1e5-ed853a0f9f99', '931680f5-9425-4c4c-bdf8-3eb179ee545d', 'c63cb47b-b3f0-4a8e-80de-ba1bf44d3036', '8138ed9f-ee6b-43d2-b859-0bde5b121e04', 'f97aa329-b72c-49e2-951a-c38b7af51464', '7266528c-de8a-4e68-be1e-d3b88d7164db', 'fc476af7-1504-4858-b328-5528720dd71e', '7e1c5c71-bc20-472a-890d-a828f09ff26b', 'ca5922e7-de8e-4261-b7a3-591858c605eb', '56642f34-d93b-4fd7-b0d9-6c8cfa47c757', 'fb586065-dd06-4ca0-adad-3a361fcb924b', '7ef8e68f-9cc9-4d6e-9505-4315dc66434f', '85c4a357-9831-4522-8339-0900c752816c', '4bb82295-5e92-4f70-8346-8e6ac88af808', '0315d7b3-788b-4de2-a27b-4de1d83fa251', 'd294a648-e52a-4f3b-9c44-b03977a30e5f', '7572695d-2dbc-47d7-aa29-5ac03afbf9bc', 'a38aaaf4-a9ce-458f-882a-fbcf7c06f6b9', '1ed66174-3a2c-4dd9-81d4-dedd76cbec23', 'c583e517-d1fb-45a4-9451-e9bfefd8b0e6', '1debbeea-ee89-4107-a417-9845978780a2', '52a584ad-bf24-4852-a820-a3227c6c0ecb', 'f010780d-549a-4214-9924-9de06f973a77', 'c93eef7b-681c-49c9-8832-d9d01429ac20', '737f6108-bd2c-41db-8393-2a72cf3ab5ae', 'fab0c1c8-1ab1-4f4b-99a4-40ab2791122a', '9707bd0b-4552-47cd-8fb9-035823823873', 'c341e0c9-c4bc-4fe8-9d91-0a55c2b27d91', 'b0076688-c85e-434d-baa8-1745641c51e5', '09e359c8-374d-482d-91fd-484b18792a99', 'cd397ab9-bc81-4607-b963-99ecb4954bfa', 'bd8aa4a5-7714-4e41-acb3-1179ebdb8181', '5f3aafaf-51f3-46d7-b77e-5ccdb869dab6', 'bb44ce1c-be36-485e-bee9-b541f395c136', '88058a8f-7ec1-45f5-89c1-e5b243e763b6', 'f3e2931f-48a8-45c6-839f-9a2c5289c87e', 'f3cdd7ec-f93b-4eb9-b75c-67dc101a0c24', '5b70ca72-da0d-4819-9b64-379ce1507828', '5b59f100-c139-4d9d-a6e7-24431522b7c9', '8537ead5-381f-45ee-8310-4ad80a8b5e72', 'f2417777-0c6b-4693-9e13-4c345708fdeb', '8338ca7c-183d-4114-ab26-53580b0351b9', 'b7305124-9e26-486f-ad6e-768339b9bb1c', 'f09e0501-0427-4e15-96f6-ce50a91d2932', 'b4a083bd-0e5c-44a6-8390-39ddd98ca9fc', 'ee8b0d20-2731-4ea9-ad6d-11b759e754fc', '5484a79c-1b8d-4301-a5a3-26f82d2f2f92', 'b3c1f96f-ff42-45b5-8913-64e21de5d5cd', '54487033-c4c1-4368-be93-921b0976b00f', '7f86fd80-e2fa-4ff9-8009-125effc3cd87', 'ed410c03-030c-4c2f-94e9-d8fc812ad3e5', 'b2d81941-488b-46ca-a520-7ff3d00ead54', '535584ab-0575-4bac-b6f0-6348d4d3a1bd', 'b29ebfe4-e16b-4f23-b180-5c962e3b5663', 'ecd3a48b-4fa0-4db3-8cb8-8f6384bdc75e', '51ac3bcc-cc9a-4588-87e9-af6b2c791ff7', 'b1f055ce-1c5b-493e-bcee-75de4fdcaef9', 'b03d54e1-aa5b-4a26-8546-5d03be688e60', '7dc4df2b-4062-4486-9c45-38779355d607', 'eb082cb1-66e0-424a-bbf4-442054f66a48', '7cb925da-4bc7-4e88-b42c-b78848018949', '7c953801-585e-4881-b12b-8eddb3ff65d8', 'acd90aab-cbfe-413a-93a6-b351b9223357', '500b78f0-bc2c-4936-bea6-cab43ad4c1f2', '4eacb859-b664-4110-9d7c-e2dd4f8cb454', '7b99ea91-a2f9-4fe7-8a06-e0d2a4840f39', 'e2c99ee2-d510-4931-8b14-f76b473619a2', '2ded1fe3-f4ce-4d1f-afb3-e301afd00632', 'a7ec0f00-34e2-4864-b78e-a7c71be42a4c', 'e2aca38f-17f3-4f08-86f9-5f87c704d933', '7b0fc540-4669-4ccc-9627-0b4a055b0a6b', '79df60d5-9a26-499a-843a-e43c4251a3c0', '46945331-1de9-4454-bd57-ce6cc9a67594', 'e0200d24-fbaa-4062-9f75-02f200d011c9', '7990f186-63dd-48eb-ba07-235f3724c30b', '4667ba0f-4bf0-405b-a80f-27b2c1815208', 'a31a6ca5-9849-4201-85b5-eb5715d67cfd', '45ce79fb-8b32-40f4-b051-4203ac4b54f9', '45482c28-4151-4d91-a844-cdefa29e3484', 'da81e7c3-e79f-46f8-9c07-0acc072ca4c4', 'a1704fea-e219-4299-ba50-1b1f49991b80', '7801af0b-561e-4c68-a653-ae3593491fe3', '77cbd2fc-6793-4bf1-9e1a-f6c10b6a8bde', 'a08dfb21-b87b-4006-adf9-f2247d500249', '2337390d-b111-4793-ab09-dbe05bdd5e81', '9fcbdde8-9a7b-4eb9-bc99-17764034060a', '40d2ea9b-bffb-4ec3-b79c-a145badbe292', '9f0c125c-1c6c-419d-a982-ed9a4033f4ae', '9ee54911-db55-432a-ba34-0a592c7de910', '201dc06f-c901-4e6e-af93-0861d0de48d3', '3c0f8e26-266b-4d04-9874-8cb21beb4062', '20149267-cee0-4123-93ad-65f6511e4a91', '73559f86-2a04-4b6c-95d6-5b95f371fd90', '1fd478f8-9ed5-4373-9044-cffaed2d2ccd', '3bc488b3-9429-4219-b994-25fd138831f6', 'd0941065-8463-4b79-ab85-61880c6523b3', '3b3f59dc-0d53-4adf-82b5-753052f2962a', '9690fb95-3771-4ed1-83d9-cdcc74ee66ca', '967de5fc-c75b-487a-ab4d-c19e9c2b6d31', '6edb559a-614f-4f3c-a05b-83ceb6985211', 'cc96709f-6c6d-4e52-8334-b73b0c1bc656', '3961f372-1ed8-4787-8580-18e0f2532608', '395456f5-2046-43ca-9e07-2efbac11e5f5', '1bfbf7c4-0846-4268-bc4a-b58203de152a', '6ddc3bc9-38e8-4ca5-ae7d-97efaea0f130', 'ffe78bac-2a4f-4537-86d3-65f37912cf25', '6ba40b06-0109-45bf-b664-f0e2f792aa32', '37c20a7e-8c27-4757-b408-35b5d17e9a8f', '92fb4979-96a1-475b-a919-23cf5471bf5d', 'c9277270-5044-4aea-a325-2f30400685ae', '67848a17-332e-4d7e-a310-767c86446424', '3598865b-42eb-4d39-9895-3a28705016e6', '192c5a0c-0934-43c1-8e89-1d3edaf196bb', '66f5f0b8-9b5f-447e-acd0-4093a7c9c125', '18f13038-6c59-4672-85b0-69b0dfe5ca48', 'fef00047-0ee8-43db-ac81-29e10c799048', '65b538ae-fa44-47ff-91dd-b24f7b8effa0', '18757ab9-7209-4c58-887b-c8857256582f', '350a9d43-8184-4358-9e28-eacce61443dd', '9014e98b-ca15-40a0-bfd7-7be996adeed5', 'c4e697eb-acde-4530-b489-b2cba1a2569c', '64cadba0-6c18-4193-85d3-ec887309ca29', '17488609-5ebb-49bb-94ae-b0f9943f6fe9', '6474c8b0-96a0-48ce-9283-9ceed7f49659', '340c7fd2-3477-4dc6-bdde-8098eb7372d7', 'fb967daf-b459-47a8-8d4f-883d312b2a86', '33c22c04-eeae-4458-b630-f570ae3e6bee', '8c939eb3-b4c8-436d-8b6b-e11596e8aaa0', 'fa8c5176-519f-414c-b293-3512af4f58f5', 'c20105bb-c64a-4dbe-aba2-12a2f6480e4e', 'f99e83c4-82d7-4f73-af44-3cec6806a22c', '11d76cd5-93d3-438c-9ede-87f8d879fb9e', '116d26d9-836e-4d5c-a9e1-c0e2b58531ca', '100072b9-d04d-417d-aaae-72536eabbbf9', '0e793bf9-744f-4b53-936a-1b9503ada488', '0afe9645-16ef-4cf0-9628-2b3532408586', '09232ab5-c088-43ed-9387-5a5011e36cea', '014d3a66-99f3-4df0-87b9-d479828ccc51', '0103c225-98b7-4858-ab8c-c3e3b034abba', 'c4b94764-d3da-48df-8497-517b8fbef073']
print(len(id_list))
n = 0
k = 0
worry_list = []
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    }
#得到商品的所有共同标签，将标签内容传到soup中
#循环打开游戏的页面，获取上面的信息

for id in id_list:
    # 得到商品id，通过访问url将商品信息输进去
    url = 'https://www.viveport.com/' + str(id)
    resp = requests.get(url, headers=headers)
    html = resp.content
    soup1 = BeautifulSoup(html, 'html.parser')
    url2 = soup1.find('option', attrs={'class': 'view-jp_v_enus'}).get('href')
    resp2 = requests.get(url2, headers=headers)
    html2 = resp2.content
    soup2 = BeautifulSoup(html2, 'html.parser')
    try:
        app_details = soup2.find_all('div', attrs={'class': 'meta-block'})
        #print(app_details)
    except:
        print("取游戏细节出错")
    try:
        iteam_name = soup2.find('div', attrs={'class': 'page-title-wrapper product'}).text.strip()
        print(iteam_name)
    except:
        iteam_name = ' '
        print('获取商品名字错误')
    try:
        iteam_description = soup2.find_all('div', attrs={'class': 'description-block'})[0].text.strip()
        print(iteam_description)
    except:
        iteam_description = ' '
        print('获取商品简介')
    try:
        iteam_price = soup2.find_all('span', attrs={'class': 'price'})[0].text.strip()
    except:
        iteam_price = ' '
        print('价格失败')
    try:
        iteam_language = soup2.find('table', attrs={'class': 'lang-supported-table'}).text.replace('Interface', '').replace('Audio', '').replace('Subtitles', '').strip()
    except:
        iteam_language = ' '
        print('语言失败')
    try:
        Game_platform = app_details[0].find('div').text.strip()
    except:
        Game_platform =' '
        print('游戏平台出错')
    try:
        Game_genre = app_details[1].find('div').text.strip()
    except:
        Game_genre =' '
        print('游戏种类出错')
    try:
        Game_playArea = app_details[2].find('div').text.strip()
    except:
        Game_playArea =' '
        print('游戏区域出错')
    try:
        if len(app_details) == 22:
            Game_Controllers = app_details[3].find('div').text.strip()
        if len(app_details) == 13:
            Game_Controllers = ' '
    except:
        Game_Controllers =' '
        print('游戏控制器出错')
    try:
        if len(app_details) == 22:
            Game_rating = app_details[4].find_all('p')[1].text.strip()
        if len(app_details) ==13:
            Game_rating = app_details[3].find_all('p')[1].text.strip()
    except:
        Game_rating =' '
        print('游戏评论出错')
    try:
        if len(app_details) ==22:
            Game_releaseDate = app_details[5].find_all('p')[1].get('data-date')
        if len(app_details) ==13:
            Game_releaseDate = app_details[4].find_all('p')[1].get('data-date')
    except:
        Game_releaseDate =' '
        print('游戏发布出错')
    try:
        if len(app_details) ==22:
            Game_latestDate = app_details[6].find_all('p')[1].get('data-date')
        if len(app_details) ==13:
            Game_latestDate = app_details[5].find_all('p')[1].get('data-date')
    except:
        Game_latestDate =' '
        print('游戏最新出错')
    try:
        if len(app_details) ==22:
            Game_version = app_details[7].text.strip().replace('Version','')
        if len(app_details) ==13:
            Game_version = app_details[6].find_all('p')[1].text.strip()
    except:
        Game_version =' '
        print('游戏版本出错')
    try:
        if len(app_details) ==22:
            Game_type = app_details[8].find_all('p')[1].text.strip()
        if len(app_details)  ==13:
            Game_type = app_details[7].find_all('p')[1].text.strip()
    except:
        Game_type =' '
        print('游戏类型出错')
    try:
        if len(app_details) ==22:
            Game_modes = app_details[9].find('div').text.strip()
        if len(app_details) ==13:
            Game_modes = app_details[8].find('div').text.strip()
    except:
        Game_modes =' '
        print('游戏玩的模式出错')
    try:
        if len(app_details) ==22:
            Game_Developer = app_details[18].find_all('p')[1].text.strip()
        if len(app_details) == 13:
            Game_Developer = app_details[9].find_all('p')[1].text.strip()
    except:
        Game_Developer = ' '
        print()
    try:
        if len(app_details) ==22:
            Game_Publisher = app_details[20].find_all('p')[1].text.strip()
        if len(app_details) == 13:
            Game_Publisher = app_details[11].find_all('p')[1].text.strip()
    except:
        Game_Publisher =' '
        print()
    try:
        print(len(app_details))
        print(id+'.csv')
        # print('日期',app_details[5].find_all('p')[1].get('data-date'))  # .get('data-date'))
        dataframe = dataframe.append(pd.DataFrame({
            'Game_Id': id,
            'Game_Name': iteam_name,
            'Game_price': iteam_price,
            'Game_description': iteam_description,
            'Game_platform': Game_platform,
            'Game_genre': Game_genre,
            'Game_playArea': Game_playArea,
            'Game_Controllers': Game_Controllers,
            'Game_rating': Game_rating,
            'Game_releaseDate': Game_releaseDate, #.get('data-date'),
            'Game_latestDate': Game_latestDate,
            'Game_version':Game_version,
            'Game_type': Game_type,
            'Game_modes':Game_modes,
            'Game_Developer': Game_Developer,
            'Game_Publisher': Game_Publisher,
            'Game_languages':iteam_language.strip(),
        },
            index=[count]))
        count += 1
        print(count)
        dataframe.to_csv("2-1_iteam_message.csv", index=False, sep=',', encoding='utf_8_sig')
    except:
        print(id ,"写文件出错")
        worry_list.append(id)
        print('worry_list',worry_list)
        continue














