.. title: 提升GH2與GX1的錄影畫質
.. slug: ptool
.. date: 20130724 00:01:32
.. tags: draft,學習與閱讀
.. link: 
.. description: Created at 20130722 22:47:23
.. ===================================Metadata↑================================================
.. 記得加tags: 人生省思,流浪動物,生活日記,學習與閱讀,英文,mathjax,自由的程式人生,書寫人生,理財
.. 記得加slug(無副檔名)，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/29_youtube.png
      :target: ../../../arch_2013/files_2013/M43/ptool_settings/29_youtube.png
   :align: center

   這是上傳到Youtube後的畫面截圖，可以看到不自然的色塊產生

.. TEASER_END


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/30_GX1_MTS.png
      :target: ../../../arch_2013/files_2013/M43/ptool_settings/30_GX1_MTS.png
   :align: center

   這是原始的影片截圖，色階明顯平順許多。

在\ `探討網路照片的奧秘`_\ 一文中，我們提到了縮圖對於數位影像的重要性，也提到了目前的Full HD規格，在主流的螢幕下相當於1:1的檢視，動態影片的畫質差異，會比更高畫素的靜態照片還要明顯，無論是縮圖的方式，或是影像壓縮的技術，都會以100%的比例呈現在螢幕上。例如上面兩張圖，都是1:1的截圖，可以很明顯的察覺到差別，也讓提升錄影畫質更具意義。除了改善錄影畫質，軔體的破解也能開啟一些原先軔體封閉的功能，例如日文版本的機身，可以透過軔體破解新增英文語言介面，以及提供PAL與NTSC之間的切換，歐規的數位相機，其錄影大多有30分鐘的限制，也能透過破解移除，在記憶卡的效能容許下，提升的流量以及良好的Scaling Matrix都能有效的讓影片中的瑕疵降到最低，整體來說，甚至有機會凌駕於專業的錄影機之上。

這裡我們以GH2與GX1為例，有關破解的相關資訊請參考\ `Ptool wiki`_\ 的頁面，我們需要以下檔案:

#. \ `Ptool3`_\ 。
#. \ `GH2的官方軔體`_\ 或\ `GX1的官方軔體`_\ 。
#. \ `GH2的Ptool設定檔`_\ 或\ `GX1的Ptool設定檔`_\。

如果您是使用GX1，請下載GX1的官方軔體，以及GX1的Ptool設定檔，同理，GH2請下載相關檔案。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/01_Ptool1.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/01_Ptool1.png
   :align: center

   Windows下直接執行ptool3.exe，Linux與Mac則安裝wine來開啟。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/02_Ptool2.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/02_Ptool2.png
   :align: center

   點選Load Firmware後，讀取由Panasonic官方網站所下載的軔體檔(.bin檔)。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/03_Ptool3.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/03_Ptool3.png
   :align: center

   如果設定檔(.ini檔)與Ptool放在同一個目錄下，則讀取軔體後，下方A~J的按鈕會亮起綠燈，分別對應seta.ini~setj.ini。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/04_Ptool4.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/04_Ptool4.png
   :align: center

   若要讀取seta.ini的設定，則用滑鼠按一下A的綠色按鈕即可將設定讀取進來。

.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/05_Ptool5.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/05_Ptool5.png
   :align: center

   檢查一下幾個重要的設定，例如Version increment一定要勾選，Interface與Movie related restrictions都勾選。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/06_Ptool6.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/06_Ptool6.png
   :align: center

   在專家設定裡，也修改了Scaling tables，這是與Quantization Parameter有關的設定。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/07_Ptool7.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/07_Ptool7.png
   :align: center

   這些專家選項是畫質與檔案流量維持平衡的關鍵。原則上選項應該都已經設定好，不需要做任何手動的更改。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/08_Ptool8.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/08_Ptool8.png
   :align: center

   選擇Save Firmware，將修改過後的軔體檔存成GX1__V12.bin或GH2__V12.bin，將原來軔體編號加1即可，請勿將原始軔體覆蓋以備日後修改或還原。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/09_Ptool9.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/09_Ptool9.png
   :align: center

   將一張由相機格式化過的SD卡連接上電腦，將剛剛的新軔體複製到記憶卡的根目錄。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/10_GH2_playback.JPG
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/10_GH2_playback.JPG
   :align: center

   將SD卡插回相機，開啟電源，確保使用原廠充飽的電池，按下播放鈕(Playback)。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/11_GH2_update.JPG
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/11_GH2_update.JPG
   :align: center

   如果是日文介面，則應該如圖所示，選擇第一個選項進行更新軔體。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/12_GX1_update2.JPG
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/12_GX1_update2.JPG
   :align: center

   更新過程千萬不要中斷電源，或進行任何操作，放在安全的地方靜靜地等他完成。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/13_GX1_ver.JPG
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/13_GX1_ver.JPG
   :align: center
 
   更新完後，版本應該不會改變。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/14_GH2_lang.JPG
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/14_GH2_lang.JPG
   :align: center

   如果原本是日文機，更新完會多出語言選項，也會出現繁體中文的選項。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/15_GH2_miss_ch.JPG
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/15_GH2_miss_ch.JPG
   :align: center

   但是中文字型是與軔體分開來的，也就是說，日文機身並不包含中文字型，所以即使出現中文選項，也無法正常顯示中文，所有的日文機應該都是這樣。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/16_GH2_en.JPG
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/16_GH2_en.JPG
   :align: center

   因此如果您的相機是日文機種，還是選擇英文介面吧!


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/17_GH2_lang_en.JPG
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/17_GH2_lang_en.JPG
   :align: center

   如果是來自香港的平輸機器，機身已經包含中文字型，無論如何，中文介面都不會受到影響，可以安心使用。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/18_GX1_ntsc_format.JPG
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/18_GX1_ntsc_format.JPG
   :align: center

   更新軔體有可能會遇到這樣的錯誤訊息，其實是因為機身切換了視訊格式所致，不需要太擔心。只要在相機上重新格式化SD卡即可。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/19_GX1_video_out.JPG
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/19_GX1_video_out.JPG
   :align: center

   香港是採用PAL規格，可以利用這個選項切換成適用於台灣的NTSC規格。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/20_GX1_ntsc.JPG
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/20_GX1_ntsc.JPG
   :align: center

   這是GX1的設定，更改成NTSC即可。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/21_GH2_video_out.jpg
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/21_GH2_video_out.jpg
   :align: center

   GH2也是一樣。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/22_GH2_ntsc.jpg
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/22_GH2_ntsc.jpg
   :align: center

   更改成NTSC。如此一來，也比較能夠減輕室內日光燈下錄到閃爍燈頻的機率。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/23_GH2_stock_24p.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/23_GH2_stock_24p.png
   :align: center

   這是Ptool論壇的Driftwood所做的Quantization parameter測試，途中的顏色愈淺，表示QP愈佳，此圖為原廠GH2的24p模式。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/24_GH3_24p.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/24_GH3_24p.png
   :align: center

   這個則是GH3原廠24p模式的測試結果(非All-I)。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/25_GH2_ClusterX.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/25_GH2_ClusterX.png
   :align: center

   這個則是經過Driftwood的破解設定所產生的結果，可以看到QP是最低的，結果是最好的一個。





.. </body>
.. <url>

.. _探討網路照片的奧秘: sharpen.html

.. _Ptool wiki: http://www.gh1-hack.info/wiki/PToolSoftware

.. _Ptool3: http://www.gh1-hack.info/ptool3d.zip

.. _GH2的官方軔體: http://panasonic.jp/support/global/cs/dsc/download/fts/dl/gh2.html

.. _GH2的Ptool設定檔: http://sophai.github.io/arch_2013/files_2013/M43/ptool_settings/seta.ini

.. _GX1的官方軔體: http://panasonic.jp/support/global/cs/dsc/download/fts/dl/gx1.html

.. _GX1的Ptool設定檔: http://sophai.github.io/arch_2013/files_2013/M43/ptool_settings/setb.ini

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
