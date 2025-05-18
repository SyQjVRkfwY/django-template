# 概要
とりあえずすぐにサーバを動かしてみたいときのサンプルプログラムです。

# 使い方
直下に移動して以下のコマンドで動かす

## ビルド
~~~
docker-compose build
~~~
imageがないサービスはDockerfileから取得するみたい

## コンテナ起動
~~~
docker-compose up -d
~~~

## ログイン
~~~
# djangoはサービス名。 docker-compose.ymlファイル内に定義。
docker-compose exec django bash
~~~

## サーバ起動
~~~
cd test-project  # manage.pyのあるディレクトリに移動
python manage.py runserver 0.0.0.0:8888
~~~

## 接続
ホストPCから、http://localhost:8888/

## 言語対応
https://qiita.com/okoppe8/items/e1c8d4b6ba24af788504
1. 翻訳を埋め込む
~~~
{% trans '翻訳する言葉' %}
~~~
2. メッセージ定義ファイルを生成
以下のコマンドをアプリケーションのディレクトリ下で実行
transタグで埋め込んだリソースのファイルを生成（更新）を行う
~~~
django-admin makemessages -l ja --extension=html,py
~~~

3. `locale/各言語のディレクトリ/django.po` を修正
~~~
msgid "翻訳する言葉"
msgstr "translation word"
~~~

4. 以下のコマンド実行
~~~
python manage.py compilemessages -l ja
~~~

# 困ったときは
## コンテナがビルド・起動しない
Docker Daemonさんがいないと動かない。
Doker-Desktopを起動

## コンテナがすぐにExitedになる
起動後にプロセスがすべて終了するのが原因。下の設定を追加してあげる
~~~
	stdin_open: true
	tty: true
~~~

## ホストからDjangoに接続できない
* ポートフォワーディングを確認
* 起動時のIPとポート番号を確認
`python manage.py runserver 0.0.0.0:8888` ← 0.0.0.0がないと繋がらない可能性あり
* コンテナにnetcatを入れて疎通できるか確認（疎通できればDjango特有の問題）