.. title: 顯示色彩的奧秘 v0.2
.. slug: colorspace
.. date: 20140405 00:40:01
.. tags: 學習與閱讀
.. link: 
.. description: Created at 20140404 21:46:01
.. ===================================Metadata↑================================================
.. 記得加tags: 人生省思,流浪動物,生活日記,學習與閱讀,英文,mathjax,自由的程式人生,書寫人生,理財
.. 記得加slug(無副檔名)，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>



.. figure:: ../../../arch_2013/files_2013/M43/colorspace/01_cal_results1.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/01_cal_results1.png
   :align: center

   螢幕校色的最終成果:白點(white point)色溫接近6500K，亮度接近120\ :math: `cd/m^2`\ ，愈接近sRGB標準，而對比愈高，細節的呈現愈好。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/02_cal_results2.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/02_cal_results2.png
   :align: center

   螢幕校色的另一個重要項目，標準色差(color difference)，或是\ :math: `\Delta E`\ 愈小愈好，代表色彩愈準確。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/03_cal_results3.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/03_cal_results3.png
   :align: center

   一般人比較少注意到的，灰階的色偏(RGB gray balance)也是很重要的，對於背光源的LCD影響比較顯著。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/04_cal_results4.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/04_cal_results4.png
   :align: center

   真正的校色，需要耗費大量的時間對於各種顏色進行校正。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/05_Benq_cal_curve.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/05_Benq_cal_curve.png
   :align: center

   一個好的螢幕在校色後，必須要儘量降低損失的色階，以此圖為例，8 bit色階在校色後，每個通道約損失了12個色階，這已經是非常好的結果。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/05_Tone_response_curve.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/05_Tone_response_curve.png
   :align: center

   校色軟體通常會一併顯示當前螢幕的色調響應曲線(tone response curves)，從這裡可以看出所有LCD螢幕的通病，也就是暗部(接近橫軸0處)有些微凸起，表示暗部並不是真的全黑，而是有些微亮度，這也是LCD螢幕的對比不佳的主要原因。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/06_Gamut.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/06_Gamut.png
   :align: center

   另外一個就是顯示器涵蓋的色域範圍，然而並不是涵蓋率愈大，顏色就愈準，也有100%涵蓋，但校色完後色階嚴重喪失，標準色差降低不下來的例子，圖中為sRGB的色域。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/07_Good_uncalibrated.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/07_Good_uncalibrated.png
   :align: center

   一個適合校色的螢幕，必須俱備幾個基本條件:白點色溫接近6500K，亮度可以調整到接近120\ :math: `cd/m^2`\ ，以及Gamma必須接近2.2，最後則是\ :math: `\Delta E`\ 愈小愈好。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/08_Lum_table.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/08_Lum_table.png
   :align: center

   測試網站提供的亮度設定與真實亮度的參數表，由於許多螢幕的預設值都遠超過120\ :math: `cd/m^2`\ ，利用這個表可以了解到這個螢幕是否有能力調整到想要的亮度值。(圖表來自tftcentral網站)


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/09_Gamma_setting_table.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/09_Gamma_setting_table.png
   :align: center

   螢幕的Gamma設定更是非常重要的參考依據，可以知道這個螢幕在mode 2是最接近Gamma 2.2的，如果不管怎麼調都沒辦法接近2.2，代表這個螢幕校色後色階將會損失嚴重。(表來自tftcentral)


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/10_Temp_table.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/10_Temp_table.png
   :align: center

   白點色溫則是另外一個重點，也牽涉到色階能保留到何種程度，從這邊可知Normal已經很接近6500K了，若使用Custom模式則可以更為接近。(表來自tftcentral)


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/11_PWM.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/11_PWM.png
   :align: center

   由於螢幕的預設亮度都超高，降低亮度時，很容易產生閃爍的現象，這是因為LCD的亮度是由背光源一閃一滅的頻率來達到降低亮度的效果，頻率愈低，人眼的視覺暫留會感覺到亮度變低，也因為這樣，低亮度下比較容易因閃爍而造成眼睛的不適，LED背光的閃爍現象經常比CCFL(陰極管)還明顯，因此這也是要考慮的重點之一。(圖來自tftcentral)


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/12_Bad_delta_E.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/12_Bad_delta_E.png
   :align: center

   這邊舉一個不適合用來校色的例子，從圖中可以看到預設的色溫十分偏離6500K，Gamma來到2.3，而\ :math: `\Delta E`\ 則很高，但是這個螢幕其實是高價位的廣色域螢幕，這代表不是螢幕愈貴，色域愈廣就愈好，有時反而會弄巧成拙。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/13_Bad_temp.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/13_Bad_temp.png
   :align: center

   這張圖看似比上一張圖好多了，但是關鍵的白點色溫，會讓校色完的色溫大大的喪失，因此一個好的螢幕其實各方面都必須要滿足，不能只看某幾項。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/14_Dell_cal_curve.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/14_Dell_cal_curve.png
   :align: center

   這個是上面的螢幕校色後的結果，可以看到色階損失了26階，這就是白點色溫不準確的問題所在。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/15_eizo_cal_curve.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/15_eizo_cal_curve.png
   :align: center

   這是另外一個螢幕的校正曲線，喪失的色階約19左右，這個螢幕和上一張都是來自於高階與高價的螢幕，反而是我們前面提到的幾個良好的校正結果，都是來自於某款平價的螢幕，這說明了價位與顏色準不準其實是兩回事，透過測試網站判斷螢幕是否適合校色才是最準確與科學的方法。


.. figure:: ../../../arch_2013/files_2013/M43/colorspace/16_Reading_mode.png
   :target: ../../../arch_2013/files_2013/M43/colorspace/16_Reading_mode.png
   :align: center




.. figure:: ../../../arch_2013/files_2013/M43/colorspace/17_colorspace1.jpg
   :target: ../../../arch_2013/files_2013/M43/colorspace/17_colorspace1.jpg
   :align: center




.. figure:: ../../../arch_2013/files_2013/M43/colorspace/18_colorspace2.jpg
   :target: ../../../arch_2013/files_2013/M43/colorspace/18_colorspace2.jpg
   :align: center






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
