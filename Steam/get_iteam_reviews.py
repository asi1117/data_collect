import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import csv
import steamreviews
import pandas as  pd
#打开一个csv文件
with open("VR_Support_Game_Inf.csv",'rt',encoding='utf-8_sig') as f:
    reader = csv.DictReader(f)
    game_list = [row['Game_id'] for row in reader]

#读取游戏id列表
app_ids = game_list
#app_ids = ['751310','698340','250820']
print(app_ids)
#app_id = 573170
#steamreviews.download_reviews_for_app_id_batch(app_ids)
df_English = pd.DataFrame()

for app_id in app_ids:
    review_dict,query_count = steamreviews.download_reviews_for_app_id(app_id)
    print(query_count)
    print(app_id)
    #review_dict = steamreviews.load_review_dict(app_id)
    reviews = review_dict.get('reviews')
    cnt_English = 0
    review_id = 1
    for recommendation_id in reviews:
        print(review_id)
        review_id = review_id+1
        inf = reviews.get(recommendation_id)
        language = inf.get('language')
        try:
            if language == 'english':
                df_English = df_English.append(pd.DataFrame({
                    'recommendation_id': recommendation_id,
                    'steam_id': inf.get('author').get('steamid'),
                    'num_games_owned': inf.get('author').get('num_games_owned'),
                    'num_reviews': inf.get('author').get('num_reviews'),
                    'playtime_forever': inf.get('author').get('playtime_forever'),
                    'playtime_last_two_weeks': inf.get('author').get('playtime_last_two_weeks'),
                    'playtime_at_review': inf.get('author').get('playtime_at_review'),
                    'last_played': inf.get('author').get('last_played'),
                    'language': inf.get('language'),
                    'review': inf.get('review'),
                    'timestamp_created': inf.get('timestamp_created'),
                    'timestamp_updated': inf.get('timestamp_updated'),
                    'voted_up': inf.get('voted_up'),
                    'votes_up': inf.get('votes_up'),
                    'votes_funny': inf.get('votes_funny'),
                    'weighted_vote_score': inf.get('weighted_vote_score'),
                    'comment_count': inf.get('comment_count'),
                    'steam_purchase': inf.get('steam_purchase'),
                    'received_for_free': inf.get('received_for_free'),
                    'written_during_early_access': inf.get('written_during_early_access')},
                    index=[cnt_English]))
                cnt_English += 1
            df_English.to_csv(app_id+'.csv',index=False, sep=',', encoding='utf_8_sig')
        except:
            print('这个评论不是英文')
    print(app_id,'这个游戏已爬完评论')
