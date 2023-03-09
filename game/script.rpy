define L = Character('Leap', color="#26aa5d")
define Me = Character('自分', color="#000000")
define Mom = Character('母', color="#6b3d01")
define God = Character('神', color="#5f6634")
define cd = Character("車掌", color="#000000")
define Ano = Character('???', color="#252525")
define Sinseki = Character("親戚", color="#080808") #色は未定
define Kyaku = Character("客", color="#070707") #色は未定
define Fri = Character("Leapの友人", color="#080808") #色は未定
define Man = Character("男", color="#b8af3b") #色は未定

init:
    $ import time
    $ import module.leapModule as leapModule

    python:
        LEAP_PATH = config.basedir + r"\game\module\leap.csv"
        #LEAP_PATH = "/game/module/leap.csv"
        leapModule.leapPathSet(LEAP_PATH)

    image bg classroom evening = im.Scale("bg classroom evening notrim.jpg", 1280, 720)
    image leap normal = im.Scale("leap normal.png", 800, 1600)
    image leap smile = im.Scale("leap smile.png", 800, 1600)
    image leap surprise = im.Scale("leap surprise.png", 800, 1600)
    image leap question = im.Scale("leap question.png", 800, 1600)
    image leap question_mark = im.Scale("leap question_mark.png", 800, 1600)
    image bg seahouse = im.Scale("bg seahouse.jpg", 1280, 720)
    image bg sea = im.Scale("bg sea.jpg", 1280, 720)
    image openingVideo:
        "opening-0001.jpg"
        pause 2.0
        "opening-0003.jpg"
        pause 2.0
        "opening-0004.jpg"
        pause 2.0
        "opening-0005.jpg"
        pause 2.0
        "opening-0006.jpg"
        pause 2.0
        "bg black.png"
        pause 2.0

    define leapPos = Position(xancor=0.0, ypos=2.15)

    $ progress = 1 #ストーリーの進行状況
    $ like = 30 #好感度

label start:
    jump opening

label rest:
    $ progress += 1
    
    menu:
        "セーブしますか？"

        "はい":
            $ renpy.call_screen("save")

        "いいえ":
            pause 0

    menu:
        "続けますか？"

        "はい":
            if progress == 2:
                jump spring
            elif progress == 3:
                jump summer
            else:
                "変数\"progress\"の設定がバグってるっぴ！"

                return
        
        "いいえ":
            "お疲れさまでした。タイトル画面に戻ります。"

            return

label badEnd_call:
    scene bg black
    with dissolve

    if(badEndCode == 1):
        "そのまま、主人公は目覚めることはなく、平凡な人生を送ったのでした。"
        "BadEnd 1 : 二度寝"

    elif(badEndCode == 2):
        "その後、二度とLeapさんと出会うことはなく、平凡な人生を送ったのでした。"
        "BadEnd 2 : 邪魔者"
    
    elif(badEndCode == 3):
        Me "...どこで間違えたんだろう..."
        "BadEnd 3 : 理想と現実"

    elif(badEndCode == 4):
        "そういうと男はニヤリと笑ってLeapちゃんとともに人ごみの中に消えていった。"
        "BadEnd 4 : No Time Return"
    
    return

label exit:
    return