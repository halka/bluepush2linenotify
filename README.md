# bluepush2linenotify
ダイソーに売っているBluetoothでスマホのカメラのシャッターが切れる装置で遊ぶアレです。

服薬した時間を忘れるので、ボタンを押したらデータベースに日時の格納・LINE NotifyでLINEに通知が飛ぶように。

## 追加で必要なもの

````
pip install requests
````

## 動かす
### LINE Notify関係の設定
https://engineering.linecorp.com/ja/blog/detail/88
### トークンを環境変数に
````
export LINE_NOTIFY_TOKEN="yourtoken'
````
### ペアリング・ソフトウェアのインストール
https://qiita.com/vimyum/items/8b7548ca8cf45383c5b0
### データベースの準備
````
sqlite3 report.db < init.sql
````
### 立ち上げっぱなしにする
````
nohup bluebutton -d="Shutter3" -c ~/config/bluebutton
````
