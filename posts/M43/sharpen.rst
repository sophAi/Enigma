.. title: 探討網路照片的奧秘
.. slug: sharpen
.. date: 20130712 13:43:16
.. tags: 學習與閱讀
.. link: 
.. description: Created at 20130620 20:38:34
.. ===================================Metadata↑================================================
.. ● 記得加上tags: 人生，狗狗，程式，生活紀錄，英文，閱讀，教養，科學，mathjax
.. ● 記得加上slug，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

我們先來看看下面四張長與寬最大640px的圖，其來源都是同一張相片:

.. figure:: ../../arch_2013/file_2013/M43/sharpen/640_P1370103.jpg
   :target: ../../arch_2013/file_2013/M43/sharpen/640_P1370103.jpg
   :align: center

   原始圖檔縮小至640px

.. figure:: https://lh4.googleusercontent.com/-P554w0SP0GE/Ud-TC2G5TSI/AAAAAAAA-0g/8EPfB0i7z24/s640/P1370103_4429113-08.jpg
   :target: https://lh4.googleusercontent.com/-P554w0SP0GE/Ud-TC2G5TSI/AAAAAAAA-0g/8EPfB0i7z24/s640/P1370103_4429113-08.jpg
   :align: center
   :width: 640px
 
   原始圖檔上傳至google相簿

.. figure:: https://farm6.staticflickr.com/5504/9093131904_94d84757d5_c.jpg
   :target: https://farm6.staticflickr.com/5504/9093131904_94d84757d5_c.jpg
   :width: 640px
   :align: center
      
   原始圖檔上傳至Flickr相簿

.. figure:: ../../arch_2013/file_2013/M43/sharpen/640_P1370103_sharpen.jpg
   :target: ../../arch_2013/file_2013/M43/sharpen/640_P1370103_sharpen.jpg
   :align: center

   Imagemagick 縮圖銳化，上傳到github。


接著來看800px解析度下的結果

.. figure:: ../../arch_2013/file_2013/M43/sharpen/800_P1370032.jpg
   :target: ../../arch_2013/file_2013/M43/sharpen/800_P1370032.jpg
   :align: center
 
   imagemagick 縮圖未銳化

未銳化的原圖，上傳至flickr後，縮圖至800px

.. figure:: https://farm8.staticflickr.com/7402/9093134142_58ea69c6b4_c.jpg
   :target: https://farm8.staticflickr.com/7402/9093134142_58ea69c6b4_c.jpg
   :align: center
   :width: 800px

   未銳化，原圖上傳至flickr


以縮圖為寬高最大800px為例，使用參數為::

convert 原始圖檔.jpg -colorspace RGB -filter LanczosSharp -distort
Resize 800x800 -unsharp 1x0.55+1.5+0.002 -colorspace sRGB -border 10 -quality
100 縮圖檔名.jpg

.. figure:: ../../arch_2013/file_2013/M43/sharpen/800_P1370032_sharpen.jpg
   :target: ../../arch_2013/file_2013/M43/sharpen/800_P1370032_sharpen.jpg
   :align: center

   imagemagick 縮圖銳化

imagemagick的參數如下::

convert 原始圖檔.jpg -colorspace RGB -filter LanczosSharp -distort Resize 800x800 -unsharp 1x0.55+1.5+0.002 -colorspace sRGB -border 10 -quality 100 縮圖檔名.jpg

縮圖最重要的兩個環節，就是避免鋸齒化以及像素捨去(downsampling)所產生的模糊化，對於前者，我們必須採用適當的


.. </body>
.. <url>



.. </url>
.. <footnote>



.. </footnote>
.. <citation>



.. </citation>
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
