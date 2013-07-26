.. title: GX1與GH2破解設定資訊
.. slug: ptool_settings
.. date: 20130726 20:37:20
.. tags: 學習與閱讀
.. link: 
.. description: Created at 20130726 16:18:09
.. ===================================Metadata↑================================================
.. 記得加tags: 人生省思,流浪動物,生活日記,學習與閱讀,英文,mathjax,自由的程式人生,書寫人生,理財
.. 記得加slug(無副檔名)，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

DREWnet T9 by Driftwood - 2013/07/26更新

我使用Ptool論壇，driftwood所調整的\ `DREWnet T8`_\ 已經很久了，其畫質與檔案容量取得很好的平衡，同時long GOP的特性使得長時間錄影的穩定性高，而前幾天才釋出的\ `DREWnet T9`_\ 參數檔，使用了新的scaling matrix，第1時間就馬上更新來嘗試!基本上錄影畫質的破解，需要流量(bit rate)，Quantization Matrix，以及GOP互相配合，三者息息相關，與靜態照片更不同的是影片檔經常是在1:1的情況下觀看的，這是因為當今主流螢幕的解析度(大於等於1920x1080)，就是為了能完整播放FullHD的影片，因此錄影畫質的提升效果明顯，然而要達到良好的畫質，並不是無限上網地增加流量，而是在檔案大小與畫質間取得平衡，例如將DREWnet套用在GX1上時，平均錄影檔增加了約1.7倍容量，其實對於一般生活錄影來說已經是很可觀的增幅，而這還是平均流量在40Mbps的情形下。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_01.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_01.png
   :align: center

   通常在充滿細節的畫面，最容易出現塊狀瑕疵，不過1:1檢視下，無論是椅子上的網點，還是布偶的毛料，DREWnet T9幾乎看不到這個問題。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_02.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_02.png
   :align: center

　 偽色或英文所稱的bending，最常出現在色階原本應該連續的地方，所謂的斷階出現的不自然色彩，其實是macroblock所產生的，即使是低光下，皮膚的色階表現也很不錯。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_03.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_Drewnet_03.png
   :align: center

   除了皮膚的色階表現良好，直線也不容易察覺到鋸齒狀，即使是動態場景(B/P frame)，表現也超乎想像的好。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_01.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_01.png
   :align: center

   雖然GX1的MP4出廠值流量比AVCHD高(20Mbps比17Mbps)，很明顯的塊狀瑕疵一覽無遺。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_02.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_02.png
   :align: center

   椅子的網格幾乎是糊成一團。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_03.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/GX1_mp4_03.png
   :align: center

   毛料也糊成一團，直線也出現鋸齒，Ptool對於MP4的破解並不完全，會造成機身無法正常播放，因此MP4的參數保留出廠值，平常使用AVCHD就足夠了。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/29_youtube.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/29_youtube.png
   :align: center

   上傳到Youtube後，影片會被轉成MP4格式，原始檔案保留的細節愈多，愈可以減輕畫質劣化的情況。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/30_GX1_MTS.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/30_GX1_MTS.png
   :align: center

   這是原始的影片截圖，幾乎跟直接將靜態照片縮圖到FullHD大小的品質一樣!色階平順漂亮。


我還沒有時間好好觀察24p還有破解前後AVCHD畫質的差異，總括來說，只要Quantization的瑕疵不易被發覺，就是很棒的畫質了，這也是錄影破解主要的目的。如果真的要探究的話，下面列出driftwood量化的測試，其用一個灰階圖格來反映Quantization後的成像，顏色愈淡，表示影像品質愈好。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/23_GH2_stock_24p.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/23_GH2_stock_24p.png
   :align: center

   此圖為原廠GH2的24p模式，在driftwood的測試裡排名第3。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/24_GH3_24p.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/24_GH3_24p.png
   :align: center

   排名第2的則是GH3原廠24p模式(非All-I)。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/25_GH2_ClusterX.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/25_GH2_ClusterX.png
   :align: center

   結果是最好的就是DREWnet，也可以說，已經超過了GH3非All-I模式所能達到的等級。

當然，無論是使用DREWnet的GH2，或是GH3，他們的硬體能力都還沒有被徹底發揮，例如driftwood的moon T7(ALL-I)可以說是跟GH3的All-I模式打對臺，使用的流量遠遠超越GH3所使用的，Ｓpizz與Nebula都是low GOP的設定，理論上畫質都比DREWnet還更上乘，將來GH3也破解了，應該也能得到更好的品質，只是回到實用性的現實面，以及基於檔案容量與穩定性的考量，在生活與親子錄影這塊，DREWnet是我所認為最平衡且實用的參數設定，在不過度暴增的影片容量下，大概只有GH2跟All-I模式下的GH3可以得到比DREWnet更佳的錄影畫質了。

錄影當然不是只有畫質這方面，還有拍攝手法，故事性，分鏡，以及畫面穩定性等，因此除了畫質，其他方面也是要努力兼顧喔!


.. </body>
.. <url>


.. _DREWnet T8: ../../../arch_2013/files_2013/M43/ptool_settings/seta.ini

.. _DREWnet T9: ../../../arch_2013/files_2013/M43/ptool_settings/setc.ini

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
