.. title: 校色的奧秘
.. slug: dispcalGUI_screen
.. date: 20140825 13:44:43
.. tags: 學習與閱讀
.. link: 
.. description: Created at 20140824 14:38:28
.. ===================================Metadata↑================================================
.. 記得加tags: 人生省思,流浪動物,生活日記,學習與閱讀,英文,mathjax,自由的程式人生,書寫人生,理財
.. 記得加slug(無副檔名)，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

我們在之前的「顯示色彩的奧秘」一節中提到，一個完整的影像色彩修正必須要有3個要
素:

#. 適合校色的螢幕
#. 生成正確的色彩定義檔(ICC profile)
#. 支援ICC profile的軟體或作業系統

.. TEASER_END

一個完整且正確的校色三者是缺一不可，環環相扣，舉個例子來說，一個高檔的螢幕卻缺乏正確的校色，或是生成了校色檔卻沒有適當的軟體支援，都會產生色彩失真的風險，在了解了螢幕的選擇對於校色的影響之後，本節將著重在軟體的部份，也就是ICC profile的生成步驟，而我們這裡採用的，其實是許多專業人士一致推薦的dispcalGUI，由於他支援的校色器非常廣泛，所提供的校色選項非常豐富且面面俱到，功能與叫色的精準度甚至讓許多官方校色軟體汗顏。光是採用的測試色塊數目就遠超過許多官方的校色軟體，還能生成非常詳細的校色報告，因此很多人反而棄原廠軟體不用而採用它，而他最大的好處就是資源非常豐富，還是跨平台的自由軟體，Windows/Linux/OSX都可以使用，甚至還能夠對手機或平板裝置進行校色。

由於dispcalGUI改版非常迅速，有關其安裝的方法請參考官方首頁，最重要的步驟是安裝argyll這個軟體，他既提供校色器的硬體支援，也是所有校色功能的核心提供者，dispcalGUI則是一個前端的介面，以Linux系統來說，只要下載他的deb或rpm檔即可安裝，同時以套件管理程式安裝argyll即可，非常方面，以ubuntu/Linux Mint來說，只要在終端機裡輸入:

apt-get install argyll

dpkg -i dispcalGUI的deb檔

即可。

dispcalGUI的畫面可以驅分成三大部份:

#. Display device
#. Calibration settings
#. Profiling settings

這三者構成了校色的3個主要的步驟，其中比較需要解釋的是Calibration與Profiling settings之間的差別，Calibration主要是著重在螢幕硬體的設定，例如螢幕的色溫，亮度設定等，這部份需要透過操作螢幕的按鈕來進行調整，如果沒有確實做好這部份，最後的校色結果可能會造成嚴重的掉階，喪失動態。

而Profiling則是生成ICC profile的設定，這個部份會決定測試色塊的數目，ICC profile的精確度等，因此實際校色的過程，其實就是先校正(calibrating)螢幕，再測試色塊生成ICC profile(profiling)

dispcalGUI的選項眾多，以下我們一一介紹

.. figure:: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_01_dispcalGUI_device.png
   :target: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_01_dispcalGUI_device.png
   :align: center

**Settings**: 也就是當前的校色設定，最右邊的按鈕可以顯示當前Profile的資訊、校正曲線、螢幕的特性、與色域空間涵蓋率等

**Update calibration**: 決定是否要覆蓋當前的Profile，還是要重新生成新的Profile

**Display device**: 顯示螢幕的型號

**Instrument**: 顯示校色器的型號，Mode則是設定校色器的校色方式，例如這邊使用LCD (generic) Adaptive HiRes是比較建議採用的選項，可以提供比較精確的校色結果。

**White level drift compensation**: 有些螢幕的白色亮度(white level)會不斷浮動，理論上比較好的螢幕亮度應該是不會隨時間有些微改變的，因此打勾這個選項會對這個問題進行修正，在色塊校正的過程會不時穿插白色的色塊，讓校色器不斷對白色做校正，得到更精確的結果，缺點是校色的時間會大幅拉長，除非螢幕的亮度真的有問題，不然其實可以不需要勾選這個選項。

**Black level drift compensation**: 功能同上，只是針對黑色的亮度，也就是如果螢幕有漏光的問題，有可能會讓黑色的亮度浮動，同樣在測試色塊的過程中會穿插大量的黑色色塊，基本上勾選該選項能提供更準確的結果，但是也會讓校色時間拉長。

接著是螢幕校正(Calibration Settings)的區塊，這個部份會設定螢幕調整的目標值，也就是說，如果我們想要螢幕符合sRGB的標準，則必須在這邊設定，dispcalGUI會根據這邊的設定提示我們如何操作螢幕的按鈕來達到這個標準，同時也會決定ICC profile裡R/G/B Gamma的修正曲線。

.. figure:: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_02_dispcalGUI_calibration.png
   :target: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_02_dispcalGUI_calibration.png
   :align: center

**Whitepoint**: 決定白點的色溫，這個選項會決定R/G/B Gamma曲線所呈現的色溫，以sRGB來說選擇Color temperature 6500K, Daylight即可，只有在很特殊的情況下(例如環境光源的色溫差異太大，例如有個螢幕旁邊有個紅色的光源之類的，才需要用到Measure對環境光源進行修正，不過若遇到這種情況下，改善環境光源才是優先要考慮的事項。

**White level**: 決定螢幕的亮度，以sRGB來說約120cd/m^2，如果您是先已經對螢幕做校正，調整螢幕的亮度讓他接近120cd/m^2，這個選項可以使用As measure，如此一來可以多保留些色階，畢竟要剛剛好落在120cd/m^2也是不太可能的事。

**Black level**: 大部分的LCD螢幕黑色的亮度都不等於0，除非黑色的亮度太過於明顯，甚至影響到灰階的表現，不然建議使用As measure，強制設定成0可能會造成色階喪失不連續等問題。

**Tone curve**: 決定Gamma值，sRGB的Gamma為2.2，除非螢幕偏離2.2許多，不然選擇sRGB即可，這個選項也會影響色階能保留的數目，因此可以多方嘗試。

**Black output offset**: 透過R/G/B Gamma曲線來修正黑色亮度不等於0的問題，建議100%即可


.. figure:: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_03_dispcalGUI_profile.png
   :target: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_03_dispcalGUI_profile.png
   :align: center




.. figure:: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_04_dispcalGUI_exec.png
   :target: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_04_dispcalGUI_exec.png
   :align: center




.. figure:: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_05_dispcalGUI_cal_window.png
   :target: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_05_dispcalGUI_cal_window.png
   :align: center




.. figure:: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_06_discalGUI_display_cal.png
   :target: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_06_discalGUI_display_cal.png
   :align: center




.. figure:: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_07_discalGUI_display_cal2.png
   :target: ../../../arch_2014/files_2014/M43/dispcalGUI_screen/800/800_07_discalGUI_display_cal2.png
   :align: center


截至目前為止，我們終於生成了ICC profile，但是故事還沒結束，最重要的部份，也就是軟體支援的部份才是重點，我們必須知道，ICC profile決定了兩個重要的步驟，一個是R/G/B Gamma曲線的修正，這個會決定顯示的色溫，暗部與亮部的表現，但這只是一半的步驟，另外一個則是矩陣轉換，也就是透過LUT(Look up table)將不準確的色彩修正成準確的色彩，一般通稱LUT Matrix的轉換，以Mac OS X來說，他的ColorSync是由作業系統底層掌管色彩管理，目的是讓所有程式都能在底層就完成完整的色彩管理的步驟，對於美術與影像處理人員來說無疑是首選的系統。

相對來說，Windows系統在色彩管理則以應用程式的支援為主，只有少數應用程式完整支援ICC Profile，例如Photoshop，色彩管理的部份必須由應用軟體的廠商來實現，大部分的程式其實是無法受惠於ICC profile的。

以Linux來進行影像處理是比較少見的情況，但其實他的色彩管理非常開放，有提供通用的函式庫供大家使用，以Gnome/Mate桌面系統來說，色彩管理是由liblcms來進行，因此許多軟體，例如基本的秀圖軟體eyeofgnome/eyeofmate都能完整支援ICC profile，其他諸如GIMP，Inkscape，Firefox，pdf軟體，Raw處理軟體都完整支援ICC profile，通常Linux系統載入ICC profile時只會進行Gamma修正，LUT Matrix的轉換則是交由應用程式去執行，幾乎可以說90%以上的影像處理場合都可以從ICC profile獲得好處，只要記得到應用程式的相關色彩管理設定裡選擇Use system color profile即可。



.. </body>
.. <url>



.. </url>
.. <footnote>



.. </footnote>
.. <citation>



.. </citation>
.. ===================================文章結束↑/語法備忘錄↓====================================
.. 格式1: 粗體(**字串**)  斜體(*字串*)  大字(\ :big:`字串`\ )  小字(\ :small:`字串`\ )
.. 格式2: 上標(\ :sup:`字串`\ )  下標(\ :sub:`字串`\ )  ``去除格式字串``
.. 項目: #. (換行) #.　或是a. (換行) #. 或是I(i). 換行 #.  或是*. -. +. 子項目前面要多空一格
.. 插入teaser分頁: .. TEASER_END
.. 插入latex數學: 段落裡加入\ :math:`latex數學`\ 語法，或獨立行.. math:: (換行) Latex數學
.. 插入figure: .. figure:: 路徑(換):width: 寬度(換):align: left(換):target: 路徑(空行對齊)圖標
.. 插入slides: .. slides:: (空一行) 圖擋路徑1 (換行) 圖擋路徑2 ... (空一行)
.. 插入youtube: ..youtube:: 影片的hash string
.. 插入url: 段落裡加入\ `連結字串`_\  URL區加上對應的.. _連結字串: 網址 (儘量用這個)
.. 插入直接url: \ `連結字串` <網址或路徑>`_ \    (包含< >)
.. 插入footnote: 段落裡加入\ [#]_\ 註腳    註腳區加上對應順序排列.. [#] 註腳內容
.. 插入citation: 段落裡加入\ [引用字串]_\ 名字字串  引用區加上.. [引用字串] 引用內容
.. 插入sidebar: ..sidebar:: (空一行) 內容
.. 插入contents: ..contents:: (換行) :depth: 目錄深入第幾層
.. 插入原始文字區塊: 在段落尾端使用:: (空一行) 內容 (空一行)
.. 插入本機的程式碼: ..listing:: 放在listings目錄裡的程式碼檔名 (讓原始碼跟隨網站) 
.. 插入特定原始碼: ..code::python (或cpp) (換行) :number-lines: (把程式碼行數列出)
.. 插入gist: ..gist:: gist編號 (要先到github的gist裡貼上程式代碼) 
.. ============================================================================================
