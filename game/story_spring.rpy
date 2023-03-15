label spring:
    $ like_meter = True

    jump spring1

label spring1:
    scene bg black

    "入学式が終わってから数週間後の夕方..."

    scene bg library evening
    with dissolve
    play music "audio/routine.mp3" volume 0.05

    Me "くぅ～、なんで俺が図書委員になってるんだ。"
    Me "まあ、別に本が嫌いってわけじゃないけど。"
    Me "しかしなんで面倒なのになっちゃうんだろうな。"
    Me "まあ、全部じゃんけんで負けた俺が悪いんだけどさ。"
    Me "はあ..."
    Me "...よし、マイナスにとっても仕方がない。もっとプラスに考えよう。"
    Me "ん？そういえば図書委員の当番は二人だったと思うけど、もう一人はどうしたんだろう？"
    Me "一年生のはずだけど、まさかサボり...?"
    
    play sound "audio/run.mp3"

    pause 1.0
    stop sound fadeout 0.5

    show leap uniform normal at leapPos
    with dissolve
    play music "audio/leap.mp3" volume 0.05
    Ano "{size=*2.0}すみませーん、遅れましたー！{/size}"

    Me "わぁ、ビックリした。"
    Me "あれ、君は確か..."
    menu:
        Me "あれ、君は確か..."

        "Leapちゃん":
            $ renpy.block_rollback()

            Me "Leapちゃんだよね。"
            
            $ like = likeChanger(like, 5)
            show leap uniform smile
            L "あっ、はいそうです。覚えてくれたんですね。"

            show leap normal
        
        "Brightstageちゃん":
            $ renpy.block_rollback()

            Me "Brightstageちゃんだよね。"
            
            $ like = likeChanger(like, -10)
            show leap uniform question
            play sound "audio/konwaku.mp3" volume 0.5
            Ano "違いますよ。私の名前を忘れたんですか。"
            show leap uniform normal
            L "私の名前はLeap\nエル　イー　エー　ピー　Leapですよ！"
        
        "新明説漢文ちゃん":
            $ renpy.block_rollback()

            Me "新明説漢文ちゃんだよね。"

            $ like = likeChanger(like, -20)
            show leap uniform question sweat
            play sound "audio/konwaku.mp3" volume 0.5
            Ano "違いますよ。ていうかそれまったく英語じゃないじゃないですか。"
            show leap uniform normal
            L "私の名前はLeap\nエル　イー　エー　ピー　Leapですよ！"

    L "それより遅れてすみません。"
    L "その、ちょっと用事がありまして..."

    menu:
        L "その、ちょっと用事がありまして..."

        "用事って？":
            $ renpy.block_rollback()

            Me "用事って？"

            L "友達に勉強を教えてまして。"

            Me "へー、やっぱり英語？"

            show leap uniform question
            play sound "audio/hit.mp3" volume 0.5
            L "やっぱりって何ですか。"

            Me "ごめんって。でも英語なんでしょ？"

            show leap uniform sad
            $ like = likeChanger(like, 5)
            L "まあそうですけど..."

            Me "..."

            L "..."
        
        "遅刻とは感心しないな":
            $ renpy.block_rollback()

            Me "遅刻とは感心しないな。"

            $ like = likeChanger(like, -15)
            show leap uniform sad
            L "すみません..."

            Me "許す。"

            $ like = likeChanger(like, 5)
            show leap uniform normal
            L "あ、意外とあっさり許してくれるんですね。"

            Me "怒るだけ損だしね。"

            L "良かった。"

            Me "それに、俺もまだほとんどしてないしね。"

            L "そうなんですね。"

        "君がもう一人の当番？":
            $ renpy.block_rollback()

            Me "君がもう一人の当番？"

            L "あっはいそうです。"
            L "ていうか図書委員会の役割分担の時に会ったと思うんですけど..."

            Me "あれ？そうだっけ？"

            $ like = likeChanger(like, -20)
            show leap uniform question sweat
            play sound "audio/konwaku.mp3" volume 0.5
            L "...先輩？"

            Me "いや、あのー、そのー..."
            Me "別に忘れてたわけじゃなくて、ほら、あれだよ。"
        
            show leap uniform question
            L "どれですか。"

            Me "..."
        
    show leap uniform question
    L "そういえば、図書委員の仕事って何するんですか？"

    Me "本の貸し出しとか返却に来た人の対応だとか、後は本棚の整理かな？"

    L "だけど放課後に本を借りたり返しに来たりする人っているんですか？"

    Me "意外といるんじゃない？知らないけど。"

    show leap uniform normal
    L "曖昧ですね。"

    Me "まあ、ほら待ってたら来るかもしれないだろ？"
    Me "とりあえず仕事が終わるまでは待たないと。"

    scene bg black
    with dissolve

    "数十分後..."

    scene bg library evening
    with dissolve
    show leap uniform normal at leapPos
    with dissolve

    Me "（...誰も来ない...）"
    Me "（き、気まずい...）"
    Me "（なんか話題でも振ったほうがいいかな。)"
    Me "..."

    L "..."

    Me "（うーん、どうしたものか。）"

    show leap uniform question
    L "先輩？"

    play sound "audio/wakeup.mp3" volume 0.5
    Me "うぉっ、な、なんだい？"

    L "英語の勉強しててもいいですか？"

    Me "ああ。別に構わないよ。"
    show leap uniform normal
    Me "（本当に英語のことが好きな子なんだなぁ。）"
    Me "（ていうか、改めて考えてみてもやっぱりおかしいよなぁ。）"
    Me "（名前がLeapってなんだよ、しかも英語好き。）"
    Me "（名が体を表しすぎてる感じだ。）"

    L "..."

    Me "..."
    Me "（とても静かになってしまった。）"
    Me "（ここは責任をもってなんか話題を振らないと。）"
    Me "そういえば、"
    menu:
        Me "そういえば、"

        "君は何で図書委員になったの？":
            $ renpy.block_rollback()

            Me "君は何で図書委員になったの？"

            show leap uniform question
            L "私ですか？"

            Me "うん。なんか理由があるのかなぁと思って。"
            Me "友達と一緒の委員会に入りたいとか、図書委員に思い入れがあるとかさ。"

            L "...特にないですね。"
            show leap uniform normal
            L "まぁ強いていうなら本を読むのは好きですね。"

            Me "そうか。"

            show leap uniform question
            L "じゃあ先輩はなんで図書委員になったんですか？"

            Me "じゃんけんで負けたから。"

            $ like = likeChanger(like, -10)
            L "..."

            Me "..."

            show leap uniform normal
        
        "本は好き？":
            $ renpy.block_rollback()

            Me "本は好き？"

            $ like = likeChanger(like, 5)
            L "本ですか？まあまあ好きですよ。"

            Me "へえ、そうなんだ。ジャンルとかは？"

            L "別にこれといった好きなジャンルはないですね。"
            L "でもSFとかファンタジーとかはよく読みますね。"
            L "一番最近に読んだものはハリー〇ッターですし。"

            Me "ハリー〇ッターね。知ってる知ってる。映画のやつね。"
            
            L "はいそれです。"

            Me "小説だとだいぶ長いんじゃない？"

            L "はい。しかもちょっと難しい英単語とかあって読みごたえがありました。"

            Me "それは良かった。ん、英単語？"
            play sound "audio/konwaku.mp3" volume 0.5
            Me "...もしかして原文のほう？"

            show leap uniform smile
            L "はいそうですよ。"

            Me "はいそうですよ、って。まぁ君からすれば当たり前なのかな？"

            show leap uniform normal
            L "先輩も本が好きなんですか？"

            Me "ん－、普通かな。てか漫画しか読まないんだよね。"

            L "そうなんですか。"

    Me "あれ、結構時間経ってるね。"

    show leap uniform surprise
    L "本当だ。あと少しですね。"
    show leap uniform question
    L "だけどなんかやり残したことがある気がするんですよね。"

    Me "やり残したこと？なんかあったっけ？"

    L "んー..."
    show leap uniform surprise
    play sound "audio/hit.mp3" volume 0.5
    L "{size=*2.0}あっ思い出した！{/size}"
    show leap uniform normal
    L "先輩～、忘れちゃいけないのは私じゃなくて先輩じゃないですか。"

    Me "え、俺？"

    L "私と初めて会った日の約束覚えてますか？"

    Me "約束？...あ、もしかして..."

    L "はい、そのもしかしてですよ。"
    show leap uniform smile
    play sound "audio/kirakira.mp3" volume 0.2
    L "英単語テストの時間ですよ！"
    show leap uniform normal
    stop sound
    L "先輩があれからどれくらい英語を勉強したのか確かめないとですね。"
    L "じゃあ始めますよ。"

    jump testPrepare

label spring2:
    play music "audio/leap.mp3" volume 0.05
    if 0 <= sumT <= 3:
        $ renpy.block_rollback()
        $ like = likeChanger(like, -15)

        show leap uniform question sweat
        L "先輩..."

        Me "ハイ..."

        L "あれからちゃんと勉強しました？"

        Me "いいえ..."

        show leap uniform question
        play sound "audio/konwaku.mp3" volume 0.5
        L "はぁ、ちゃんとやらないとだめじゃないですか。"
        L "英語は基礎ができてなんぼ、このままじゃ先輩英語がもっとダメになってしまいますよ。"

        Me "次こそは本気出します..."
        
        show leap uniform normal

    elif 4 <= sumT <= 7:
        $ renpy.block_rollback()
        $ like = likeChanger(like, 5)

        show leap uniform normal
        L "及第点って感じですね。"

        Me "まあまあだろ。どう？"

        L "どう？じゃないですよ。"
        L "及第点ってだけで別にできてるって程でもないでしょうに。"
        L "もし次があるんだとしたら、次はもっと良くなってくださいよ。"

        Me "精進いたします。"
    
    elif 8 <= sumT <= 10:
        $ renpy.block_rollback()
        $ like = likeChanger(like, 15)

        show leap uniform surprise
        L "ちゃんとできてるじゃないですか。"
        show leap uniform smile
        L "英語を勉強してくれたんですね。"

        Me "ふっ、俺だってやるときはやるんだよ。"

        show leap uniform normal
        L "先輩のことだからできないとばかり思ってましたよ。"

        Me "それはどういう意味だよ。"

        show leap uniform smile
        L "冗談ですよ～。"
        show leap uniform normal
        L "さすが先輩といったところでしょうか。"

        play sound "audio/syakin.mp3" volume 0.1
        Me "(｀・v・)ｴｯﾍﾝ!!"

        L "{size=*0.8}チョロ{/size}"

        play sound "audio/poyon.mp3"
        Me "なにか言った？"

        L "何も言ってないですよ。"

    if like < 0:
        jump badEndSpring
    else:
        jump normalEndSpring
    
label normalEndSpring:
    Me "そうこうしてるうちにもう時間になったな。"
    Me "結局誰も来なかったね。"
    
    L "本当ですね。"
    L "だけどそれなりには楽しかったですよ。"
    show leap uniform smile
    L "先輩と話せましたし、英単語テストもできましたし。"

    Me "それは良かった。"

    show leap uniform normal
    play sound "audio/poyon.mp3"
    L "先輩も英単語テストできて良かったですよね？"

    menu:
        L "先輩も英単語テストできて良かったですよね？"

        "もちろん":
            Me "もちろん。"
            Me "次があったらまたよろしく頼むよ。"
        
    $ like = likeChanger(like, 5)
    L "こちらこそよろしくお願いします。"
    L "なにげに問題出すほうも楽しいですしね。"

    Me "それはそれは。"

    L "では帰りましょうか。"

    Me "そうだね。"

    scene bg black
    with dissolve
    stop music fadeout 2.0

    jump rest

label badEndSpring:
    $ renpy.block_rollback()
    $ like_meter = False
    stop music

    Me "そうこうしてるうちにもう時間になったな。"
    Me "結局誰も来なかったね。"

    show leap uniform sad
    L "..."

    Me "..."
    Me "俺は結構楽しかったけど君は？"

    L "..."

    Me "..."

    play sound "audio/wakeup.mp3" volume 0.5
    L "先輩。"

    Me "なに？"

    L "用事を思い出したので、お先に失礼します。"

    play sound "audio/run.mp3"

    pause 1.0

    stop sound fadeout 0.5
    hide leap
    with dissolve

    Me "えっ、あ..."
    Me "ちょっと馴れ馴れしかったかな、失敗したな。"

    scene bg black
    with dissolve

    "それから数日後"

    scene bg rouka day
    with dissolve
    show leap uniform surprise at leapPos
    with dissolve

    Me "あ。"

    L "あ。"

    show leap uniform sad

    Me "あっ、えっと..."

    L "すみません失礼します。"

    Me "分かったよ。"

    play sound "audio/run.mp3"

    pause 1.0

    stop sound fadeout 0.5
    hide leap
    with dissolve

    Me "嫌われちゃったかな。"

    scene bg black
    with dissolve

    "その日の放課後"

    scene bg rouka evening
    with dissolve

    Me "はぁ、今日はなんかどっと疲れたな。早く帰ろ。"

    Ano "ね～あれ面白いよね。"
    Ano "それな～。"

    Me "うるさいな。廊下まで聞こえてくるぞ。\nやれやれだぜ。"

    Ano "あっそういえばさ、あれどうなったん？Leap？"

    show leap uniform normal at leapPos
    with dissolve

    Me "！？"

    Fri "あれだよ、ちょっと気になるとか言ってた先輩だよ。"

    Me "！？！？！？"

    L "あぁ、あの先輩ね。"

    Fri "そうそう、なんか進展でもあった？"

    L "ん－、特にないかな。"
    L "というか違ったかも。"

    Fri "何が？"

    L "あの先輩、思ってたのと少し違ったかもしれない。"

    play music "audio/distance.mp3" volume 0.1
    Me "えっ..."

    Fri "あー、パット見でいいな～と思って近づいてみたら、思ってたのと違ったパターンね。わかるわ～。"

    L "うん。"
    L "初めて会ったときは良いなって思ったけど、"
    L "この前の委員会でなんか苦手になっちゃったな。"

    Me "..."

    stop music
    $ badEndCode = 3

    jump badEnd_call