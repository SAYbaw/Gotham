# basic.show_number(decin2) #M
# basic.show_number(decinx)  #L
def conv(num: number):
    x = 0
    while x < 8:
        if num / 2 - int(num / 2) != 0:
            list2[x] = 1
        else:
            list2[x] = 0
        num = int(num / 2)
        x += 1
    # set up screen
    basic.clear_screen()
    x = 1
    while x < 5:
        led.plot_brightness(x, 4, 5)
        x += 1
    x = 1
    while x < 5:
        led.plot_brightness(x, 2, 5)
        x += 1
    n = 0
    while n < 4:
        if list2[n] == 1:
            led.plot(4 - n, 4)
        n += 1
    n = 4
    while n < 8:
        if list2[n] == 1:
            led.plot(8 - n, 2)
        n += 1

def on_button_pressed_a():
    global hh, tt, uu, mm, ll, decin
    if decip == True and allset == False:
        if hhs == False:
            hh = hh + 1
            if hh == 3:
                hh = 0
            basic.show_number(hh)
        if hhs == True and tts == False:
            tt = tt + 1
            if hh == 2:
                troll = 6
            else:
                troll = 10
            if tt == troll:
                tt = 0
            basic.show_number(tt)
        if hhs == True and tts == True:
            uu = uu + 1
            if hh == 2:
                uroll = 6
            else:
                uroll = 10
            if uu == uroll:
                uu = 0
            basic.show_number(uu)
    if decip == False:
        # if mms:
        # basic.show_string("true")
        if mms == False:
            mm = mm + 1
            if mm == 16:
                mm = 0
            basic.show_string("" + (hexa[mm]))
        if mms and lls == False:
            # asic.show_string("z")
            ll = ll + 1
            if ll == 16:
                ll = 0
            basic.show_string("" + (hexa[ll]))
    if allset:
        decin = decin + 1
        if decin > 255:
            decin = 255
        # basic.show_number(decin)
        convx(decin)
        conv(decin)
input.on_button_pressed(Button.A, on_button_pressed_a)

def convx(dex: number):
    global decin2, decinx
    decin2 = int(dex / 16)
    decinx = dex - decin2 * 16

def on_button_pressed_ab():
    basic.clear_screen()
    basic.show_number(decin)
    # show Dec
    basic.show_string("=")
    convx(decin)
    basic.show_string("" + (hexa[decin2]))
    # show Hex most sig
    basic.show_string(":")
    basic.show_string("" + (hexa[decinx]))
    # show Hex least sig
    conv(decin)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global decin, uus, tts, hhs, allset, lls, mms
    if allset == True:
        # basic.show_string("allset =t")
        decin = decin - 1
        if decin < 0:
            decin = 0
        # basic.show_number(decin)
        convx(decin)
        conv(decin)
    if decip == True and allset == False:
        if hhs == True and tts == True:
            uus = True
        if hhs == True and tts == False:
            tts = True
            basic.show_string("U")
        if hhs == False:
            hhs = True
            basic.show_string("T")
        if hhs == True and tts == True and uus == True and decip == True:
            allset = True
            decin = hh * 100 + tt * 10 + uu
            # +1  #1 added b pressed takes 1 away
            conv(decin)
    if decip == False and allset == False:
        # Hex in
        if mms == True:
            lls = True
        if mms == False and lls == False:
            mms = True
            basic.show_string("L")
        if mms and lls:
            # basic.show_number(mm)
            # basic.show_string(":")
            # basic.show_number(ll)
            decin = mm * 16 + ll
            # basic.show_number(decin)
            convx(decin)
            conv(decin)
            allset = True
input.on_button_pressed(Button.B, on_button_pressed_b)

uus = False
decinx = 0
decin2 = 0
lls = False
mms = False
tts = False
hhs = False
allset = False
hexa: List[str] = []
uu = 0
tt = 0
hh = 0
decin = 0
ll = 0
mm = 0
selected = False
h = 0
hexip = False
if selected == False:
    if input.button_is_pressed(Button.B):
        basic.show_string("M")
        decip = False
    else:
        basic.show_string("H")
        decip = True
    selected = True
mm = -1
ll = -1
selected = False
decip
current = decin
hh = -1
tt = -1
uu = -1
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
hexa = ["0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"]
hexnum = [128, 64, 32, 16, 8, 4, 2, 1]
