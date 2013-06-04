.. title: 解放M43相機的實力
.. slug: M43_power
.. date: 20130604 15:03:06
.. tags: 
.. link: 
.. description: Created at 20130604 13:46:32
.. ===================================Metadata↑================================================
.. ● 記得加上tags: 人生，狗狗，程式，生活紀錄，英文，閱讀，教養，科學，mathjax
.. ● 記得加上slug，會以slug內容作為檔名(html檔)
.. ===================================文章起始↓================================================

從GF1開始，一直都沒有好好使用過GF1的Raw檔格式，因為主要是用Linux，還沒有時間好好研究，一直到第二個小baby快出生了，才比較有心去研究一下什麼是Raw檔，測試的結果發現Raw檔轉換成jpeg果然好太多，jpeg直出顏色有點怪異且平淡，而且能救的部份有限，看看下圖的差異(點選放大):


.. figure:: http://farm8.staticflickr.com/7355/8944800437_40bf61f216.jpg
   :target: http://farm8.staticflickr.com/7355/8944800437_40bf61f216.jpg
   :width: 500px
   :align: center

   (相機輸出JPEG)

.. figure:: http://farm9.staticflickr.com/8261/8945422564_950e569a95.jpg
   :target: http://farm9.staticflickr.com/8261/8945422564_950e569a95.jpg
   :width: 500px
   :align: center

   (RAW轉JPEG)

.. figure:: http://farm8.staticflickr.com/7446/8944799671_433a53f617.jpg
   :target: http://farm8.staticflickr.com/7446/8944799671_433a53f617.jpg
   :width 500px
   :align: center

   (JPEG直出)

.. figure:: http://farm8.staticflickr.com/7378/8944799319_1d841c923b.jpg
   :target: http://farm8.staticflickr.com/7378/8944799319_1d841c923b.jpg
   :width: 500px
   :align: center

   (RAW轉JPEG)

可以觀察到RAW轉JPEG的細節其實更多，立體感也更好，膚色也很容易調到想要的樣子，此外GH2的RAW檔似乎照的範圍比JPEG還要再廣些，可以觀察畫面邊緣，JPEG感覺好像是被裁剪過一點點，如此一來或許以14mm的焦段配合16:9的比例，照出來的等效焦距還能比14mm更廣。(補充:後來知道這個裁切是因為機身數位修正變形的緣故)

RAW檔還有一個更大的好處，就是那些什麼機身的色彩啦，白平衡什麼blahblah的設定都可以不用去管他了，只要注意3個地方就好:

#. 光圈值
#. 快門值
#. ISO值



這樣最大的好處就是把拍照的手續降到最低，只要專心在構圖跟準確曝光就夠了~當然由於線性Gamma的特性，其實最正確的曝光應該是離過曝裁切再低一點才能確保色階的平滑以及減少暗部雜訊，普通認為寧可暗不可接近過曝的觀點其實不儘正確，因此記得也把相機的histogram功能打開，時時注意到有沒有亮部裁切就行了，這些在Raw聖經這本書裏面都有詳細解說，簡單設定好後，對於相機日文介面苦手的老婆，真是一大福音，我也可以把有限Fn鈕分配給曝光跟對焦相關的功能，例如:

#. Fn1為曝光模式，用來決定點測光還是中央重點測光等.。
#. Fn2為對焦模式(Off/Q-AF/C-AF)
#. Fn3為畫面比例(16:9/4:3/3:2/1:1)



原本1跟2是分配給ExTele擴展望遠跟色彩調整，改用Raw檔後這兩個設定就沒有意義了，所以最後改成以上的設定了~只是如此一來我要考慮要不要乾脆把IResolution跟IDynamic功能關掉...還能節省點電量加快反應速度

當初使用JPEG直出是因為Linux使用Picasa還蠻方便的，雖然中文目錄名稱有時都是方塊，不過跟Picasa相簿整合不錯，速度也蠻快的，改用RAW檔後第一個要確認的就是影像處理的部份，光是這部份就花了我好幾天的時間研究，還去圖書館借了一本DSLR Raw檔聖經來K(蠻推荐這一本的)，終於完全了解所謂Raw histogram跟Output histogram的差別，還有Exposure,shade,brightness,contrast跟Gamma曲線的關係，當然還有最重要的線性Gamma的概念以及Raw檔的格式，這些觀念建議想進入Raw的世界的人一定要好好花時間了解一下，用Raw還有一個特性就是相機的數位修正是無效的，例如暗角，桶狀變形，跟色散差，因此這可讓我傷腦筋一陣子了，好在我查到Linux上還有Lensfun這個資料庫，用apt下載後去/usr/share/lensfun裏面觀察一下鏡頭修正檔，slr-panasonic的部份只有部份機種，而且沒有任何修正參數，有些描述甚至不是很正確，深入研究後發現其實這個Library是可以線上update的，而我的作法是去Sourceforge加入Rawstudio最新的PPA，將Rawstudio更新到最新，然後利用裏面更新Lensfun的功能就可以將鏡頭修正參數下載了，目前lensfun只有紀錄20mm,14-42mm跟45-200mm，而我有的鏡頭是20mm跟14-45mm，而其中14-42mm並沒有包含色散差的修正參數，就我以前比較過14-45mm跟14-42mm的各項表現也知道兩者的變形跟色散差可能不同，所以14-45mm的參數部份可能得找時間用方格紙跟日光燈自己try了。

Linux下支援Raw檔的編輯軟體其實不少，例如ufraw, Rawstudio跟RawTherapee，其中只有Rawstudio有PPA，其他兩者的最新版都要用Source去編譯，其實編譯的方法並不難，只要在configure時觀察看看少了哪些標頭檔，再去apt-get安裝對應的Library(選有dev的字樣的)就行了，有機會再詳述吧~總之ufraw在configure時要將lensfun的選項開啟，不然預設是關閉的，而RawTherapee似乎不支援lensfun，所以暫時忽略，目前就是ufraw跟Rawstudio交替使用，兩者在處理raw檔都還蠻佔資源的，不像處理jpeg那樣即時，其中ufraw對於細部的調整參數最詳細，可以切換的algorithm也最多，而Rawstudio就有點簡單些，不過基本的gamma曲線跟denoise還是有，兩者都支援Lens correction，其實他們的操作都跟Windows下的Camara Raw或是Lightroom差不多，而Rawstudio的批次處理功能比較完整，同時也可以上傳到Picasa，所以算是目前的主力~上面那些照片就是用Rawstudio完成的~雖然可調參數稍微少些，但其實就算參數多如Lightroom，也大多是對應到Gamma曲線，所以其實只要會調Gamma曲線就夠了，同時，Rawstudio也支援Copy/Paste Setting，雖然處理每個檔要花的時間不少，但通常處理完第一個檔案，就可以把Setting copy到剩下的圖檔，再微調即可，反而省下更多的時間。

.. figure:: http://rawstudio.org/screenshots/RS2-copy_settings.png
   :align: center
   :target: http://rawstudio.org/screenshots/RS2-copy_settings.png

(截至RawStudio網站)

從這裡也可以證實我長久以來的疑慮，就是Panasonic的發色問題根本就出在白平衡上，利用Raw檔就可以跳過這個問題，即使是GF1在白熱燈泡下白平衡也不儘正確，雖然說都可以用一張白紙來自訂白平衡，終究還是多一道手續，所以想想不如還是放棄使用機身本身的矯正白平衡功能，專心拍照比較重要，其他的就留給後製吧!新機種G3已經發表了，有不少人在爭論jpeg色調的問題，我想一切都是幻覺..改用Raw吧!

這幾天的嘗試，除了發現GH2真的能力之外，也終於正式解決Linux下編輯GH2所有檔案的問題，以後照片就交給Rawstudio跟ufraw，而影片就是Kdenlive，播放則是smplayer+vdpau(GPU解碼)，真是快樂無比，誰說Linux下無法處理相片跟影片呢?沒有Photoshop,lightroom,威力導演,Primere..我們還有一票自由又好用的東西可以取代呢~

PS.我用來處理GH2的電腦是採用KDE(強烈建議)，一般工作則是用Gnome

\ `Lensfun`_\

\ `RawStudio PPA`_\



還有\ `ufraw`_\ 主站，比較特別是他有將raw histogram秀出來，也就是相機本身未經過Gamma轉換過的histogram，同時還有把各個Channel(RGB)的Gamma曲線一併秀出來，所以要做最細部微調時可以採用這個軟體，同時他所提供的lens correction選項也最多，光是演算法的部份就可以選用數種，只是他的批次功能必須在CLI下才能執行，沒有比RawStudio方便，不過除噪效果一級棒，ISO1600以上可能就要動用到他來除噪了。不知道能不能讓他們的曲線設定共用..找一天研究看看。

截幾張RawStudio的圖來:

.. image:: http://rawstudio.org/screenshots/RS2-loupe.png
   :align: center
   :target: http://rawstudio.org/screenshots/RS2-loupe.png

還可以upload到Facebook,flickr:

.. image:: http://rawstudio.org/screenshots/RS2-flickr.png
   :align: center
   :target: http://rawstudio.org/screenshots/RS2-flickr.png

跟Picasa:

.. image:: http://rawstudio.org/screenshots/RS2-picasa.png
   :align: center
   :target: http://rawstudio.org/screenshots/RS2-picasa.png


其他截圖請參考\ `RawStudio Screenshot`_\

.. _Lensfun: http://lensfun.berlios.de/manual/

.. _RawStudio PPA: https://launchpad.net/~rawstudio/+archive/ppa

.. _RawStudio Screenshot: http://rawstudio.org/screenshots.php

.. _ufraw: http://ufraw.sourceforge.net/Guide.html

.. ===================================文章結束↑/語法備忘錄↓====================================
.. ● 格式1 ― 粗體(**字串**)  斜體(*字串*)  大字(\ :big:`字串`\ )  小字(\ :small:`字串`\ )
.. ● 格式2 ― 上標(\ :sup:`字串`\ )  下標(\ :sub:`字串`\ )  ``去除格式字串``
.. ● 項目 ― #. (換行) #.　或是a. (換行) #. 或是I(i). 換行 #.  或是*. -. +. 子項目前面要多空一格
.. ● 插入teaser分頁 ― .. TEASER_END
.. ● 插入latex數學 ― 段落裡加入\ :math:`latex數學`\ 語法，或獨立行.. math:: (換行) Latex數學
.. ● 插入figure ― .. figure:: 路徑(換行):width: 320(換行):align: center(換行):target: 路徑
.. ● 插入slides ― .. slides:: (空一行) 圖擋路徑1 (換行) 圖擋路徑2 ... (空一行)
.. ● 插入youtube ― ..youtube:: 影片的hash string
.. ● 插入url ― 段落裡加入\ `連結字串`_\  URL區加上對應的.. _連結字串: 網址 (儘量用這個)
.. ● 插入直接url ― \ `連結字串` <網址或路徑>`_ \    (包含< >)
.. ● 插入footnote ― 段落裡加入\ [#]_\ 註腳    註腳區加上對應順序排列.. [#] 註腳內容
.. ● 插入citation ― 段落裡加入\ [引用字串]_\ 名字字串  引用區加上.. [引用字串] 引用內容
.. ● 插入sidebar ― ..sidebar:: (空一行) 內容
.. ● 插入contents ― ..contents:: (換行) :depth: 目錄深入第幾層
.. ● 插入原始文字區塊 ― 在段落尾端使用:: (空一行) 內容 (空一行)
.. ● 插入本機的程式碼 ― ..listing:: 放在listings目錄裡的程式碼檔名 (讓原始碼跟隨網站) 
.. ● 插入特定原始碼 ― ..code::python (或cpp) (換行) :number-lines: (把程式碼行數列出)
.. ● 插入gist ― ..gist:: gist編號 (要先到github的gist裡貼上程式代碼) 
.. ============================================================================================
