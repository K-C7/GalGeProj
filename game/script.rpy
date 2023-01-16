define L = Character('Leapちゃん', color="#26aa5d")
define Me = Character('自分', color="#000000")
define Tea = Character('担任', color="#006d75")
define God = DynamicCharacter("godName", color="#5f6634")
define S = Character("生徒", color="#000000")


init:
    $ import module.leapModule as leapModule

    python:
        LEAP_PATH = config.basedir + r"\game\module\leap.csv"
        print(LEAP_PATH)
        leapModule.leapPathSet(LEAP_PATH)

    image bg classroom evening = im.Scale("bg classroom evening notrim.jpg", 1280, 720)


label start:
    jump Opeaning


label op:
    scene bg black

    $ godName = "???"

    God "「...よ ...よ」"

    God "「名はなんと申す?」"

    $ playerName = renpy.input("プレイヤー名を入力してください。")

    God "「[playerName]よ...[playerName]よ...」"

    Me "「...この声は...?」"

    $ godName = "神"

    God "「わしは全国の受験生を合格へ導く受験の神じゃ!」"

    Me "「受験の神...？そんな人が一体何の用ですか？」"

    God "「お主、困っている教科があるのじゃろう?」"

    Me "「ギクッ！じ、実は...」"

    jump subSelect


label subSelect:
    menu:
        "英語":
            # God "nan"
            $ subject = "英語"

        "国語":
            God "まだ準備中じゃ。"
            jump subSelect

        "数学":
            God "まだ準備中じゃ。"
            jump subSelect

        "化学":
            God "まだ準備中じゃ。"
            jump subSelect
    
    Me "実は[subject]が苦手で..."
    
    God "「なるほど、[subject]じゃな?」"

    menu:
        "はい":
            jump op2
        
        "いいえ":
            God "「では何の教科が苦手なのじゃ?」"
            jump subSelect


label op2:
    God "「そうかそうか、ならばわしに任せるのじゃ!」"

    # 効果音予定地

    Me "「...今の音は一体？」"
    
    God "「なに、すぐに分かるわい!じゃあワシはもう行くからの。」"

    Me "「あ、ちょっと待っ...」"

    scene bg white
    with dissolve

    scene bg classroom evening

    "ザワザワ"

    Me "...寝てたのか。それにしても変な夢だったなぁ。"

    show teacher at center

    Tea "「お前ら静かにしろー。HRを始めるぞー。」"

    Tea "「二年生になってまだ一週間しか経ってないが、今日は転校生を紹介するぞ。じゃ、入ってくれ。」"

    hide teacher
    with dissolve

    pause 1.0

    show leap at center:
        zoom 1.2
    with dissolve

    L "「ハ...えっと、こんにちは。イギリスから来ました。リープといいます。今日からよろしくお願いします。」"

    S "「結構可愛くね？」"

    S "「聞いた？イギリスから来たんだって！」"

    Tea "「リープは長い間イギリスに住んでいたんだが、今年日本に帰ってきたんだ。仲良くしてやってくれ。」"

    Me "なるほど、帰国子女のリープさんか...英語ができない俺には縁のない子だな..."

    Tea "「じゃあ、リープの席は...おっ、[playerName]の隣の席が空いてるな。あそこに座ってくれ。」"

    L "「わかりました。」"

    Me "...おいおい、マジかよ。"

    "こうして、英語が苦手な俺とペラペラなLEAPさんとの学校生活が始まるのだった..."

    # プロローグ終わり






label modeSelect:

    scene bg classroom evening

    show leap at center:
        zoom 1.2

    $ part = 0
    $ numOfQue = 0

    L "それでは、今日はどのPartを練習しますか？"

    menu:
        "Part1":
            Me "じゃあPart1で。"
            $ part = 1

        "Part2":
            Me "じゃあPart2で。"
            $ part = 2
        
        "Part3":
            Me "じゃあPart3で。"
            $ part = 3

        "Part4":
            Me "じゃあpart4で。"
            $ part = 4
    
    L "分かりました、Part[part]ですね。"
    L "何問ほど出したらいいでしょうか？"

    menu:
        "10問":
            Me "10問で。"
            $ numOfQue = 10

        "20問":
            Me "20問で。"
            $ numOfQue = 20

        "50問":
            Me "50問で。"
            $ numOfQue = 50

        "100問":
            Me "100問で。"
            $ numOfQue = 100

    L "了解です。それでは、Part[part]を[numOfQue]問出題するのでよろしいでしょうか。"

    menu:
        "Yes":
            L "はい、ではいきますよ。"
            call examMode(part,numOfQue) from _call_examMode

        "No":
            L "あれ、聞き間違えたかしら..."
            jump modeSelect
    

label examMode(part,numOfQue):
    $ optNum = 3 #ここを変えると選択肢を手動で増やす必要アリ、触らないことを勧める
    $ questionNumber = 1
    $ minMax = []
    
    $ resultList = []

    $ leapModule.makeExam(part,numOfQue)
    $ minMax = leapModule.partToRange(part)

    while questionNumber <= numOfQue:
        $ exam = leapModule.getExam(questionNumber,minMax[0],minMax[1],optNum)
        $ leapNum = exam[0]
        $ ans = exam[1]
        $ que = exam[2]
        $ opt = exam[3]

        $ selected = 0

        # L "第[questionNumber]問、Leap[leapNum]番です。\n[que]は？"

        menu:
            L "第[questionNumber]問、Leap[leapNum]番です。\n[que] は？"

            "[opt[0]]":
                $ selected = 0
            "[opt[1]]":
                $ selected = 1
            "[opt[2]]":
                $ selected = 2
            "[opt[3]]":
                $ selected = 3
        
        $ CC_ansT = "1b615d" 
        # CCはColorCodeの略、変数に保存できるかのテスト用です。

        if(opt[selected] == ans):
            $ leapModule.ansExam(True)
            L "正解です！\n{color=#26aa5d}[ans]{/color} の意味は [que] です。"
            $ resultList.append([leapNum, ans, que, 1])
        else:
            $ leapModule.ansExam(False)
            L "不正解です。\n[que] は {color=#26aa5d}[ans]{/color} です。"
            $ resultList.append([leapNum, ans, que, 0])
        
        $ questionNumber += 1
            
    $ sumT = leapModule.resultExam()

    L "結果は、[numOfQue]問中[sumT]問正解でした。"

label EndSelect:
    L "この後どうされますか？"

    menu:
        "今回の単語を復習する。":
            L "了解です。"
            "復習モードに移行します。"
            jump review
        
        "間違った単語をMy単語帳に保存する。":
            "保存中です..."
            pause 1.0
            "My単語帳に保存されました。"
            jump EndSelect

        "同じ条件で続ける。":
            L "了解です。ではいきますよ。"
            call examMode(part,numOfQue) from _call_examMode_1
            jump exit

        "条件を変えて続ける。":
            L "了解です。"
            "モード選択画面に戻ります。"
            jump modeSelect
        
        "休憩する。":
            L "了解です。今日もお疲れさまでした。"
            jump exit


label review:
    $ questionNumber = 1

    while questionNumber <= numOfQue:
        $ leapNum = resultList[questionNumber-1][0]
        $ ans = resultList[questionNumber-1][1]
        $ que = resultList[questionNumber-1][2]
        $ tf = resultList[questionNumber-1][3]

        if(tf == 1):
            L "第[questionNumber]問、Leap[leapNum]番は正解でした。\n[que] は [ans] です。"
        else:
            L "第[questionNumber]問、Leap[leapNum]番は不正解でした。\n[que] は [ans] です。"
        
        $ questionNumber += 1
    
    menu:
        "同じ条件で続ける。":
            L "了解です。ではいきますよ。"
            call examMode(part,numOfQue) from _call_examMode_2
        "条件を変えて続ける。":
            L "了解です。"
            "モード選択画面に戻ります。"
            jump modeSelect
        "休憩する。":
            L "了解です。今日もお疲れさまでした。"
            jump exit
    

label exit:
    $ renpy.quit()