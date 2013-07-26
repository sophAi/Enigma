.. title: GX1與GH2破解設定資訊
.. slug: ptool_settings
.. date: 20130727 00:26:08
.. tags: 學習與閱讀
.. link: 
.. description: Created at 20130726 16:18:09
.. ===================================Metadata↑================================================
.. 記得加tags: 人生省思,流浪動物,生活日記,學習與閱讀,英文,mathjax,自由的程式人生,書寫人生,理財
.. 記得加slug(無副檔名)，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

由於破解軔體的步驟大同小異，我將其獨立於\ `Ptool更新軔體程序`_\ 一文，本文則不定時分享最新的破解參數設定，搭配Ptool則可進行錄影畫質的修改。


DREWnet T9 (Trial 9) by Driftwood - 2013/07/26更新
-----------------------------------------------------------

環境: GX1+Sandisk 45MB/s USH-I與GH2+Toshiba Class 10 23MB/s 白卡

我使用Ptool論壇\ `driftwood`_\ 所調整的\ `DREWnet T8`_\ 錄影參數已經很久了，driftwood近期的設定檔算是Ptool論壇成立以來集大成之作，其畫質與檔案容量取得很好的平衡，同時long GOP的特性使得長時間錄影的穩定性高，而前幾天才釋出的\ `DREWnet T9`_\ 參數檔，使用了新的scaling matrix，對我來說是一大消息，也讓這篇Ptool的資訊分享延期。錄影畫質的破解，需要流量(bit rate, 8 bit=1 Byte)，Quantization Matrix，以及GOP互相配合，三者息息相關，與靜態照片不同的是影片檔經常是在1:1的情況下觀看的，因為當今主流螢幕所提供的解析度(大於或等於1920x1080)，就是為了能完整播放FullHD的影片，因此畫質的差別很容易以肉眼分辨，要達到良好的畫質，並不是無限上網地增加流量，而是在檔案大小與畫質間取得平衡，選擇DREWnet最重要的原因是其針對Scaling matrix做了許多調整，將流量平均分配給I/P/B frame，而非僅僅拉抬流量(通常也要設定auto quantizer)。流量過高往往也會降低錄影的穩定性，太複雜的場景容易使錄影中斷，因此在流量不過度暴增的前提下提升畫面的細節才是最聰明的辦法，在driftwood的描述裡，DREWnet T9具有以下特性:

#. 80Mbps constant in 24p modes for exceptional quality.

#. 1080i/FSH Maybe only around 40Mbps but the quantisation and PSNR is brilliant!

#. 720p modes Just the best there is. (事實上1080i/FSH(同時也是GH2的HBR以及GX1的FSH)所採用的scaling matrices跟720p是相同的)。

由於平常我是GH2與GX1混合拍攝，為了將混合格式轉檔(pull down)所需的成本降到最低，大多偏向採用1080p30(FSH)的錄影格式，使用DREWnet讓1080p30的錄影檔平均增加了約1.7倍的容量，對於生活錄影來說已經是很可觀的增長。24p無疑畫質更佳，但是所需的記憶卡空間也更多，如果各位拍攝影片的頻率非常高，例如紀錄小孩的成長，出外旅遊，同時還要兼顧靜態照片所需的額外容量，則FSH模式已經是綽綽有餘。不管是靜態還是動態攝影，「剛剛好」是很重要的原則。

.. TEASER_END

為了讓各位對於錄影畫質的提升有點概念，以下我們以GX1的MTS檔1:1截圖來檢視之，使用FSH(1080p30)模式錄影。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_01.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_01.png
   :align: center

   GX1的MTS檔。通常在充滿細節的畫面，最容易出現塊狀瑕疵，不過1:1檢視下，無論是椅子上的網點，還是布偶的毛料，DREWnet T9幾乎觀察不到色塊的存在。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_02.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_02.png
   :align: center

　 偽色或英文所稱的color bending，最常出現在色階不連續的地方，其產生的不自然色彩，其實是macroblock所造成的，破解後的GX1，即使是低光下，皮膚的色階表現也很不錯。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_03.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_03.png
   :align: center

   除了皮膚的色階表現良好，直線也不容易產生鋸齒，即使是動態場景(B/P frame)，表現也超乎想像的好。

接著我們來檢視GX1原廠的MP4錄影，場景相同，流量為20Mbps。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_01.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_01.png
   :align: center

   雖然GX1的MP4出廠值流量比AVCHD高(20Mbps比17Mbps)，很明顯全螢幕播放塊狀瑕疵一覽無遺。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_02.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_02.png
   :align: center

   椅子的網格幾乎是糊成一團，對比DREWnet幾乎是完整呈現的紋理，差距實在是太大了。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_03.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_03.png
   :align: center

   毛料也糊成一團，直線也出現鋸齒，Ptool對於MP4的破解並不完全，會造成機身無法正常播放，同時考量到記憶卡空間不夠時，也需要一個小巧的錄影格式，因此MP4的參數完全沒有更動，正常情況下使用MTS就足夠了。

下面是上傳到youtube後全螢幕的截圖，當時還是使用DREWnet T8。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/29_youtube.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/29_youtube.png
   :align: center

   上傳到Youtube後，影片會被轉成MP4格式，原始檔案保留的細節愈多，愈可以減輕畫質劣化的情況。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/30_GX1_MTS.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/30_GX1_MTS.png
   :align: center

   這是原始的影片截圖，幾乎跟直接將靜態照片縮圖到FullHD大小的品質一樣!色階平順漂亮，細節保留完整。


我還沒有時間好好觀察24p還有破解前後AVCHD畫質的差異，總括來說，只要Quantization的瑕疵不易被發覺，就達到破解的目了。真的要探究的話，下面列出driftwood量化的測試，其用一個灰階圖格來反映Quantization後的成像，顏色愈淡，表示影像品質愈好。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/23_GH2_stock_24p.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/23_GH2_stock_24p.png
   :align: center

   此圖為GH2原廠的24p模式，在driftwood的測試裡排名第3。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/24_GH3_24p.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/24_GH3_24p.png
   :align: center

   排名第2的則是GH3原廠24p模式(非All-I)。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/25_GH2_ClusterX.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/25_GH2_ClusterX.png
   :align: center

   排名第1的是DREWnet與GH2，換句話說，已經超過了GH3非All-I模式所能達到的程度。

當然，無論是使用DREWnet的GH2或是GH3，他們的硬體能力都還沒有被徹底發揮，例如driftwood的moon T7(ALL-I)可以說是跟GH3的All-I同性質的設定，採用的流量甚至遠遠超越GH3，Spizz與Nebula都是low GOP的設定，理論上畫質都比DREWnet還更上乘，有興趣的人可以嘗試看看，將來GH3能夠破解了，應該也能得到同等的品質，只是回到現實面，以及基於檔案容量與穩定性的考量，在生活紀錄這方面，DREWnet是我認為最平衡且最實用的參數設定，最大80Mbps的流量(約10MB/s)幾乎適用於所有class 10的SD卡，市面上大概只有破解的GH2，All-I模式下的GH3，還有高價位的專業錄影設備可以得到比DREWnet更佳的錄影畫質了。這也說明軟體的因素，在數位攝影裡經常是遠大於硬體的差別，同樣的觀念在\ `探討網路照片的奧秘`_\ 一文中也清楚地揭示。

使用了兩天還沒發生任何問題，如果發生無法立即預覽影片的現象，只要重新開機就可以順利播放了，對影片檔本身是沒有影響的，有關T9的一些細節，Ptool論壇有很熱鬧的討論，有進一步的資訊再分享給各位囉！最後，錄影不是只有畫質的追求，還有拍攝手法，故事性，分鏡，以及畫面穩定度等，因此畫質「足夠」之餘，其他方面也是要努力兼顧喔!


PS. 破解軔體前請確實閱讀Ptool軔體破解程序的需知，因為電源中斷導致機身變磚是不在保固內，請自行承擔風險喔~

.. </body>
.. <url>

.. _Ptool更新軔體程序: ptool.html

.. _driftwood: http://www.personal-view.com/talks/discussion/7580/driftwood-cluster-x-series-3moon-t7Ѕrіzz-t6nebula-t7drewnet-t9/p1

.. _DREWnet T8: ../../../arch_2013/files_2013/M43/ptool_settings/seta.ini

.. _DREWnet T9: ../../../arch_2013/files_2013/M43/ptool_settings/setc.ini

.. _探討網路照片的奧秘: sharpen.html

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
