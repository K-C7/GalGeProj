# とりまプレーンテキストで実装
# 細かな演出などは後!!こだわりだすと納期に間に合いません!!
# コピペ -> フォーマット -> デメ語の修正 -> 演出

# 呼び出しは"jump summer"でお願いします。


label summer:
    jump sum1


label sum1:
    scene bg black

    "８月の某所"
    "多くの学校では夏休みが始まり多くの学生が勉強や遊びに熱を入れてる中、そうではない男がいた"

    # 背景：海の家
    scene bg seahouse
    with dissolve
    play music "audio/everyday.mp3" volume 0.1 fadein 1.0

    Me "はあ～..."
    Me "友達はみんな夏休みを謳歌してるっていうのになんで俺は..."
    Me "海の家の手伝いをしなきゃいけないんだよ。"

    "そう、この男は親戚の仕事の手伝いに駆り出されていたのだ。"

    Me "折角の夏休みだってのに..."
    Me "なーんで目の前に海があるのに泳げないんだ。"

    # 登場：親戚
    show sinseki
    with dissolve

    Sinseki "おーい、サボってんじゃねーぞ。"

    Me "サボってませんよ。"

    Sinseki "あともう少ししたら開店だから、それまでに準備しろよ。"
    Sinseki "今日は晴れてるし最高の海水浴日和だ。"
    Sinseki "今日は人がたくさん来るぞぉ。"
    Sinseki "ちゃんと働いてくれよ？"

    hide sinseki
    with dissolve

    Me "ハイハイ、高校生の貴重な時間と引き換えに給料分の仕事はしますよ。"
    Me "（こっちはまだ宿題も終わってないってのに。）"
    Me "（まぁせっかく来たんだし頑張るか。）"

    # 背景：黒
    scene bg black
    with dissolve
    stop music fadeout 2.0

    "数時間後のお昼時"

    # 背景：海の家　音：ザワザワ
    scene bg seahouse
    with dissolve
    play music "audio/zawazawa.mp3" volume 0.05 fadein 1.0

    Me "（あ゛～～～～～）"
    Me "（忙しすぎるぅ～～）"
    Me "（こっちはちょっとした手伝いのつもりで来てるんだぞ。）"

    Kyaku "すみませーん。"

    Me "はーい。"

    Kyaku "ビールお願いできますかー？"

    Me "分かりました。はいどうぞ。"

    Ano "すみませーん。"

    Me "はーい..."
    Me "（ん？　どっかで聞いたことがあるような？）"
    stop music fadeout 1.0
    play sound "audio/wakeup.mp3" volume 0.5
    Me "！？！？！？"

    # 登場：Leap　Leap友達
    show leap normal at leapPos
    with dissolve
    show friend at left
    with dissolve
    play music "audio/retroparty.mp3" volume 0.05 fadein 1.0

    menu:
        "あ":
            $ like -= 5

            Me "あ。"

            show leap surprise
            L "あ。"

            Fri "ん？知り合い？"

            show leap normal
            L "えっ？あっいや、違うよ。"
        

        "Leapちゃん！？":
            $ like += 0

            Me "Leapちゃん！？"

            show leap question
            play sound "audio/poyon.mp3"
            L "先輩？"

            Fri "ん？知り合い？"

            show leap normal
            L "えっあ、うん、まぁ。"
        

        "ご注文は？":
            $ like -= 15

            Me "ご注文は？"

            show leap question
            L "..."

            show leap normal

    Fri "あのーすみません。"
    Fri "ジュースください。"

    Me "はーい、どれにしますか？"

    Fri "んー、コーラで。"
    Fri "Leapは？"

    L "えっ。"
    L "わ...わたしもコーラで。"

    Me "承りました。"
    Me "少しお待ちください。"
    Me "..."
    Me "（oh…）"
    play sound "audio/konwaku.mp3" volume 0.5
    Me "こういう感じで知り合いと会うってのは気まずいというかなんというか。"
    Me "まあ今は仕事中だし、仕事に集中しなきゃ。"
    Me "お待たせしました。"
    Me "こちらコーラ２つになります。"

    Fri "ありがとうございます。"
    Fri "よし、行こう。"

    L "..."

    Me "..."

    hide leap
    with dissolve
    hide friend
    with dissolve

    pause 2.0

    # 背景：黒
    scene bg black
    with dissolve
    stop music fadeout 2.0

    "それから一時間後"

    # 背景：海の家
    scene bg seahouse
    with dissolve
    show sinseki
    with dissolve
    play music "audio/everyday.mp3" volume 0.1 fadein 1.0

    Sinseki "もう昼の時間は過ぎたな。"
    Sinseki "おーい、そっちは大丈夫か？"

    Me "はい、大丈夫です。"

    Sinseki "よし、じゃあお前海行ってこい。"

    Me "え、いいんですか？"

    Sinseki "ああ、これからは客も少なくなるし俺一人でも回せる。"
    Sinseki "お前もせっかく海に来たんだから、海に行ってこい！"

    Me "わかりました、ありがとうございます。"
    Me "じゃあ、行ってきます。"

    scene bg black
    with dissolve
    stop music fadeout 1.0
    play sound "audio/run.mp3" fadein 0.5

    pause 1.0
    stop sound fadeout 0.5

    # 背景：海
    scene bg sea
    with dissolve
    play music "audio/sazanami.mp3" volume 0.1 fadein 1.0

    Me "とは言ったものの、なんかもう疲れちゃってはしゃぐ気分じゃないんだよなぁ。"
    Me "なんかその辺で休んでおこう。"
    Me "よし、じゃあこの辺で..."

    # 登場：Leap(水着)
    show leap normal at leapPos
    with dissolve
    stop music fadeout 1.0

    Me "あ..."

    show leap surprise
    L "あ..."

    show leap normal
    play music "audio/leap.mp3" volume 0.05

    Me "久しぶり。"

    L "お久しぶりです。"

    Me "さっきは何かごめんね。"

    L "いえいえこちらこそ。"

    menu:
        "友達はどうしたの":
            $ like -= 10

            Me "友達はどうしたの？"

            L "あっちの方で泳いでますよ。"

            Me "あっそうなんだ。"
            Me "君は泳がないの？"

            show leap question
            L "いえ、少し疲れてしましまして。"

            Me "あー、泳ぐのは結構疲れるよね。"

            show leap normal
            L "ですよね。自分の運動不足を実感しました。"

            Me "それはそれは。"

            L "先輩は泳がないんですか？"

            Me "本当は泳ぐつもりだったけど、いいかな。"

            show leap question_mark
            play sound "audio/poyon.mp3"
            L "何でですか？"

            Me "店の手伝いで疲れちゃって。"

            show leap normal
            L "そうなんですか、お疲れ様です。"


        "仕事の時は何かごめんね":
            $ like += 5

            Me "仕事の時は何かごめんね。"

            L "あっ、いえいえ。こちらこそすみませんでした。"

            Me "まさか手伝いに来た先でLeapちゃんと会うなんて思ってなくてさ。"

            L "へー、お手伝いで来ていらっしゃったんですね。"

            Me "そうなんだけど、まさか海の家の手伝いがこんなに辛いとは..."

            show leap question
            play sound "audio/konwaku.mp3" volume 0.5
            L "確かに大変そうでしたね。"

            Me "いやー本当に大変だった。"
            Me "海に来たのに泳ぐ元気もないよ。"

            show leap normal
            L "そうなんですか、私もちょうど泳ぎ疲れて休んでいるところなんですよ。"

            Me "そうなんだ。"


    # （①少々減少　②少々増加）

    Me "だけど泳がなくてもいいもんだね。"

    show leap question_mark
    L "なんでですか？"

    Me "ほら、青い空、白い砂浜、それに海。"
    Me "なんというか夏って感じでいいじゃん。"

    show leap normal
    L "確かにそうですね。"
    show leap question_mark
    L "ところで先輩、休憩はいつまでなんですか？"

    Me "んー、もう少し休んだらまた仕事に戻ろうかな。"

    show leap normal
    L "あっそうなんですね。"

    Me "どうしたの？休憩の時間なんて聞いて？"

    L "いや別に何でもないですよ。"

    Me "...もしかして暇なの？"

    L "まあ、ざっくりいうとそうなりますね。"

    Me "..."
    Me "よし、"
    menu:
        "よし、"

        "泳ぎに行くか":
            $ like -= 20

            Me "泳ぎに行くか。"

            show leap question
            L "疲れたって言ってませんでしたか？"

            Me "いや、Leapちゃんも退屈してるかなぁと思って。"
            Me "それにせっかく海に来たんだしさ。"

            play sound "audio/konwaku.mp3" volume 0.5
            L "いや、別に私はもう泳ぎたくないんですけど。"
            L "もう泳ぎ疲れました。"

            Me "あれ？そっか。"

            show leap normal

            #（大きく減少して③の選択肢に行く）
            jump sum2


        "ビーチバレーでもする？":
            $ like -= 10

            Me "ビーチバレーでもする？"

            play sound "poyon.mp3"
            show leap question
            L "二人でですか？"

            Me "ほら、海来たって感じがするじゃん。"

            L "疲れてるんじゃないんですか？"

            Me "まあ、疲れてるけど頑張るよ。"

            show leap normal
            L "いえいえ、無理しなくていいですよ。"
            L "私も疲れてますし。"

            Me "えぇ？あぁ、そう？"
            #（少し減少して③の選択肢に行く）
            jump sum2

        
        "英単語テストでもする？":
            jump sum2


label sum2:
    Me "じゃあ、英単語テストでもする？"

    show leap smile
    play sound "audio/kirakira.mp3" volume 0.2
    L "{size=*2.0}良いですね！{/size}"

    Me "うわ、ビックリした。"

    show leap normal
    L "あっ、すみません。つい。"
    L "だけどやりましょうよ。"

    Me "..."
    Me "君、本当に英語が好きなんだね。"

    L "もちろんです。"
    L "だけど先輩に一つ聞いてもいいですか？"

    Me "ん、なに？"

    show leap question_mark
    L "なんで英単語テストしようなんて言ったんですか？"

    Me "手軽にできて時間をつぶせるからかな。"

    show leap normal
    L "へー。"

    Me "あと、君が喜びそうだったから。"

    L "..."
    #（表情を赤らめて）(なお、素材はない)
    L "なるほど。"

    Me "？"
    Me "どうかした？"

    L "あっ、いえ何でもありません。"
    L "じゃあ問題だしますよ。"
    L "夏休みの成果、出してくださいね！"

    jump testPrepare


label sum3:
    play music "audio/leap.mp3" volume 0.05

    if 0 <= sumT <= 3:
        $ like -= 15
    
        show leap question
        L "...先輩？"

        Me "..."

        L "先輩。"

        Me "ハイ..."

        L "ちゃんと夏休みの宿題ちゃんとやってます？"

        Me "まだやってないです..."

        play sound "audio/konwaku.mp3" volume 0.5
        L "はぁ..."
        L "..."
        show leap normal
        L "ちゃんとやってくださいね。"

        Me "わかりました..."

        L "少なくとも英語はやらないとだめですよ、このままじゃ。"

        Me "ごめんなさい..."


    elif 4 <= sumT <= 7:
        $ like += 0

        show leap normal
        L "まあまあ頑張りましたね。"

        Me "俺も成長してるしね。"

        L "だけどこれで満足しちゃだめですよ。"
        L "今回できたからって、次回もいい結果とは限らないんですからね。"

        Me "ＯＫ、善処する。"

        show leap question
        L "そういえばちゃんと課題はやりましたか？"

        Me "...あ。"

        show leap normal
        L "...ちゃんと終わらせないとだめですよ？"


    elif 8 <= sumT <= 10:
        show leap smile
        L "さすがですね先輩。"
        L "夏休みに怠けず勉強してたんですね。"

        Me "いや、別に。"

        show leap normal
        L "本当ですかぁ～私には見え見えですよ。"

        Me "英語は勉強してるよ。"
        Me "まあ、宿題はまだしてないんだけどね。"

        L "え。"
        L "...先輩っていつもそうですよね。宿題のことを何だと思ってるんですか。"
        L "まったく、ちゃんと宿題はやってくださいね。"

        Me "ハイ。"


    # バッドエンド処理
    if(like < 0):
        stop music fadeout 1.0

        Me "だいぶ時間がたったな。"

        L "そうですね。"

        Me "そうだ、喉乾いたし飲み物取ってくるよ。"
        Me "Leapちゃんは何がいい？"

        L "私は何でもいいです。"

        Me "好きな飲み物とかは？"

        L "特にないですね。"

        Me "...そっか。"
        Me "じゃあ行ってくるね。"

        scene bg black
        with dissolve
        play sound "audio/walk.mp3" volume 0.05

        pause 2.0

        # 背景：海の家
        scene bg seahouse
        with dissolve
        stop sound

        Me "何の飲み物にしようかな。"
        Me "んー、コーラにしよう。"
        Me "Leapちゃんのはどうしようかなぁ～。"

        show sinseki
        with dissolve
        Sinseki "おい。"

        Me "何ですか？"

        Sinseki "ちょっと手伝ってくれ。"

        play sound "audio/doyo-n.mp3" volume 0.05
        Me "え、今急いでるんですけど。"

        Sinseki "いいだろ、ちょっとぐらい。"
        Sinseki "そもそも、君は手伝いに来てるんだろ。"
        
        Me "まあそうですけど..."
        Me "で、何やればいいんです？"

        # 暗転
        scene bg black
        with dissolve

        pause 2.0

        # 背景：海
        scene bg sea
        with dissolve

        Me "おじさんの手伝いしてたら結構時間が経っちゃったよ。"
        Me "Leapちゃん待ってくれてるかな。"
        Me "あっ、いた。"
        Me "Leapちゃ..."

        # 登場：Leap＆男
        show leap smile at leapPos
        with dissolve
        show otoko at left
        with dissolve
        play music "audio/distance.mp3" volume 0.1 fadein 2.0

        Me "あの男の人は誰だろう？知り合いかな？"
        Me "だけどそんな感じはしないな。もしかしてナンパかな？"
        Me "助けないと！"

        Man "俺たち話し合うね。"
        
        L "そうですね！"

        play sound "audio/shock.mp3" volume 0.1
        Me "！？"

        L "あっ、先輩。遅かったですね。"

        Man "へー先輩？"

        Me "ごめんね遅れて、はい飲み物。"
        Me "それでそちらの方は？"

        L "さっき出会ったんですけど、とても話の分かる方でとても英語が上手なんですよ。"
       
        Me "...そうなんだ。"

        L "先輩も一緒に話してみてはどうですか？"

        Man "Hello, I'm a new member of the board of directors. Today is a perfect day for swimming!"
        
        Me "おっ...おｋ。"

        L "It really is."
        
        Man "But still, there are so many people here today. I've lost my friend."
        
        L "I see! That's tough."
        
        Man "Well, but I'm sure those guys can handle it.HAHAHA!"
        
        L "haha."
        
        play sound "audio/konwaku.mp3" volume 0.5
        Me "（やばい、発音が良すぎて全然わかんねぇ。）"
        
        Man "That's when I saw this cute girl and I just had to ask her out."
        
        L "I don't think I'm cute.///"
        
        Man "You are cute. You think so too, don't you, senpai?"
        
        Me "えっ...ああ...ん？"
        Me "（なんて言ったのか聞き取れなかった。）"

        show leap question
        L "..."
        show leap normal

        Man "oops.英語が聞き取れなかったかな？"
        Man "まあいいや。それより君たち英語のテストしてなかったかい？"

        L "してました。"

        Me "（この人何で知ってるんだ？）"

        Man "それさ、Meにもやらしてくれよ。"

        show leap smile
        L "もちろんいいですよ。"
        L "ではいきますね。"

        # 暗転
        scene bg black
        with dissolve

        pause 2.0

        scene bg sea
        with dissolve
        show leap smile at leapPos
        with dissolve
        show otoko at left
        with dissolve

        L "わぁ～スゴイ！全部あってます。"

        Me "..."

        Man "こんなの楽勝だぜ。"
        Man "あと何十問、何百問出されても大丈夫だね。"

        L "ホントにすごいです。"

        Man "先輩とMeどっちがスゴイのかな？"

        show leap normal
        L "えっ、ああ。"
        L "あなたのほうがスゴイですけど、先輩だって負けてません！"
        show leap smile
        L "ですよね！先輩！"

        Me "あっ、もっもちろんだよ。"

        Man "へー、そうなんだ..."
        Man "君たち結構仲良いんだね。"
        Man "もしかして付き合ってたりするの～？"

        show leap surprise

        Me "！？"
        
        L "！？"

        Man "どうなのどうなの？"

        show leap question
        L "いや、別に付き合ってるとかはないです。"

        Man "付き合ってないんだね"

        Me "..."

        Man "おっと！もうこんな時間だ。"
        Man "そろそろあいつらを探しに行かなきゃな。"

        show leap normal
        L "お友達をですか？"

        Man "That's right."
        Man "だけどMeこの海の事ほとんど知らないんだよ。"
        Man "だからさLeapちゃん探すの手伝ってくれないかな。"

        Me "いやそれなら僕が。"

        Man "別に構わないが、Meのfriendsはみんなアメリカ人だ。よ"
        Man "この人ごみの中、仮に見つけたとして君は英語で話せるのかい？"
        
        Me "ぐぅ..."

        L "そっそれに先輩は海の家の手伝いがあるんですよね。"
        show leap smile
        L "人助けは私に任せてください。"

        Me "Leapちゃん..."

        L "それでは失礼します。先輩。"

        Man "じゃ、そういう事だから。"
        Man "Bye bye, senpai."

        $ badEndCode = 4
        jump badEnd_call

    Me "だいぶ休んだな。"

    L 'そうですね。'
    L "いい暇つぶしになりました。"
    L "先輩はこの後も例のお手伝いをやるんですか？"

    Me "あー、多分。"

    Sinseki "おーい何処だー。"

    show leap question_mark
    L "あれ？先輩呼ばれてるんじゃないんですか？"

    Me "あっホントだ！"

    Fri "Leapちゃん何処～？"

    Me "あれは..."

    show leap normal
    L "私も呼ばれてるみたいですね。"
    L "..."
    L "今日はもうお別れですね。"

    Me "そうだね。"

    L "次あった時も英語の問題出してあげますので、覚悟しておいてくださいね。"
    
    Me "お手柔らかにお願いするよ。"
    Me "じゃあ俺そろそろ行くね。"

    L "そうですね、私も行かなきゃ。"
    show leap smile
    L "さようなら！"

    Me "じゃあね。"

    scene bg black
    with dissolve

    jump rest