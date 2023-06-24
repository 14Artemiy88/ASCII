# ASCII
ASCII graphic in terminal

<details>
  <summary>Requirements</summary>

    cv2
    numba
</details>

<details>
  <summary>Usage</summary>

 ```
usage: main.py [-h] [-s SCALE] [-ch CHARS] [-c | -b | -p] path

positional arguments:
path                  Path to file, 0 for webcam video

options:
-h, --help            show this help message and exit
-s SCALE, --scale SCALE
Scale, default 70
-ch CHARS, --chars CHARS
Chars
-c, --colored         Colored, default false
-b, --bg              Black background with colored image, default false
-p, --pixelart        Pixelart style, default false
 ```
</details>

<details>
  <summary>Example</summary>

 ```
/rrrrr/rrrrr//rr/rrrrrrrrrr((l(l1l(((llllllllllll((((((((((rr/rr//rr/r///rr/rrrrr((rrr(((((rr((r((rr(
rrrrrrrr(r/rrrrr/r((rr((r(l(1(((((llllllllllllllll((lrr(((((rr/r!:r($lrrrrrrrl!rrr(rrrr((((((((((((l(
r(r((rrrr(rr(rr((r((r((ll((((ll(lllllllllllllll11llllll(l(((((rrrrr(((l1941W44l4411((9Z4((l((((((((ll
(((r(((r(r((((((((((l(((l(((lll1l1lll1111111111111l1lllllllll((lrZ4rZ9r(WH@@9H$8W49lll((((((((((((l(l
(((((((r(((l((((lllll((l(llllll1lll1111111111111111111lr: 1lllZ4Z/rr((r8(4$@@@@$@$@8$$$8$9((((lllllll
((((((((((l(lll(((llll(lllllll1111111111111111111111 1l1! rl!(lZ((rr(lrZHW8@@@@@@@@$@@@@@@@$lllllllll
((l((((lllll(l(l((ll(llllll11111111111l1111111111/9..W. .. llllll((((rr((rl$@@@@@@@$@@@@@@@@@8H1l1lll
lll(((l111l(lll(l((lllll1111111111111Z11111111l:l! :. /.11111lll((rr(l(4(l((W8W@@@@@@@@@@@@@@@HZl1111
1111111(ll111llllll1llll1111ZZZZZZ1ZZZZZZZZ1Z$Z1.r.    11Z111l1((l(r(((l98@4H(8@@@@$$W89@$@$@@H4Z1111
Z1Z411111111111l11lZ1ZZ11111ZZZZZZZZZZZZZZZlW($9 :@:  :l1111111ll((l((((l4@@8148@@@@$8$@@@@@@$1Z11111
l1ZZZ111111111Z1Z1ZZZZZZZZZZZZZZZZZZZZ44W4:$.Z:. rl  .11ZZ1Z111l11lll1l(l8@@@@@@@@$@@@$@@@@@@$1ZZZZ1Z
l1lZZ1Z1ZZZZZ44ZZ1ZZ1!  4ZZ4444444444$1.:: !98H/ 8.   4ZZZZZZZ1Z.r/11111ll8@@@@@@@@@$$$@@@@@@HZZZZZZZ
l111111Z1ZZZ444ZZZZZ444  Z444444444//H44ZZZ4    1 lZ1! 1ZZZZrZ9l 11Z1Z1ZZZZ9Z$$@@@@@$$@@@@@@4ZZZZ1ZZ1
Z111Z1Z1ZZZZZ44444lHl :: /44H444444r444444444!9   Z!44H:ZZZZZZr/ !ZZ:ZZ4ZZ444H88$9@@@@@@@@$94Z4ZZZ111
1ZZZZZZZ4ZZZ444444444rl   4.4444444HZ 44444Z./  1.4Z4444H1rZ:1.   :!ZZZZZ44444HH48@@$49444444ZZ1ZZZl1
1ZZZ14ZZ44444444HHH$.   : Z.:Z4ZZZ44444444441! Z44Z441444Z448     :    Z4444Z41(HHW44H4444Z4ZZ4111111
1Z4ZZZ4Z4H44HH44/   ! :  . !4H444444444444H .  444H444444ZZ44Z11@  rr ../   :1lH44HHHHHH4444Z44Z411Z1
Z11Z4Z44HHHH8 :   ! : r (444444444HHH4HHHHlrr  H4HHHZ444ZZZZZZ1Zll. !/Z!::Hl4:    .1HHHHHHHH44ZZ11111
Z4Z14444H4 ( :  !  l ! .Z4Z44HZ4HHHHHH1HH99:. (H844H!H4ZH4Z111Z1HH . :/4HZ..(!H99H!..     HHHZZZZ1ZZZ
41ZZ4444!  ..  . .://  4444444444(HHHH:HHZl Zr(H(99.H44!4H4411.Z4HH.r .4Hl41/!.H9999HZl...     4Z4ZZ4
Z1444/   . . l: :.: : Z9H4WHH44HHH. HH9(:::$ :r 11 Z/.r4H449Z144Z499!  !8Z1(l9 ./WWW99W9!:1:r!  44114
4ZZ/    l : / (:.lZ. !HHHH444444 1191:9:!Z.@..Wr1  .   W94ZZ1Z4444HW:!.  1Zl4W999 !W9999WH.9H(  ZZ4ZZ
Z  :/444448. 1 ZH8r  (HZ4H4H4H44HHl H.9. WH9/.l (:/:lr. (l .lHHH4HWW!1 :. ll4WWWWWW9HWWW99H99H. 91r4Z
.r4Z441   :Z149!   4H44449H44@.  (H:.9:4@99 W!.!/ .  .!/r/(Z1  r Z / 1 . lWWWWWWWWWWWW999999   WH.4
rH4444ZZ.  14HH9r    H4ZHHH4HHl1  :r@1 l91$W9  .r::./..            4:   /.  W8888888W8WWWWWWWr   HHH:
4/ZW9HZ! (ZH44111   44H4HW1 ! r    8 9Z /: 4 :ll1!  /.: .  8WWW             88WW!88888888WWWW  9 H999
49444Hr (9H44Zlr. rrHH8H4HH       . /!91: :9.      . . 81W   W88814ZZ11Z    .W8888/$88888888H  9 9WWW
1H9999 Z49H991l .  99Z /     .: 1  /  /            H   W88$WZ  H1411l/r/88889 $8$88r 888888W. W4.999W
H999H 4H9W9WW.   :(/8 l.   9999l          4    W /4   l8888$8$     ll//$$88rrWW$88ll W888W99 ZW WH99H
HW99H1rZH!WW9 ..   .    .9WWHH9. ll : :4. !    l! W  $$Z$$$$94HZ    1 8$$$$$H 8$8lW   WW9WWr:9W 99HHW
949H.Z.9H9WH:     Z :H99WWW9WH.r8WZ 9 l     /r   lr $(Z$$$4HW/ 44@    . $$$$ZH  !r9 lWWWW99:W9!HHH9W9
ZZ1(1Z9HHl99  .W99W9 W9W9999 1  9WW1994  .::.:  / / 88 @4ll!1Z!/!!8$$  .   . 4  :   Z999W4:W99W9HH999
W44 44 H499  W8$88Z    8899$ .  WW88W$Z.     /(.:    W1Zl   !Z .r$@8$@@W!9          .9WW: H99l999HW9H
91ZlHH($H44H99WWW888      8 . WWZW9H9W9WW8W81    @ r .1Z   W  .  @@$!$$$$ !      W8W8WZ /999/H999WW9W
4Z1ZZ4rWHWHH9H89W8$8l   W     .r WW8.WWW:.888WW$4  /  /     !:.    1@( : r   $8ZW88888 WWWW1WWW8W9W91
1ZH4H4Z941ZH999WWW8$$.       4  8WW 9WW 9  ..!(4lW        9 !4  !.  /!$$1($($8$88888l.48WW8WWWW888. .
ZHHWW99:H999HWWW8888$$.$      r9WH 498Z             (:       ./ !! Z H @@$@$@@$$$$4.8$$8$8888WW8.(/ .
8W8W98  48WH988W888$$$$$@$@ . 9H:.l889Zr         .     8    .   (/ 9!.4@$$@@@@$$l@$@@$$$$$$ .:H :r.  
W9W449HHHW999W88$$8$$$@@@$@$$@$$$$@l(// $        .9   9  .l!   !/ ..  @@@@@@@Z@@@@@@@@@:  l .444 .:  
W999HHH99499W$8$$$$$WW$$@$@@WZ11lZr!4Z@   @1/     Z  (.1  .      .     W @@$88$$@: :  (l .l11. /     
8W9H99/ZW4WWWW8@4(l(114H(llZ(Hl!Z/Z!!(HH. Z(  4H$$W((!Z  .      (W (r:!H( WWW(.     .                
88$88W./WWWW88@ (4H !(Hl(1!1(1W1W:/ W1Z  .   : l H /     .     r((  l:    /   .   HrZl/:     .  4! .
W8W888rl8$8888@Z .l !::!(.(r1rrr.  W l((.       .          @:   :.  l4ZZ!::((/  :   r         !      
WW988WW$$4$@$8$@$$Z /:  !: !!!     ll@. .            (!.W.    9H9/ZH.lZl1Z41 .    ..        : .   !  
/W9$8W88$9@$$$@@@@$$$$             8 l !   .!.    / /     991 : l4.1/11/!.!/l    .. ::.  /  (      .r
...:lWW98$8$$$$$$@$@@@@@@W.        : !.    $@@$$     ! !41Z1ZH.:(l4 /  r.  :       r          /. ZZ14
WHr :.!.  .!(Z@$$@@@@@@@@@@@@@@@@@@ZW( .       !..l !((rr    .   .lZ:l!  r     :/  .     :rlZ414:/l.1
9WWW$8W8W$$$$$$$$@@@@@@@@@@@@@@@@1H4l /   ::4(      !  :((lr: . 4        .  r /l.    ..rZ44:1. .Z444l
W$8$89W9888$8$$$$@$@@@@$@@@@$88HZ.r  !14:             (.: ( .       ! l:       !/.   .: .(ZZ( Z(14lll
11:. 41/.148$WW99rrr!  (ZWH/9H.  ..(.                     .   .   !.        :.r(  .(1l1lZ1:ll! .!l/::
//!!/       .      :/Zll    ! (      !:     !!: :   . 1! !:1  !   .  !(494H1llZZ ((Z1ZlZ/ lrZZ4ZH1444
 ```
</details>
