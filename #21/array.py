#coding:utf-8

import json
import urllib.request


#############################################################
# Web APIの関数化
# 英単語を引数としてWeb APIを実行する
def get_json_data(english_day):
    # urlの値は直して実行してください
    # url = http://(アクセスの都合により省略)/days.php?word=
    url = 
    response = urllib.request.urlopen(url + english_day)
    
    data = json.loads(response.read().decode('utf-8'))
    return data
#############################################################


#############################################################
# 例題1 配列の作り方、アクセスの仕方
# 1. 空の配列を作成
# 2. Web APIからデータを取得
# 3. 取得したデータを配列に追加
# 4. 2.と3.を再度2回行う
# 5. 配列の最初の要素を出力する
# 6. 配列の要素を順にすべて出力する
#############################################################
day_array = []                      # 1.空の配列を作成
day_data = get_json_data('sunday')  # 2.get_json_dataを実行してデータを取得する
day_array.append(day_data)          # 3.配列にデータを追加する

day_array.append(get_json_data('monday'))   # 2.と3.を一度に行う場合
day_array.append(get_json_data('tuesday'))  # 2.と3.を一度に行う場合


# 配列の一番最初の要素を出力する
print(day_array[0])

# 配列の要素を順にすべて出力する
# day_dataにday_arrayのデータが順次代入される
for day_data in day_array:
    print(day_data)
#############################################################



#############################################################
# 例題2 簡単なキャッシュの実装
# (配列にデータが入っているところからスタート)
# 配列の要素に{"sunday":"日曜"}が
# ・あった場合、"found in the cache"と見つけた要素を出力する
# ・なかった場合、"not found in the cache"とWeb APIから"sunday"を渡した結果を出力する
#############################################################
# 該当する曜日が見つかったか否かのチェックフラグ
found_day_data = False

for day_data in day_array:
    
    # 配列の要素が検索する値と同じである場合
    if day_data == {"sunday":"日曜"}:

        # データが見つかったので配列のデータを表示
        print("found in the cache")
        print(day_data)
        
        # 曜日が見つかったので、チェックフラグをTrueに
        found_day_data = True


# チェックフラグがFalse＝曜日が見つからなかった場合
if found_day_data == False:
    
    #データが無かったのでWeb APIからデータを取得して表示
    print("not found in the cache")
    print(get_json_data('sunday'))
#############################################################
