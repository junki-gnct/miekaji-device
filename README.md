# 見え家事 測定デバイス用プログラム
procon31/自由部門/見え家事の測定デバイス用のプログラムです。

## セットアップ
基本的に上から順に実行すれば大丈夫です
1. ペアリング先デバイスのMACアドレスの確認＋ペアリングモードへの切り替え
    - Galaxy(Android 10)での例
        1. 端末の設定を開く
        1. 下にスクロールし端末情報を開く
        1. ステータスを開く
        1. Bluetoothアドレスを確認する
        1. 設定のトップに戻る
        1. 接続を開く
        1. Bluetoothを開く
        1. 下記デバイスセットアップを行う
    
    - Xperia(Android 8)での例
        1. 端末の設定を開く
        1. 下にスクロールしシステムを開く
        1. 端末情報を開く
        1. 機器の状態を開く
        1. Bluetoothアドレスを確認する
        1. 設定のトップに戻る
        1. 機器接続を開く
        1. Bluetoothを開く
        1. 下記デバイスセットアップを行う

1. デバイスのセットアップ
```bash
# リポジトリのクローン
$ git clone https://github.com/junki-gnct/miekaji-device.git; cd miekaji-device

# 依存関係のインストール
$ chmod a+x install.sh; ./install.sh

# 再起動
$ sudo reboot

# デバイスのペアリング (FF:FF:FF:FF:FF:FFは各自のMACアドレスに置き換えて実行する)
# (画像1参考)
$ sudo bluetoothctl
> scan on # 周辺のデバイスのスキャンを開始する
  # 1でメモしたMACアドレスが
  # [NEW] Device FF:FF:FF:FF:FF:FF デバイス名
  # のように表示されるまで待つ
> scan off # 新規デバイススキャンを停止する
> pair FF:FF:FF:FF:FF:FF # ペアリング
# [agent] Confirm passkey xxxxx (yes/no)と表示されたら
> yes
# ここで携帯電話側でもペアリング承認をする。(画像2参考)
> trust FF:FF:FF:FF:FF:FF # 自動再接続の設定
> exit

# 自動起動の登録 & 起動 (/opt/miekaji/ にインストールされます)
$ chmod a+x startup.sh; ./startup.sh
```

## 参考資料
- [画像1](https://gyazo.com/0513dcdde3e5f1f949c4325b9e4e02e8)
- [画像2](https://gyazo.com/13b4e6b2ebe4d4ba00879cde028d0e76)

## 回路図
[![Circuit Diagram](https://i.gyazo.com/af1956b7e4ff45ba144d9fd651b26e98.png)](https://gyazo.com/af1956b7e4ff45ba144d9fd651b26e98)

## 動作環境
- Raspbian GNU/Linux 10.4 (with 5.4.51+ #1333 Linux Kernel)
- Python 3.7.3

## 関連リンク
- [アプリ](https://github.com/junki-gnct/miekaji-app)
- [サーバー](https://github.com/junki-gnct/miekaji-server)
