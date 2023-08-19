class ImportTutorial():

    # コンストラクタを定義する
    def __init__(self):
        # クラスの内で使う変数 (インスタンス変数)を定義したいときには、変数名の前に「self.」を付ける
        self.s = "ここまで頑張りました!!Day4へようこそ〜"
    
    # 文字列「s」を表示する関数「printChar」を定義する
    def printChar(self):
        print(self.s)

# インスタンス生成
IMPORT_TUTORIAL = ImportTutorial()