# Day1　タートルグラフィックスでPythonを学ぼう
プログラミングやPythonの初学者でも安心！PC画面上にお絵描きをしてくれる「タートルグラフィックス」で、自分の書いたコードが動く体験をしてみましょう。
- Pythonはじめの一歩 (「import」というおまじない・処理を呼び出す「関数」)
- 変数 (演算子)
- 制御構文 (for文・if文)


# Day2 NumPyを扱うコツ
テトリスは、7種類のブロック (「ミノ」と呼びます) + ブロックの置かれていない状態の計8種類のマスを、高さ22段×横10列の盤面に並べている、と言えます。
そしてソースコードでは、置かれていない状態を「0」、I字型のミノを「1」、L字型のミノを「2」・・・とした、「0」から「7」までの数字が220個並んだものによって表現されています。

この数字の並びを「配列」と呼びます。配列はその値を読み書きしたり、値を使って計算したりできます。ここでは、テトリスのソースコードに登場する配列の操作をピックアップして学びます。
- リスト・配列・NumPy配列の違い
- サイズ (reshape)
- 結合 (vstack)
- 削除 (delete)
- 検索 (where)
- 演算 (sum・mean・max・min)
- 乱数 (random)

![説明会スライドp.12](/PythonTetris_p12.png)


# Day3 classの使い方
ソースコードをキレイに、かつ便利に書きまとめる方法に、「関数」と「クラス」があります。テトリスのソースコードにも、もちろん関数が使われています。クラスの使い方まで理解できれば、ソースコードで処理が呼び出されている流れを完璧に掴めるでしょう。ここでは、実際に関数とクラスを書いてもらうことで理解を深めます。
- 関数 (引数・戻り値)
- クラス (関数との違い)
- クラスの継承とオーバーライド


## 【Step1】数当てゲーム「NumberDetect.py」を読んでみる
PCがランダムで選んだ1〜9の値を、ヒントを頼りにキーボード入力で当てるゲームです。

- 「import」で乱数のモジュールを使えるようにする
- 関数「input」で、キーボードからの入力を文字列で受け取る
- while文を「continue」して繰り返す or 「break」してループを抜ける
- クラスの書き方 (コンストラクタ「init」/メンバ変数「self」)
- クラスの使い方 (クラス変数 vs. インスタンス変数)

#### 出力例
```
1~9の正の整数値を入力してください:tsuyoshi
正の整数ではありません
1~9の正の整数値を入力してください:10000
1~9の値ではありません。
1~9の正の整数値を入力してください:5
大きいです
1~9の正の整数値を入力してください:3
小さいです
1~9の正の整数値を入力してください:4
正解です！
かかった回数は3回です
```


## 【Step2】文字数カウンター「CountString.py」を穴埋めする
キーボードで入力した文字列の中に指定した文字がいくつ登場するか、カウントするツールです。

- コード上にある「★」の箇所を書き換えることで、プログラムを完成させてください。
- さっき読んだ「NumberDetect.py」がヒントになるかも…？

#### 出力例
```
文字列を入力してください:PythonTetrisIsSugokuTanoshii
数えたい文字を1文字入力してください:i
PythonTetrisIsSugokuTanoshii　の中に　i　は　3　個あります。
```

## 【Step3】RPG風対戦ゲーム「BattlePlayer.py」を自作する
自分 vs. モンスター！ランダムで襲いかかってくる攻撃に、自分もランダムで攻撃し返すゲームを作ろう

- 初期HPは、両者ともに「30」に設定してください。
- ダメージは、1〜10の値をランダムに相手に与えます or 相手から受けます

Q. まず、この対戦ゲームはどのような処理が順番に行われる？<br>
Q. クラスを使うとしたら、何を定義すべき？<br>
Q. ここまで書いた「NumberDetect.py」「BattlePlayer.py」から流用できそうなところは？<br>

#### 出力例
```
あなたの体力: 30
相手の体力: 30
あなたの攻撃
相手に 9 ダメージを与えました
相手の残り体力は 21 です
相手の攻撃
相手から 3 ダメージを受けました
あなたの残り体力は 27 です
あなたの攻撃
相手に 2 ダメージを与えました
相手の残り体力は 19 です
相手の攻撃
相手から 2 ダメージを受けました
あなたの残り体力は 25 です
あなたの攻撃
相手に 4 ダメージを与えました
相手の残り体力は 15 です
相手の攻撃
相手から 4 ダメージを受けました
あなたの残り体力は 21 です
あなたの攻撃
相手に 6 ダメージを与えました
相手の残り体力は 9 です
相手の攻撃
相手から 8 ダメージを受けました
あなたの残り体力は 13 です
あなたの攻撃
相手に 7 ダメージを与えました
相手の残り体力は 2 です
相手の攻撃
相手から 3 ダメージを受けました
あなたの残り体力は 10 です
あなたの攻撃
相手に 8 ダメージを与えました
あなたの勝ち！！！
```
