# ストーリー時の処理
label testPrepare:
    $ mode = 'story'
    $ answerWay = 'fourChoice'
    $ isReview = False

    play music "audio/exam.mp3" volume 0.05

    if progress == 1:
        $ minNum = 1
        $ maxNum = 200
        $ numOfQue = 10
    elif progress == 2:
        $ minNum = 201
        $ maxNum = 400
        $ numOfQue = 10
    elif progress == 3:
        $ minNum = 401
        $ maxNum = 600
        $ numOfQue = 10
    elif progress == 4:
        $ minNum = 601
        $ maxNum = 800
        $ numOfQue = 10
    elif prograss == 5:
        $ minNum = 801
        $ maxNum = 1000
        $ numOfQue = 10
    elif prograss == 6:
        $ minNum = 1
        $ maxNum = 1000
        $ numOfQue = 10
    else:
        $ minNum = 1
        $ maxNum = 100
        $ numOfQue = 10

    jump exam

label initExamMode:
    scene bg classroom evening
    show leap normal at leapPos
    play music "audio/leap.mp3" volume 0.05
    $ isReview = False

    jump modeSelect

label modeSelect:
    L "それでは、どうやって勉強しますか？"
    menu:
        L "それでは、どうやって勉強しますか？"

        "単語を覚える":
            $ mode = 'learn'

            Me "単語を覚えたいな。"

            jump rangeSelect
        
        "テストをする":
            $ mode = 'exam'

            jump rangeSelect

        "休憩する":
            Me "疲れたから、いったん休憩したいな。"

            L "了解です。お疲れさまでした。"

            jump exit
    
label rangeSelect:
    L "分かりました。"
    L "範囲はどうしますか？"

    show leapseclist at topleft: #leap範囲表の表示
        zoom 0.8
        pos (20, 150)

    python: #範囲選択 自分で入力
        flag = False
        while flag == False:
            kariNum = renpy.input("何番から？")
            minNum = leapModule.verifyValue(kariNum)
            if minNum == -1:
                renpy.say(None, "数字を入力してください。")
            else:
                flag = True
            
            renpy.block_rollback() #これがないと稀にバグる
        
        flag = False
        while flag == False:
            kariNum = renpy.input("何番まで？")
            maxNum = leapModule.verifyValue(kariNum, minNum)
            if maxNum == -1:
                renpy.say(None, "数字を入力してください。")
            else:
                flag = True
            
            renpy.block_rollback() #これがないと稀にバグる

    Me "[minNum]番から[maxNum]番の範囲でお願い。"

    hide leapseclist #leap範囲表を隠す
    
    L "分かりました。[minNum]番から[maxNum]番ですね。"

    # learnモードなら準備終了、examモードなら出題数選択に飛ぶ
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

label learn: #指定した範囲の日本語と英語を載せるだけ
    $ leapNumber = minNum載せるだけ

    while leapNumber <= maxNum:
        $ en, jp = leapModule.getWords(leapNumber)

        L "[leapNumber]番、[en]の意味は\n[jp]です。"

        $ leapNumber += 1
    
    L "以上です。お疲れさまでした。"

    jump endSelect

label numOfQueSelect: #問題数選択
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
            python: #自分で入力
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
                    
                renpy.block_rollback() #これがないと稀にバグる

    Me "[numOfQue]問で。"

    show leap normal
    L "分かりました。[numOfQue]問ですね。"

    jump answerWaySelect

label answerWaySelect: #解答形式選択 四択かスペル入力
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
    $ renpy.block_rollback() #これ以前へのロルバの禁止 ズル防止のため
    $ questionNumber = 1 #問題番号の初期化
    $ withHint = False #スペル入力時のヒントの設定の初期化
    if isReview == False: #復習モードでないとき
        $ tfList = [0 for i in range(0, numOfQue)] #問題の正誤リストの初期化
        $ leapModule.makeExam(minNum, maxNum, numOfQue) #問題の初期化
    $ optNum = 3 #ここを変えると選択肢を手動で増やす必要アリ、触らないことを勧める

    while questionNumber <= numOfQue: #問題数の分だけループ
        #（復習モード時）正誤リストの問題番号目が正になっているときその問題を飛ばす
        if tfList[questionNumber-1] == 1:
            $ questionNumber += 1
        else:
            if answerWay == 'fourChoice': #四択出題の時
                #問題の選択肢の製作
                $ leapNum, ans, que, opt = leapModule.getExam(questionNumber,answerWay,minNum,maxNum,optNum)
                $ selected = 0 #どの選択肢を選んだか

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

                $ renpy.block_rollback() #これ以前へのロルバの禁止 ズル防止のため

                if(opt[selected] == ans): #正解した場合
                    $ tfList[questionNumber-1] = 1 #正誤リストの問題番号目を正にする
                    show leap smile
                    play sound "audio/seikai.mp3" volume 0.1
                    L "{color=#26aa5d}正解{/color}です！\n[que] は\n{color=#26aa5d}[ans]{/color} です。"
                else: #不正解の場合
                    show leap question
                    play sound "audio/hazure.mp3" volume 0.1
                    L "{color=#ED1616}不正解{/color}です。\n[que] は\n{color=#26aa5d}[ans]{/color} です。"
                
                $ renpy.block_rollback() #これ以前へのロルバの禁止 ズル防止のため
                $ questionNumber += 1
        

            elif answerWay == 'spell': #スペル入力のとき
                show leap question_mark
                # 問題の製作
                $ leapNum, ans, que = leapModule.getExam(questionNumber,answerWay)
                
                if withHint: #ヒントが出ているとき
                    $ initial = ans[0] #正解の頭文字を取得
                    $ kariQue = "第{0}問、Leap{1}番です。\n{2} は？\nHint: {3} から始まるよ。".format(questionNumber,leapNum,que,initial).replace('[','(').replace(']',')')
                else: #ヒントが出ていないとき
                    $ kariQue = "第{0}問、Leap{1}番です。\n{2} は？\n(hを入力すると頭文字が出ます。)".format(questionNumber,leapNum,que).replace('[','(').replace(']',')')
                
                $ spell = renpy.input(kariQue) #解答を入力

                $ renpy.block_rollback() #これ以前へのロルバの禁止 ズル防止のため

                if spell == "h": #入力がhのときヒントを表示
                    $ withHint = True
                elif spell == ans: #正解の場合
                    $ tfList[questionNumber-1] = 1 #正誤リストの問題番号目を正にする
                    $ withHint = False #ヒント設定の初期化
                    $ questionNumber += 1
                    show leap smile
                    play sound "audio/seikai.mp3" volume 0.1
                    L "{color=#26aa5d}正解{/color}です！\n[que] は\n{color=#26aa5d}[ans]{/color} です。"
                else: #不正解の場合
                    $ withHint = False #ヒント設定の初期化
                    $ questionNumber += 1
                    show leap question
                    play sound "audio/hazure.mp3" volume 0.1
                    L "{color=#ED1616}不正解{/color}です。\n[que] は\n{color=#26aa5d}[ans]{/color} です。"
            

            else:
                "変数\"answerway\"の設定がバグってるっぴ！"

                jump modeSelect
    
    $ sumT = sum(tfList) #合計正解数の計算
    $ rateT = round((sumT / numOfQue) * 100, 1) #正解率の計算
    if isReview == False: #復習モードでないとき
        if(numOfQue == sumT): #全問正解なら
            show leap smile
            L "結果は、[numOfQue]問中全問正解でした。素晴らしいです！"
        elif(numOfQue - sumT == 1): #一問間違いなら
            show leap normal
            L "結果は、[numOfQue]問中１問間違えでした。おしいです。"
        else: #二個以上間違えた場合
            show leap normal
            L "結果は、[numOfQue]問中[sumT]問正解で、正答率は[rateT]％でした。"

    $ isReview = False #復習モード設定の初期化

    jump endSelect

label endSelect:
    show leap normal

    if mode == 'learn': #learnモードの時
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
            
            "戻る":
                jump modeSelect
    

    elif mode == 'exam':
        L "この後どうされますか？"
        menu:
            L "この後どうされますか？"

            "間違えた問題を復習する" if rateT != 100: #正解率が100%でないなら表示
                $ isReview = True #復習モードに移行

                Me "間違えた問題を復習したいな。"

                L "了解です。ではいきますよ。"

                jump exam

            "同じ条件で続ける":
                Me "もう一回やりたいな。"

                L "了解です。ではいきますよ。"

                jump exam

            "条件を変えて続ける":
                Me "別の条件でやりたいな。"

                jump rangeSelect
            
            "戻る":
                jump modeSelect


    elif mode == 'story': #ストーリー時の処理
        if progress == 1:
            stop music
            jump opening2
        elif progress == 2:
            stop music
            jump spring2
        elif progress == 3:
            stop music
            jump sum3
        elif progress == 4:
            stop music
            jump fall3
        elif progress == 5:
            stop music
            jump winter2
        elif progress == 6:
            stop music
            jump ending_judgement
        else:
            "変数\"progress\"がバグってるっぴ！"

            return

    else:
        L "変数\"mode\"がバグってるっぴ！"

        jump modeSelect