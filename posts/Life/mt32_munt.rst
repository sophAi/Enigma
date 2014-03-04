.. title: linux: 安裝MT32-emulator (Munt)
.. slug: mt32_munt
.. date: 20140304 12:30:31
.. tags: draft
.. link: 
.. description: Created at 20130916 14:22:40
.. ===================================Metadata↑================================================
.. 記得加tags: 人生省思,流浪動物,生活日記,學習與閱讀,英文,mathjax,自由的程式人生,書寫人生,理財
.. 記得加slug(無副檔名)，會以slug內容作為檔名(html檔)，同時將對應的內容放到對應的標籤裡。
.. ===================================文章起始↓================================================
.. <body>

先clone git::

    git clone https://github.com/munt/munt.git


安裝libasound2-dev,libxpm-dev,cmake\ ::

apt-get install libasound2-dev libxpm-dev libxt-dev libX11-dev cmake

到munt/mt32emu目錄下::

    cmake .
    make
    sudo make install

會在/usr/local/lib/下建立libmt32emu.a以及/usr/local/include/mt32emu下建立mt32emu標頭檔

進入munt/mt32emu_alsadrv::

    make
    make install

會將mt32d跟xmt32放到/usr/local/bin/下

記得將所有*.ROM檔放到/usr/share/mt32-rom-data/裡

#. xmt32是一個虛擬的MT-32圖形介面模擬器，可以顯示虛擬的音源器畫面，秀出SYSEX訊號，直接修改reverb等級，還能錄製音樂。

#. xmt32或mt32d　--help可以顯示選項，如果會掉音建議用-i選項將buffer開大，預設是40 (40 msec)::

    mt32d -i 100 -x 200

表示buffer至少100，最大200，改太大好像沒什麼用。CPU速度的因素比較大。

啟動dosbox前，先在終端機執行mt32d或xmt32，會顯示目前的alsa port，預設應該是129:0，把這個設定加到dosbox.conf裡

這個MT32 Emulator在K8 2.5雙核心上仍然跑得有點吃力，會掉音，但是在I5 3.6G四核心上就OK!


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
