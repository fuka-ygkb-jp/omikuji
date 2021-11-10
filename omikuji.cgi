#!/usr/local/bin/perl
#+------------------------------------------------------------------------
#|おみくじ 1.0                                                  1999/06/26
#|                                (C)不可思議絵の具(http://yugen.main.jp/)
#+------------------------------------------------------------------------
###呼び出しを許可するページ
###http://から含めたURLでないと上手く行きません。
$accept = 'http://your_domain/~your_account/cgi-bin/omikuji.html';



#☆☆ここからユーザ変更不可☆☆
#+------------------------------------------------------------------------
if ($ENV{"HTTP_REFERER"} ne $accept) {		#他のページからの呼び出しには応答しない
	exit;
} else {
	&rnd;
	&put_img;
	exit;
}

### [乱数発生]
sub rnd {
	srand(time + $$);				#乱数発生の準備
	$n = int(rand(6));				#乱数を発生させる
}

### [イメージを表示]
sub put_img {
	open(IMG, "./${n}.gif");
	@data_gif = stat(IMG);
	$byte = $data_gif[7];					#ファイルサイズを取得
	print "Content-type: image/gif\n";		#HTTPヘッダを返す
	print "Content-length: $byte\n\n";		#画像サイズをブラウザに渡す
	print <IMG>;							#バイナリデータを渡す
	close(IMG);
}
