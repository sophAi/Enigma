.. title: 數位照片的奧秘
.. slug: sharpen
.. date: 20130807 12:08:54
.. tags: 學習與閱讀
.. link: 
.. description: Created at 20130620 20:38:34
.. ===================================Metadata↑================================================
.. ● 記得加上tags: 人生，狗狗，程式，生活紀錄，英文，閱讀，教養，科學，mathjax
.. ● 記得加上slug，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

我們先來看看下面四張長與寬最大640px的圖，其來源都是同一張相片:

.. figure:: ../../../arch_2013/files_2013/M43/sharpen/640_P1370103.jpg
   :target: ../../../arch_2013/files_2013/M43/sharpen/640_P1370103.jpg
   :align: center

   原始圖檔縮小至640px，上傳至github。

.. TEASER_END

.. figure:: https://lh4.googleusercontent.com/-P554w0SP0GE/Ud-TC2G5TSI/AAAAAAAA-0g/8EPfB0i7z24/s640/P1370103_4429113-08.jpg
   :target: https://lh4.googleusercontent.com/-P554w0SP0GE/Ud-TC2G5TSI/AAAAAAAA-0g/8EPfB0i7z24/s640/P1370103_4429113-08.jpg
   :align: center
   :width: 640px
 
   原始圖檔上傳至google相簿，以640px呈現。

.. figure:: https://farm6.staticflickr.com/5504/9093131904_94d84757d5_c.jpg
   :target: https://farm6.staticflickr.com/5504/9093131904_94d84757d5_c.jpg
   :width: 640px
   :align: center
      
   原始圖檔上傳至Flickr相簿，以640px呈現。

.. figure:: ../../../arch_2013/files_2013/M43/sharpen/640_P1370103_sharpen.jpg
   :target: ../../../arch_2013/files_2013/M43/sharpen/640_P1370103_sharpen.jpg
   :align: center

   Imagemagick 縮圖至640px並銳化，上傳到github。


接著來看800px解析度下的結果:

.. figure:: ../../../arch_2013/files_2013/M43/sharpen/800_P1370032.jpg
   :target: ../../../arch_2013/files_2013/M43/sharpen/800_P1370032.jpg
   :align: center
 
   原始圖檔直接縮小至800px，上傳至github。

.. figure:: https://lh5.googleusercontent.com/-Fh9yCjBNUF0/Ud-pSM5JRnI/AAAAAAAA-0s/WSAKPSTyzgY/s800/P1370032_4429113-08.jpg
   :target: https://lh5.googleusercontent.com/-Fh9yCjBNUF0/Ud-pSM5JRnI/AAAAAAAA-0s/WSAKPSTyzgY/s800/P1370032_4429113-08.jpg
   :align: center
   :width: 800px

   原始圖檔上傳至google相簿，以800px呈現。

.. figure:: https://farm8.staticflickr.com/7402/9093134142_58ea69c6b4_c.jpg
   :target: https://farm8.staticflickr.com/7402/9093134142_58ea69c6b4_c.jpg
   :align: center
   :width: 800px

   原始圖檔上傳至Flickr相簿，以800px呈現。


.. figure:: ../../../arch_2013/files_2013/M43/sharpen/800_P1370032_sharpen.jpg
   :target: ../../../arch_2013/files_2013/M43/sharpen/800_P1370032_sharpen.jpg
   :align: center

   imagemagick 縮圖至800px並銳化，上傳至github。

不知道各位比較喜歡那一種呈現方式呢?

imagemagick的參數如下::

    convert 原始圖檔.jpg -colorspace RGB -filter LanczosSharp -distort Resize 800x800 -unsharp 1x0.55+1.5+0.002 -colorspace sRGB -border 10 -quality 100 縮圖檔名.jpg

縮圖最重要的兩個環節，就是避免鋸齒化以及像素捨去(down sample)所產生的模糊化，這兩者無論是對於靜態影像或是動態影像都是非常重要的，對於去鋸齒化，我們參考\ `Nicolas Robidoux`_ [#]_\ 教授所建議的參數，使用distort Resize搭配-filter LanczosSharp，LanczosSharp其實是屬於Windowed SincFast演算法，可以用Verbose模式將細部的設定列出，例如在命令列下達::

    convert null: -filter LanczosSharp -define filter:verbose=1 -resize 2 null: | grep '^#'

則會顯示::

    # Resize Filter (for graphing)
    #
    # filter = SincFast
    # window = SincFast
    # support = 3
    # win-support = 3
    # scale_blur = 0.981251
    # practical_support = 2.94375

這就是LanczosSharp的細部參數。所謂的縮圖，其實跟tensor transformation有關，因為一張圖其實就是以一個龐大的矩陣儲存影像資訊，有關SincFast演算法可以參考\ `Resampling Filters`_ [#]_\ 這方面的資訊。

而對於銳化這部份，效果比較好的是使用Gaussian Mask，類似的方式如\ `Smart Sharpen`_ [#]_\ ，使用Photoshop或GIMP即可針對畫面線條的邊緣進行銳化，而跳過色階變化平滑的區域(例如膚色，或是天空)，這樣一來，就不會一併將雜訊銳化而造成不自然的雜點，而imagemagick使用-unsharp這個參數，unsharp mask這詞是來自於傳統底片式攝影所使用的暗房技術，目的是得到邊緣銳利化的結果，在數位影像裡，透過將原圖減去一定比例的模糊化影像，所得到的差異影像(邊緣)疊加回原圖，以造成邊緣銳利化的效果，更省去了滑鼠點來點去的繁瑣步驟，很適合用來一次處理大量的圖片。-unsharp參數在\ `Eric Jeschke`_ [#]_\  的文章裡有很詳細的解說，以我們所使用的銳化參數為例::


    -unsharp 1x0.55+1.5+0.002

所使用的四個數字分別是Gaussian Mask的Radius(每個像素周圍列入銳化計算的像素範圍)、Sigma(Gaussian遮罩的半高寬，或是Standard Deviation)、Amount(邊緣黑白的差距)、以及Threshold(像素間對比差異要高於這個值才會列入銳化的計算)。在Eric的文章裡提到很多Radius與Sigma的計算方式，不過我們這邊取的參數，是筆者經過多次嘗試，而得到與Flickr縮圖銳化最接近的參數，同時，銳化與縮圖也有先後次序，筆者建議先進行縮圖再銳化，因為要做到與Flickr相簿同樣的效果，先銳化時必須要大大加強銳化的強度，容易讓照片產生不自然的顆粒，同時縮圖的速度也會比較慢。銳化的過程儘量在縮圖時進行，意即儘量保留原始未銳化的圖檔，以利於日後縮圖銳化成各個解析度之用。

看到這裡，我們對網路上所廣為流傳的許多資訊應該會更有概念，例如:

#. 為什麼非縮圖不可?
#. 1:1檢視靜態照片與1:1檢視動態影片，何者才有必要性?現今主流螢幕的解析度?
#. 相機所提供的高畫素，目的為何?
#. 鏡頭的銳利度(MTF-50)，片幅的大小(135, APS, 4/3,...)，感光元件的種類(Bayer、Foveon X3)等差異，在縮圖的情況下是否還能夠呈現?
#. 數位相機的總畫素平均遠高於Full HD(1080p)的解析度，因此錄影的影像品質會不會受到縮圖(down sample)方式極大的影響?
#. 您有沒有在網路上見過高檔，大片幅相機拍攝的數位照片，清晰度竟然比一般DC還差?
#. 您有沒有遇到過片幅比較大的數位相機，其錄製的影片清晰度竟然比片幅小的數位相機還低?
#. 數位照片是否都是後製過的?
#. 許多相機宣稱移除低通濾鏡或是AA Filter，真的是為了提升畫面銳利度嗎?

這些問題，筆者先不作進一步說明，留給各位思考。

接著我們將示範如何撰寫python程式來利用imagemagick實現大量自動化的縮圖銳化工作，我們的目的是將集中在一個目錄下的所有jpg檔予以縮圖並銳化，然後自動生成包含圖片連結的reStructuredText(ReST)的文章範例，換句話說，在網路文章裡插入圖片，不再需要繁複的上傳照片與拷貝連結等手續，僅需要將要包含的圖片按照順序集中在一個資料夾裡，執行程式就可以自動生成文章，照片也會依照順序排列，剩下的工作就僅是補上文字而已。同時，我們也不用擔心網站所提供的圖床會將照片品質劣化，只要事先將圖片縮好，任何網站都可以呈現出品質良好的縮圖照片。

.. </body>
.. <url>

.. _Nicolas Robidoux: http://www.imagemagick.org/Usage/filter/nicolas/

.. _Resampling Filters: http://www.imagemagick.org/Usage/filter/#gaussian_other

.. _Smart Sharpen: http://gimpguru.org/Tutorials/SmartSharpening2/

.. _Eric Jeschke: http://redskiesatnight.com/2005/04/06/sharpening-using-image-magick/

.. </url>
.. <footnote>

.. [#] http://www.imagemagick.org/Usage/filter/nicolas/

.. [#] http://www.imagemagick.org/Usage/filter/#gaussian_other

.. [#] http://gimpguru.org/Tutorials/SmartSharpening2/

.. [#] http://redskiesatnight.com/2005/04/06/sharpening-using-image-magick/

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
