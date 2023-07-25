import random

def random_roll(probability):
    if random.random() < probability:
        # 48%の確率でこのブロックが実行される
        # ここに処理を記述する
        # print("Process executed!(Rolled)")
        return True
    else:
        # 52%の確率でこのブロックが実行される
        # 何もしない場合はこのブロックに記述する
        #print("Nothing happened.")
        return False
# 48%の確率で処理を実行
# process_with_probability(0.48)
