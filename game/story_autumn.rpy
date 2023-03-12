label fall_bad:
L 'じゃあスタート位置につきましょうか'

# 背景：校庭（トラック）
scene bg taiikusai

'二人は大きな緊張に押しつぶされそうになりながらもスタート位置についた'

$ zakoName = "審判"
Zako 'では、位置について'
Zako 'よーい'
Zako 'ドン'

$ zakoName = "実況"
Zako 'おーーと、勢いよく前に飛び出したのは赤い彗星チームだ'

$ zakoName = "解説"
Zako '周りのチームより３倍の速度ですね'

$ zakoName = "実況"
Zako 'それを、追うのは星の白銀チーム'

$ zakoName = "解説"
Zako 'パワフルかつ精密な動きですね'

$ zakoName = "実況"
Zako 'それから巻き返し始めたのは青眼の白龍チーム'

$ zakoName = "解説"
Zako '海馬君さすがに早いですね'

$ zakoName = "実況"
Zako 'そして、それにぴったりついて行ってるのは緑の悪魔チーム'

$ zakoName = "解説"
Zako 'すごい執着力ですね。恐怖すら感じます'

$ zakoName = "実況"
Zako 'そして、トップから３馬身ぐらい離れて黒い三連星チームです'

$ zakoName = "解説"
Zako '二人三脚なので二連星です'

$ zakoName = "実況"
Zako 'オルテガ君マッシュ君頑張ってください'

$ zakoName = "解説"
Zako 'そして、全てのチーム最後の一直線に入りましたね'

Me '（よし、行けるぞ）'
Me '（このままなら一位になれるかもしれない）'

'と、その時'

$ badEndCode = 5
jump badEnd_call