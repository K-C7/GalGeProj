label opening:
    jump opening1

label opening1:
    scene bg black

    "Note: 会話中に下の「ロールバック」ボタンを押すと、\nひとつ前の画面に戻ることができます。\n一部の場面を除いて基本的に使用できるので、ぜひご活用ください。"
    "Note: また、セーブは各章終了時にのみすることができます。\nご了承ください。"

    scene bg room
    with dissolve
    play music "audio/morning.mp3" volume 0.05 fadein 1.0

    "3月某日"
    "春休みがもう終ろうとしていた、ある日。"

    play sound "audio/thunder.mp3" volume 0.05
    Mom "{size=*2.0}おきなさーい。{/size}"

    $ nidoneCount = 0
    jump opening1_menu1

label opening1_menu1:
    if(nidoneCount >= 3):
        $ renpy.block_rollback()
        $ badEndCode = 1
        
        jump badEnd_call
    
    menu:
        "起きる":
            Me "起きてるよー。"

        "二度寝する":
            $ nidoneCount += 1

            Me "..."

            jump opening1_menu1
    
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
    stop music fadeout 1.0

    Me "この神社に来るのも久しぶりだな。"
    Me "じゃあ、お祈りでもするか。"
    play sound "audio/charin.mp3"
    Me "二礼二拍手一礼っと。"
    Me "(どうか神様、「英語」がもっと得意になりますように。)"
    Me "よし。帰るか。"

    scene bg shrine day guwan:
        zoom 1.2
    with dissolve
    play music "audio/blow.mp3" volume 0.2 fadein 1.0

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
    $ like_meter = True

    play sound "audio/wakeup.mp3" volume 0.5
    Me "...何が起きた？"
    Me "気絶していたのか？今は何時だ？"
    Me "！！！"
    play sound "audio/thunder.mp3" volume 0.05
    Me "{size=*2.0}５時！！{/size}"
    Me "早く帰らないと母さんに叱られる！急げ！"

    scene bg black
    with dissolve

    # $ renpy.movie_cutscene("movie/opening.mpg")
    play music "audio/kagurasuzu.mp3" volume 0.3
    scene openingVideo
    pause 14.0

    scene bg road day
    with dissolve
    play music "audio/routine.mp3" volume 0.05 fadein 1.0

    "数日後"

    Me "今日から２年生か。"
    Me "しかし過ぎてみると春休みって短く感じるな。"
    Me "って時間やばいな。このままだと電車乗れないぞ。"
    Me "初日からいきなり遅刻は困るから少し急ぐか。"
    
    play music "audio/run.mp3" fadein 1.0

    pause

    scene bg black
    stop music
    play sound "audio/hit.mp3" volume 0.5

    pause

    scene bg road day

    Me "うわっ！"

    Ano "きゃっ！"

    Me "（急ぐあまり、人とぶつかってしまった。謝らないと。）"
    Me "あのーすみません。お怪我はあり...？"

    show leap uniform normal at leapPos
    with dissolve
    play music "audio/leap.mp3" volume 0.05 fadein 1.0

    Me "かっ..."
    Me "（かわいい...）"

    show leap uniform surprise
    Ano "大丈夫ですか！？"

    Me "あっ、ああ。大丈夫だよ。"

    show leap uniform question
    Ano "同じ制服？"
    Ano "あのー、もしかして同じ学校の先輩なんですか？"

    Me "（たしかに同じ制服だけど、この子誰だ？学校で見たことないぞ。）"

    show leap uniform surprise
    Ano "あーーーっ！先輩！"

    Me "何？"

    Ano "早くしないと電車乗れませんよ？"

    Me "あっ、ホントだ！急がないと！！"

    scene bg black
    with dissolve
    stop music
    play sound "audio/run.mp3" fadein 1.0

    pause 2.0

    stop sound fadeout 1.0

    pause 1.0

    scene bg train day
    with dissolve

    show leap uniform normal at leapPos
    with dissolve
    play music "audio/train.mp3" volume 0.2 fadein 1.0

    Me "何とか間に合った。"

    Ano "そうですね。"

    Me "（そしてこの子だれなんだ？）"
    Me "（新入生、か？）"
    # Me "ﾄｩﾝｸﾄｩﾝｸ"
    Me "…"

    Ano "…"

    show leap uniform question sweat
    Ano "どうしたんですか先輩？"

    Me "いっ、いやなんでも。"

    show leap uniform surprise
    Ano "あっ！そういえば名乗ってなかったですね。"

    show leap uniform normal
    L "私、Leapといいます。"

    pause

    play sound "audio/poyon.mp3"
    Me "...は？Leap？"
    Me "（どういうことだ？どうなっているんだ？）"
    Me "英単語の？"

    L "はい。"

    Me "え？"
    Me "あっ、ああ、キラキラネーム的な？"

    show leap uniform question sweat
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
    show leap question at leapPos
    with dissolve

    Me "............."
    Me "あれか。"
    Me "........"
    play sound "audio/thunder.mp3" volume 0.05
    Me "いや、こうはならないだろ。"

    show leap uniform question sweat
    L "どうしたんですか先輩、そんな難しい顔して。"
    
    Me "いや、何でもないよ。"

    L "...そんなに私の名前変ですか？"
    
    Me "........"
    Me "俺の気のせいだった、気にしないでくれ。"

    show leap uniform normal
    L "あっそうですか。良かった。"
    
    Me "（いや、良くないだろ。）"
    Me "（このままだとこちらの印象は悪くなるし、もっと差し障りのない話題に変えなければ。）"
    Me "あっそうだ、"

    $ passedNew = False
    $ passedClub = False

    jump opening1_menu2

label opening1_menu2:
    menu:
        Me "あっそうだ、"

        "君は新入生、でいいんだよね？" if passedNew == False:
            $ passedNew = True

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

            jump opening1_menu2

        "LEAPちゃんって何か部活入るの？" if passedClub == False:
            $ passedClub = True

            show leap uniform question
            L "うーん。"
            L "まだ決めてないですね。"

            L "何かおすすめとかありますか？"

            Me "..."
            Me "実は俺部活入ってないんだよね。"

            show leap uniform surprise
            L "えっ、そうなんですか。"

            show leap uniform question
            L "何で入らなかったんですか？"

            Me "うーーーん。"
            Me "入りたいところがなかったから？"
            Me "..."

            L "..."

            Me "（会話が終わってしまった。何か次の話題はないのか？）"

            show leap uniform normal

            jump opening1_menu2
        
        "LEAPちゃんって得意教科何？":
            L "当ててみてください。"

            menu:
                L "当ててみてください。"

                "英語":
                    Me "英語だろ。"

                    show leap uniform surprise
                    L "なんでわかったんですか？"

                    Me "(いや、分かるだろ。)"
                    Me "なんとなくそんな気がしたんだ。"

                "数学":
                    Me "んー、まさかの数学？"

                    L "違いまーす。正解は英語でした。"

                    Me "引っ掛けとかじゃなかったか。"

                    show leap uniform question
                    L "何がですか？"

                    Me "いや、なんでもない。"
                    
                "国語":
                    Me "んー、まさかの国語？"

                    L "違いまーす。正解は英語でした。"

                    Me "引っ掛けとかじゃなかったか。"

                    show leap uniform question
                    L "何がですか？"

                    Me "いや、なんでもない。"

    show leap uniform normal
    L "そうなんですか、じゃあ先輩はどうなんですか？"
        
    Me "何が？"

    show leap uniform question  
    L "英語は得意なんですか？"
        
    Me "...実は結構苦手で..."
    Me "期始めの実力テストでは毎回酷い点数しかとれなくて。"
    Me "本当に誰かに教えてもらいたいくらいだよ。"
        
    show leap uniform normal  
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
        L "先輩、いきますよ。"

        "挑戦する":
            $ renpy.block_rollback()

            Me "やるしかないのか。"

            jump testPrepare
        
        "断る":
            $ renpy.block_rollback()
            $ like_meter = False

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

label opening2:
    play music "audio/leap.mp3" volume 0.05
    $ renpy.block_rollback()

    if 0 <= sumT <= 3:
        $ like = likeChanger(like, -15)

        show leap uniform normal
        L "わぁ、本当に英語が苦手なんですね。"

        Me "く、くそぉ..."

        show leap uniform question
        L "勉強してます？"

        Me "苦手なんだからしょうがないだろ。"

        show leap uniform normal
        L "いや、先輩。むしろこれは伸びしろですよ。"

        Me "伸びしろ？"

        L "今英語があまり覚えられていないというのは、これからもっと英語を覚えられるということの裏返し。"
        L "先輩はこれから伸びますよ。"

        Me "そ、そうかな。"

        L "そうですよ！"

        Me "じゃあ、ちゃんと英語勉強するか。"

        show leap uniform normal
        L "その調子です。それなら付き合ってあげますよ。"

        Me "えっ、それって...？"

        show leap uniform question
        L "？英語のテストをですよ？"

        show leap uniform normal

    elif 4 <= sumT <= 7:
        $ like = likeChanger(like, 5)

        show leap uniform normal
        L "まあまあじゃないですか。"

        Me "そうかな。"

        L "単語はちゃんと覚えられてるってことですし、素晴らしいと思いますよ！"

        Me "そっか。ありがとう。"

        L "もしまたご一緒することがあったら、その時はまた英語の問題を出してあげますよ。"

        Me "そうなった時はよろしく頼むよ。"
    
    elif 8 <= sumT <= 10:
        $ like = likeChanger(like, 15)

        show leap uniform smile
        L "すごいじゃないですか！英語が苦手って嘘じゃないんですか？"

        Me "今回はたまたまできただけだよ。"

        show leap uniform normal
        L "本当ですかー？"
        L "でも、この調子なら実力テストもいい点数取れると思いますよ。"

        Me "そうかな。"

        show leap uniform surprise
        L "あっ、そうだ。先輩は毎日この電車を使ってるんですか？"

        Me "そうだけど。"

        show leap uniform normal
        L "じゃあ、また今度会ったときも問題出してあげますよ。"

        Me "{size=*0.8}...だるいな。{/size}"

        show leap uniform question
        L "なにか言いました？"

        Me "いや、ありがとうって言ったんだ。"

        show leap uniform normal
        L "それなら良かったです。"
    
    stop music fadeout 1.0

    Cd "次は〇〇駅、〇〇駅に到着します。車内にお忘れ物のないようにご注意ください。"
    Cd "お出口は左側です。扉にご注意ください。"

    Me "おっ、着いたな。"

    L "そうですね。"

    Me "君のおかげで退屈はしなかったよ。"

    L "それ褒めてます？"

    Me "褒めてるよ。"

    show leap uniform smile
    L "ふふふ、それはありがとうございます。"

    show leap uniform normal
    L "じゃあ、学校に行きましょうか。"

    Me "そうだな。"

    scene bg black
    with dissolve

    "この物語は謎の少女Leapちゃんと数奇な恋愛な恋愛を追う物語である。"

    jump rest