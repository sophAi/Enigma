.. title: 感光元件的差異對縮圖的影響
.. slug: resize
.. date: 20130713 08:51:26
.. tags: 學習與閱讀
.. link: 
.. description: Created at 20130712 16:37:44
.. ===================================Metadata↑================================================
.. 記得加tags: 人生省思,流浪動物,生活日記,學習與閱讀,英文,mathjax,自由的程式人生,書寫人生,理財
.. 記得加slug(無副檔名)，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

感謝Happyspirit兄二話不說大力相助，提供這三張測試照片，分別是採用\ `Foveon X3`_\ 的Sigma DP2 Merrill (DP2M)\ [#]_\ ，採用一般常見的\ `Bayer`_ [#]_\ 排列\ `live MOS`_ [#]_\ 的Panasonic GH2搭配20mm F1.7餅乾鏡，以及具有\ `Ultra Pixel`_ [#]_\ 感光元件的智慧型手機HTC New One，這三台性格迥異的相機正好讓小弟實驗縮圖情況下不同感光元件所呈現的差異，由於每台相機的自動白平衡有些許差異，使用的鏡頭也不同，因此我們將重點放在畫面的中心部位的清晰度，也就是理論上最能夠呈現照片解析力的地方，以下是這三張圖片，經過一般的銳利化過程，也就是我們先前所使用Flickr銳化參數所得到的成品。

.. figure:: ../../../arch_2013/files_2013/M43/sharpen/800_01_DP2M.jpg
   :target: ../../../arch_2013/files_2013/M43/sharpen/800_01_DP2M.jpg
   :align: center

   DP2M測試照，原始圖檔的尺寸為4704x3136(3:2)。

.. TEASER_END

.. figure:: ../../../arch_2013/files_2013/M43/sharpen/800_02_GH2_20mm.JPG
   :target: ../../../arch_2013/files_2013/M43/sharpen/800_02_GH2_20mm.JPG
   :align: center

   GH2測試照，原始圖檔的尺寸為4976x2800(16:9)。

.. figure:: ../../../arch_2013/files_2013/M43/sharpen/800_03_new_one.jpg
   :target: ../../../arch_2013/files_2013/M43/sharpen/800_03_new_one.jpg
   :align: center

   HTC New One測試照，原始圖檔為2688x1520(16:9)。


裁切出中心部位後，我們先來看1:1檢視的部份:

.. figure:: ../../../arch_2013/files_2013/M43/sharpen/DP2M_1_to_1.png
   :target: ../../../arch_2013/files_2013/M43/sharpen/DP2M_1_to_1.png
   :align: center

   DP2M 中央以1:1呈現，未經縮圖與銳化。

.. figure:: ../../../arch_2013/files_2013/M43/sharpen/GH2_1_to_1.png
   :target: ../../../arch_2013/files_2013/M43/sharpen/GH2_1_to_1.png
   :align: center

   GH2 中央以1:1呈現，未經縮圖與銳化。

.. figure:: ../../../arch_2013/files_2013/M43/sharpen/New_One_1_to_1.png
   :target: ../../../arch_2013/files_2013/M43/sharpen/New_One_1_to_1.png
   :align: center

   New One 中央以1:1呈現，未經過縮圖與銳化。

為了方便比較，我將縮圖銳化的中央裁切部位放在一起，圖中所指的一般銳化為先前提到的Flickr銳化標準參數::

    -unsharp 1x0.55+1.5+0.002

而加強銳化的參數為::

    -unsharp 1x0.72+1.5+0.002

這裡我們分成兩階段測試，如下圖

.. figure:: ../../../arch_2013/files_2013/M43/sharpen/Enhanced_sharpen_crop.png
   :target: ../../../arch_2013/files_2013/M43/sharpen/Enhanced_sharpen_crop.png
   :align: center

   先裁切出中央花樣的部份，然後再縮圖銳化至800px


.. figure:: ../../../arch_2013/files_2013/M43/sharpen/Enhanced_sharpen_zoom.png
   :target: ../../../arch_2013/files_2013/M43/sharpen/Enhanced_sharpen_zoom.png
   :align: center

   先將原圖縮圖至800px，然後裁切出中央花樣的部位。

最後我們將套用加強銳化參數的GH2與New One照片與一般銳化的DP2M照片放在一起做為總結。


.. figure:: ../../../arch_2013/files_2013/M43/sharpen/800_01_DP2M.jpg
   :target: ../../../arch_2013/files_2013/M43/sharpen/800_01_DP2M.jpg
   :align: center

   DP2M測試照，一般銳化，以800px呈現。

.. figure:: ../../../arch_2013/files_2013/M43/sharpen/800_02_GH2_20mm_sharpen.jpg
   :target: ../../../arch_2013/files_2013/M43/sharpen/800_02_GH2_20mm_sharpen.jpg
   :align: center

   GH2測試照，加強銳化，以800px呈現。


.. figure:: ../../../arch_2013/files_2013/M43/sharpen/800_03_new_one_sharpen.jpg
   :target: ../../../arch_2013/files_2013/M43/sharpen/800_03_new_one_sharpen.jpg
   :align: center 

   New One測試照，加強銳化，以800px呈現。

這些測試雖然不能稱得上定性與定量，不過至少能為以下的問題提供些思考方向:

#. 感光元件的差異，在縮圖下是否可以分辨得出來?
#. 縮圖銳化的效果，有沒有可能遠大於鏡頭與感光元件，以及片幅的差別?
#. 為什麼要縮圖?
#. 是否有不後製的數位照片存在?

必須澄清的是，筆者並不是「頂級器材無用論」的信奉者，例如這個實驗中，我們可以發現，即使清晰度藉由銳化過程達到相似的等級，部份照片的高光以及暗部細節其實喪失很多，並不利於進一步的後製與還原影像資訊，筆者認為對於高階器材正確的認知，或許不是在於畫質的保證，而是「更高的後製寬容度」，這也是目前主流觀念裡經常產生誤解的地方 ― 不管我們使用了多少位元的AD轉換，使用了多高的位元紀錄色階，使用多銳利的鏡頭與多精細的感光元件，最後的成品總是會遇到必然的限制，就是縮圖與降低位元(動態範圍)，有如湖泊有大有小，但是他們最終都只有一樣大小的出水口，因此不是所有資訊都得以保留，甚至我們可以說，愈豐富的原始Raw資料，在轉換成JPG並縮至可以觀看的照片尺寸的過程中，損失的資訊量其實是愈大的。諸如GH2或是DP2M將近1600萬畫素的JPG照片，若以300dpi輸出，能印刷至A3尺寸，遠大於正常照片所需的解析度，在我們縮圖至能夠正常觀看的大小時，其實捨棄了將近80~90%以上的畫素資訊\ [#]_\ ；真正能夠完整保留的，反而是照片的構圖、故事性、以及光線的運用，就這點就足以讓人重新思考所謂的畫質在數位攝影裡所代表的意義。

.. </body>
.. <url>

.. _Foveon X3: http://en.wikipedia.org/wiki/Foveon_X3

.. _Bayer: http://en.wikipedia.org/wiki/Bayer_filter

.. _live Mos: http://en.wikipedia.org/wiki/Live_MOS

.. _Ultra Pixel: http://en.wikipedia.org/wiki/Ultra_Pixel_Technology

.. </url>
.. <footnote>

.. [#] http://en.wikipedia.org/wiki/Foveon_X3

.. [#] http://en.wikipedia.org/wiki/Bayer_filter

.. [#] http://en.wikipedia.org/wiki/Live_MOS

.. [#] http://en.wikipedia.org/wiki/Ultra_Pixel_Technology

.. [#] 以主流寬螢幕1920x1080的解析度(16:9)，約為207萬像素，因此1600萬像素(4:3或3:2比例)縮圖至螢幕可以顯示的最大範圍，將低於207萬畫素，也就是捨棄掉將近87%以上的畫素，更不用說一般在網路相簿分享的照片，是遠小於螢幕最大可顯示的範圍。

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
