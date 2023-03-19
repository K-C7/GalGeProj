label winter:
    $ like_meter = True

    jump winter1

label winter1:
    scene bg black
    
    "体育大会も終わり、気温もぐっと下がり始めたころ。"
    "ある大きな問題を抱えている男がいた。"

    scene bg classroom day
    with dissolve
    play music "audio/morning.mp3" volume 0.05 fadein 1.0
    show boyssilhouette at Position(xancor=0.0, ypos=1.5)
    with dissolve

    $ zako1Name = "生徒１"
    $ zako2Name = "生徒２"

    Zako1 "もう少しでクリスマスだな。"

    Zako2 "ああそうだな。"

    Zako1 "...お前クリスマスに一緒に過ごす人いる？"

    Zako2 "...いねぇよ。"

    Zako1 "...やっぱりか。"

    Zako2 "やっぱりってなんだよ。"

    hide boyssilhouette
    with dissolve

    Me "..."
    Me "はぁ～あ。そろそろクリスマスか..."
    Me "子供の頃はウキウキしてたけど、高校生にまでなると一人でいる現実に泣けてくるよ。"
    Me "俺にもクリスマスを共にしてくれる彼女できねぇかなぁ～"
    Me "まぁ俺には無縁の話か。"

    pause 2.0

    show leap uniform question at leapPos
    with dissolve
    play music "audio/leap.mp3" volume 0.05
    L "何が無縁の話なんですか？"

    menu:
        L "何が無縁の話なんですか？"

        "うわでた":
            $ renpy.block_rollback()
            $ passedDemon = False

            Me "うわでた。"

        "出たな英単語テストの悪魔！":
            $ renpy.block_rollback()
            $ passedDemon = True

            Me "出たな英単語テストの悪魔！"

        "悪霊退散":
            $ renpy.block_rollback()
            $ passedDemon = False

            Me "！悪霊退散！"

    if passedDemon == False:
        $ like = likeChanger(like, -10)
        
    show leap uniform question sweat
    L "なんですかその言い方は！"
    show leap uniform question
    L "まったく...私のことを何だと思ってるんですか..."

    Me "ごめんごめん。"

    if passedDemon:
        Me "だけど実際そうじゃん。"

        L "まぁ...否定はしませんけど..."

    show leap uniform sad
    L "あーあ、せっかくクリスマス一緒に過ごしてあげようかと思ってたんですけどねぇ。"

    Me "！？！？！？"

    show leap uniform normal
    L "でもなー、どうしますかねー？"
    L "今謝るなら許してあげないこともな..."

    Me "すみませんでした。"

    show leap uniform question sweat
    L "は、速いですね。"

    Me "クリぼっちは嫌なんです...お願いします..."

    show leap uniform normal
    L "まったく...そんなに言うなら仕方ないですね～"
    L "クリスマスは一緒にいてあげてもいいですよ？"

    Me "本当に！？ありがとう！"

    L "でも、今年のクリスマスは学校と被ってるんですよねー。"

    show leap uniform question
    L "それなので、クリスマスの日の放課後に集合して遊びにでも行きます？"

    Me "そうだね！そうしよう。"

    show leap uniform surprise
    L "あ、ちょっと待ってくださいね。"

    play sound "audio/writing.mp3" volume 0.1

    pause 2.0

    stop sound

    show leap uniform normal
    L "これ、私の電話番号です。何かあったら連絡してくださいね。"
    
    Me "ああ、ありがとう。じゃあ俺のも...{w=2.0}はい。"

    L "ありがとうございます。"
    show leap uniform surprise
    L "あっ、もう少しで授業始まっちゃいますね。"
    show leap uniform normal
    L "では私は戻りますね。また会いましょう。"

    Me "うん、じゃあね。"

    scene bg black
    with dissolve
    stop music fadeout 2.0

    "クリスマス当日"

    scene bg genkan
    with dissolve
    play music "audio/routine.mp3" volume 0.05

    Me "せっかくのクリスマスだけども、相変わらず学校は疲れるなぁ。"
    Me "Leapちゃんはまだかな。まだ来てなさそうだけど..."

    show leap uniform surprise at leapPos
    L "先輩先輩、どこ見てるんですか？"

    play music "audio/leap.mp3" volume 0.05
    Me "うぉ、いつの間に。"
    
    show leap uniform question
    L "今来たところですよ。{p}それより遅れてすみません。部活を早く切り上げるつもりだったんですけど..."

    menu:
        L "今来たところですよ。それより遅れてすみません。部活を早く切り上げるつもりだったんですけど..."

        "来るのが遅い":
            $ renpy.block_rollback()

            Me "来るのが遅い！"

            show leap uniform sad
            $ like = likeChanger(like, -10)
            L "す、すみません..."

            Me "別に謝らなくていいよ。ただ、今日が本当に楽しみでさ。"

            show leap uniform surprise
            L "えっ..."

            Me "もし来なかったらどうしようかと思って、すごく心配してたんだ。"

            show leap uniform normal
            $ like = likeChanger(like, 15)
            L "あっ、ああ、ありがとうございます。"
        
        "別にいいよ":
            $ renpy.block_rollback()

            Me "別にいいよ。"

            show leap uniform question
            L "先輩、もしかして怒ってます？"

            Me "いや、怒ってないよ。"

            show leap uniform question sweat
            L "怒ってますよね？"

            Me "怒ってないって。"

            show leap uniform sad
            $ like = likeChanger(like, -20)
            L "ごめんなさい..."

            Me "いや、だから......ごめん。"

        "大丈夫":
            $ renpy.block_rollback()

            Me "こっちも今来たところだから大丈夫だよ。"

            L "そうなんですか。なら良かったです。"

            Me "（まあ結構待ったんだけど。）"
            
        
    Me "じゃあ行こっか。"

    show leap uniform question
    L "行く場所は決まってるんですか？"

    Me "うん。" 

    show leap uniform normal
    L "じゃあ、今日のデートは先輩に任せますね。"

    Me "デッデート！！？？"

    show leap uniform surprise
    L "えっ気づいてなかったんですか！？"
    show leap uniform normal
    L "男女でクリスマスにお出かけするんですから、{w}これはれっきとしたデートですよ。"
    L "ちゃんとリードしてくださいね。"

    Me "わっわかったよ。"

    show leap uniform smile
    L "お願いしますね、先輩。"

    scene bg black
    with dissolve
    stop music fadeout 2.0

    "デートは先輩のプラン通り順調に進み、{p}二人は放課後のクリスマスを存分に楽しんだ。"
    "そして、最後の目的地、駅前のイルミネーションに向かう。"

    scene bg irumi
    with dissolve
    play music "audio/zawazawa.mp3" volume 0.05 fadein 1.0
    show leap uniform normal at leapPos
    with dissolve

    Me "駅前だし結構混んでるね。"

    L "本当ですね。"

    Me "今日一緒にいてくれてありがとね。"

    L "こちらこそ、先輩とのデート、楽しかったですよ。"
    L "本当に初めてのデートですか？"

    Me "そうだよ。"

    show leap uniform normal
    L "じゃあ、私が初めてのデート相手ですね。"

    Me "なっ...何言ってんだよ。"

    show leap uniform smile
    L "ふふっ"

    Me "..."

    show leap uniform normal
    L "..."

    Me "...綺麗だね。"

    L "...何がですか？"

    menu:
        L "...何がですか？"

        "イルミネーション":
            $ renpy.block_rollback()

            Me "イルミネーションだよ。"

            $ like = likeChanger(like, -20)
            show leap uniform sad
            L "..."
            L "確かにきれいですね。"
            L "私なんて霞んでしまうくらいに..."

            Me "...？"
        
        "Leapちゃん":
            $ renpy.block_rollback()

            Me "...Leapちゃんだよ。"

            $ like = likeChanger(like, 10)
            show leap uniform question sweat
            L "えっ...先輩、もう一度言ってください。"

            Me "何度も言わせないでよ、恥ずかしい..."

            L "綺麗だなんで初めて言われました。"
            show leap uniform smile
            L "先輩、ありがとうございます！"

            Me "...どういたしまして。"
        
        "あそこのお姉さん":
            $ renpy.block_rollback()

            $ like_meter = False

            jump winter_bad
    
    show leap uniform question
    L "...{p}先輩？"

    Me "どうしたの？"

    L "私と初めて会った日のこと覚えてます？"

    Me "もちろん。"

    show leap uniform normal
    L "それから、先輩とはいろいろありましたよね。"

    Me "確かにね。委員会が同じだったり、海で出会ったり、体育大会一緒に出たり..."
    Me "...そして、こうしてLeapちゃんと一緒にデートしてるしね。"
    Me "出会いは街角でぶつかっただけってのにね？"
    Me "不思議だね。"

    L "確かに...そうですね。"
    L "..."
    L "......."
    show leap uniform question
    L "...先輩..."
    L "英単語テスト、しませんか..."

    Me "え、英単語テスト！"
    Me "えっ今！？"

    L "はい...今..."

    Me "（あれ？すごい真剣な顔してる？）"
    
    show leap uniform normal
    L "では行きますよ。"

    call testPrepare

    play music "audio/leap.mp3" volume 0.05

    if 0 <= sumT <= 6:
        $ renpy.block_rollback()
        $ like = likeChanger(like, -15)

        show leap uniform question
        L "先輩..."
        L "このテストももう五回目です。"
        L "それで、７割も取れないってどういうことですか？"

        Me "えっああ、ごめん。"

        show leap uniform question sweat
        L "ちゃんと勉強してます？"

        Me "まっまあ、それなりには..."

        show leap uniform question
        L "それなりじゃダメです。もっとちゃんとやってください。"

        Me "わっ分かったよ。"
        Me "だけど、何でそんな言うの？"

        show leap uniform surprise
        L "えっ..."
        show leap uniform question
        L "あ..."
        show leap uniform sad
        L "すみません。"

        Me "いやいや、こっちこそごめんね。"

    elif 7 <= sumT <= 10:
        $ renpy.block_rollback()
        $ like = likeChanger(like, 10)

        L "流石先輩ですね。"

        Me "そうかな。"

        L "最初あった時とは見違えるように成長しましたね。"

        Me "これも全部君のおかげだよ。"

        L "そ、そう言われると照れますね。"

        Me "本当にそう思う。"
        Me "一年前は本当に嫌いだった英語だけれども、{p}今となっては君との英単語テストも楽しいと思えるよ。"

        show leap uniform smile
        L "それはうれしい限りです。"
        show leap uniform sad
        L "{size=*0.8}もう私がいなくても大丈夫なくらいですね。{/size}"

        Me "何か言った？"

        show leap uniform normal
        L "何でもないです。"

    Me "じゃあ、そろそろ帰ろうか。"

    show leap uniform normal
    L "そうですね。"

    Me "..."

    L "..."

    scene bg black
    with dissolve

    pause 2.0

    scene bg train night
    with dissolve
    play music "audio/train.mp3" volume 0.2 fadein 1.0
    show leap uniform normal at leapPos
    with dissolve

    "そして、同じ電車に乗り家に帰る二人。"
    "二人は終始無言であった。"
    "それは、楽しいデートの余韻に浸っているからなのか、\n明日からのいつも変わらない日々を喘いでいるのか。"
    "もしくはその両方なのか、はたまたまた違う大きな理由があるのかは分からない。"
    "だがしかし、二人の間に今日を名残惜しむ感情が流れていることは確かであった。"

    stop music fadeout 1.0
    Cd "駅に到着しました。車内にお忘れ物のないようご注意ください。"
    Cd "お出口は左側です。扉にご注意ください。"

    Me "着いたね。"

    L "そうですね。"

    scene bg station night
    with dissolve
    show leap uniform normal at leapPos
    with dissolve

    Me "今日は本当に楽しかったよ、ありがとう。"

    L "私の方こそありがとうございました。"
    L "思ってた以上に楽しかったです。"

    Me "また、行けたらいいね。"

    L "また、ですか..."

    Me "Leapちゃんが良かったら、また一緒にデートできないかな。"

    L "...{p}...もちろんです。"
    show leap uniform smile
    L "いつかまたデートしましょう、約束ですよ？"

    Me "あぁ、約束だ。"
    Me "じゃあ、僕こっちだから。じゃあね。"

    show leap uniform normal
    L "先輩..."
    L "さようなら..."

    scene bg black
    with dissolve

    jump rest

label winter_bad:
    $ renpy.block_rollback()

    Me "あそこのお姉さんがだよ。"

    $ like_meter = False
    show leap uniform question
    stop music fadeout 1.0
    L "...え？"
    show leap uniform sad
    L "...何でそんなこと言うんですか？"

    Me "あっ、いや今の冗談で..."

    L "...先輩。"

    Me "...何でしょうか。"

    L "..."
    L "先輩は、何でいつも私のことを見てくれないんですか？"

    Me "え？"
    Me "いや、そんなつもりは..."

    L "先輩が見てくれないならもういいです。"
    
    Me "？Leapちゃん？"

    L "先輩、今日は先に失礼します。"
    
    Me "え、あ、ちょっと待っ..."

    show leap uniform normal yami
    L "冗談でも言って良いことと悪いことがあるんですよ、先輩。"
    L "また一つ賢くなりましたね。"
    L "では、さようなら。"

    Me "..."

    scene bg black
    with dissolve

    "駅前の綺麗なイルミネーションで別れた二人。"
    "その二人には決定的な溝ができてしまった。"
    "...そのはずだった。"
    "クリスマスから数日後..."

    scene bg classroom day
    with dissolve

    Me "..."
    Me "あれから数日経ったけど、Leapちゃんと会わないな..."
    Me "何であんなこと言ってしまったんだろう..."
    Me "おふざけであんなこと言わなきゃ..."
    Me "..."
    Me "...謝りに行こう。"
    Me "ちゃんと謝れば許してくれるかもしれない。"
    Me "俺たちには一年間の思い出があるんだ。"
    Me "そうだ、きっと大丈夫。"

    scene bg black
    with dissolve

    "その日の放課後"

    scene bg classroom evening
    with dissolve

    Me "でも、どうやってLeapちゃんに謝ろう。"
    Me "Leapちゃんの家知らないしなぁ。{w}...あっ！"
    Me "そういえば、連絡先もらってたな...あったあった。"
    Me "だけど、いきなり電話だとLeapちゃんも困るよな..."
    Me "...{w}いや、くよくよしててもだめだ。"
    Me "ここは誠心誠意、謝ろう。"

    "ﾄｫﾙﾙﾙﾙﾙﾙ... ﾄｫﾙﾙﾙﾙﾙﾙ..."

    Me "あれ？電話に出ないな。"
    Me "いや...それもそうか。{p}そりゃ出ないよなぁ。"
    Me "...切るか。"

    "ﾋﾟｨ"

    Me "！？（つながった...！）{p}..."

    L "..."

    "電話がつながったというのに、二人は無言だった。"
    "そして、その沈黙を先に破ったのは..."

    L "先輩？"

    "Leapだった。"

    L "お久しぶりですね。"

    Me "あっ、ああ、久しぶりだな。"
    Me "ど、どうしたの？。"
    Me "最近学校に来てないじゃん。"
    Me "何かあったの？"

    L "先輩には関係ないことですよ。"

    Me "えっ？"

    L "いえ、違いますね。{p}あのクリスマスの日のこととは関係ないというほうが正しいですね。"

    Me "そうか..."
    Me "だけど、学校に来ないのは..."

    L "先輩！そんなことより先輩に大事なお話があるんです。"

    Me "ど、どうしたの？"

    L "だけどそれは電話では話すことはできません。"
    L "なので、今から送る場所まで来てください。"
    L "安心してください。先輩にも馴染みの場所ですから。"

    Me "...分かった。"

    scene bg black
    with dissolve
    play music "audio/run.mp3" fadein 1.0

    "送られた場所の所まで、急いで向かう先輩。"
    "とても不穏な気配を感じながらも、{p}これを逃したらもう次はないという直感からか、足に力が入る。"
    "そして、到着した。"

    stop music fadeout 1.0

    Me "ここって..."

    scene bg shrine day
    with dissolve

    show leap uniform normal yami at leapPos
    L "先輩...意外と早かったですね。"
    L "もう少し、遅いと思ってました。"

    Me "...それで話ってなんだ？"

    L "まあまあそんな焦らずに。とりあえず息を整えましょう。"

    "先輩が少し息を整えたのは見計らってLeapが言う。"

    L "先輩..."

    Me "なに？"

    L "私があのとき何を言ったか覚えてます？"

    Me "あの時...？"

    L "はい、クリスマス、駅前のイルミネーションで別れるときに。"

    Me "..."

    show leap uniform sad yami
    L "やっぱり覚えてないですよね。"

    "Leapは喋りながらゆっくりと先輩に歩み寄る。"

    L "私は確かに言ったんですけどね..."
    L "『先輩は、何でいつも私のことを見てくれないんですか？』って。"

    play sound "audio/stungun.mp3" volume 0.05

    pause 1.0

    stop sound

    "不意に、バチンという大きな音とともに、電流が体中を走った。"

    Me "！？！？"
    Me "（体が動かない...）"

    show leap uniform normal yami
    L "しびれて動けなくなった先輩もカワイイですよ。"

    play music "audio/distance.mp3" volume 0.1
    Me "うっ...ぐっ..."
    Me "何で...こんなこと..."

    L "何で？"
    L "ふふふ、先輩って本当鈍感でカワイイ。"
    L "こんなカワイイ先輩にはご褒美に教えてあげますよ。"
    L "先輩のことが大好きだからですよ..."
    L "大好きで大好きで胸が張り裂けそうだったのに..."
    show leap uniform sad yami
    L "なのに、"
    L "先輩が私のほうを見てくれないから。"
    L "見てくれないからいけないんですよ。"

    Me "俺は...ただ...謝りた...かった...だけ..."

    show leap uniform normal yami
    L "律儀ですね先輩、そんな先輩もカワイイ。"
    L "あっそうだ先輩。{p}私がこの数日間、学校に行かず何をしていたか分かりますか？"

    Me "...っく..."

    L "分かりませんか先輩？"
    L "ほらもっと考えてくださいよ。"
    L "いつもみたいに..."
    
    Me "..."

    L "...分からないですか..."
    L "ふふふ、正解は..."
    L "先輩との愛の巣を、これから二人で一生を過ごす場所を用意してたんですよ。"

    Me "なっ..."
    
    L "本当なら出来次第、先輩を呼ぶつもりだったんですけどね。"
    L "まさか、先輩から来てくれるなんて思ってませんでしたよ。"
    L "こんなこともあるんですね。"
    L "まあ、どちらにしても、{p}これからは、私のことしか見れないようにしてあげます。"
    L "そして、先輩が好きな英単語テストたくさんしてあげます。"
    L "楽しみですね。ふふふ。"
    L "フフフフフフフフフフフフフ"
    L "だから先輩。"
    stop music
    L "少しの間、寝ていてくださいね。"

    play sound "audio/stungun.mp3" volume 0.05
    "バチン"

    stop sound

    $ badEndCode = 6
    
    jump badEnd_call