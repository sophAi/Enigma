.. title: Ptool更新軔體程序
.. slug: ptool
.. date: 20130730 12:04:07
.. tags: 學習與閱讀
.. link: 
.. description: Created at 20130722 22:47:23
.. ===================================Metadata↑================================================
.. 記得加tags: 人生省思,流浪動物,生活日記,學習與閱讀,英文,mathjax,自由的程式人生,書寫人生,理財
.. 記得加slug(無副檔名)，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

有關Ptool的參數設定細節，請參考另一篇―\ `Ptool的參數檔`_\ 。

更新軔體除了可以替日文機增加英文介面，提升錄影畫質，還能在PAL與NTSC規格切換；例如自香港平行輸入的繁體中文GX1，其為PAL規格，因此他只提供~25fps(1080p50或720p50)的錄影模式，同時還有30分鐘的錄影限制，經過軔體修改後，即可隨時在PAL與NTSC(~30fps,1080p30/i60或720p60等)間切換，也可以移除30分鐘錄影的限制，台灣與日本地區是屬於NTSC。早期PAL規格的相機，因為與台灣日光燈掃描頻率不同步，容易在室內錄影畫面中產生移動的條紋，這現象困擾著許多人，而NTSC規格比較不容易產生類似的問題，不過後期的機種已經能透過更改快門速度來解決這個問題了。

.. TEASER_END

這裡我們以GH2與GX1為例來進行軔體修改與升級的分解步驟，詳細的資訊請參考\ `Ptool wiki`_\ 的原文頁面:

#. 務必使用「充飽電力」的「原廠電池」，請勿使用副廠電池。
#. 請下載\ `Ptool3`_\ ，這是用來修改軔體參數的程式(ptool3.exe)。
#. 請下載\ `GH2的官方軔體`_\ 或\ `GX1的官方軔體`_\ ，我們將利用Ptool來更改軔體的參數(例如:GX1__V11.bin)。
#. 請下載\ `Ptool的參數檔`_\ ，由於參數檔隨時更新，我將其集中在另一篇討論(例如setc.ini)。

確實檢查上述的步驟，並確保下載的檔案完整，我們即可開始進行軔體修改與更新的動作，如果參數檔設定錯誤，頂多是讓相機動作不正常(例如錄影中斷)，並不至於導致相機故障，以我在論壇的經驗，也未曾聽聞過類似事件，唯一有可能造成故障的因素是使用「未充飽」或「非原廠」的電池，嚴重者可能會造成無法正常開機，所以請大家謹記這個守則，更新前務必檢查電池並確實充電，同時不要在軔體更新過程中關閉相機電源或進行任何操作，就可以安心進行破解程序了。另外更新後的相機，請不要進入所謂的「工程模式」，會使相機運作不正常，諸如抓不到鏡頭，如果不小心進入工程模式，只要跳出工程模式後，按照下列步驟重新更新一次軔體即可恢復正常。

由於中文字型是由相機上的ROM而非軔體提供，因此日文介面的Panasonic相機，在經過軔體修改後僅能出現英文介面，中文字型是無法正常顯示的，而原本已有中文介面的相機，更新軔體前後均不受影響，中文與各式語言介面都可以保留。

以下是軔體修改的分解動作:

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

   在專家設定裡，Scaling tables是與Quantization Parameter有關的設定。


.. figure:: ../../../arch_2013/files_2013/M43/ptool_settings/07_Ptool7.png
   :target: ../../../arch_2013/files_2013/M43/ptool_settings/07_Ptool7.png
   :align: center

   這些專家選項是畫質與檔案容量維持平衡的關鍵，相關的參數必須要經過耗時的測試才能得到。


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


更新完軔體後，請記得將SD卡根目錄下的軔體檔案刪除，不然下次開機按下播放鈕時，又會再次詢問是否要升級軔體喔!

Ptool的參數檔是標準的ini檔案，有興趣的人可以使用記事本或編輯器檢視裏面的內容，也可直接將設定值複製與貼上，在Ptool論壇裡也有許多不同的參數檔可供下載使用，建議大家有興趣可以多方嘗試，找出最適合自己的參數檔。


.. </body>
.. <url>

.. _Ptool wiki: http://www.gh1-hack.info/wiki/PToolSoftware

.. _Ptool3: http://www.gh1-hack.info/ptool3d.zip

.. _GH2的官方軔體: http://panasonic.jp/support/global/cs/dsc/download/fts/dl/gh2.html

.. _GX1的官方軔體: http://panasonic.jp/support/global/cs/dsc/download/fts/dl/gx1.html

.. _Ptool的參數檔: ptool_settings.html

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
