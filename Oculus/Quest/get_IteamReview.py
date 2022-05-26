#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2022年5月20日
主要爬取英國亞馬遜關於oculus——rifs的評論
@author: luyijun
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

"""
Created on 2022年5月24日

@author: luyijun
"""

# %%% relevent packages & modules

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import time
import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import  traceback
# %%% relevent website
id_list = ['4220006248051477', '4988470131168299', '2821509184606966', '3890197214406211', '4046879905345967', '5230505793640167', '3106117596158066', '3815577785147028', '5437449896288644', '3158342884265828', '5077315605654672', '4554248281328321', '2280319701979278', '5334662579895130', '4900967296622279', '3967680489996895', '2302319493201737', '3671539682885620', '6937410016334124', '5157404804284116', '2374555582668563', '4705981139481778', '1968697563211639', '2465388190184288', '4281519998581593', '2731491443600205', '3215828205181680', '4015163475201433', '3594982710558708', '4584847304916084', '3438333449611263', '4048766301899067', '4531913893511480', '3589600511140268', '3684804704932159', '5352920984748732', '6148239151883485', '3831620133609128', '4014704425248676', '4657783360977535', '2160364850746031', '4847484705291911', '3488568914506549', '3630025217090808', '3652037328256745', '3647259232032222', '3683568971682157', '3697657733661230', '3899112273551602', '2031826350263349', '4148745208478773', '6126469507395223', '6102857836422862', '4949538568409451', '4636949963023496', '4243111539050423', '4103186286403181', '2637179839719680', '4714094898617280', '3749621795127676', '3566126356743668', '3385318684883998', '4197310213682418', '5068085479875775', '3878215958952165', '2097356583640894', '3982869578392875', '4207810312567000', '4723352327707414', '2570320959694625', '3759841040728627', '3230671513714717', '3327842470656115', '3432432656819712', '2562230633857728', '3635172946605196', '3931148300302917', '2301375123298882', '4214902388537196', '2970998659623177', '2514011888645651', '3327317663977182', '3600836956645933', '3669819606376951', '4901911359882668', '2948202345202575', '3922378427824210', '2886115781495034', '3916601848368970', '2913958855307200', '2544573735586536', '3044409625637497', '3256881337690839', '3414062495337180', '3003818956320639', '5353996901307344', '1918967004876383', '3126295830741280', '3816141331792031', '4784171281624823', '4143574335654608', '3317083428365473', '3420508614708029', '3202625546470498', '3422717251188752', '3591949650852844', '3634830803298285', '2441213515992073', '3180994211970184', '2562090053828017', '3895994960415614', '3285668754893704', '2088366894520136', '2236053486488156', '2753873371404693', '2401648309868679', '3392175350802835', '4113720305326115', '2792447070854325', '1760132027421053', '3688751474502123', '3433698816645881', '2108767382537806', '2617233878395214', '2548290978591281', '3070239359662935', '1884760688319818', '3682965538398068', '4603898999650318', '3193476307357463', '3755552521124500', '3882524545155280', '3349689215139117', '3844657785549661', '3622969487764448', '2985592331490872', '3727135290647922', '3726478607381266', '2853664488067174', '3323166227771391', '2708465082504733', '2898438393596104', '2719294624823942', '3723136981093558', '3231001163584154', '2537261906377373', '3446712548672561', '2436897736439055', '2977398372335251', '2395213267267320', '2446271755437605', '3484270071659289', '3092079454190601', '3789736921099233', '1961984627245151', '2799962826754702', '2564158073609422', '3043045549099845', '2897337400373711', '2610547289060480', '2913996261988381', '2814449548618112', '2249318828413747', '3857024597703276', '2446085128829455', '4174249979259348', '3675568169182204', '1920879634657108', '2307085352735834', '2159739540797724', '2567459230020142', '2462678267173943', '2245426295493320', '2557519677620753', '2264524423619421', '2874244485968712', '3384742628260377', '2202354219893697', '2866842926757434', '2327302830679091', '2927141310670477', '2004774962957063', '2807364355977144', '2540541942723653', '2004328649624954', '3895528293794893', '2900834523285203', '3002729676463989', '2540393919317658', '4421540051219573', '2677344882310094', '2334376869949242', '2849273531812512', '2873640696088444', '3159481670763523', '3162101440489458', '3087966124548124', '2450698034945641', '2632963266829659', '2302118823192509', '3327542460590280', '2718107161580827', '2833307773392914', '2942600475808591', '2926036530794417', '2773034772778845', '2685959161497510', '2412327085529357', '2933720383334150', '3793077684043441', '2531338473623578', '3386618894743567', '2371757336252737', '2484044451715693', '2215004568539258', '1891638294265934', '2451131601675079', '3628344387191267', '1924930950878181', '3457685900909916', '3759082287499712', '2449350021843569', '2652937004788947', '1706349256136062', '2632034163584300', '2124523024270629', '2476104599150595', '2702419963135346', '1995434190525828', '2260701747375712', '2366136696841248', '2522558964527688', '2333124776756148', '3044656825604617', '2615129151844974', '1976071352472244', '2592096760842149', '2436667223120459', '2557465320986444', '3006696236087408', '3397161850356438', '2173576192720129', '2359857214088490', '1990852827683397', '2736496286381191', '2507216576060698', '2032870023439846', '2393300320759737', '2967784573246968', '2406880882663555', '2515021945210953', '2190353671014400', '1954488057986071', '2280285932034855', '2376737905701576', '2245906048808858', '2299967930057156', '2228678273856228', '2426206484098337', '1917371471713228', '2917608654922903', '2439217169469931', '1427490644042488', '2279149812197085', '2104963472963790', '2436558143118760', '3008315795852749', '2567395559960697', '2725629380835491', '2404437756348346', '2078236868960051', '2082941345119152', '2128482130504783', '2115015981923610', '2223615721048141', '2096339947076151', '2055718171162796', '1551165681653074', '2121787737926354', '2586839431358655', '2257223740990488', '2675955252474460', '2221553561229188', '2133027990157329', '2035353573194060', '2582932495064035', '2325731427501921', '2434361173248640', '2345082335516570', '1978992975501648', '2337198749686376', '1951863938215666', '2180753588712484', '2055554051161375', '1995306573932043', '2398880980156491']
id =0
while (id<len(id_list)):#第一次循环进行传递id
    website = 'https://www.oculus.com/experiences/quest/'+str(id_list[id])

    # %%% initialize chrome
    # open website
    driver = Chrome()
    driver.get(website)
    driver.maximize_window()

    time_star = time.time()
    # %%% collect all reviews
    reviews_one_store = []
    condition_to_continue = True
    dataframe = pd.DataFrame()
    count = 0


    while (condition_to_continue):#进行取信息
        try:
            WebDriverWait(driver, 10).until(
                # 爬取一頁的所有的相關數據
                EC.visibility_of_element_located((By.XPATH, '//div[@class="app-review"]')))
        except:
            print("首页有个小问题")
        reviews = driver.find_elements(by=By.XPATH, value='//div[@class="app-review"]')
        print(len(reviews))
        r = 0

        # Finding all the reviews in the website and bringing them to python
        for r in range(len(reviews)):

            try:
                soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")
            except:
                # I got an errorr saying that element is not attached to the page document
                # To solve this I put an explicit wait condition that tells Selenium to wait until the element is available to be clicked on
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[@class="app-review"]')))
                # reviews = driver.find_elements_by_xpath("//li[@class='review-item']")
                reviews = driver.find_elements(by=By.XPATH, value='//div[@class="app-review"]')
                soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'), "html.parser")

            # scrape raw html
            try:
                scrap_date = datetime.datetime.now()

            except:
                info = traceback.format_exc()
                print(info)
            try:
                review_text = soup.find('div', attrs={'class': 'clamped-description__content'}).text
                print(review_text)
            except:
                review_text = ''
                print("評論文本這裏有問題")
            try:
                review_data = soup.find('div', attrs={'class': 'app-review__date'}).text
                print(review_data)
            except:
                review_data = ''

            try:
                review_title = soup.find('h1', attrs={'class': 'bxHeading bxHeading--level-5 app-review__title'}).text

                print(review_title)
            except:
                review_title = ''
                print('提取評論標題出異常')
            try:
                review_rating = len(soup.find_all('i',attrs={'class': 'bxStars bxStars--white'}))
                print(review_rating)
            except:
                review_rating = ''
                print('提取評分出異常')
            try:
                review_helpful = soup.find('button', attrs={'class' :'button review-helpful-button'}).text.split('|')[1]
                print(review_helpful)
            except:
                review_helpful= ''
                print('有用出错')
            try:
                review_response = soup.find('p', attrs={'class':'bxParagraph bxParagraph--level-1 developer-response__body'}).text
                print(review_response)
            except:
                review_response = ''
                print('作者没回馈')
            try:
                review_author = soup.find('h1', attrs={'class': 'bxHeading bxHeading--level-5 app-review__author'}).text
                print(review_author)
            except:
                review_author = ''
                print('评论作者错误')
            dataframe = dataframe.append(pd.DataFrame({
                'scrapping_date': scrap_date,
                'review_author': review_author,
                'review_title': review_title,
                'one_reviews_text': review_text,
                'review_date': review_data,
                'review_rating': review_rating,
                'review_helpful': review_helpful,
                'review_feedback':review_response,
                },
                index=[count]))
            count += 1
            print(count)

            dataframe.to_csv(str(id_list[id])+".csv", index=False, sep=',', encoding='utf_8_sig')
            print(str(id_list[id])+".csv")
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="mount"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[8]/div/div[3]/div[7]/button[2]/div').click()
        except:
            print("这个游戏评论已爬完")
            break
        # try:
        #     button_click = soup.find('button',attrs={'class','button button--disabled button--secondary app-review-pager__button'}).get_attribute('disabled')
        # except:
        #     print('在最后一页出错')
        # if button_click:
        #     break
        else:
            time.sleep(10)
    id = id + 1
# %%% data cleaning


















