import random
import time

class BattlePlayer():
    # メンバ変数(=今回ほしい属性値)はhpのみ
    def __init__(self, hp):
        self.hp = hp

    # ダメージ分減算する関数
    def damaged(self, damage):
        self.hp -= damage

    # 倒せたかどうか判定する関数
    def judgeDeath(self):
        if self.hp <= 0:
            return True

        else:
            return False

# 【今回のポイント】似たような特性を持つものはインスタンスを2つ作ることで効率化可能！
player = BattlePlayer(30)
computer = BattlePlayer(30)

# (エレガントじゃない)
print("あなたの体力: 30")
print("相手の体力: 30")

while True:
    # (↓のコードを入れると、それっぽい動きになります)
    time.sleep(1)
    
    print("あなたの攻撃")
    
    time.sleep(1)

    # ダメージは1ループでしか使わないのでクラスには組み込みませんでした
    # ダメージを決定し、相手にダメージを与える
    playerAttackDamage = random.randint(1,10)
    computer.damaged(playerAttackDamage)
    print("相手に " + str(playerAttackDamage) + " ダメージを与えました")

    time.sleep(1)
    
    # 倒せたなら終了、そうでなければ続行
    if computer.judgeDeath():
        print("あなたの勝ち！！！")
        break
    else:
        print("相手の残り体力は "  + str(computer.hp) + " です")

    # (これ以下は自分と相手が逆になって繰り返しです)
    time.sleep(1)

    print("相手の攻撃")
    
    time.sleep(1)

    computerAttackDamage = random.randint(1,10)
    player.damaged(computerAttackDamage)
    print("相手から " + str(computerAttackDamage) + " ダメージを受けました")

    time.sleep(1)
    
    if player.judgeDeath():
        print("あなたの負け。。。")
        break
    else:
        print("あなたの残り体力は "  + str(player.hp) + " です")
    
            
