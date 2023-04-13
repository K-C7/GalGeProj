# ストーリー時の処理
label testPrepare:
    # 初期化
    $ mode = 'story' #モード
    $ JpEn = True #解答方向
    $ answerWay = 'fourChoice' #テストの解答方法
    $ optNum = 3 #選択肢数（ここを変えると選択肢の処理を自分で増やす必要アリ）
    $ isReview = False #復習モードかどうか
    # BGM ラスボス戦時は変える
    if progress == 6:
        play music "audio/lastboss.mp3" volume 0.05
    else:
        play music "audio/exam.mp3" volume 0.05
    # 問題の範囲、問題数 ストーリーの進行状況で変える
    if progress == 1:
        $ minNum = 1 #範囲の最小値
        $ maxNum = 200 #範囲の最大値
        $ numOfQue = 10 #問題数
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
    elif progress == 5:
        $ minNum = 801
        $ maxNum = 1000
        $ numOfQue = 10
    elif progress == 6:
        $ minNum = 1
        $ maxNum = 1000
        $ numOfQue = 10
    else:
        $ minNum = 1
        $ maxNum = 100
        $ numOfQue = 10

    jump exam

# 学習モード時の初期化
label initExamMode:
    scene bg classroom evening #背景
    play music "audio/leap.mp3" volume 0.05 #BGM
    $ isReview = False #復習モードかどうか
    $ progress = 0 #ストーリーの進行状況 ここでは無関係なので0

    jump modeSelect

# モード選択
label modeSelect:
    show leap uniform question at leapPos
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

            show leap uniform normal
            L "了解です。お疲れさまでした。"

            jump exit
    
# 範囲選択
label rangeSelect:
    show leap uniform normal
    L "分かりました。"
    show leap uniform question
    L "範囲はどうしますか？"

    # leap範囲表の表示
    show leapseclist at topleft:
        zoom 0.8
        pos (20, 150)

    python:
        # minNumにintが入力されるまで繰り返す
        flag = False
        while flag == False:
            kariNum = renpy.input("何番から？")
            minNum = leapModule.verifyValue(kariNum)
            # kariNumがintでない時
            if minNum == -1:
                renpy.say(None, "数字を入力してください。")
            else:
                flag = True
            
            renpy.block_rollback() #これがないと稀にバグる
        
        # maxNumにintが入力されるまで繰り返す
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

    # leap範囲表を隠す
    hide leapseclist

    show leap uniform normal
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

# 指定した範囲の日本語と英語を載せるだけ
label learn:
    # leap番号の初期化
    $ leapNumber = minNum

    while leapNumber <= maxNum:
        $ en, jp = leapModule.getWords(leapNumber)

        L "[leapNumber]番、[en]の意味は\n[jp]です。"

        $ leapNumber += 1
    
    L "以上です。お疲れさまでした。"

    jump endSelect

# 問題数選択
label numOfQueSelect:
    show leap uniform question
    L "何問ほど出したらいいでしょうか？"
    menu:
        L "何問ほど出したらいいでしょうか？"

        "20問":
            $ numOfQue = 20
            # numOfQueが最大問題数より大きい時
            if numOfQue > maxNum - minNum + 1:
                $ numOfQue = maxNum - minNum + 1

        "範囲内の全問":
            $ numOfQue = maxNum - minNum + 1

        # 自分で範囲入力
        "その他":
            python:
                # numOfQueにintが入力されるまで繰り返す
                flag = False
                while flag == False:
                    try:
                        kariNum = int(renpy.input("何問出す？"))
                        numOfQue = int(kariNum)
                        if numOfQue > maxNum - minNum + 1:
                            numOfQue = maxNum - minNum + 1
                
                    # kariNumがintでない時
                    except:
                        renpy.say(None, "数字を入力してください。")
                    
                    else:
                        flag = True
                    
                renpy.block_rollback() #これがないと稀にバグる

    Me "[numOfQue]問で。"

    show leap uniform normal
    L "分かりました。[numOfQue]問ですね。"
    L "では、[minNum]番から[maxNum]番の範囲で[numOfQue]問を出題するのでいいですか。"
    menu:
        L "では、[minNum]番から[maxNum]番の範囲で[numOfQue]問を出題するのでいいですか？"

        # 「OK」でexamへ、「やっぱ待って」で最初からやり直す
        "OK":
            L "分かりました。"

            jump answerWaySelect
                
        "やっぱ待って":
            Me "やっぱ待って！"

            L "分かりました。では最初からいきましょう。"

            jump modeSelect

# 解答形式選択:四択かスペル入力
label answerWaySelect:
    show leap uniform question
    L "解答形式はどのようにしますか？"
    menu:
        L "解答形式はどのようにしますか？"

        # 最大問題数が4より少ないとき非表示
        "４択問題" if maxNum - minNum + 1 >= 4:
            $ answerWay = 'fourChoice'
            $ optNum = 3 #選択肢数-1（ここを変えると選択肢の処理を自分で増やす必要アリ）

            Me "４択でお願い。"

            show leap uniform normal
            L "了解です。４択形式ですね。"

            jump directionSelect

        "スペル入力":
            $ answerWay = 'spell'

            Me "じゃあ、スペルが合ってるか判定してほしいな。"

            show leap uniform normal
            L "了解です。スペル形式ですね。"
            L "ではいきますよ。"

            jump exam

# 解答方向選択:和英か英和
label directionSelect:
    show leap uniform question
    L "英語と日本語のどちらで答えますか？"
    menu:
        L "英語と日本語のどちらで答えますか？"

        "英語":
            $ JpEn = True

            Me "英語で。"

            show leap uniform normal
            L "分かりました。英語ですね。"

        "日本語":
            $ JpEn = False

            Me "日本語で。"

            show leap uniform normal
            L "分かりました。日本語ですね。"
    
    L "ではいきますよ。"

    jump exam

# 問題を出す 学習モード時だけでなくストーリー時もここで処理する
label exam:
    $ renpy.block_rollback() #これ以前へのロルバの禁止 ズル防止のため

    # 変数の初期化
    $ questionNumber = 1 #問題番号
    $ withHint = False #スペル入力時のヒントの有無
    # 復習モードでない時（復習モードの時は正誤リストと問題リストを使いまわす）
    if isReview == False:
        $ tfList = [0 for i in range(0, numOfQue)] #問題の正誤リスト 0なら不正解、1なら正解
        $ leapModule.makeExam(minNum, maxNum, numOfQue) #問題リスト

    # 合計問題数だけ出題を繰り返す
    while questionNumber <= numOfQue:
        # 正誤リストの問題番号目が1（正解）になっている時問題を飛ばす(実質復習モード時のみ)
        if tfList[questionNumber-1] == 1:
            # 問題番号を進める
            $ questionNumber += 1
        else:
            # 四択問題の時
            if answerWay == 'fourChoice':
                # 問題の取得
                # 和英の時
                if JpEn:
                    $ leapNum, ans, que = leapModule.getExam(questionNumber)
                # 英和の時
                else:
                    $ leapNum, que, ans = leapModule.getExam(questionNumber)
                    $ ans = leapModule.jpSeparater(ans)
                # 選択肢の取得
                $ opt = leapModule.getOption(questionNumber, JpEn, minNum, maxNum, optNum)
                $ selected = 0 #選んだ選択肢の識別番号

                # ストーリー時の立ち絵処理
                if (mode == 'story') & (progress == 3):
                    show leap mizugi question
                elif (mode == 'story') & (progress == 4):
                    show leap sport question
                elif (mode == 'story') & (progress == 6):
                    show leap uniform normal yami
                else:
                    show leap uniform question
                # 問題と選択肢の出題と表示
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

                # 正解時
                if(opt[selected] == ans):
                    # 正誤リストの問題番号目を1（正解）にする
                    $ tfList[questionNumber-1] = 1
                    # 正解音を鳴らす
                    play sound "audio/seikai.mp3" volume 0.1
                    # ストーリー時の立ち絵処理
                    if (mode == 'story') & (progress == 3):
                        show leap mizugi smile
                    elif (mode == 'story') & (progress == 4):
                        show leap sport smile
                    elif (mode == 'story') & (progress == 6):
                        show leap uniform normal yami
                    # 通常時の立ち絵処理
                    else:
                        show leap uniform smile
                    L "{color=#26aa5d}正解{/color}です！\n[que] は\n{color=#26aa5d}[ans]{/color} です。"
                # 不正解時
                else:
                    # 不正解音を鳴らす
                    play sound "audio/hazure.mp3" volume 0.1
                    # ストーリー時の立ち絵処理
                    if (mode == 'story') & (progress == 3):
                        show leap mizugi sad
                    elif (mode == 'story') & (progress == 4):
                        show leap sport sad
                    elif (mode == 'story') & (progress == 6):
                        show leap uniform normal yami
                    # 通常時の立ち絵処理
                    else:
                        show leap uniform sad
                    L "{color=#ED1616}不正解{/color}です。\n[que] は\n{color=#26aa5d}[ans]{/color} です。"
                
                $ renpy.block_rollback() #これ以前へのロルバの禁止 ズル防止のため
                # 問題番号を進める
                $ questionNumber += 1
        

            # スペル入力の時
            elif answerWay == 'spell':
                # 問題の取得
                $ leapNum, ans, que = leapModule.getExam(questionNumber)
                
                show leap uniform question

                # ヒントがONの時
                if withHint:
                    # 正解の頭文字を取得
                    $ initial = ans[0]
                    # 問題文の作成
                    $ kariQue = "第{0}問、Leap{1}番です。\n{2} は？\nHint: {3} から始まるよ。".format(questionNumber,leapNum,que,initial).replace('[','(').replace(']',')')
                # ヒントがOFFの時
                else:
                    # 問題文の作成
                    $ kariQue = "第{0}問、Leap{1}番です。\n{2} は？\n(hを入力すると頭文字が出ます。)".format(questionNumber,leapNum,que).replace('[','(').replace(']',')')
                
                # 問題の出題と表示
                $ spell = renpy.input(kariQue)

                $ renpy.block_rollback() #これ以前へのロルバの禁止 ズル防止のため

                # 入力がhの時
                if spell == "h":
                    # ヒントをONにする
                    $ withHint = True
                # 正解時
                elif spell == ans:
                    # 正誤リストの問題番号目を1（正解）にする
                    $ tfList[questionNumber-1] = 1
                    # 正解音を鳴らす
                    play sound "audio/seikai.mp3" volume 0.1

                    show leap uniform smile
                    L "{color=#26aa5d}正解{/color}です！\n[que] は\n{color=#26aa5d}[ans]{/color} です。"
                    
                    # ヒント設定の初期化（OFF）
                    $ withHint = False
                    # 問題番号を進める
                    $ questionNumber += 1
                # 不正解時
                else:
                    # 不正解音を鳴らす
                    play sound "audio/hazure.mp3" volume 0.1

                    show leap uniform sad
                    L "{color=#ED1616}不正解{/color}です。\n[que] は\n{color=#26aa5d}[ans]{/color} です。"
                    
                    # ヒント設定の初期化（OFF）
                    $ withHint = False
                    # 問題番号を進める
                    $ questionNumber += 1


            # "answerway"の設定がおかしい時
            else:
                "変数\"answerway\"の設定がバグってるっぴ！"

                # 最初に戻る
                jump initExamMode
    
    # 合計正解数の計算
    $ sumT = sum(tfList)
    # 正解率の計算
    $ rateT = round((sumT / numOfQue) * 100, 1) 
    # 復習モードでない時
    if isReview == False:
        # 特定ストーリー時1
        if (mode == 'story') & (progress == 3):
            # 全問正解の時
            if(numOfQue == sumT):
                show leap mizugi smile
                L "結果は、[numOfQue]問中全問正解でした。素晴らしいです！"
            # 一問間違いの時
            elif(numOfQue - sumT == 1):
                show leap mizugi normal
                L "結果は、[numOfQue]問中１問間違えでした。おしいです。"
            # 二問以上間違えた時
            else:
                show leap mizugi normal
                L "結果は、[numOfQue]問中[sumT]問正解で、正答率は[rateT]％でした。"
        # 特定ストーリー時2
        elif (mode == 'story') & (progress == 4):
            # 全問正解の時
            if(numOfQue == sumT):
                show leap sport smile
                L "結果は、[numOfQue]問中全問正解でした。素晴らしいです！"
            # 一問間違いの時
            elif(numOfQue - sumT == 1):
                show leap sport normal
                L "結果は、[numOfQue]問中１問間違えでした。おしいです。"
            # 二問以上間違えた時
            else:
                show leap sport normal
                L "結果は、[numOfQue]問中[sumT]問正解で、正答率は[rateT]％でした。"
        # 特定ストーリー時3
        elif (mode == 'story') & (progress == 6):
            pause 0.0
        # 通常時
        else:
            # 全問正解の時
            if(numOfQue == sumT):
                show leap uniform smile
                L "結果は、[numOfQue]問中全問正解でした。素晴らしいです！"
            # 一問間違いの時
            elif(numOfQue - sumT == 1):
                show leap uniform normal
                L "結果は、[numOfQue]問中１問間違えでした。おしいです。"
            # 二問以上間違えた時
            else:
                show leap uniform normal
                L "結果は、[numOfQue]問中[sumT]問正解で、正答率は[rateT]％でした。"

    # 復習モード設定の初期化（OFF）
    $ isReview = False

    jump endSelect

# 事後処理
label endSelect:
    # 特定ストーリー時の立ち絵処理
    if (mode == 'story') & (progress == 3):
        show leap mizugi normal
    elif (mode == 'story') & (progress == 4):
        show leap sport normal
    elif (mode == 'story') & (progress == 6):
        show leap uniform normal yami
    # 通常時の立ち絵処理
    else:
        show leap uniform normal

    # learnモードの時
    if mode == 'learn':
        L "この後どうされますか？"
        menu:
            L "この後どうされますか？"

            # 同じ設定でもう一回
            "もう一周する":
                Me "もう一周お願いできる？"

                L "了解です。ではいきますよ。"

                jump learn

            # モードは同じで範囲を変える
            "範囲を変える":
                Me "範囲を変えたいな。"

                jump rangeSelect
            
            # 同じ範囲でテストをする
            "この範囲でテストをする":
                $ mode = 'exam'

                Me "じゃあ、今の範囲でテストをしたいな。"

                L "了解です。"

                jump numOfQueSelect
            
            # 最初に戻る
            "戻る":
                jump modeSelect
    

    # examモードの時
    elif mode == 'exam':
        L "この後どうされますか？"
        menu:
            L "この後どうされますか？"

            # 復習モードに移行する
            # 全問正解の時非表示
            "間違えた問題を復習する" if rateT != 100:
                #復習モードをON
                $ isReview = True

                Me "間違えた問題を復習したいな。"

                L "了解です。ではいきますよ。"

                jump exam

            # 同じ設定でもう一回
            "同じ条件で続ける":
                Me "もう一回やりたいな。"

                L "了解です。ではいきますよ。"

                jump exam

            # 設定を変えてテスト
            "条件を変えて続ける":
                Me "別の条件でやりたいな。"

                jump rangeSelect
            
            # 最初に戻る
            "戻る":
                jump modeSelect


    # ストーリー時
    elif mode == 'story':
        # 元のlabelに戻る
        return
