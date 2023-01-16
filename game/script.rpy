define L = Character('Leapちゃん', color="#26aa5d")
define Me = Character('自分', color="#000000")
define Tea = Character('担任', color="#006d75")
define God = DynamicCharacter("godName", color="#5f6634")
define S = Character("生徒", color="#000000")


init:
    $ import module.leapModule as leapModule

    python:
        LEAP_PATH = config.basedir + r"\game\module\leap.csv"
        print(LEAP_PATH)
        leapModule.leapPathSet(LEAP_PATH)

    image bg classroom evening = im.Scale("bg classroom evening notrim.jpg", 1280, 720)


label start:
    jump Opeaning


label op:
    scene bg black

    $ godName = "???"

    God "「...よ ...よ」"

    God "「名はなんと申す?」"

    $ playerName = renpy.input("プレイヤー名を入力してください。")

    God "「[playerName]よ...[playerName]よ...」"

    Me "「...この声は...?」"

    $ godName = "神"

    God "「わしは全国の受験生を合格へ導く受験の神じゃ!」"

    Me "「受験の神...？そんな人が一体何の用ですか？」"

    God "「お主、困っている教科があるのじゃろう?」"

    Me "「ギクッ！じ、実は...」"

    jump subSelect


label subSelect:
    menu:
        "英語":
            # God "nan"
            $ subject = "英語"

        "国語":
            God "まだ準備中じゃ。"
            jump subSelect

        "数学":
            God "まだ準備中じゃ。"
            jump subSelect

        "化学":
            God "まだ準備中じゃ。"
            jump subSelect
    
    Me "実は[subject]が苦手で..."
    
    God "「なるほど、[subject]じゃな?」"

    menu:
        "はい":
            jump op2
        
        "いいえ":
            God "「では何の教科が苦手なのじゃ?」"
            jump subSelect


label op2:
    God "「そうかそうか、ならばわしに任せるのじゃ!」"

    # 効果音予定地

    Me "「...今の音は一体？」"
    
    God "「なに、すぐに分かるわい!じゃあワシはもう行くからの。」"

    Me "「あ、ちょっと待っ...」"

    scene bg white
    with dissolve

    scene bg classroom evening

    "ザワザワ"

    Me "...寝てたのか。それにしても変な夢だったなぁ。"

    show teacher at center

    Tea "「お前ら静かにしろー。HRを始めるぞー。」"

    Tea "「二年生になってまだ一週間しか経ってないが、今日は転校生を紹介するぞ。じゃ、入ってくれ。」"

    hide teacher
    with dissolve

    pause 1.0

    show leap at center:
        zoom 1.2
    with dissolve

    L "「ハ...えっと、こんにちは。イギリスから来ました。リープといいます。今日からよろしくお願いします。」"

    S "「結構可愛くね？」"

    S "「聞いた？イギリスから来たんだって！」"

    Tea "「リープは長い間イギリスに住んでいたんだが、今年日本に帰ってきたんだ。仲良くしてやってくれ。」"

    Me "なるほど、帰国子女のリープさんか...英語ができない俺には縁のない子だな..."

    Tea "「じゃあ、リープの席は...おっ、[playerName]の隣の席が空いてるな。あそこに座ってくれ。」"

    L "「わかりました。」"

    Me "...おいおい、マジかよ。"

    "こうして、英語が苦手な俺とペラペラなLEAPさんとの学校生活が始まるのだった..."

    # プロローグ終わり 

label exit:
    $ renpy.quit()