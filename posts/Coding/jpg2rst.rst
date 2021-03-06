.. title: 自動化縮圖與生成文章檔案
.. slug: jpg2rst
.. date: 20140304 14:24:37
.. tags: 自由的程式人生
.. link: 
.. description: Created at 20130712 23:17:53
.. ===================================Metadata↑================================================
.. 記得加tags: 人生省思,流浪動物,生活日記,學習與閱讀,英文,mathjax,自由的程式人生,書寫人生,理財
.. 記得加slug(無副檔名)，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

.. figure:: ../../../arch_2013/files_2013/Coding/jpg2rst/800/800_Collage.jpg
   :target: ../../../arch_2013/files_2013/Coding/jpg2rst/800/800_Collage.jpg
   :align: center



在了解了縮圖對於照片的影響，以及Imagemagick的使用方法，我們現在將這些資訊實用化，應用在網路文章的寫作，我的目標有以下幾個:

#. 將滑鼠點擊的次數降到最低。
#. 跨平台的可能性。
#. 未來應用的擴充性。
#. 方便性。

.. TEASER_END

這裡筆者以python程式進行上述目標的實作，請先去\ `Imagemagick`_ [#]_\ 網站下載convert套件並安裝好，確定他可以執行如下的縮圖指令

   convert 原始圖檔.jpg -colorspace RGB -filter LanczosSharp -distort Resize 800x800 -unsharp 1x0.55+1.5+0.002 -colorspace sRGB -border 10 -quality 100 縮圖檔名.jpg

接著下載並安裝筆者的jpg2rst套件::

    git clone https://github.com/sophAi/jpg2rst.git jpg2rst
    cd jpg2rst
    sudo easy_install *.egg

工作流程如下:

#. 把想要縮圖的照片集中在一個目錄下。
#. 執行jpg2rst.main()。
#. 自動產生所有照片的縮圖到對應解析度的目錄下。
#. 同時生成包含照片路徑的文件檔，這裡我們採用reStructuredText(ReST)格式。

這個檔案總共包含4個py檔，分別執行不同的工作，例如:

.. listing:: jpg2rst/file_tools.py python

其主要的任務是搜尋當前以及所有子目錄下的特定檔案，如同search()開頭所述，我們只要指定keyword，他就會將符合特徵的檔案列表傳回，我們將會利用這個列表來進行縮圖以及生成文字範例檔的工作，search()的用途當然不只是在縮圖，日後可以非常方便的用他來做大量處理檔案的工作。

.. listing:: jpg2rst/fig_tools.py python

有了search()傳回的檔案列表，我們將其輸入至resize()這個函式裡，並指定圖形長與寬最大的解析度(例如800)，他會偵測並將縮圖輸出到一個新的目錄(800/)，同時也會自動略過已經縮圖過的圖檔，如果解析度的部份輸入none，則不會進行縮圖銳化的工作。

.. listing:: jpg2rst/rst_tools.py python

resize()會輸出縮圖銳化後的檔案列表，我們可以進一步將其輸入到add_fig()函式裡，他會自動擷取vim的ReST範例檔，並且將所有縮圖的圖片連結加進去，例如 

::

    .. figure:: ../gallaries/640/640_01_P1370103_sharpen.jpg
       :target: ../gallaries/640/640_01_P1370103_sharpen.jpg
       :align: center

由於search()會自動依照檔案名稱排序，一個小技巧就是於檔名開頭加上01、02、03...等編號。

您可以將ReST範例檔儲存在~/.vim/template/temp_rst.txt檔案裡，有關vim的自動文件範例檔筆者會另外說明，簡單來說，他可以偵測您創造的文字檔是屬於哪種格式(C++, Python, Latex...等)，然後利用對應的範例檔生成文件，是個非常強大且高效率的功能。

最後是jpg2rst.py這個程式，其實就是用來整合上面3個函式，讓我們的工作流程得以實現，裏面有些目錄的設定，可以依照需求修改;不難發現，任何一個函式都可以獨立運作，例如我們可以單獨使用resize()來測試縮圖銳化的參數，也可以用search()來蒐集任何檔案，或是用add_fig()來重整文章的圖片連結，除了幫我們省去不少縮圖銳化的功夫，更可以在其餘工作裡派上用場，等於是辛苦一次受用無窮的工具，當我們不斷進行例行性的操作時，一個良好的自動化工具可以大大提高工作效率，讓我們有更多時間陪陪家人，或是喝杯咖啡思考一下。

.. </body>
.. <url>

.. _Imagemagick: http://www.imagemagick.org/script/binary-releases.php#iOS

.. </url>
.. <footnote>

.. [#] http://www.imagemagick.org/script/binary-releases.php#iOS

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
