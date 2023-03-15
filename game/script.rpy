define config.has_quicksave = False
define config.has_autosave = False
define _game_menu_screen = 'load'

define L = Character('Leap', color="#26aa5d")
define Me = Character('自分', color="#000000")
define Mom = Character('母', color="#6b3d01")
define God = Character('神', color="#5f6634")
define Cd = Character("車掌", color="#000000")
define Ano = Character('???', color="#252525")
define Sinseki = Character("親戚", color="#080808") #色は未定
define Kyaku = Character("客", color="#070707") #色は未定
define Fri = Character("Leapの友人", color="#080808") #色は未定
define Man = Character("男", color="#b8af3b") #色は未定

$ zako1Name = ""
define Zako1 = DynamicCharacter("zako1Name", color="#080808")
$ zako2Name = ""
define Zako2 = DynamicCharacter("zako2Name", color="#080808")

init:
    $ import module.leapModule as leapModule

    python:
        #LEAP_PATH = config.basedir + r"\game\module\leap.csv"
        LEAP_PATH = "/game/module/leap.csv"
        leapModule.leapPathSet(LEAP_PATH)
    
    # 好感度を上下させる関数
    python:
        def likeChanger(like, deltaLike):
            like += deltaLike
            if like > 100:
                like = 100
                        
            return like

    image bg classroom evening = im.Scale("bg classroom evening notrim.jpg", 1280, 720)
    image bg seahouse = im.Scale("bg seahouse.jpg", 1280, 720)
    image bg sea = im.Scale("bg sea.jpg", 1280, 720)
    image bg taiikusai = im.Scale("bg taiikusai.png", 1280, 720)
    image bg taiikusai mono = im.Scale("bg taiikusai mono.png", 1280, 720)
    image bg school ground = im.Scale("bg school ground.jpg", 1280, 720)
    image bg station = im.Scale("bg station.jpg", 1280, 720)
    image bg hospital = im.Scale("bg hospital.png", 1280, 720)
    image bg city1 = im.Scale("bg city1.jpg", 1280, 720)
    image bg city2 = im.Scale("bg city2.jpg", 1280, 720)
    image bg city3 = im.Scale("bg city3.jpg", 1280, 720)
    image bg city4 = im.Scale("bg city4.jpg", 1280, 720)
    image bg city evening = im.Scale("bg city evening.jpg", 1280, 720)
    image bg road evening = im.Scale("bg road evening.jpg", 1280, 720)
    image bg room evening = im.Scale("bg room evening.jpg", 1280, 720)
    image bg shrine evening guwan = im.Scale("bg shrine evening guwan.jpg", 1280, 720)
    image bg irumi = im.Scale("bg irumi.jpeg", 1280, 720)
    image leap normal = im.Scale("leap normal.png", 800, 1600)
    image leap smile = im.Scale("leap smile.png", 800, 1600)
    image leap surprise = im.Scale("leap surprise.png", 800, 1600)
    image leap question = im.Scale("leap question.png", 800, 1600)
    image leap question_mark = im.Scale("leap question_mark.png", 800, 1600)
    image leap uniform kuro = im.Scale("leap uniform kuro.png", 800, 1600)
    image leap uniform normal = im.Scale("leap uniform normal.png", 800, 1600)
    image leap uniform normal yami = im.Scale("leap uniform normal yami.png", 800, 1600)
    image leap uniform question sweat = im.Scale("leap uniform question sweat.png", 800, 1600)
    image leap uniform question = im.Scale("leap uniform question.png", 800, 1600)
    image leap uniform sad yami = im.Scale("leap uniform sad yami.png", 800, 1600)
    image leap uniform sad = im.Scale("leap uniform sad.png", 800, 1600)
    image leap uniform smile = im.Scale("leap uniform smile.png", 800, 1600)
    image leap uniform surprise = im.Scale("leap uniform surprise.png", 800, 1600)
    image leap sport normal = im.Scale("leap sport normal.png", 800, 1600)
    image leap sport question = im.Scale("leap sport question.png", 800, 1600)
    image leap sport sad = im.Scale("leap sport sad.png", 800, 1600)
    image leap sport smile = im.Scale("leap sport smile.png", 800, 1600)
    image leap sport surprise = im.Scale("leap sport surprise.png", 800, 1600)
    image leap sport silhouette = im.Scale("leap sport silhouette.png", 800, 1600)
    image leap mizugi normal = im.Scale("leap mizugi normal.png", 800, 1600)
    image leap mizugi question sweat = im.Scale("leap mizugi question sweat.png", 800, 1600)
    image leap mizugi question = im.Scale("leap mizugi question.png", 800, 1600)
    image leap mizugi sad = im.Scale("leap mizugi sad.png", 800, 1600)
    image leap mizugi smile = im.Scale("leap mizugi smile.png", 800, 1600)
    image leap mizugi surprise = im.Scale("leap mizugi surprise.png", 800, 1600)

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

    define leapPos = Position(xancor=0.0, ypos=2.15) #Leapちゃんの位置
    define sinPos = Position(xancor=0.0, ypos=1.3) #親戚の位置
    # 以下の位置は0以上1以下
    define heartImageAlignX = 0.02 #好感度のハートのx位置
    define heartImageAlignY = 0.05 #好感度のハートのy位置
    define heartImageSize = 0.3 #好感度のハートの大きさ
    define heartTextAlignX = 0.045 #好感度のテキストのx位置
    define oneDigitGosa = 0.008 #好感度のテキストが一桁の時にずれる誤差
    define heartTextAlignY = 0.09 #好感度のテキストのy位置
    define heartTextSize = 40 #好感度のテキストの大きさ

label start:
    $ progress = 1 #ストーリーの進行状況
    $ like = 30 #好感度

    jump opening


label rest:
    $ progress += 1 #ストーリーの進行度増加
    $ like_meter = False #好感度の非表示化
    
    menu:
        "セーブしますか？"

        "はい":
            $ renpy.call_screen("save")

        "いいえ":
            pause 0.0
        
    menu:
        "続けますか？"

        "はい":
            if progress == 2:
                jump spring
            elif progress == 3:
                jump summer
            elif progress == 4:
                jump fall
            elif progress == 5:
                jump winter
            elif progress == 6:
                jump ending
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

    elif(badEndCode == 5):
        '薄れゆく意識の中で、Leapちゃんの呼ぶ声だけが聞こえた'
        L '先輩！　先輩！？　せんぱ...'
        "BadEnd 5 : 止まるんじゃねぇぞ"
    
    elif(badEndCode == 6):
        Me "その音を境に、僕の未来は真っ黒に染まった。"
        "BadEnd 6 : It's no use crying over split milk."
    
    elif(badEndCode == 7):
        "BadEnd 7 : 現実"
        "もう少し好感度をあげてみたら、何かが起きるかも...！？"
        jump exit
    
    stop music fadeout 2.0
    pause 2.0

    return


label exit:
    return