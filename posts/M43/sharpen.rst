.. title: flickr縮圖銳化探討
.. slug: sharpen
.. date: 20130705 10:45:45
.. tags: draft,學習與閱讀
.. link: 
.. description: Created at 20130620 20:38:34
.. ===================================Metadata↑================================================
.. ● 記得加上tags: 人生，狗狗，程式，生活紀錄，英文，閱讀，教養，科學，mathjax
.. ● 記得加上slug，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

為什麼要縮圖?
------------------

目前的數位相機，其圖檔尺寸是遠超過網頁分享的需求，例如1600萬畫素的照片，相當於A3尺寸的大小，因此在相對解析度小很多的電腦螢幕上，不縮圖大概只能觀看照片的一個很小的角落。縮圖會讓照片清晰度大大降低。不管你用的相機與鏡頭再好，若是縮圖的環節出問題，只會讓照片細節糊成一片，許多人會刻意去做1:1的照片檢視，或是參考知名評測網站的鏡頭銳利度評比(MTF-50)，希望藉此能得到心目中理想的銳利畫質，但是除非要印成海報(A3尺寸的海報其實也是不上不下的)，縮圖才是最後成像的表現之處，這個步驟的重要性往往凌駕於器材所能提供的銳利度，如果不注重縮圖，反而會使得畫質看起來還比低階的器材糟糕，而且非常明顯，而透過良好的縮圖銳化參數，甚至會讓人誤以為器材具有極高的銳利度呈現，說穿了，鏡頭銳利度評比其實已經流於帳面上數據的測試，事實上在縮圖的情形下，照片是無法反映鏡頭真正的銳利度。同時縮圖除了會讓影像模糊，也會一併降低雜訊的呈現，更讓許多雜訊測試的表現流於數據高低之比較，所以我們可以說，縮圖的工作遠比選擇低雜訊，高銳利度的器材還更為重要，卻是很多人所忽略的。因此經常會出現耗費財力所添購的頂級器材,網頁照片的銳利度卻遠不及低階廉價，卻有良好縮圖銳化的器材這種極為尷尬的事情。

由於網路服務的發展迅速，現在有很多人都將照片上傳到網路相簿，而必然的，這些網路相簿一定要將照片縮至正常螢幕可以顯示的範圍，各家網路相簿所使用的縮圖技術不同，目前大眾一致公認縮圖品質最好的應該是Flickr相簿莫屬，這不禁讓我好奇的想要知道他到底用了哪些參數，由於早期，Flickr使用的是imagemagick這個影像轉換自由軟體，因此底下我們用imagemagick的convert套件來探討縮圖銳化的秘密。

imagemagick是一個發展已久的自由軟體，他廣為被許多網頁與自由軟體的愛好者採用，由於他是以指令為主，大大降低了跨平台的門檻，更有利於作為網站的影像處理模組，以及大量處理圖檔，也就是說無論你是使用何種作業系統，都可以利用他，由於他採用的架構簡單，學一次終身受用，歷久彌新，搭配其他自由軟體可以擦出更強大的火花，例如你可以一次對上萬個照片進行處理，轉檔，或縮圖，然後自動生成網址或路徑於文字檔裡，真的要說唯一的缺點就是純文字指令讓他看起來一點都不新潮，好似上個世紀的老舊古董(他的確是)。

為什麼需要自己做縮圖的銳化呢?有以下幾點的好處:

#. 縮圖銳化的效果可以自行掌控。
#. 事先寫好的script可以在彈指間完成大量例行性的縮圖工作，當然他能做的遠超過此。
#. 不會有圖床支援的問題，我們可以將事先銳化好的縮圖上傳至任何網站，討論區，與社交網站，不需要另外開啟Flickr帳號轉貼網頁語法，而能達到同等效果。
#. 非常方便的保留縮圖銳化的結果，當然你也可以先把原始照片上傳到Flickr，再下載回來。
#. 理論上，網路相簿的銳化只有在縮圖過程才會進行，因此這代表只要您正確選擇上傳圖檔的比例(例如640x480)，圖片是不會經過網站的縮圖程序(假設你已經先縮圖並銳化好了)

以縮圖為寬高最大640px為例，使用參數為::

convert 原始圖檔.jpg -colorspace RGB -filter LanczosSharp -distort
Resize 640x640 -unsharp 1x0.55+1.5+0.002 -colorspace sRGB -border 10 -quality
100 縮圖檔名.jpg

.. figure:: ../../arch_2013/file_2013/M43/sharpen/640_P1370103.jpg
   :target: ../../arch_2013/file_2013/M43/sharpen/640_P1370103.jpg
   :align: center

   imagemagick 未銳化


.. figure:: https://farm6.staticflickr.com/5504/9093131904_94d84757d5_c.jpg
   :target: https://farm6.staticflickr.com/5504/9093131904_94d84757d5_c.jpg
   :width: 640px
   :align: center
      
   未銳化，上傳至flickr

.. figure:: ../../arch_2013/file_2013/M43/sharpen/640_P1370103_sharpen.jpg
   :target: ../../arch_2013/file_2013/M43/sharpen/640_P1370103_sharpen.jpg
   :align: center

   imagemagick 銳化


接著來看800px解析度的結果，使用無銳化的縮圖參數::

convert P1370032_sharpen.jpg -colorspace RGB -filter LanczosSharp -distort Resize 800x800 -colorspace sRGB -border 10 -quality 100 800_P1370032.jpg

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


也許您會說，既然有Flickr，為何要自找麻煩，其實我也使用Flickr好一陣子，由於他並不是完全免費，在介面與速度上也有諸多限制，而網路科技日躍千里，很多服務經常突然的關閉，改朝換代，或是轉換重心，雖然目前Flickr看起來仍是很受歡迎的網路相簿，短期內應該不至於出現什麼問題，但是他所使用的技術與服務其實都不是我們所能掌控的，隨著他的功能擴充，嘗試跨足社交領域等，無論是執行效率以及網頁體積也出現緩慢與肥大的症狀，歸功於日益複雜化的功能與介面(聽起來很耳熟，不是嗎?)，同時我們也必須適應不斷改變的新介面。換言之，使用這類網路服務，我們是處於被動的狀態，只有接受與不接受兩種選擇，他也不斷承受競爭者的壓力，勢必讓功能愈來愈複雜以免遭到取代，如果未來有個新的網路相簿，提供跟Flickr一樣好的縮圖畫質，介面更快，我們是不是反而得花更多時間轉移相片呢?說穿了，我們其實是用一時的方便換取未來的選擇性，如果有個方法，可以讓我們複製某些網路相簿的優勢，同時排除其帶給我們的限制，所需要的代價僅是「學習」一個可以受用無盡技術，這不是最好的方式嗎?這也是Hacker的基本精神，我一直不覺得學習這些東西會帶來任何困擾，真正的阻礙其實是來自沒有門路或良好的學習管道，還有一點點的惰性與對於改變所產生的不安。

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