■ビルド
	docker-compose build
		imageがないサービスはDockerfileから取得するみたい

■コンテナ起動
	docker-compose up -d

■ログイン
	docker-compose exec <サービス名> bash



■困ったときは
	・コンテナがすぐにExitedになる
		起動後にプロセスがすべて終了するのが原因。下の設定を追加してあげる
		stdin_open: true
        	tty: true

	・ホストからDjangoに接続できない
		・ポートフォワーディングを確認
		・起動時のIPとポート番号を確認
			python manage.py runserver 0.0.0.0:8888
		・コンテナにnetcatを入れて疎通できるか確認（疎通できればDjango特有の問題）