import random
from pyscript import document

# 1～50までの乱数
ans=random.randint(1,50)
    
# グローバル変数
n=0
low=1
high=50
    
# 関数1
def start(event):
    # 関数内のグローバル変数の宣言
    global n, ans, low, high
        
    # ユーザーからの入力
    user=document.getElementById("user").value
        
    # エラーハンドリング
    try:

    # 型変換（文字→整数値）
        x=int(user)

    except ValueError:
        result=document.getElementById("result")
        result.textContent="1から50までの整数を入力してください"
        result.style.color="black"
        return

    # 回数のカウント
    n += 1

    # 判定
    if x==ans:
        msg=f"お見事！　正解は、{ans}です。あなたは{n}回で当てました！"
        color="red"
        # もう一回ボタンを表示
        document.getElementById("retry").style.display="inline"

    elif x<low:
        msg=f"小さすぎます。{low}以上です。"
        color="black"
    elif x>high:
        msg=f"大きすぎます。{high}以下です。"
        color="black"
    elif x<ans:
        low=x
        msg=f"ヒント：{low} => {high}"
        color="blue"
    else:
        high=x
        msg=f"ヒント：{low} => {high}"
        color="blue"
    # 結果表示
    result=document.getElementById("result")
    result.textContent=msg # テキスト更新
    result.style.color=color # 文字色を変更
    document.getElementById("user").value = "" # 入力欄を空にする

# 関数2（Enterキー）
def on_keydown(event):
    if event.key == "Enter":
        start(event)
    
# ここは関数の外
document.getElementById("user").addEventListener("keydown", on_keydown)

# 関数3（もう一回？）
def retry(event):
    global n, ans, low, high
    n=0
    low=1
    high=50
    ans=random.randint(1,50)
    result=document.getElementById("result")
    result.textContent="新しいゲーム！。1から50までの整数を入力してください。"
    result.style.color="black"
    document.getElementById("user").value = "" # 入力欄を空にする
    # もう一回ボタンを非表示
    document.getElementById("retry").style.display="none"