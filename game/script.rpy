define L = Character('Leap', color="#26aa5d")
define Me = Character('自分', color="#000000")
define Mom = Character('母', color="#6b3d01")
define God = Character('神', color="#5f6634")
define cd = Character("車掌", color="#000000")
define Ano = Character('???', color="#252525")

init:
    $ import module.leapModule as leapModule

    python:
        LEAP_PATH = config.basedir + r"\game\module\leap.csv"
        #LEAP_PATH = "/game/module/leap.csv"
        leapModule.leapPathSet(LEAP_PATH)

    image bg classroom evening = im.Scale("bg classroom evening notrim.jpg", 1280, 720)
    image leap normal = im.Scale("leap normal.png", 800, 1600)
    image leap smile = im.Scale("leap smile.png", 800, 1600)
    image leap surprise = im.Scale("leap surprise.png", 800, 1600)
    image leap question = im.Scale("leap question.png", 800, 1600)
    image leap question_mark = im.Scale("leap question_mark.png", 800, 1600)

    define leapPos = Position(xancor=0.0, ypos=2.15)

    $ progress = 1 #ストーリーの進行状況
    $ like = 30#好感度


label start:
    jump Opening1

label exit:
    return