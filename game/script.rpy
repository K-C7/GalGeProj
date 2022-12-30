define L = Character('Leapちゃん', color="#26aa5d")
define Me = Character('自分', color="#000000")

init:
    $ import module.leapModule as leapModule

    image bg classroom evening = im.Scale("bg classroom evening notrim.jpg", 1280, 720)

label start:

    scene bg classroom evening

    show leap at center:
        zoom 1.2

    jump modeSelect

label modeSelect:

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
            L "第[questionNumber]問、Leap[leapNum]番です。\n[que]は？"

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
            L "正解です！[ans]の意味は[que]です。"
        else:
            $ leapModule.ansExam(False)
            L "不正解です。[ans]の意味は[que]です。"
        
        $ questionNumber += 1
            
    $ sumT = leapModule.resultExam()

    L "結果は、[numOfQue]問中[sumT]問正解でした。"
    L "もう一度、同じ条件で練習しますか？"

    menu:
        "Yes":
            L "了解です。ではいきますよ。"
            call examMode(part,numOfQue)
            jump exit
        
        "No":
            L "了解です。今日もお疲れさまでした。"
            jump exit
    

label exit:
    $ renpy.quit()