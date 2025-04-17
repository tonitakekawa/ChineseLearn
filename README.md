# ChineseLearn

🎓 中国語の発音をブラウザから練習できるAIアプリ。  
Whisperで音声認識、gTTSで発音チェック。お題とピンイン表示もあり。
サーバー：python クライアント：web

## 機能

- お題取得（例：你好）
- 音声録音→認識
- 認識結果＋ピンイン表示
- TTSでお題を発音（聞いて真似できる）

## 動作検証
Windows11 + python3.9

## 実行方法

```bash
pip install -r requirements.txt
python server.py
```

## 実装の方針
丽が設計し、技術的に可能なセグメントでGPTが実装し、丽が統合した。評価はまた別の第三者に委ねる。

## Special Thanks

* 設計：丽
* 実装：大体GPT 4o(OpenAI)  
* 技術検証：大体GPT 4o(OpenAI)
* 評価：Yさん、W先生

## 最後に

たぶん、pip freeze > requirements.txt は、忘れる。

