# 1~9の数を当てるゲーム
import random

class NumberDetect():
    
	# 初期化 NumberDetect関数を使った際に最初に入る値
    def __init__(self):
        self.num = random.randint(1,9)
        self.answerTime = 0
    
	# ユーザが予想した値が正解かどうか判定する関数　正解ならTrue, 不正解ならFalseを返す
    def judge(self, inputNum):
        self.answerTime += 1
        
        if inputNum == self.num:
            print("正解です！")
            return True
        else:
            if inputNum > self.num:
                print("大きいです")
            else:
                print("小さいです")
            return False

# インスタンス生成
game = NumberDetect()

while True:
    userInput = input("1~9の正の整数値を入力してください:")
    
	# 入力が正の整数かどうかを判定　
    if not userInput.isdecimal():
        print("正の整数ではありません")
        continue
    
	# 文字列→整数に変換
    n = int(userInput) 
    
    if n <= 0 or n >= 10:
        print("1~9の値ではありません。")
        continue
    
    if game.judge(n):
        print("かかった回数は" + str(game.answerTime) + "回です")
        break
    
