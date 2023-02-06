label testPrepare:
    $ mode = 'story'
    $ answerWay = 'fourChoice'

    play music "audio/exam.mp3" volume 0.05

    if progress == 1:
        $ minNum = 1
        $ maxNum = 100
        $ numOfQue = 10

    else:
        $ minNum = 1
        $ maxNum = 100
        $ numOfQue = 10
        #あとでいじってください

    jump exam

label initExamMode:
    scene bg classroom evening
    show leap question_mark at leapPos
    play music "audio/leap.mp3" volume 0.05

    jump modeSelect

label modeSelect:
    L "それでは、今日はどうやって勉強しますか？"

    menu:
        L "それでは、今日はどうやって勉強しますか？"

        "単語を覚える":
            $ mode = 'learn'

            Me "単語を覚えたいな。"
        
        "テストをする":
            $ mode = 'exam'

            Me "単語を覚えてるかテストしたいな。"

    jump rangeSelect
    
label rangeSelect:

    show leap normal at leapPos
    L "分かりました。"

    show leap question_mark at leapPos
    L "範囲はどうしますか？"

    show leapseclist at topleft:
        zoom 0.8
        pos (20, 20)

    python:
        flag = False
        while flag == False:
            kariNum = renpy.input("何番から？")
            minNum = leapModule.verifyValue(kariNum)
            if minNum == -1:
                renpy.say(None, "数字を入力してください。")
            else:
                flag = True
            
            renpy.block_rollback()
        
        flag = False
        while flag == False:
            kariNum = renpy.input("何番まで？")
            maxNum = leapModule.verifyValue(kariNum, minNum)
            if maxNum == -1:
                renpy.say(None, "数字を入力してください。")
            else:
                flag = True
            
            renpy.block_rollback()

    
    show leap normal at leapPos
    
    Me "[minNum]番から[maxNum]番の範囲でお願い。"

    hide leapseclist
    
    L "分かりました。[minNum]番から[maxNum]番ですね。"

    if mode == 'learn':
        L "ではいきますよ。"

        menu:
            L "ではいきますよ。"

            "OK":
                jump learn

            "やっぱ待って":
                Me "やっぱ待って！"

                L "分かりました。では最初からいきましょう。"

                jump modeSelect

    elif mode == 'exam':
        jump numOfQueSelect

    else:
        L "変数\"mode\"の設定がバグってるっぴ！"
        
        jump modeSelect

label learn:
    $ leapNumber = minNum

    while leapNumber <= maxNum:
        $ en, jp = leapModule.getWords(leapNumber)

        L "[leapNumber]番、[en]の意味は\n[jp]です。"

        $ leapNumber += 1
    
    L "以上です。お疲れさまでした。"

    jump endSelect

label numOfQueSelect:
    show leap question_mark at leapPos
    L "何問ほど出したらいいでしょうか？"

    menu:
        L "何問ほど出したらいいでしょうか？"

        "15問":
            $ numOfQue = 15
            if numOfQue > maxNum - minNum + 1:
                $ numOfQue = maxNum - minNum + 1

        "範囲内の全問":
            $ numOfQue = maxNum - minNum + 1

        "その他":
            python:
                flag = False
                while flag == False:
                    try:
                        kariNum = int(renpy.input("何問出す？"))
                        numOfQue = int(kariNum)
                        if numOfQue > maxNum - minNum + 1:
                            numOfQue = maxNum - minNum + 1
                
                    except:
                        renpy.say(None, "数字を入力してください。")
                    
                    else:
                        flag = True
                    
                renpy.block_rollback()

    Me "[numOfQue]問で。"

    show leap normal at leapPos
    L "分かりました。[numOfQue]問ですね。"

    jump answerWaySelect

label answerWaySelect:
    show leap question_mark at leapPos
    L "それでは、解答形式はどのようにしますか？"

    menu:
        L "それでは、解答形式はどのようにしますか？"

        "４択問題" if maxNum - minNum + 1 >= 4:
            $ answerWay = 'fourChoice'

            Me "４択でお願い。"

            show leap normal at leapPos
            L "了解です。それでは、[minNum]番から[maxNum]番の範囲で[numOfQue]問を、四択形式で出題しますね。"

        "スペル入力":
            $ answerWay = 'spell'

            Me "じゃあ、スペルが合ってるか判定してほしい。"

            show leap normal at leapPos
            L "了解です。それでは、[minNum]番から[maxNum]番の範囲で[numOfQue]問を、スペル形式で出題しますね。"

            menu:
                L "了解です。それでは、[minNum]番から[maxNum]番の範囲で[numOfQue]問を、スペル形式で出題しますね。"

                "OK":
                    L "ではいきますよ。"

                    jump exam
                
                "やっぱ待って":
                    Me "やっぱ待って！"

                    L "分かりました。では最初からいきましょう。"

                    jump modeSelect

label exam:
    $ isReview = False

    $ questionNumber = 1
    $ resultList = []
    $ leapModule.makeExam(minNum, maxNum, numOfQue)
    $ optNum = 3 #ここを変えると選択肢を手動で増やす必要アリ、触らないことを勧める

    while questionNumber <= numOfQue:
        if answerWay == 'fourChoice':
            $ leapNum, ans, que, opt = leapModule.getExam(questionNumber,answerWay,minNum,maxNum,optNum)
            $ selected = 0

            show leap question_mark at leapPos

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

            $ renpy.block_rollback()

            if(opt[selected] == ans):
                $ leapModule.ansExam(questionNumber, True)
                $ resultList.append([leapNum, ans, que, 1])

                show leap smile at leapPos

                L "{color=#26aa5d}正解{/color}です！\n[que] は\n{color=#26aa5d}[ans]{/color} です。"

                show leap normal at leapPos

            else:
                $ leapModule.ansExam(questionNumber, False)
                $ resultList.append([leapNum, ans, que, 0])

                show leap question at leapPos

                L "{color=#ED1616}不正解{/color}です。\n[que] は\n{color=#26aa5d}[ans]{/color} です。"

                show leap normal at leapPos
        
        elif answerWay == 'spell':
            $ leapNum, ans, que = leapModule.getExam(questionNumber,answerWay)
            $ kariQue = "第{0}問、Leap{1}番です。\n{2} は？".format(questionNumber,leapNum,que).replace('[','(').replace(']',')')
            $ spell = renpy.input(kariQue)
            $ renpy.block_rollback()

            if spell == ans:
                $ leapModule.ansExam(questionNumber, True)
                $ resultList.append([leapNum, ans, que, 1])

                show leap smile at leapPos

                L "{color=#26aa5d}正解{/color}です！\n[que] は\n{color=#26aa5d}[ans]{/color} です。"

                show leap normal at leapPos
            else:
                $ leapModule.ansExam(questionNumber, False)
                $ resultList.append([leapNum, ans, que, 0])

                show leap question at leapPos
                L "{color=#ED1616}不正解{/color}です。\n[que] は\n{color=#26aa5d}[ans]{/color} です。"
                show leap normal at leapPos

        $ questionNumber += 1
            
    $ sumT = leapModule.resultExam()
    $ rateT = round((sumT / numOfQue) * 100, 1)

    if(numOfQue == sumT):
        L "結果は、[numOfQue]問中全問正解でした。素晴らしいです！"
    elif(numOfQue - sumT == 1):
        L "結果は、[numOfQue]問中１問間違えでした。おしいです。"
    else:
        L "結果は、[numOfQue]問中[sumT]問正解で、正答率は[rateT]％でした。"

    jump endSelect

label endSelect:
    if mode == 'learn': 
        L "この後どうされますか？"

        menu:
            L "この後どうされますか？"

            "もう一周する":
                Me "もう一周お願いできる？"

                L "了解です。ではいきますよ。"

                jump learn

            "範囲を変える":
                Me "範囲を変えたいな。"

                jump rangeSelect
            
            "この範囲でテストをする":
                $ mode = 'exam'

                Me "じゃあ、今の範囲でテストをしたいな。"

                L "了解です。"

                jump numOfQueSelect
            
            "テストをする":
                $ mode = 'exam'

                Me "じゃあ、テストをしたいな。"

                jump rangeSelect
            
            "休憩する":
                Me "疲れたから、いったん休憩したいな。"

                L "了解です。お疲れさまでした。"

                jump exit
    
    elif mode == 'exam':
        L "この後どうされますか？"

        menu:
            L "この後どうされますか？"

            "今回のテストを復習する" if isReview == False:
                $ isReview = True

                Me "復習がしたいな。"

                L "了解です。ではいきますよ。"

                jump review

            "同じ条件で続ける":
                Me "もう一回やりたいな。"

                L "了解です。ではいきますよ。"

                jump exam

            "条件を変えて続ける":
                Me "別の条件でやりたいな。"

                jump rangeSelect
            
            "単語を覚える":
                $ mode = 'learn'

                Me "やっぱり単語を覚えたいな。"

                jump rangeSelect

            "休憩する":
                Me "疲れたから、いったん休憩したいな。"

                L "了解です。お疲れさまでした。"

                jump exit

    elif mode == 'story':
        if progress == 1:
            stop music

            jump Opening2
    
    else:
        L "変数\"mode\"がバグってるっぴ！"

        jump modeSelect
    
label review:
    $ questionNumber = 1

    while questionNumber <= numOfQue:
        $ leapNum, ans, que, tf = resultList[questionNumber-1]

        if(tf == 1):
            L "第[questionNumber]問、Leap[leapNum]番は正解でした。\n[que] は [ans] です。"
        
        else:
            L "第[questionNumber]問、Leap[leapNum]番は不正解でした。\n[que] は [ans] です。"
        
        $ questionNumber += 1
    
    jump endSelect