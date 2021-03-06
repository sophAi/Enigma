.. title: 數位照片的奧秘 - Color banding(色階不連續)
.. slug: banding
.. date: 20131003 21:38:07
.. tags: 學習與閱讀, draft
.. link: 
.. description: Created at 20130930 20:30:40
.. ===================================Metadata↑================================================
.. 記得加tags: 人生省思,流浪動物,生活日記,學習與閱讀,英文,mathjax,自由的程式人生,書寫人生,理財
.. 記得加slug(無副檔名)，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

我們先來看看下面幾張圖，請注意左上部位天空的色階。


.. figure:: ../../../arch_2013/files_2013/M43/banding/800/800_P1390829.jpg
   :target: ../../../arch_2013/files_2013/M43/banding/800/800_P1390829.jpg
   :align: center

   Imagemagic縮圖至800px並銳化，上傳至github pages。


.. TEASER_END
   
.. figure:: https://farm3.staticflickr.com/2870/10018447765_821c487da9_c.jpg
   :target: https://farm3.staticflickr.com/2870/10018447765_821c487da9_c.jpg
   :width: 800px
   :align: center

   原圖上傳Flickr相簿，以800px呈現。

.. figure:: https://lh4.googleusercontent.com/-eNuSM9Av4YA/UkluUAk2s1I/AAAAAAABIYE/xDvrqmJ7Dt4/s800/P1390829.jpg" 
   :target: https://lh4.googleusercontent.com/-eNuSM9Av4YA/UkluUAk2s1I/AAAAAAABIYE/xDvrqmJ7Dt4/s800/P1390829.jpg" 
   :width: 800px
   :align: center

   原圖上傳到google+(picasa)相簿，以800px呈現。

.. figure:: ../../../arch_2013/files_2013/M43/banding/640/640_P1390829.jpg
   :target: ../../../arch_2013/files_2013/M43/banding/640/640_P1390829.jpg
   :align: center

   Imagemagic縮圖至640px並銳化，上傳至github pages。


.. figure:: https://farm3.staticflickr.com/2870/10018447765_821c487da9_z.jpg
   :target: https://farm3.staticflickr.com/2870/10018447765_821c487da9_z.jpg
   :width: 640px
   :align: center

   原圖上傳Flickr相簿，以800px呈現。

.. figure:: https://lh4.googleusercontent.com/-eNuSM9Av4YA/UkluUAk2s1I/AAAAAAABIYE/xDvrqmJ7Dt4/s640/P1390829.jpg
   :target: https://lh4.googleusercontent.com/-eNuSM9Av4YA/UkluUAk2s1I/AAAAAAABIYE/xDvrqmJ7Dt4/s640/P1390829.jpg
   :width: 640px
   :align: center

   原圖上傳到google+(picasa)相簿，以640px呈現。

從上面幾張圖清楚顯示所謂「色階不連續(color banding)」的現象，這個問題大多是在捨棄顏色資訊的過程中產生的(color reduction)，簡單來說，一張數位照片從按下快門開始，必須經過一連串捨棄色彩資訊的過程，例如36 bits 色彩深度(color dpeth)的Raw資訊，最後只有24 bits的色彩深度會塞進我們最終的成品(RGB)，即使這樣仍是很龐大的影像資訊，因此還要進一步以破壞性壓縮來降低檔案容量，例如色度採樣(Chroma subsampling)與量子化(Quantization)，兩者都會捨棄更多色彩的細節，這樣捨棄再捨棄的過程，造成幾乎無可避免的「色階不連續」呈現於大多數壓縮容量的影像裡。

上面的例子赤裸裸的呈現不同的處理方式所產生的差異，我們分別採用先前提到的Imagemagick縮圖銳化程序，以及最多人使用的網路相簿，分別是Flickr網路相簿，以及Google+(Picasa)網路相簿，其中Picasa上傳時勾選了「保留原始圖檔的畫質」，以儘量減輕畫質的減損，所有照片都是由同一個原始圖檔生成的。而這個任何人都可以重覆的實驗告訴我們，這才是一個數位照片「畫質」區分的所在。

為了更進一步了解這些照片經過哪些處理，下面分別將800px的圖檔經過加強對比與灰階化，其套用的Gamma曲線是一模一樣的，同樣的，我們把注意力放在左上半部的色彩區塊：

.. figure:: ../../../arch_2013/files_2013/M43/banding/800/800_P1390829_band.jpg
   :target: ../../../arch_2013/files_2013/M43/banding/800/800_P1390829_band.jpg
   :align: center

   Imagemagic縮圖至800px並銳化，降飽和提高對比，上傳至github pages。

.. figure:: ../../../arch_2013/files_2013/M43/banding/800/800_flickr_band.jpg
   :target: ../../../arch_2013/files_2013/M43/banding/800/800_flickr_band.jpg
   :align: center

   flickr下載的800px圖檔，降飽和提高對比(參數同上)，上傳至github pages。


.. figure:: ../../../arch_2013/files_2013/M43/banding/800/800_google_band.jpg
   :target: ../../../arch_2013/files_2013/M43/banding/800/800_google_band.jpg
   :align: center

   google+下載的800px圖檔，降飽和提高對比(參數同上)，上傳至github pages。


我曾經一度懷疑Flickr有額外加強dither的程度，不過放大來看後，確定那些雜點分佈其實是高度量化的結果，也就是說，與第一張由Imagemagick縮圖並處理的圖檔相比，Flickr仍是屬於壓縮率較高的(檔案容量較小)，不過其結果跟最高畫質非常接近，而google+或是Picasa的成品則產生惱人的斷階，像年輪一般地破壞整個畫面，難以讓任何稍稍注重畫質的人接受，不過其檔案容量也是最小的。

從這裡我們可以知道數位照片的「畫質」，並不一定會經由感光元件的動態，鏡頭的銳利度等硬體呈現出明顯差異，那是因為數位照片就是「一連串捨棄色彩與細節等資訊」的過程，許多人喜歡以1:1的比例來評斷畫質的好壞，卻沒有注意到100%像素檢視(也就是所謂的pixel peeping)離最終可完整檢視的照片還有一大段距離，只有經過縮圖後才是，高動態與完美細節的Raw資訊，亦離最終成品遠矣，只有將細節捨棄過後的東西才是，這些才是「畫質」真正決勝負的戰場。



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
