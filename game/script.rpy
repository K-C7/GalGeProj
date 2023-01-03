define L = Character('Leapちゃん', color="#26aa5d")
define Me = Character('自分', color="#000000")
define God = DynamicCharacter("godName",color="#5f6634")


init:
    $ import module.leapModule as leapModule

    image bg classroom evening = im.Scale("bg classroom evening notrim.jpg", 1280, 720)


label start:
    jump op


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
    
    God "「なるほど、[subject]じゃな?」"

    menu:
        "はい":
            jump opEnd
        
        "いいえ":
            God "「では何の教科が苦手なのじゃ?」"
            jump subSelect


label opEnd:
    God "「そうかそうか、ならばわしに任せるのじゃ!」"

    # 効果音予定地

    Me "「...今の音は一体？」"
    
    God "「なに、すぐに分かるわい!じゃあワシはもう行くからの。」"

    Me "「あ、ちょっと待っ...」"

    scene bg white
    with dissolve

    pause 1.0

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
            call examMode(part,numOfQue)

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
            jump exit

        "同じ条件で続ける。":
            L "了解です。ではいきますよ。"
            call examMode(part,numOfQue)
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
            call examMode(part,numOfQue)
        "条件を変えて続ける。":
            L "了解です。"
            "モード選択画面に戻ります。"
            jump modeSelect
        "休憩する。":
            L "了解です。今日もお疲れさまでした。"
            jump exit
    

label exit:
    $ renpy.quit()