#coding:utf-8

import json
from urllib import request

# 英単語を引数として実行する
def get_json_data(english_day):
    # urlの値は直して実行してください
    # url = http://(アクセスの都合により省略)/days.py?word=
    url = 
    response = request.urlopen('' + english_day)
    data = json.loads(response.read().decode('utf-8'))
    return data


#関数は定義済みのところから開始

day_map = {}                        #1
day_data = get_json_data('sunday')  #2
day_map.update(day_data)            #3

day_map.update(get_json_data('moanday'))     #2と3を一度に行う場合
day_map.update(get_json_data('tuesday'))    #2と3を一度に行う場合


#day_mapは作成済みのところから開始

if 'monday' in day_map:         #keyに"monday"があるか確認

    # キーがあった(=キャッシュにある)
    print('found in the cache')
    print(day_map['monday'])
    
else:
    # キーが無い(=キャッシュに無い)
    print('not found in the cache')

    data = get_json_data('monday')
    print(data['monday'])

    # この一行でも'月曜'を表示できる
    # print(get_json_data('monday')['monday'])
