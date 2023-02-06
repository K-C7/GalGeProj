label Opening1:
    "Note: 会話中に下の「ロールバック」ボタンを押すと、\nひとつ前の画面に戻ることができます。\n一部の場面を除いて基本的に使用できるので、ぜひご活用ください。"

    scene bg room
    with fade

    play music "audio/morning.mp3" volume 0.05

    "3月某日"
    "春休みがもう終ろうとしていた、ある日。"

    Mom "{size=*2.0}おきなさーい。{/size}"

    $ nidoneCount = 0
    jump Opening1_menu1

label Opening1_menu1:
    if(nidoneCount >= 3):
        $ badEndCode = 1
        
        jump badEnd_call
    
    menu:
        "起きる":
            Me "起きてるよー。"

        "二度寝する":
            Me "..."

            $ nidoneCount += 1

            jump Opening1_menu1
    
    pause 2.0

    Mom "宿題は終わったの？終わってなかったら今日中にもさっさと始めなさい。"

    Me "もう終わってるよ。とっくに。"
    
    Mom "あら、終わってるの？"
    Mom "じゃあ、せっかくだし神社にでも行ってきたら？初詣も行ってないんだし。"

    Me "えー、神社？"

    menu:
        "理由を尋ねる":
            Me "何で？"

        "拒否する":
            Me "行きたくなーい。"
    
    Mom "いいじゃないの。さっさと行ってきなさい。"

    scene bg shrine day
    with fade

    stop music

    Me "この神社に来るのも久しぶりだな。"
    Me "じゃあ、お祈りでもするか。"
    
    play sound "audio/charin.mp3"

    Me "二礼二拍手一礼っと。"
    Me "(どうか神様、「英語」がもっと得意になりますように。)"
    Me "よし。帰るか。"

    #背景をぐわんぐわんにする

    play music "audio/blow.mp3" volume 0.2

    "ざわ...ざわ..."

    Me "うっ...急に頭痛がっ..."

    "ざわ...ざわ..."

    Ano "貴様の願いをかなえてやろう..."

    Me "(なんだこの声は...)"

    menu:
        "お前は誰だ...！":
            Me "誰だッ...！"
        
        "何奴...！":
            Me "何奴...！"

        "貴様はッ！":
            Me "貴様はッ！"

    God "我は神なり..."
    God "もう一度言う..."
    God "貴様の願いをかなえてやろう！"

    scene bg white
    with dissolve

    stop music
    play sound "audio/holysound.mp3" volume 0.3
    
    Me "うっ...なんだこの光は...！"
    Me "ウワアァァァァァァァァァァ！"

    scene bg black
    with dissolve

    "..."

    scene bg shrine evening
    with fade

    play sound "audio/wakeup.mp3" volume 0.5

    Me "...何が起きた？"
    Me "気絶していたのか？今は何時だ？"
    Me "！！！"
    Me "{size=*2.0}５時！！{/size}"
    Me "早く帰らないと母さんに叱られる！急げ！"

    scene bg black
    with dissolve

    $ renpy.movie_cutscene("movie/opening.mpg")

    scene bg road day

    play music "audio/routine.mp3" volume 0.05

    "数日後"

    Me "今日から２年生か。"
    Me "しかし過ぎてみると春休みって短く感じるな。"
    Me "って時間やばいな。このままだと電車乗れないぞ。"
    Me "初日からいきなり遅刻は困るから少し急ぐか。"
    
    play music "audio/run.mp3"

    pause

    scene bg black

    stop music
    play sound "audio/hit.mp3"

    pause

    scene bg road day

    Me "うわっ！"

    Ano "きゃっ！"

    Me "（急ぐあまり、人とぶつかってしまった。謝らないと。）"
    Me "あのーすみません。お怪我はあり...？"

    show leap normal at leapPos
    
    play music "audio/leap.mp3" volume 0.05

    Me "かっ..."
    Me "（かわいい...）"

    show leap surprise

    Ano "大丈夫ですか！？"

    Me "あっ、ああ。大丈夫だよ。"

    show leap question_mark

    Ano "同じ制服？"
    Ano "あのー、もしかして同じ学校の先輩なんですか？"

    Me "（たしかに同じ制服だけど、この子誰だ？学校で見たことないぞ。）"

    show leap surprise

    Ano "あーーーっ！先輩！"

    Me "何？"

    Ano "早くしないと電車乗れませんよ？"

    Me "あっ、ホントだ！急がないと！！"

    scene bg train day

    show leap normal at leapPos

    play music "audio/train.mp3" volume 0.2

    Me "何とか間に合った。"

    Ano "そうですね。"

    Me "（そしてこの子だれなんだ？）"
    Me "（新入生、か？）"
    # Me "ﾄｩﾝｸﾄｩﾝｸ"
    Me "…"

    Ano "…"

    show leap question

    Ano "どうしたんですか先輩？"

    Me "いっ、いやなんでも。"

    show leap surprise

    Ano "あっ！そういえば名乗ってなかったですね。"

    show leap normal

    L "私、Leapといいます。"

    pause

    Me "...は？Leap？"
    Me "（どういうことだ？どうなっているんだ？）"
    Me "英単語の？"

    L "はい。"

    Me "え？"
    Me "あっ、ああ、キラキラネーム的な？"

    show leap question

    L "キラキラネーム？私の名前ってそんなにおかしいですか？"

    Me "？？？"
    Me "（狂っているのは世界？それとも俺？）"
    Me "(確かに初対面の後輩に「キラキラネーム」って言う人間は狂っているのか？)"
    Me "（いや...待てよ、そういえばあの時...）"

    play sound "audio/poyon.mp3"
    scene bg remember:
        zoom 1.28
    with fade

    pause

    scene bg train day
    with dissolve

    show leap normal at leapPos

    Me "............."
    Me "あれか。"
    Me "........"
    Me "いや、こうはならないだろ。"

    show leap question

    L "どうしたんですか先輩、そんな難しい顔して。"
    
    Me "いや、何でもないよ。"

    show leap question_mark

    L "...そんなに私の名前変ですか？"
    
    Me "........"
    Me "俺の気のせいだった、気にしないでくれ。"

    show leap normal
    
    L "あっそうですか。良かった。"
    
    Me "（いや、良くないだろ。）"
    Me "（このままだとこちらの印象は悪くなるし、もっと差し障りのない話題に変えなければ。）"
    Me "あっそうだ、"

    jump Opening1_menu2

label Opening1_menu2:
    menu:
        "君は新入生、でいいんだよね？":
            Me "君は新入生、でいいんだよね？"
            
            L "はい、そうですよ。"
            L "先輩こそ二年生でいいんですよね？"

            Me "ああ、そうだよ。"
            Me "もしかして近所だったりするの？"

            L "んーそうですねー。"
            L "まぁ多分近いと思いますよ？"
            L "近くに神社がありますよ。"

            Me "神社..."

            L "はい。"

            Me "（会話が終わってしまった。何か次の話題はないのか？）"

            jump Opening1_menu2

        "LEAPちゃんって何か部活入るの？":
            show leap question

            L "うーん。"
            L "まだ決めてないですね。"

            show leap normal

            L "何かおすすめとかありますか？"

            Me "..."
            Me "実は俺部活入ってないんだよね。"

            show leap surprise

            L "えっ、そうなんですか。"

            show leap question_mark

            L "何で入らなかったんですか？"

            Me "うーーーん。"
            Me "入りたいところがなかったから？"
            Me "..."

            show leap question

            L "..."

            Me "（会話が終わってしまった。何か次の話題はないのか？）"

            show leap normal

            jump Opening1_menu2
        
        "LEAPちゃんって得意教科何？":
            L "当ててみてください。"

            menu:
                "英語":
                    Me "英語だろ。"

                    show leap surprise

                    L "なんでわかったんですか？"

                    Me "(いや、分かるだろ。)"
                    Me "なんとなくそんな気がしたんだ。"

                "数学":
                    Me "んー、まさかの数学？"

                    L "違いまーす。正解は英語でした。"

                    Me "引っ掛けとかじゃなかったか。"

                    show leap question

                    L "何がですか？"

                    Me "いや、なんでもない。"
                    
                "国語":
                    Me "んー、まさかの国語？"

                    L "違いまーす。正解は英語でした。"

                    Me "引っ掛けとかじゃなかったか。"

                    show leap question

                    L "何がですか？"

                    Me "いや、なんでもない。"

    show leap normal

    L "そうなんですか、じゃあ先輩はどうなんですか？"
        
    Me "何が？"

    show leap question
        
    L "英語は得意なんですか？"
        
    Me "...実は結構苦手で..."
    Me "期始めの実力テストでは毎回酷い点数しかとれなくて。"
    Me "本当に誰かに教えてもらいたいくらいだよ。"
        
    show leap normal
        
    L "苦手なんですね。へー。"
    L "..."
    
    Me "..."
    
    L "...じゃあそうだ。"
    L "これも何かの縁、電車が駅に着くまで私が英語の問題を出してあげますよ！"
    
    play music "audio/beat.mp3" volume 0.5

    Me "！！"
    Me "（まずい展開になってしまった。"
    Me "下手に教えてなんて言わなければよかった。）"
    Me "（いや、だけど新しい後輩の前で恥をさらすわけにはいかないし、ここで少しはいい印象を与えたい。）"
    
    stop music

    L "先輩、いきますよ。"

    menu:
        "挑戦する":
            Me "やるしかないのか。"

            jump testPrepare
        
        "断る":
            Me "..."

            L "先輩...？"

            Me "非常に言いにくいんだけど、"
            Me "気に障るんだよ、君。"

            L "え..."

            Me "もう関わらないでくれ。"

            hide leap
            with dissolve

            $ badEndCode = 2
            
            jump badEnd_call

label Opening2:
    $ progress = 2

    play music "audio/leap.mp3" volume 0.05

    if 0 <= sumT <= 3:
        L "わぁ、本当に英語が苦手なんですね。"

        Me "く、くそぉ..."

        L "勉強してます？"

        Me "苦手なんだからしょうがないだろ。"

        L "いや、先輩。むしろこれは伸びしろですよ。"

        Me "伸びしろ？"

        L "今英語があまり覚えられていないというのは、これからもっと英語を覚えられるということの裏返し。"
        L "先輩はこれから伸びますよ。"

        Me "そ、そうかな。"

        show leap smile

        L "そうですよ！"

        Me "じゃあ、ちゃんと英語勉強するか。"

        show leap normal

        L "その調子です。それなら付き合ってあげますよ。"

        Me "えっ、それって...？"

        show leap question

        L "？英語のテストをですよ？"

    elif 4 <= sumT <= 7:
        L "まあまあじゃないですか。"

        Me "そうかな。"

        show leap smile

        L "単語はちゃんと覚えられてるってことですし、素晴らしいと思いますよ！"

        Me "そっか。ありがとう。"

        show leap normal

        L "もしまたご一緒することがあったら、その時はまた英語の問題を出してあげますよ。"

        Me "そうなった時はよろしく頼むよ。"
    
    elif 8 <= sumT <= 10:
        show leap smile

        L "すごいじゃないですか！英語が苦手って嘘じゃないんですか？"

        Me "今回はたまたまできただけだよ。"

        show leap normal

        L "本当ですかー？"
        L "でも、この調子なら実力テストもいい点数取れると思いますよ。"

        Me "そうかな。"

        L "あっ、そうだ。先輩は毎日この電車を使ってるんですか？"

        Me "そうだけど。"

        L "じゃあ、また今度会ったときも問題出してあげますよ。"

        Me "{size=*0.8}...だるいな。{/size}"

        show leap question

        L "なにか言いました？"

        Me "いや、ありがとうって言ったんだ。"

        L "それなら良かったです。"
    
    stop music
    with dissolve

    cd "次は〇〇駅、〇〇駅に到着します。車内にお忘れ物のないようにご注意ください。"
    cd "お出口は左側です。扉にご注意ください。"

    Me "おっ、着いたな。"

    L "そうですね。"

    Me "君のおかげで退屈はしなかったよ。"

    L "それ褒めてます？"

    Me "褒めてるよ。"

    show leap smile

    L "ふふふ、それはありがとうございます。"

    show leap normal

    L "じゃあ、学校に行きましょうか。"

    Me "そうだな。"

    scene bg black
    with dissolve

    "体験版はここまでです。\n続きは製品版でお楽しみください。"
    "to be continued..."

    jump exit

label badEnd_call:
    show bg black
    with dissolve

    if(badEndCode == 1):
        "そのまま、主人公は目覚めることはなく、平凡な人生を送ったのでした。"
        "BadEnd 1 : 二度寝"

    elif(badEndCode == 2):
        "その後、二度とLeapさんと出会うことはなく、平凡な人生を送ったのでした。"
        "BadEnd 2 : 邪魔者"