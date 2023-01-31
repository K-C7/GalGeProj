label testPrepare:
    $ config.rollback_enabled = False
    $ mode = 'story'
    $ answerWay = 'fourChoice'

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

label modeSelect:
    scene bg classroom evening

    show leap at center:
        zoom 1.2
    
    $ config.rollback_enabled = False

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
    L "分かりました。範囲はどうしますか？"

    show leapseclist at topleft:
        zoom 0.8
        pos (20, 20)

    python:
        flag = False
        while flag == False:
            try:
                kariNum = renpy.input("何番から？")
                minNum = int(kariNum)
                if minNum < 1:
                    minNum = 1
            
            except:
                renpy.say(None, "数字を入力してください。")
                
            else:
                flag = True
        
        flag = False
        while flag == False:
            try:
                kariNum = renpy.input("何番まで？")
                maxNum = int(kariNum)
                if maxNum > 1935:
                    maxNum = 1935
        
            except:
                renpy.say(None, "数字を入力してください。")
            
            else:
                flag = True
    
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

    Me "[numOfQue]問で。"

    L "分かりました。[numOfQue]問ですね。"

    jump answerWaySelect

label answerWaySelect:
    L "それでは、解答形式はどのようにしますか？"

    menu:
        L "それでは、解答形式はどのようにしますか？"

        "４択問題" if maxNum - minNum + 1 >= 4:
            $ answerWay = 'fourChoice'

            Me "４択でお願い。"

            L "了解です。それでは、[minNum]番から[maxNum]番の範囲で[numOfQue]問を、四択形式で出題しますね。"

        "スペル入力":
            $ answerWay = 'spell'

            Me "じゃあ、スペルが合ってるか判定してほしい。"

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
                $ leapModule.ansExam(questionNumber, True)
                $ resultList.append([leapNum, ans, que, 1])

                L "正解です！\n[que] は {color=#26aa5d}[ans]{/color} です。"

            else:
                $ leapModule.ansExam(questionNumber, False)
                $ resultList.append([leapNum, ans, que, 0])

                L "不正解です。\n[que] は {color=#26aa5d}[ans]{/color} です。"
        
        elif answerWay == 'spell':
            $ leapNum, ans, que = leapModule.getExam(questionNumber,answerWay)
            $ kariQue = "第{0}問、Leap{1}番です。\n{2} は？".format(questionNumber,leapNum,que).replace('[','(').replace(']',')')
            $ spell = renpy.input(kariQue)

            if spell == ans:
                $ leapModule.ansExam(questionNumber, True)
                $ resultList.append([leapNum, ans, que, 1])

                L "正解です！\n[que] は {color=#26aa5d}[ans]{/color} です。"

            else:
                $ leapModule.ansExam(questionNumber, False)
                $ resultList.append([leapNum, ans, que, 0])

                L "不正解です。\n[que] は {color=#26aa5d}[ans]{/color} です。"
        
        $ questionNumber += 1
            
    $ sumT = leapModule.resultExam()

    L "結果は、[numOfQue]問中[sumT]問正解でした。"

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

                $ renpy.block_rollback()
                $ config.rollback_enabled = True

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

                $ renpy.block_rollback()
                $ config.rollback_enabled = True

                jump exit

    elif mode == 'story':
        if progress == 1:
            $ renpy.block_rollback()
            $ config.rollback_enabled = True

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