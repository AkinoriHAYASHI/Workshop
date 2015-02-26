#! /usr/local/bin/python3
import io, sys, cgi

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


query = cgi.FieldStorage()

word = 'saturday'

# Getデータを取得する
if 'word' in query:
    word = query['word'].value


# 文字列比較のため小文字にする
word = word.lower()

if word == 'sunday':
    result = '{"sunday" : "日曜"}'
elif word == 'monday':
    result = '{"monday" : "月曜"}'
elif word == 'tuesday':
    result = '{"tuesday" : "火曜"}'
elif word == 'wednesday':
    result = '{"wednesday" : "水曜"}'
elif word == 'thursday':
    result = '{"thursday" : "木曜"}'
elif word == 'friday':
    result = '{"friday" : "金曜"}'
else:
    result = '{"saturday" : "土曜"}'


print('Content-type: text/html; charset=UTF-8')
print()
print(result)