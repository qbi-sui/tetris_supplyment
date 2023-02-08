# キーボードで入力した文字列の中に、指定した文字がいくつ登場するか、カウントするプログラム


# 文字列「s」の中から、ある文字「key」を数える機能を持ったクラス「GetKeyNum」を定義する
class GetKeyNum():

    # コンストラクタを定義する
    def __init__(self, s):
        self.s = s
    
    # 文字列に並んでいる文字を1つずつ調べる関数「countChar」を定義する
    def countChar(self, key):
        
        # 探したい文字を数える変数を用意しておく
        count = 0
        
        # 「for c in 検索する文字列」と書くと「c」には順に1文字ずつ保存される
        for c in self.s:
            if c == key:
                count += 1
        
        return count


# キーボードからの入力を、関数「input」で文字列として受け取る
userInput = input("文字列を入力してください:")
key = input("数えたい文字を1文字入力してください:")

# (クラスとして作った機能を使うときは、とある1行を書く必要があります)
counter = GetKeyNum(userInput)

# 例えば「aabbccddの中にaは2個あります。」のように表示する
print(counter.s + "　の中に　" + key + "　は　" + str(counter.countChar(key)) + "　個あります。")
