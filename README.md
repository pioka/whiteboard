# whiteboard
:construction:クラス内電子掲示板（まだ改良中）です。  
内部ネットワークでの利用を目的としたもので、  SSL周りの整備をしていないので外部への公開はおすすめしません。しないだろうけど。

## 動作環境
- Python`3.5+`   

または  

- docker-compose`1.13.0+`  

## つかいかた
### 秘密鍵の事前設定
```sh
### on Python ###
$ export DJANGO_SECRET_KEY=XXXXXXXX

### on Docker
#Dockerfile内の`ENV DJANGO_SECRET_KEY`の行を書き換えてください
```


### セットアップ

```sh
### on Python ###
$ pip install -r requirements.txt
$ python manage.py migrate

### on Docker ###
$ docker-compose build
```

### 管理者ユーザ作成

```sh
### on Python ###
$ python manage.py createsuperuser

### on Docker ###
$ docker-compose run web python manage.py createsuperuser
```

### サーバ起動

```sh
### on Python ###
$ python manage.py runserver 0.0.0.0:80

### on Docker ###
$ docker-compose up
```

### ユーザの追加（管理者ユーザのみ可）
`http://<HOSTNAME>/admin/auth/user/add/`からユーザを追加する

### ボードの追加
`http://<HOSTNAME>/create_board`からボードを追加する
