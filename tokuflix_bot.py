import telebot
import re
                                                                          ## TOKEN
bot = telebot.TeleBot("1658023349:AAEl41ckDmUjAX8bEeaI3vHp3eFCkvQR8AI")
##--------------------------------------------------------------------------------
                                                                          ## SÉRIES
@bot.message_handler(regexp="/kamen rider")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/11/1971-kamen-rider.html')

@bot.message_handler(regexp="/kamen rider x")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/11/1974-kamen-rider-x.html')

@bot.message_handler(regexp="/amazon")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/11/1974-kamen-rider-amazon.html')

@bot.message_handler(regexp="/stronger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/11/1975-kamen-rider-stronger.html')

@bot.message_handler(regexp="/skyrider")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/11/1979-kamen-rider-skyrider.html')

@bot.message_handler(regexp="/kamen rider")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1971-kamen-rider.html')

@bot.message_handler(regexp="/kamen rider filmes")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/12/1971-kamen-rider-filmes.html')

@bot.message_handler(regexp="/v3")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/1973-v3.html')

@bot.message_handler(regexp="/x")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1974-kamen-rider-x.html')

@bot.message_handler(regexp="/amazon")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1974-kamen-rider-amazon.html')

@bot.message_handler(regexp="/stronger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1975-kamen-rider-stronger.html')

@bot.message_handler(regexp="/skyrider")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1979-kamen-rider-skyrider.html')

@bot.message_handler(regexp="/galaxy king")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1980-8-kamen-riders-vs-galaxy-king.html')

@bot.message_handler(regexp="/super1")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1980-kamen-rider-super-1.html')

@bot.message_handler(regexp="/super-1")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1980-kamen-rider-super-1.html')

@bot.message_handler(regexp="/shin")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1992-shin-kamen-rider.html')

@bot.message_handler(regexp="/zo")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1993-kamen-rider-zo.html')

@bot.message_handler(regexp="/j")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1994-kamen-rider-j.html')

@bot.message_handler(regexp="/world")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1994-kamen-rider-world.html')

@bot.message_handler(regexp="/kuuga")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2000-kamen-rider-kuuga.html')

@bot.message_handler(regexp="/agito")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2001-kamen-rider-agito.html')

@bot.message_handler(regexp="/ryuki")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2002-kamen-rider-ryuki.html')

@bot.message_handler(regexp="/555")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2003-kamen-rider-555.html')

@bot.message_handler(regexp="/blade")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2004-kamen-rider-blade.html')

@bot.message_handler(regexp="/hibiki")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2005-kamen-rider-hibiki.html')

@bot.message_handler(regexp="/kabuto")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2006-kamen-rider-kabuto.html')

@bot.message_handler(regexp="/den o")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2007-kamen-rider-den-o.html')

@bot.message_handler(regexp="/den-o")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2007-kamen-rider-den-o.html')

@bot.message_handler(regexp="/kamen rider den-o")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2007-kamen-rider-den-o.html')

@bot.message_handler(regexp="/kiva")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2008-kamen-rider-kiva.html')

@bot.message_handler(regexp="/w")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2009-kamen-rider-w.html')

@bot.message_handler(regexp="/double")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2009-kamen-rider-w.html')

@bot.message_handler(regexp="/decade")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/2009-decade.html')

@bot.message_handler(regexp="/ooo")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2010-kamen-rider-ooo.html')

@bot.message_handler(regexp="/fourze")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2011-kamen-rider-fourze.html')

@bot.message_handler(regexp="/wizard")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/2012-kamen-rider-wizard.html')

@bot.message_handler(regexp="/gaim")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/2013-kamen-rider-gaim.html')

@bot.message_handler(regexp="/drive")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/2014-kamen-rider-drive.html')

@bot.message_handler(regexp="/ghost")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/2015-kamen-rider-ghost.html')

@bot.message_handler(regexp="/ex-aid")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/07/2016-kamen-rider-ex-aid.html')

@bot.message_handler(regexp="/exaid")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/07/2016-kamen-rider-ex-aid.html')

@bot.message_handler(regexp="/ex aid")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/07/2016-kamen-rider-ex-aid.html')


@bot.message_handler(regexp="/build")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/07/2017-kamen-rider-build.html')

@bot.message_handler(regexp="/zero one")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/2019-kamen-rider-zero-one.html')

@bot.message_handler(regexp="/zero-one")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/2019-kamen-rider-zero-one.html')

@bot.message_handler(regexp="/kamen rider")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/11/1971-kamen-rider.html')

@bot.message_handler(regexp="/ichigo")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/11/1971-kamen-rider.html')

@bot.message_handler(regexp="/ichigo")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/11/1971-kamen-rider.html')

@bot.message_handler(regexp="/gorenger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/1975-gorenger.html')

@bot.message_handler(regexp="/jakq")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1977-jakq.html')

@bot.message_handler(regexp="/battle fever j")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1979-battle-fever-j.html')

@bot.message_handler(regexp="/denziman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1980-denziman.html')

@bot.message_handler(regexp="/sun vulcan")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1981-sun-vulcan.html')

@bot.message_handler(regexp="/goggle v")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1982-goggle-v.html')

@bot.message_handler(regexp="/goggle v legendado")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1982-goggle-v-legendado.html')

@bot.message_handler(regexp="/dynaman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1983-dynaman.html')

@bot.message_handler(regexp="/bioman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1984-bioman.html')

@bot.message_handler(regexp="/maskman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1987-maskman.html')

@bot.message_handler(regexp="/liveman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1988-liveman.html')

@bot.message_handler(regexp="/liveman-dublado")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/03/1988-liveman-dublado.html')

@bot.message_handler(regexp="/turboranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1989-turboranger.html')

@bot.message_handler(regexp="/fiveman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1990-fiveman.html')

@bot.message_handler(regexp="/jetman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1991-jetman.html')

@bot.message_handler(regexp="/zyuranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1992-zyuranger.html')

@bot.message_handler(regexp="/dairanger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1993-dairanger.html')

@bot.message_handler(regexp="/kakuranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1994-kakuranger.html')

@bot.message_handler(regexp="/ohranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1995-ohranger.html')

@bot.message_handler(regexp="/carranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1996-carranger.html')

@bot.message_handler(regexp="/megaranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1997-megaranger.html')

@bot.message_handler(regexp="/gingaman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1998-gingaman.html')

@bot.message_handler(regexp="/gogo five")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1999-gogo-five.html')

@bot.message_handler(regexp="/timeranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2000-timeranger.html')

@bot.message_handler(regexp="/gaoranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2001-gaoranger.html')

@bot.message_handler(regexp="/hurri")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/07/2002-hurri.html')

@bot.message_handler(regexp="/abaranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2003-abaranger.html')

@bot.message_handler(regexp="/dekaranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2004-dekaranger.html')

@bot.message_handler(regexp="/magiranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2005-magiranger.html')

@bot.message_handler(regexp="/boukenger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2006-boukenger.html')

@bot.message_handler(regexp="/gekiranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2007-gekiranger.html')

@bot.message_handler(regexp="/go onger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2008-go-onger.html')

@bot.message_handler(regexp="/shinkenger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2009-shinkenger.html')

@bot.message_handler(regexp="/goseiger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/2010-goseiger.html')

@bot.message_handler(regexp="/gokaiger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/2011-gokaiger.html')

@bot.message_handler(regexp="/go busters")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/2012-go-busters.html')

@bot.message_handler(regexp="/akibaranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/2012-akibaranger.html')

@bot.message_handler(regexp="/kyoryuger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/2013-kyoryuger.html')

@bot.message_handler(regexp="/akibaranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/2013-akibaranger.html')

@bot.message_handler(regexp="/toqger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/2014-toqger.html')

@bot.message_handler(regexp="/ninninger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/11/2015-ninninger.html')

@bot.message_handler(regexp="/zyuohger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/2016-zyuohger.html')

@bot.message_handler(regexp="/kyuranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/2017-kyuranger.html')

@bot.message_handler(regexp="/lupinranger vs patranger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/2018-lupinranger-vs-patranger.html')

@bot.message_handler(regexp="/kamen rider")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1971-kamen-rider.html')

@bot.message_handler(regexp="/kamen rider")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/11/1971-kamen-rider.html')

@bot.message_handler(regexp="/gavan dublado")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1982-gavan-dublado.html')

@bot.message_handler(regexp="/gavan legendado")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/1982-gavan-legendado.html')

@bot.message_handler(regexp="/sharivan dublado")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1983-sharivan-dublado.html')

@bot.message_handler(regexp="/kamen rider filmes")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/12/1971-kamen-rider-filmes.html')

@bot.message_handler(regexp="/shaider dublado")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1984-shaider-dublado.html')

@bot.message_handler(regexp="/spielvan")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1986-spielvan.html')

@bot.message_handler(regexp="/metalder")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1987-metalder.html')

@bot.message_handler(regexp="/winspector")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1990-winspector.html')

@bot.message_handler(regexp="/solbrain")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1991-solbrain.html')

@bot.message_handler(regexp="/exceedraft")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1992-exceedraft.html')

@bot.message_handler(regexp="/janperson")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1993-janperson.html')

@bot.message_handler(regexp="/b fighter kabuto")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/11/1996-b-fighter-kabuto.html')

@bot.message_handler(regexp="/ultra q")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/11/1966-ultra-q.html')

@bot.message_handler(regexp="/ultraman 80")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/10/1980-ultraman-80.html')

@bot.message_handler(regexp="/kamen rider")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2019/11/1971-kamen-rider.html')

@bot.message_handler(regexp="/ultra q")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1966-ultra-q.html')

@bot.message_handler(regexp="/ultraman ace")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/07/1972-ultraman-ace.html')

@bot.message_handler(regexp="/ultraman 80")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/08/1980-ultraman-80.html')

@bot.message_handler(regexp="/ultraman great")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/08/1990-ultraman-great.html')

@bot.message_handler(regexp="/ultraman tiga")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/08/1996-ultraman-tiga.html')

@bot.message_handler(regexp="/ultraman dyna")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/08/1997-ultraman-dyna.html')

@bot.message_handler(regexp="/ultraman gaia")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/1998-ultraman-gaia.html')

@bot.message_handler(regexp="/kamen rider")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1971-kamen-rider.html')

@bot.message_handler(regexp="/zone fighter")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1973-zone-fighter.html')

@bot.message_handler(regexp="/kaiketsu lion maru")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1972-kaiketsu-lion-maru.html')

@bot.message_handler(regexp="/kikaider")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1972-kikaider.html')

@bot.message_handler(regexp="/kikaider 01")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1973-kikaider-01.html')

@bot.message_handler(regexp="/fuun lion maru")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1973-fuun-lion-maru.html')

@bot.message_handler(regexp="/kaiketsu zubat")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1977-kaiketsu-zubat.html')

@bot.message_handler(regexp="/zubat")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1977-kaiketsu-zubat.html')

@bot.message_handler(regexp="/kaiketsu")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1977-kaiketsu-zubat.html')

@bot.message_handler(regexp="/spider man")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1978-spider-man.html')

@bot.message_handler(regexp="/machineman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1984-machineman.html')

@bot.message_handler(regexp="/bicrosser")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1985-bicrosser.html')

@bot.message_handler(regexp="/cybercop")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1988-cybercop.html')

@bot.message_handler(regexp="/patrine")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1990-patrine.html')

@bot.message_handler(regexp="/voicelugger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1999-voicelugger.html')

@bot.message_handler(regexp="/ryukendo")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2006-ryukendo.html')

@bot.message_handler(regexp="/lion maru g")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2006-lion-maru-g.html')

@bot.message_handler(regexp="/panchanne")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2007-panchanne.html')

@bot.message_handler(regexp="/tomica hero rescue force")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2008-tomica-hero-rescue-force.html')

@bot.message_handler(regexp="/tomica hero rescue fire")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/2009-tomica-hero-rescue-fire.html')

@bot.message_handler(regexp="/godzilla")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1954-godzilla.html')

@bot.message_handler(regexp="/godzilla ataca novamente")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1955-godzilla-ataca-novamente.html')

@bot.message_handler(regexp="/godzilla o rei dos monstros")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/1956-godzilla-o-rei-dos-monstros.html')

@bot.message_handler(regexp="/king kong")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/1962-king-kong-vs-godzilla.html')

@bot.message_handler(regexp="/mothra vs godzilla")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/1964-mothra-vs-godzilla.html')

@bot.message_handler(regexp="/ghidorah o monstro tricefalo")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/1964-ghidorah-o-monstro-tricefalo.html')

@bot.message_handler(regexp="/invasao do astro monstro")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/1965-invasao-do-astro-monstro.html')

@bot.message_handler(regexp="/godzilla vs ebirah")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/1966-godzilla-vs-ebirah.html')

@bot.message_handler(regexp="/o filho de godzilla")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/1967-o-filho-de-godzilla.html')

@bot.message_handler(regexp="/kamen rider cavaleiro d")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/01/2009-kamen-rider-cavaleiro-d.html')

@bot.message_handler(regexp="/sukeban deka")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1985-sukeban-deka.html')

@bot.message_handler(regexp="/macross tv")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/10/1982-macross-tv.html')

@bot.message_handler(regexp="/don dracula")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1982-don-dracula.html')

@bot.message_handler(regexp="/hokuto no ken")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/1984-hokuto-no-ken.html')

@bot.message_handler(regexp="/hokuto no ken movie")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/08/1986-hokuto-no-ken-movie.html')

@bot.message_handler(regexp="/hokuto no ken 2")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/08/1987-hokuto-no-ken-2.html')

@bot.message_handler(regexp="/zillion")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/1987-zillion.html')

@bot.message_handler(regexp="/city hunter")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/1987-city-hunter.html')

@bot.message_handler(regexp="/city hunter 2")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/08/1988-city-hunter-2.html')

@bot.message_handler(regexp="/shurato")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1989-shurato.html')

@bot.message_handler(regexp="/patlabor tv")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1989-patlabor-tv.html')

@bot.message_handler(regexp="/samurai warriors")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1989-samurai-warriors.html')

@bot.message_handler(regexp="/city hunter 357 magnum")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/08/1989-city-hunter-357-magnum.html')

@bot.message_handler(regexp="/city hunter 3")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/1989-city-hunter-3.html')

@bot.message_handler(regexp="/guyver")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1989-guyver.html')

@bot.message_handler(regexp="/lodoss war")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/1990-lodoss-war.html')

@bot.message_handler(regexp="/fly")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1991-fly.html')

@bot.message_handler(regexp="/super campeoes j")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1992-super-campeoes-j.html')

@bot.message_handler(regexp="/sailor moon classic")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1992-sailor-moon-classic.html')

@bot.message_handler(regexp="/ninja scroll")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/1993-ninja-scroll.html')

@bot.message_handler(regexp="/sailor moon r")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/08/1993-sailor-moon-r.html')

@bot.message_handler(regexp="/Ketai Sousakan")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/04/2008-ketai-sousakan-7.html')

@bot.message_handler(regexp="/Ketai")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/04/2008-ketai-sousakan-7.html')

@bot.message_handler(regexp="/Sousakan")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/04/2008-ketai-sousakan-7.html')

@bot.message_handler(regexp="/crystania")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/1995-crystania.html')

@bot.message_handler(regexp="/tenchi muyo universe")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/1995-tenchi-muyo-universe.html')

@bot.message_handler(regexp="/el hazard wanderers")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/1995-el-hazard-wanderers.html')

@bot.message_handler(regexp="/samurai x dublado")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/1996-samurai-x-dublado.html')

@bot.message_handler(regexp="/crystania")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/1996-crystania.html')

@bot.message_handler(regexp="/samurai x leg")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/1996-samurai-x-leg.html')

@bot.message_handler(regexp="/lodoss war")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/04/1998-lodoss-war.html')

@bot.message_handler(regexp="/super hero spirits")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/2000-super-hero-spirits.html')

@bot.message_handler(regexp="/super sentai spirits")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/2004-super-sentai-spirits.html')

@bot.message_handler(regexp="/super sentai spirits")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/02/2006-super-sentai-spirits.html')

@bot.message_handler(regexp="/gransazer")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/01/2003-gransazer.html')


@bot.message_handler(regexp="/sukeban deka II")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1985-sukeban-deka-ii.html')

@bot.message_handler(regexp="/sukeban 2")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/05/1985-sukeban-deka-ii.html')

@bot.message_handler(regexp="/kiramager")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/01/2020-kiramager.html')

@bot.message_handler(regexp="/zenkaiger")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/03/2021-zenkaiger_9.html')

@bot.message_handler(regexp="/patrine")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/03/1990-patrine.html')

@bot.message_handler(regexp="/jaspion")
def handle_message(message):
    bot.reply_to(message, 'Jaspion está com a SATO ainda... Mas quem sabe, em breve..')

@bot.message_handler(regexp="/changeman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/06/1985-changeman-dublado_24.html')

@bot.message_handler(regexp="/flashman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/06/1986-flashman-dublado_25.html')

@bot.message_handler(regexp="/jirayia")
def handle_message(message):
    bot.reply_to(message, 'jirayia está com a SATO ainda... Mas quem sabe, em breve..')

@bot.message_handler(regexp="/power ranger")
def handle_message(message):
    bot.reply_to(message, 'Não tem Power Rangers no Tokuflix, pois existe licença para PR no Brasil.')

@bot.message_handler(regexp="/kamen rider saber")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/2020-kamen-rider-saber_15.html')

@bot.message_handler(regexp="/Blue")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/01/1994-blue-swat_18.html')

@bot.message_handler(regexp="/Swat")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/01/1994-blue-swat_18.html')

@bot.message_handler(regexp="/podcast")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/p/podcast-tokuflix.html')

@bot.message_handler(regexp="/saber")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/09/2020-kamen-rider-saber_15.html')

@bot.message_handler(regexp="/power rangers")
def handle_message(message):
    bot.reply_to(message, 'Não tem Power Rangers no Tokuflix, pois existe licença para PR no Brasil.')

@bot.message_handler(regexp="/ultraman")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2020/06/1966-ultraman.html')

@bot.message_handler(regexp="/robomaru")
def handle_message(message):
    bot.reply_to(message, 'https://www.tokuflix.com/2021/09/1982-batten-robomaru_5.html')

@bot.message_handler(regexp="/bokunopico")
def handle_message(message):
    bot.reply_to(message, 'boku-no-QUEM???')

@bot.message_handler(regexp="/good bot")
def handle_message(message):
    bot.reply_to(message, 'Muito obrigado! --> Tokuflix.com :)')
bot.polling()

