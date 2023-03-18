label fall:
    $ like_meter = True

    jump fall1

label fall1:
    scene bg black

    "夏休みが明けてから数か月、今日は待ちに待った体育祭。"
    "学年を超えて交流し、それぞれのチームが切磋琢磨して優勝を狙っていく。"
    "そんな日に、一人乗り気じゃない男がいた..."

    scene bg taiikusai
    with dissolve
    play music "audio/tanukiti.mp3" volume 0.05 fadein 1.0

    Me "あ～あ、体育祭かぁ..."
    Me "なんで体育祭なんてあるんだよ、どうせ活躍できるのは陽キャだけなのに。"
    Me "毎年戦犯かましてる俺みたいな奴にスポットライトは当たりはしないよ。"
    Me "やってらんないZE!"

    "そう、この男は運動音痴なのである。"

    Me "まぁ、今年こそは戦犯にならないために頑張らないとなぁ。"
    Me "そういえば、俺の出る競技ってなんだっけ。えーっと..."
    Me "午前中は徒競走で、午後は二人三脚か。"
    Me "徒競走はビリ確定として、二人三脚か。ぺアの足を引っ張らないようにしないと。"
    Me "{size=*0.8}...二人三脚だけに。{/size}"

    "おまけにギャグのセンスも壊滅的である。"

    Me "てか、俺のペアって誰なんだろう。"
    Me "この二人三脚、学年混合なんだよなぁ。初めて会う人と組むとか正気の沙汰じゃねぇ。そして何より気まずい。"
    Me "確か午後の競技の詳細は体育館前の掲示板で発表されるんだったな。"
    Me "二人三脚のペアもそこで分かるのかな。発表の時間までもう少しだし、確認しに行くか。"

    stop music fadeout 2.0
    scene bg black
    with dissolve

    scene bg taiikusai
    with dissolve
    play music "audio/zawazawa.mp3" volume 0.05 fadein 1.0

    Me "掲示板の前は人が多いな。みんな確認しに来てるのかな。"

    show leap sport silhouette at leapPos
    with dissolve
    stop music fadeout 1.0

    Me "ん...？あれは..."

    show leap sport normal
    with dissolve

    Me "Leapちゃん！？"

    play music "audio/leap.mp3" volume 0.05
    
    L "あっ！先輩！"
    L "どうしたんですか？"

    Me "二人三脚に出るから、ペアを確認しに来たんだ。"

    L "奇遇ですね。私も二人三脚に出るので確認に来たんですよ。"
    L "ところで、先輩は何チームなんですか？"

    Me "赤い彗星チームだよ。Leapちゃんは？"

    show leap sport smile
    L "私も同じです！頑張りましょうね！"

    Me "う、うん。頑張ろうね。"
    Me "（Leapちゃんと同じチームだったのか...これは戦犯とか言ってる場合じゃないな。頑張ろう。）"

    show leap sport surprise
    L "だけどペア表が張り出されるのはもう少しかかるみたいですね。"

    Me "そっかー、まぁ待つしかないか。"

    show leap sport normal
    L "もしかしたら同じペアかもしれませんね。"

    menu:
        L "もしかしたら同じペアかもしれませんね。"

        "そうだったら嬉しいな":
            $ renpy.block_rollback()

            Me "そうだったら嬉しいな。"
            Me "俺、あんまり友達いないからさ。Leapちゃんがペアだったらすごい助かるよ。"

            show leap sport question
            L "そう言ってもらえるのは嬉しいですけど、先輩友達いないんですか？"

            Me "ぐぅ..."

            show leap sport normal
            L "そういえば先輩は部活入ってませんもんね。"

            Me "部活入ったからってできるもんじゃないぞ。"

            L "私はいますよ。"

            Me "..."

            show leap sport sad
            $ like = likeChanger(like, -10)
            L "なんかすみません。"

        "めったなこと言うんじゃない":
            $ renpy.block_rollback()

            Me "めったなこと言うんじゃない！"

            $ like = likeChanger(like, -5)
            show leap sport surprise
            L "何でですか！"

            Me "俺は協調性がない。"
            Me "..."
            Me "こういう協力する競技は苦手なんだ、ごめんね。"

            show leap sport smile
            $ like = likeChanger(like, 15)
            L "そんなことないですよ、先輩は優しい人ですよ！"

            Me "うぅ...ありがとう..."
    
    show leap sport surprise
    L "あっ、紙が張り出されましたよ。"

    Me "ほんとだ。えーっと、俺の名前は...お、あったあった。"
    Me "で、ペアは..."
    Me "！？"

    Me "Leap...ちゃん..."

    show leap sport normal
    L "...どうやら本当にペアみたいですね。よろしくお願いします、先輩！"

    Me "よっ、よろしく。"
    Me "（こんな偶然ってあるんだな...）"

    show leap sport smile
    L "二人三脚は午後からでしたよね。一緒に頑張りましょうね！"

    Me "う、うん。"

    stop music fadeout 2.0
    scene bg black
    with dissolve

    "そこで二人は別れた。"
    "そして、午前競技が始まって数時間後..."

    scene bg taiikusai
    with dissolve
    play music "audio/zawazawa.mp3" volume 0.05

    Me "は～、結局徒競走はビリだったな。"
    Me "午前中の俺が出る競技はもう終わったな、ていうか午前競技自体がもう終わりか。"
    Me "教室に戻って昼飯でも食べよう。"

    show leap sport normal at leapPos
    with dissolve
    L "あっ先輩～"
    play music "audio/leap.mp3" volume 0.05

    Me "あ、Leapちゃん。"

    show leap sport surprise
    L "さっきの徒競走見てましたよ。"
    L "ビリでしたね。"

    Me "うるさいやい。"

    show leap sport normal
    L "だけど大丈夫ですよ。二人三脚では重要なのはスピードだけじゃないですから。"

    Me "と、言いますと？"

    L "二人三脚は協力して勝つ競技です。"
    L "ですからさらに親睦を深めるついでに、一緒にお昼ご飯を食べましょう。"

    Me "おっ、おう、いいよ。どこで食べるの？"

    show leap sport question
    L "どこがいいですか？"

    $ passedOkujou = False
    $ passedKoutei = False

    jump fall1_menu

label fall1_menu:
    show leap sport question

    menu:
        L "どこがいいですか？"

        "屋上" if passedOkujou == False:
            $ renpy.block_rollback()
            $ passedOkujou = True

            Me "屋上はどう？。"

            show leap sport normal
            L "いいですね。そこにしましょう。"

            scene bg black
            with dissolve
            play sound "audio/walk.mp3" volume 0.05 fadein 1.0

            pause 2.0

            scene bg okujou
            with dissolve
            stop sound fadeout 1.0
            play music "audio/zawazawa.mp3" volume 0.05 fadein 1.0
            show leap sport normal at leapPos

            L "着きましたね。"

            Me "結構人がいるね。"

            L "こんな青空ですから、皆屋上で食べたいのでしょう。"

            Me "...やっぱり場所を変えない？"

            show leap sport question
            L "何でですか？"

            Me "いや～こんだけ人が多いと食事に集中できないよ。"

            L "んー、確かにそうですね。場所を変えましょうか。"

            $ like = likeChanger(like, -10)

            jump fall1_menu
        
        "校庭" if passedKoutei == False:
            $ renpy.block_rollback()
            $ passedKoutei = True

            Me "校庭はどう？"

            show leap sport normal
            L "いいですね。そこにしましょう。"

            scene bg black
            with dissolve
            play sound "audio/walk.mp3" volume 0.05 fadein 1.0

            pause 2.0

            scene bg taiikusai
            with dissolve
            stop sound fadeout 1.0
            play music "audio/blow.mp3" volume 0.05 fadein 1.0
            show leap sport normal at leapPos

            L "着きましたね。"
            L "体育祭だからか、思ったよりたくさんの人が校庭でご飯を食べてますね。"

            Me "本当だね。"
            Me "..."

            show leap sport surprise
            L "..."

            Me "結構砂がまってるね..."

            show leap sport question
            L "そうですね..."

            Me "...傘とかテントとかあったりする？"

            L "あると思います？"

            Me "...外はやめようか。"

            $ like = likeChanger(like, -10)

            jump fall1_menu
        
        "教室":
            Me "教室はどう？"

            L "いいですね。そこにしましょう。"

            jump fall2

label fall2:
    stop music
    scene bg black
    with dissolve
    play sound "audio/walk.mp3" volume 0.05 fadein 1.0

    pause 2.0

    scene bg classroom day
    with dissolve
    stop sound fadeout 1.0
    show leap sport normal at leapPos
    with dissolve

    L "着きましたね。"
    L "ちょうどよく空き教室があって良かったですね。"

    Me "...勝手に入って大丈夫なの？"

    show leap sport question
    L "大丈夫ですよ、バレませんて。"
    show leap sport normal
    L "そんなことよりお昼ご飯を食べましょうよ。"

    Me "まあそうするか。"

    scene bg black
    with dissolve

    "食事中"

    scene bg classroom day
    with dissolve
    play music "audio/leap.mp3" volume 0.05 fadein 1.0
    show leap sport normal at leapPos

    Me "そういえば、さっき親睦を深めるって言ってたけど、何をするの？"

    show leap sport question
    L "先輩、二人三脚において私たちに足りないものはなんだと思います？"

    Me "運動能りょ..."

    show leap sport surprise
    play sound "audio/thunder.mp3" volume 0.05
    L "{size=*2.0}違う。{/size}"
    L "二人三脚において私たちに足りないものは、{p}{size=*2.0}情熱、思想、理念、頭脳、気品、優雅さ、勤勉さ！{/size}"
    play sound "audio/thunder.mp3" volume 0.05
    L "そして何よりもーー{w=1.5}絆が足りない！"

    Me "絆～？"
    Me "絆って何をするんだよ。"

    show leap sport question
    L "先輩～、もううすうす感づいてるんじゃないんですか？"

    Me "まさか..."

    $ passedDoping = False
    $ passedNinin = False
    
label fall2_menu:
    show leap sport question
    menu:
        Me "まさか..."

        "ドーピング" if passedDoping == False:
            $ renpy.block_rollback()
            $ passedDoping = True

            show leap sport surprise
            L "そんなわけないじゃないですか、めったなこと言わないでください。"
            $ like = likeChanger(like, -20)
            L "ふざけてるんですか？"
        
            Me "ごっごめんよ。"

            jump fall2_menu      

        "二人三脚の練習" if passedNinin == False:
            $ renpy.block_rollback()
            $ passedNinin = True

            show leap sport sad
            L "ううぅぅ、そうだけどそうじゃない..."
            
            Me "俺らが次やる競技は二人三脚なんだろ。"
            Me "練習しなきゃ。"

            $ like = likeChanger(like, -10)
            show leap sport question
            L "言ってることはごもっともだけど、ほらもっとあるじゃないですか。"
            L "私たちの絆を高めるものが。ね？"

            Me "そうだな..."

            jump fall2_menu
        
        "英単語テスト":
            $ renpy.block_rollback()

            jump fall3
        
label fall3:
    show leap sport normal
    L "Exactly.\nその通りでございます。"
    L "私たちが出会った原点、英単語テストのために頑張ってきた思い出。"
    L "英単語テストは私たちの絆そのものですよ。"
        
    Me "なる...ほど？"

    L "では、私たちの絆を試すためにも行きますよ。"

    Me "はいはいわかったよ。"

    call testPrepare

    play music "audio/leap.mp3" volume 0.05

    if 0 <= sumT <= 3:
        $ renpy.block_rollback()
        $ like = likeChanger(like, -15)

        show leap sport question
        L "..."

        Me "..."

        show leap sport surprise
        L "先輩..."

        Me "何でしょうか..."

        show leap sport question
        L "...やっぱ何でもないです。"

        Me "..."

        L "..."

    if 4 <= sumT <= 7:
        $ renpy.block_rollback()
        $ like = likeChanger(like, 5)

        show leap sport normal
        L "まあまあですね。"

        Me "頑張ったんだけどなぁ。"

        L "だけど先輩ならもっといけます！"
        L "その調子で頑張りましょう！"

        Me "OK."

    if 8 <= sumT <= 10:
        $ renpy.block_rollback()
        $ like = likeChanger(like, 15)

        show leap sport smile
        L "すごいです先輩！"

        Me "まあね。"

        show leap sport normal
        L "私たちの絆も深まったことですし、{p}これで二人三脚も一位間違いなしですね！"

        Me "ああ、一緒に頑張ろう。"

    scene bg black
    with dissolve

    "そして、昼休みも終わり、午後の部が始まった。"
    "多くの生徒が競技に熱を入れ、歓声であふれる中、"
    "やっと二人三脚が始まった。"

    scene bg taiikusai
    with dissolve
    play music "audio/zawazawa.mp3" volume 0.05 fadein 1.0
    show leap sport normal at leapPos

    L "もう少しで私たちの番ですね。"

    Me "そ、そうだね。"

    show leap sport question

    L "先輩？もしかして緊張してます？"

    menu:
        L "先輩？もしかして緊張してます？"

        "別に緊張してないし":
            $ renpy.block_rollback()

            Me "別に緊張してないし。"

            L "本当ですか？{p}...足震えてますけど。"

            Me "これは、いや、そうだ。武者震いだよ。"

            show leap sport normal
            L "ならいいですけど。"

            Me "大船に乗った気持ちでいたまえ。"

            $ like = likeChanger(like, 5)
            show leap sport smile
            L "それは頼もしいです！"

        "緊張するに決まってるじゃないか":
            $ renpy.block_rollback()

            Me "緊張するに決まってるじゃないか。"

            $ like = likeChanger(like, -10)

            show leap sport normal
            L "それもそうですね。"

            Me "ああ、こけたりしたらどうしよう。"

            L "大丈夫ですよきっと。"

            Me "本当に？"

            L "May be..."
        
        "緊張してるのは君の方なんじゃないの":
            $ renpy.block_rollback()

            Me "緊張してるのは君の方なんじゃないの？"

            show leap sport question
            L "別に私は平気ですけど..."

            Me "本当かなぁ？"

            L "疑ってるんですか？"

            Me "別に疑ってるとかでは..."

            show leap sport surprise
            L "二人三脚で大切なのは絆って言いましたよね！"

            Me "ごめん..."

            show leap sport question
            L "..."

            $ like = likeChanger(like, -20)
    
    $ zako1Name = "実況"
    Zako1 "第〇レースは星の白銀チームの勝利でした。次のレースのペアは準備を始めてください。"

    show leap sport normal
    L "先輩、私たちの番が回ってきましたよ。"

    Me "そうだね。"

    L "では、足を出してください。"

    Me "あっ、俺が結ぶよ。"
    Me "（あれ？結び方ってこれでいいのかな？）"
    Me "（まあいいか。）"

    show leap sport question
    L "先輩、結び終わりました？"

    Me "ああ、終わったよ。"

    if like < 0:
        jump fall_bad
    else:
        jump fall_normal

label fall_normal:
    show leap sport question
    L "なんか結び方違くないですか？"
    L "そんな結び方で大丈夫ですか？"

    Me "あれ、違ったっけ？"

    L "私が結びなおしましょうか？"

    menu:
        L "私が結びなおしましょうか？"

        "一番いいのを頼む":
            $ renpy.block_rollback()

            Me "一番いいのを頼む。"

            show leap sport normal

            L "わかりました。"

            L "...{w=1.5}はい、結び終わりましたよ。"

            Me "ありがとう。"

            show leap sport smile
            L "このぐらいお安い御用です。"
            show leap sport normal
            L "じゃあスタート位置につきましょうか。"
        
        "大丈夫だ問題ない":
            $ renpy.block_rollback()

            show leap sport normal
            L "じゃあスタート位置につきましょうか。"

            jump fall_bad

    stop music fadeout 1.0
    hide leap
    with dissolve
    scene bg school ground
    with fade
    
    "二人は緊張しつつも、先の特訓の効果に期待を寄せながらスタートラインに立った。"

    $ zako1Name = "審判"
    Zako1 "では、位置について。"
    Zako1 "よーい、"
    play sound "audio/pistol.mp3" volume 0.05
    Zako1 "ドン！"

    play music "audio/undoukai.mp3" volume 0.05

    $ zako1Name = "実況"
    $ zako2Name = "解説"

    Zako1 "おーっと、勢いよく前に飛び出したのは赤い彗星チームだ！"
    
    Zako2 "周りのチームより３倍の速度ですね。"

    Zako1 "それを追うのは星の白銀チーム！"

    Zako2 "パワフルかつ精密な動きですね！"

    Zako1 "それから巻き返し始めたのは青眼の白龍チーム！"
    Zako1 'そして、それにぴったりついて行ってるのは緑の悪魔チーム！'

    Zako2 "すごい執着力ですね。恐怖すら感じます。"

    Zako1 "そして、トップから３馬身ぐらい離れて黒い三連星チームです。"

    Zako2 "二人三脚なので二連星です。"
    Zako2 "そして、全てのチームが最後の一直線に入りましたね。"

    Me "（よし、行けるぞ。）"
    Me "（このままなら一位になれるかもしれない。）"
    Me "（これが訓練の成果...！）"

    Zako1 "ゴーーーーール！！！"
    stop music
    play sound 'audio/kansei.mp3' volume 0.05
    Zako1 "一位は赤い彗星チームだあああああ！"

    Zako2 "流石のチームワークでしたね！"

    Zako1 "そして、二位は緑の悪魔チーム、三位は星の白銀チーム、四位は青眼の白龍チーム、五位は黒い三連星チームになりました。"

    show leap sport smile at leapPos
    play music "audio/victory.mp3" volume 0.05

    Me "やったぞおおおおお！"
    
    L "やりましたね先輩！"

    Me "ホントだな！"
    Me "これもお昼休みの特訓のおかげかもしれないな。"

    L "絶対そうですよ。"

    Me "そうだな。"

    L "先輩と二人三脚できて本当に良かったです。"

    Me "俺もだよ。"

    "そして彼らの二人三脚は終わった。"
    "体育大会全体の結果は赤い彗星チームが二位で終わった。"
    "だが、二人の心の距離は大きく縮まったのである。"

    scene bg black
    with dissolve
    stop music fadeout 2.0

    jump rest

label fall_bad:
    $ renpy.block_rollback()
    $ like_meter = False
    
    # L 'じゃあスタート位置につきましょうか'

    # 背景：校庭（トラック）
    stop music fadeout 1.0
    hide leap
    with dissolve
    scene bg school ground
    with fade

    '二人は大きな緊張に押しつぶされそうになりながらもスタート位置についた。'

    $ zako1Name = "審判"
    Zako1 'では、位置について。'
    Zako1 'よーい、'
    play sound "audio/pistol.mp3" volume 0.05
    Zako1 'ドン！！'

    play music "audio/undoukai.mp3" volume 0.05

    $ zako1Name = "実況"
    $ zako2Name = "解説"

    Zako1 'おーーと、勢いよく前に飛び出したのは赤い彗星チームだ!!'

    Zako2 '周りのチームより３倍の速度ですね。'

    Zako1 'それを、追うのは星の白銀チーム。'

    Zako2 'パワフルかつ精密な動きですね。'

    Zako1 'それから巻き返し始めたのは青眼の白龍チーム。'
    Zako1 'そして、それにぴったりついて行ってるのは緑の悪魔チーム。'

    Zako2 'すごい執着力ですね。恐怖すら感じます。'

    Zako1 'そして、トップから３馬身ぐらい離れて黒い三連星チームです。'

    Zako2 '二人三脚なので二連星です。'

    Zako2 'そして、全てのチーム最後の一直線に入りましたね。'

    Me '（よし、行けるぞ。）'
    Me '（このままなら一位になれるかもしれない。）'

    'と、その時。'
    '二人の足を結んでいたひもは、突如としてほどけてしまった。'
    'そして、二人は勢い余って転んでしまう。'

    stop music
    show leap sport surprise at leapPos
    L "あっ！"

    Me 'あっ、ああ、あああ、どうしようどうしよう...'
    Me 'もうだめだおしまいだ...'
    Me '何でほどけちゃったんだ...'

    show leap sport question
    L '先輩！？'

    Me 'あの時...'

    # 背景：結ぶ描写のスクリーンショット
    show kutuhimono at center:
        zoom 0.67
    with dissolve

    pause 1.0

    hide kutuhimono
    show kutuhimono2 at center:
        zoom 0.67
    with dissolve

    pause 1.0 

    hide kutuhimono2
    with dissolve

    Me '....畜生。'

    play music "audio/distance.mp3" volume 0.1

    Zako1 'ゴーーーーール！！！'
    Zako1 '一位は黒い三連星チームだああ！！！'
    play sound "audio/kansei.mp3" volume 0.05

    Zako2 'すごいチームワークでしたね。'

    Zako1 'そして、二位は緑の悪魔チーム、三位は星の白銀チーム、四位は青眼の白竜チーム。'
    Zako1 '赤い彗星チームは惜しくもリタイアとなってしまいました。'

    scene bg taiikusai mono
    with dissolve

    Me 'この時僕から血の気が引いていくのをはっきりと感じた。'
    Me '足に力が入らなくなって、頭がぼーっとする。'
    Me '観客の嘲るような笑い声だけが聞こえる。'
    Me 'たくさんの人の前で恥をかいたあげく、'
    Me 'Leapちゃんの足を引っ張てしまった罪悪感を感じ、'

    scene bg black
    stop music
    Me '次の瞬間、目の前が真っ暗になった。'


    $ badEndCode = 5
    jump badEnd_call