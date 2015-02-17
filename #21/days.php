<?php
// Web APIとして使用するスクリプトです

// 入力値が無い場合を鑑み初期値を設定
$i = 'saturday';

// URLから"word"に対応するデータがあれば、$iに代入
if(array_key_exists('word', $_GET)) {
	$i = $_GET['word'];
}

// 文字列比較のため、すべて小文字に変換しなおす
$i = strtolower($i);

// $iの文字列により返却するjsonデータを決定
switch ($i) {
	case 'sunday':
		$str = '{"sunday" : "日曜"}';
		break;

	case 'monday':
		$str = '{"monday" : "月曜"}';
		break;

	case 'tuesday':
		$str = '{"tuesday" : "火曜"}';
		break;

	case 'wednesday':
		$str = '{"wednesday" : "水曜"}';
		break;

	case 'thursday':
		$str = '{"thursday" : "木曜"}';
		break;

	case 'friday':
		$str = '{"friday" : "金曜"}';
		break;

	default:
		$str = '{"saturday" : "土曜"}';
		break;

}

// jsonとして結果を出力(=レスポンスとして返す)
print "$str";

?>