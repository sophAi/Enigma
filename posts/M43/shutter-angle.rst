.. title: GH2/GX1 - 24p, 60i, 30p, 還有60p，以及快門速度(shutter speed or shutter angle)的關係(v0.1)
.. slug: shutter-angle
.. date: 20130913 10:08:37
.. tags: 學習與閱讀
.. link: 
.. description: Created at 20130412 11:35:57

.. 請記得加上slug，會以slug名稱產生副檔名為.html的文章
.. 同時，別忘了加上tags喔!
.. <body>

*****************
各式錄影規格
*****************

5/23更新，有人提到以GH2錄影時，60i或60p比24p還流暢，其實是忽略了錄影階段shutter speed才是真正的影響因素，不然現今的電影錄製(24p)都不能應用在動作片上了。GH2比GX1以及其他類似的相機方便的地方就是，他的shutter speed是可以手動選擇的，GX1則只能在1/50s,1/60s,1/100s,以及1/120s間切換，至於其他不能手動調整快門速度的相機呢?我猜frame rate是多少，快門速度就固定是多少吧!另外，日光燈下的水波紋也是跟shutter speed有關，例如GX1的PAL機身，只要將shutter speed設成1/60s的倍數，就可以消除60Hz電壓頻率下日光燈的閃爍紋。那為什麼有人會強調只有NTSC的機身才能消除呢?原因在於這些機身的shutter speed都是固定在frame rate的倍數無法調整， 總而言之，GX1以後的Panasonic M43相機應該就不會再有PAL或NTSC的日光燈水波紋問題了，最後內文小更新有關高frame rate對slow motion的幫助。

5/10更新，把一些該加上去的連結都補上了。 

.. TEASER_END

開始前，先麻煩各位惡補一下interlaced跟progressive的分別，以及field(場)與frame(影格，禎)的區別

可先參考wikipedia，而以下的解釋都以NTSC為例，如對應到PAL，請將30p/60i/60p或30fps改成25p/50i/50p及25fps:

首先我們先認識一下各個FHD/HD的寫法，根據EBU的規範:

    1080i60表示1920x1080 interlaced, 60 fields per second，其中奇與偶數field組成一個frame

    1080i/30表示1920x1080 interlaced, 30 frames per second，跟1080i60未必是等價的

    1080p/24表示1920x1080 progressive, 24 frames per second 

    720p/60表示1280x720 progressive, 60 frames per second 

以此類推，然而1080p/30，1080p/60都是最早的AVCHD 1.0的規範裡尚未制定的，如果數位相機或錄影機的sensor output本身可以輸出30p 該如何是好呢?

GH2的HBR或是GX1的AVCHD裡的1080i60就是這個情況下的產物，在這兩個模式下，sensor output都是30p (30 frames per second, 30fps)，那麼要如何將30p包裝到60i的格式裡呢?

最簡單的方法就是將30p的每一個frame複製成兩個一模一樣的field，每個field還是一樣只有奇數行或偶數行，只是來源是同一個畫面，就可以用60i的格式儲存30p的內容，如此一來也不需要去交錯，即使影片播放軟體辨認成60i的影片，他仍是貨真價實的30p，這個方法稱為progressive segmented frame(PsF)，在progressive的螢幕上播放(LCD--液晶螢幕)，不會有任何交錯格式的現象產生。這就是為什麼如果GX1可以破解流量，將可以非常逼近GH2的HBR模式。

要辨認這個1080i60是否為PsF的方式包裝30p的內容，必須從廠商所提供的規格去了解，例如說明書裏面寫到:

1080i60, sensor output 30fps

就表示這是用30p的輸出儲存到1080i60的格式裡，也就是貨真價實的1080p/30，例如GX1的說明書，還有GH2的國外官網對HBR模式都是這樣註明的。

而GH2的說明書裡寫的是1080i60, sensor output為60i，表示sensor output為60fps，是貨真價實的60i，也就是兩個完全不同畫面的field，因此在非交錯掃描的播放設備上會出現鋸齒狀的交錯瑕疵，如這個網址的畫面:

http://www.100fps.com/

在原生交錯掃描的CRT(映像管)電視機上，播放真實60i的影片是效果最好的，因為他的掃描頻率就幾乎是60Hz(正確來說是59.94Hz)，以奇數行畫面與偶數行畫面的順序交互秀出，因為這個特性加上人眼視覺暫留，不會察覺到任何影像呈現的問題，同時還能用30p的頻寬實現60 fps，這其實是一個很聰明的方法，然而現在這種CRT螢幕已經愈來愈少了，現今大部分的播放設備，例如LCD都是屬於Progressive的方式(不分奇偶行，也就是只能呈現一個完整的frame)呈現畫面，因此60i的影片在播放上會出現問題，需要模擬交錯掃描，也就是所謂「去交錯(deinterlacing)」要做的事，去交錯有分blender, interpolation,跟doubler，根據使用的演算法不同，最後得到的frame rate其實會不同，例如blender的frame rate可能為30 frames per second(30fps)，而doubler的frame rate則為60 frames per second(60fps)，有人認為60i為30 frames per second，其實是不太正確的(即使是NTSC的wiki說明也點不周全，容易產生誤導)，他的畫面錄製仍然為60fps(60 fields/s)，每一個field都來自一個獨立的畫面，只是後端播放時，會根據去交錯的方法而變成30 frames per second或60 frames per second。

因此GH2的1080i60完全是針對交錯掃描的CRT而生的，而其HBR模式以及GX1的1080i60則骨子裡是真的1080p/30，只是為了考量現有播放設備的相容性，以60i的格式包裝30p的內容。那麼錄影時shutter speed/angle要如何選擇呢?

如果是GH2的1080i60，則1/120s為180度 shutter angle，也就是每個field曝光一半的時間，因為sensor output是60 fields per second，同理可推，60p為1/120s，24p為1/48s；如果是GH2的HBR或GX1的1080i60，則1/60s為180度 shutter angle(每個frame曝光一半的時間)，因為sensor output都是30 frames per second，1080i60(非PsF)為1/120s而非1/60s的原因是在錄製階段，是要看field而不是看frame，因為frame rate是可以在播放端決定，而且所謂的field才是真正獨立的畫面，因此shutter angle的計算式要用field rate而不是frame rate的。事實上，Shutter speed的設定效果遠大於frame rate或field rate的選擇，例如有人會說24p有「電影感」，其實是nonsense(不好意思，筆者以前也說過電影感這種話)，只有shutter speed的設定才會造成影片的流暢與停頓感，就算都設在180度shutter angle，30fps跟60fps的畫面凝結感與曝光度也不同，與其執著於shutter angle設成180度，不如考量shutter speed對畫面真正的影響，才不會落入shutter angle的迷思，因此我都建議別人多試試不同的shutter speed。真的想要有電影的流暢感，請以1/48s的shutter speed為界限調整。而實情更有可能是--真正的電影感是不存在的。

較快的shutter speed，會讓畫面的停頓感更顯著(英文叫stutter)，容易凝結流動中的物體，例如水滴，而較慢的shutter speed，則容易產生動態殘影(motion blur)，有時反而不容易察覺到畫面的停頓而覺得流暢許多，同時shutter speed也會決定一個field/frame曝光的程度，是跟光圈與ISO值連動的。因此適時的調整shutter speed對於錄影來說是一件重要的事。另外要提到的是，理論上shutter angle大於360度就等於每個frame/field均完整的曝光，例如24p的shutter speed無法低於1/24s，HBR無法低於1/30s，不過有趣的是，如果將GH2的手動錄影模式設成720/60p，則shutter speed可以慢到1/30s，相當於720 shutter degree，這個問題就算是筆者去Ptool論壇詢問也沒有人給出答案...。

那麼24p, 30p, 60p(frame rate)真正影響的是什麼呢?有兩個層面，一個是播放端的更新頻率，例如LCD為60Hz, CRT可能為72Hz，那麼24p在60Hz的設備上播放就產生同步的問題，同理，30/60p在72Hz的設備上也有同步的問題，這個就跟播放軟體，顯示卡，以及螢幕間的設定與協調有關，小弟的建議是使用60Hz設備的人儘量用30/60p，或是將24p轉成30/60p也是可以(2-3 pulldown)，在播放與處理影片面臨的問題最小，另一層面則是frame rate愈小，panning的果凍效應(jello effect)也會愈明顯，這是因為GH2/GX1是採用Rolling shutter的機制紀錄畫面，因此拍動作的場景可以使用GH2的720p/60格式(sensor output 60fps)大幅改善直線搖擺的問題，而GX1的720p/60的sensor output還是30 fps，因此果凍效應跟切換到1080i60模式(PsF)是差不多的，另外60p/i的錄製，對於slow motion的後製效果也比較好，因為每秒取得的畫面更多。

而1080p/60是屬於AVCHD2.0的規範，由上可知無論是1080i60或是1080p60都可以涵蓋1080p30的影片內容，因此看不到真正有關1080p/30的規範，未來的播放與錄影設備應該會漸漸朝向1080p/60發展。

希望以上一次釐清所有跟錄影模式有關的問題。

.. </body>

