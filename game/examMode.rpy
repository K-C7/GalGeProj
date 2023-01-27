label modeSelect:

    scene bg classroom evening

    show leap at center:
        zoom 1.2

    $ mode = 0 #0なら学習モード、1なら本番
    $ part = 0
    $ numOfQue = 0
    $ minNum, maxNum = 0, 0

    L "それでは、今日はどの範囲で練習しますか？"

    menu:
        "カスタム範囲":
            Me "じゃあ、この範囲から出してほしいな。えっと..."

            jump rangeSelect

        "一つのPart":
            Me "じゃあ、このPartから出してほしいな。えっと..."

            jump partSelect
        
        "全範囲":
            $ minNum, maxNum = 1, leapModule.getLastNum()

            Me "全範囲でお願い。"

            L "分かりました。全範囲ですね。"

            jump numOfQueSelect
            
label rangeSelect:
    python:
        flag = False
        while flag == False:
            try:
                kariNum = renpy.input("何番から？")
                minNum = int(kariNum)
        
            except:
                renpy.say(None, "数字を入力してください。")
            
            else:
                flag = True
        
        flag = False
        while flag == False:
            try:
                kariNum = renpy.input("何番まで？")
                maxNum = int(kariNum)
        
            except:
                renpy.say(None, "数字を入力してください。")
            
            else:
                flag = True

    Me "[minNum]番から[maxNum]番の範囲でお願い。"
    
    L "分かりました。[minNum]番から[maxNum]番ですね。"

    jump numOfQueSelect

label partSelect:
    menu:
        "Part1":
            Me "Part1で。"
            $ part = 1

        "Part2":
            Me "Part2で。"
            $ part = 2
        
        "Part3":
            Me "Part3で。"
            $ part = 3

        "Part4":
            Me "part4で。"
            $ part = 4
    
    L "分かりました、Part[part]ですね。"

    $ minNum, maxNum = leapModule.partToRange(part)

    jump numOfQueSelect

label numOfQueSelect:
    L "何問ほど出したらいいでしょうか？"

    menu:
        "10問":
            $ numOfQue = 10

        "30問":
            $ numOfQue = 30

        "50問":
            $ numOfQue = 50
        
        "その他":
            python:
                flag = False
                while flag == False:
                    try:
                        kariNum = int(renpy.input("何問出す？"))
                        numOfQue = int(kariNum)
                
                    except:
                        renpy.say(None, "数字を入力してください。")
                    
                    else:
                        flag = True

    Me "[numOfQue]問で。"

    L "分かりました。[numOfQue]問ですね。"

    $ isCorrectValue = leapModule.verifyValue(minNum, maxNum, numOfQue)
    if isCorrectValue != True:
        L "範囲か問題数がおかしいですよ。最初から確認しましょう。"

        jump modeSelect

    else:
        if part == 0:
            L "了解です。それでは、[minNum]番から[maxNum]番の範囲で[numOfQue]問出題するのでよろしいでしょうか。"
        else:
            L "了解です。それでは、Part[part]から[numOfQue]問出題するのでよろしいでしょうか。"
            
        menu:
            "Yes":
                jump answerWaySelect

            "No":
                L "あれ、聞き間違えたかしら..."

                jump modeSelect

label answerWaySelect:
    L "それでは、解答形式はどのようにしますか？"

    menu:
        "４択問題":
            $ answerWay = 0
            Me "４択でお願い。"
            jump examModeFourChoice

        "スペル入力":
            $ answerWay = 1
            Me "じゃあ、スペルが合ってるか判定してほしい。"
            jump examModeSpell
    
label testPrepare(progress):
    $ mode = 1

    if progress == 1:
        $ minNum = 1
        $ maxNum = 100
        $ numOfQue = 10
    else:
        $ minNum = 1
        $ maxNum = 100
        $ numOfQue = 10
        #あとでいじってください

    jump examModeFourChoice

label examModeFourChoice:
    $ config.rollback_enabled = False

    $ optNum = 3 #ここを変えると選択肢を手動で増やす必要アリ、触らないことを勧める
    $ questionNumber = 1
    $ resultList = []
    $ leapModule.makeExam(minNum, maxNum, numOfQue)

    L "了解です、ではいきますよ。"

    while questionNumber <= numOfQue:
        $ exam = leapModule.getExamFourChoice(questionNumber,minNum,maxNum,optNum)
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
            $ leapModule.ansExam(questionNumber, True)
            $ resultList.append([leapNum, ans, que, 1])
            L "正解です！\n{color=#26aa5d}[ans]{/color} の意味は [que] です。"

        else:
            $ leapModule.ansExam(questionNumber, False)
            $ resultList.append([leapNum, ans, que, 0])
            L "不正解です。\n[que] は {color=#26aa5d}[ans]{/color} です。"
        
        $ questionNumber += 1
            
    $ sumT = leapModule.resultExam()

    L "結果は、[numOfQue]問中[sumT]問正解でした。"

    $ renpy.block_rollback()
    $ config.rollback_enabled = True

    jump EndSelect

label examModeSpell:
    $ config.rollback_enabled = False

    $ questionNumber = 1
    $ resultList = []
    $ leapModule.makeExam(minNum, maxNum, numOfQue)

    L "了解です、ではいきますよ。"

    while questionNumber <= numOfQue:
        $ exam = leapModule.getExamSpell(questionNumber,minNum,maxNum)
        $ leapNum = exam[0]
        $ ans = exam[1]
        $ que = exam[2]

        $ spell = renpy.input("第[questionNumber]問、Leap[leapNum]番です。\n[que] は？")
        
        $ CC_ansT = "1b615d" 
        # CCはColorCodeの略、変数に保存できるかのテスト用です。

        if spell == ans:
            $ leapModule.ansExam(questionNumber, True)
            $ resultList.append([leapNum, ans, que, 1])
            L "正解です！\n{color=#26aa5d}[ans]{/color} の意味は [que] です。"
        else:
            $ leapModule.ansExam(questionNumber, False)
            $ resultList.append([leapNum, ans, que, 0])
            L "不正解です。\n[que] は {color=#26aa5d}[ans]{/color} です。"
        
        $ questionNumber += 1
            
    $ sumT = leapModule.resultExam()

    L "結果は、[numOfQue]問中[sumT]問正解でした。"

    $ renpy.block_rollback()
    $ config.rollback_enabled = True

    jump EndSelect

label EndSelect:
    if mode == 0:
        L "この後どうされますか？"
        
        menu:
            "今回の単語を復習する。":
                L "了解です。"
                "復習モードに移行します。"
                jump review

            "同じ条件で続ける。":
                if answerWay == 0:
                    jump examModeFourChoice
                else:
                    jump examModeSpell

            "条件を変えて続ける。":
                L "了解です。"
                "モード選択画面に戻ります。"
                jump modeSelect
            
            "休憩する。":
                L "了解です。今日もお疲れさまでした。"
                jump exit

    elif mode == 1:
        if progress == 1:
            call Opening2(sumT)

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
            if answerWay == 0:
                jump examModeFourChoice
            else:
                jump examModeSpell

        "条件を変えて続ける。":
            L "了解です。"
            "モード選択画面に戻ります。"
            jump modeSelect
        "休憩する。":
            L "了解です。今日もお疲れさまでした。"
            jump exit