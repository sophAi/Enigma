.. title: 縮圖下銳利度的差別？
.. slug: resize 
.. date: 20130710 10:29:53
.. tags: draft,學習與閱讀
.. link: 
.. description: Created at 20130709 21:33:52
.. ===================================Metadata↑================================================
.. 記得加tags: 人生省思,流浪動物,生活日記,學習與閱讀,英文,mathjax,自由的程式人生,書寫人生,理財
.. 記得加slug(無副檔名)，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

承蒙Mobile01網友Happyspirit的協助，我得以取得三台相機的測試照片，其中一台，是使用著名的FoveonX3感光元件的Sigma DP2 Merrill(DP2M)，另外一台則是Panasonic GH2，最後則是智慧型手機HTC New One，之所以會把這三台完全無法搭在一起的相機放在一起，主要是想要釐清一個問題―縮圖下銳利度的差距能降低到多少呢?

以影像的精細度來說，在Foveon X3感光元件的加持下，DP2M無疑具有最大的優勢(3:2, 4704x3136)，而GH2則屬於可換鏡頭相機中解析度中下的(測試照為16:9, 4976x2800)，至於HTC New One的拍攝結果(16:9, 2688x1520)，則應該貼近大多數的智慧型手機，如果說，以DP2M為一個目標，透過縮圖與銳化的處理，而能達到接近的銳利感，

由於這三台照相機的解析度，與鏡頭的焦距，最大開放光圈都不同，因此比較起來會稍微麻煩點，同時要如何比較更是一大問號，這裡我們儘量把變因降到最低，只裁切中央最清晰的部份，並試著將三張照片的白平衡調整至一致，然後同時縮圖到長寬最大800px，這樣的步驟，其實跟把照片縮小，然後再分享到網路上相同，我們先來看看原圖直接縮圖到800px的結果，這裡我們使用等同於flickr相簿的一般銳化縮圖參數::

-unsharp 1x0.55+1.5+0.002

.. figure:: ../galleries/800/800_01_DP2M.jpg
   :target: ../galleries/800/800_01_DP2M.jpg
   :align: center

   DP2M 原圖，一般銳化


.. figure:: ../galleries/800/800_02_GH2_20mm.jpg
   :target: ../galleries/800/800_02_GH2_20mm.jpg
   :align: center

   GH2 原圖，一般銳化


.. figure:: ../galleries/800/800_03_new_one.jpg
   :target: ../galleries/800/800_03_new_one.jpg
   :align: center

   New One 原圖，一般銳化


接著裁切中央最清晰的部位，儘量消除視角的差距，同樣使用相同的一般銳化參數。

.. figure:: ../galleries/800/800_04_DP2M_crop.jpg
   :target: ../galleries/800/800_04_DP2M_crop.jpg
   :align: center

   DP2M 中央裁切，一般銳化


.. figure:: ../galleries/800/800_05_GH2_20mm_crop.jpg
   :target: ../galleries/800/800_05_GH2_20mm_crop.jpg
   :align: center

   GH2 中央裁切，一般銳化


.. figure:: ../galleries/800/800_06_new_one_crop.jpg
   :target: ../galleries/800/800_06_new_one_crop.jpg
   :align: center

   New One 中央裁切，一般銳化

我們會發現，在縮圖至800px的情況下，三者的差距其實不明顯，尤其是布料的質感。


.. .. figure:: ../galleries/800/800_07_DP2M_bw.jpg
..    :target: ../galleries/800/800_07_DP2M_bw.jpg
..    :align: center




.. .. figure:: ../galleries/800/800_08_GH2_20mm_bw.jpg
..    :target: ../galleries/800/800_08_GH2_20mm_bw.jpg
..    :align: center




.. .. figure:: ../galleries/800/800_09_new_one_bw.jpg
..    :target: ../galleries/800/800_09_new_one_bw.jpg
..    :align: center



.. .. figure:: ../galleries/800/800_07_DP2M_bw.jpg
..    :target: ../galleries/800/800_07_DP2M_bw.jpg
..    :align: center

..    DP2M org

.. .. figure:: ../galleries/800/800_08_GH2_20mm_bw_sharpen.jpg
..    :target: ../galleries/800/800_08_GH2_20mm_bw_sharpen.jpg
..    :align: center

..    GH2 sharpen

.. .. figure:: ../galleries/800/800_09_new_one_bw_sharpen.jpg
..    :target: ../galleries/800/800_09_new_one_bw_sharpen.jpg
..    :align: center

..    New One sharpen

以上的圖檔均使用一般銳化參數(flickr參數)::

-unsharp 1x0.55+1.5+0.002

.. figure:: ../galleries/800/800_04_DP2M_crop.jpg
   :target: ../galleries/800/800_04_DP2M_crop.jpg
   :align: center

   DP2M 中央裁切，一般銳化

.. figure:: ../galleries/800/800_05_GH2_20mm_crop_sharpen.jpg
   :target: ../galleries/800/800_05_GH2_20mm_crop_sharpen.jpg
   :align: center

   GH2 中央裁切，加強銳化

使用參數::

-unsharp 1x0.7+1.5+0.002

.. figure:: ../galleries/800/800_06_new_one_crop_sharpen.jpg
   :target: ../galleries/800/800_06_new_one_crop_sharpen.jpg
   :align: center

   New One 中央裁切，加強銳化

使用參數::

-unsharp 1x0.7+1.5+0.002


最後將一般銳化跟加強銳化放在一起比較:

.. figure:: ../galleries/800/800_05_GH2_20mm_crop.jpg
   :target: ../galleries/800/800_05_GH2_20mm_crop.jpg
   :align: center

   GH2 中央裁切，一般銳化

.. figure:: ../galleries/800/800_05_GH2_20mm_crop_sharpen.jpg
   :target: ../galleries/800/800_05_GH2_20mm_crop_sharpen.jpg
   :align: center

   GH2 中央裁切，加強銳化

.. figure:: ../galleries/800/800_06_new_one_crop.jpg
   :target: ../galleries/800/800_06_new_one_crop.jpg
   :align: center

   New One 中央裁切，一般銳化

.. figure:: ../galleries/800/800_06_new_one_crop_sharpen.jpg
   :target: ../galleries/800/800_06_new_one_crop_sharpen.jpg
   :align: center

   New One 中央裁切，加強銳化

最後看看銳化後的GH2與New One:


.. figure:: ../galleries/800/800_01_DP2M.jpg
   :target: ../galleries/800/800_01_DP2M.jpg
   :align: center

   DP2M 原圖，一般銳化


.. figure:: ../galleries/800/800_02_GH2_20mm_sharpen.jpg
   :target: ../galleries/800/800_02_GH2_20mm_sharpen.jpg
   :align: center

   GH2 原圖，加強銳化


.. figure:: ../galleries/800/800_03_new_one_sharpen.jpg
   :target: ../galleries/800/800_03_new_one_sharpen.jpg
   :align: center

   New One 原圖，加強銳化


以影像的精細度來說，在Foveon X3感光元件的加持下，DP2M無疑具有最大的優勢(3:2, 4704x3136)，而GH2則屬於可換鏡頭相機中解析度中下的(測試照為16:9, 4976x2800)，至於HTC New One的拍攝結果(16:9, 2688x1520)，則應該貼近大多數的智慧型手機，如果說，以DP2M為一個目標，透過縮圖與銳化的處理，而能達到接近的銳利感，

有趣的是DP2M的解析度其實與GH2很接近(如果GH2採用3:2則解析度為4768x3184)，理論上兩者能提供的影像細節是很相當的，差別可能在DP2M在處理紋理上，由於沒有低通濾鏡，理論上會比較有優勢


.. figure:: ../galleries/800/DP2M_zoom.jpg
   :target: ../galleries/800/DP2M_zoom.jpg
   :align: center

   DP2M 原圖，1:1裁切


.. figure:: ../galleries/800/GH2_zoom.jpg
   :target: ../galleries/800/GH2_zoom.jpg
   :align: center

   GH2 原圖，1:1裁切


.. figure:: ../galleries/800/New_One_zoom.jpg
   :target: ../galleries/800/New_One_zoom.jpg
   :align: center

   New One 原圖，1:1裁切

如果以「手機照可以越級挑戰高階相機」這個結論來看，其實還言之過早，我們也可以觀察到，在色階的呈現上，手機損失的部位較多，因此以編輯照片的寬容度來說，仍是較高階的相機較有彈性，但總體來說，一張照片的畫質，其實感光元件只能提供20%的助力，光是縮圖這部份，就會產生極大的不確定性喔!

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
