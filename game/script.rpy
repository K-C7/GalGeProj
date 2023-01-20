define L = Character('Leap', color="#26aa5d")
define Me = Character('自分', color="#000000")
define Mom = Character('母', color="#6b3d01")
define Tea = Character('担任', color="#006d75")
define God = Character('神', color="#5f6634")
define S = Character("生徒", color="#000000")
define Ano = Character('???', color="#252525")

init:
    $ import module.leapModule as leapModule

    python:
        LEAP_PATH = config.basedir + r"\game\module\leap.csv"
        print(LEAP_PATH)
        leapModule.leapPathSet(LEAP_PATH)

    image bg classroom evening = im.Scale("bg classroom evening notrim.jpg", 1280, 720)

    $ progress = 1 #ストーリーの進行状況


label start:
    jump Opening1

label exit:
    $ renpy.quit()