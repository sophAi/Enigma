.. title: 使用MathJax與Latex數學
.. slug: mathjax
.. date: 2013-05-25 00:27:05
.. tags: mathjax
.. link: 
.. description: Created at 2013-05-24 13:45:28

.. 請記得加上slug，會以slug名稱產生副檔名為.html的文章
.. 同時，別忘了加上tags喔!

************
mathjax測試
************

.. 文章起始

要讓nikola編輯的文章載入MathJax很簡單，只要在tags裡加入mathjax即可。例如::

	.. tags: mathjax, my_other_tags, ...

然後在段落裡插入math語法，例如::

	The first equation using mathjax is as following :math:`\alpha=\beta+\gamma`

會顯示 
    
The first equation using mathjax is as following :math:`\alpha=\beta+\gamma`

或是使用以下語法獨立顯示數學式子於一行::

	.. math::
      
	   \int \frac{dx}{1+ax}=\frac{1}{a}\ln(1+ax)+C

則如下

.. math::

   \int \frac{dx}{1+ax}=\frac{1}{a}\ln(1+ax)+C

根據conf.py的設定，可以決定上式置中或是靠左，我是選擇置中，這樣看起來比較不會跟上下段落擠在一起。

可惜的是Vst (VIM)還無法支援，轉PDF時的數學式子方案還要再研究一下。

這裡有個小插曲，第一次使用mathjax時發現數學式子只有FireFox表現最為正常，其他瀏覽器都無法正常載入mathjax，檢查一下原始碼，發現是因為用了MathML(只有FireFox原生支援)，Google Chrome使用者必須額外安裝\ `MathJax for Chrome`_\ ,才能正常顯示數學式子了，更不用說其他如IE，safari, opera等，應該都是無法正常顯示吧？如果用html-ccs的方式，則可以繞MathML的相容性，html必須包含::

	<div class="math">
	\begin{equation*}
	\int \frac{dx}{1+ax}=\frac{1}{a}\ln(1+ax)+C
	\end{equation*}
	</div>

而如果是使用MathML，在html檔是這樣的::

	<div>
	<math xmlns="http://www.w3.org/1998/Math/MathML" mode="display"><mtable><mtr><mtd><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>a</mi></mrow></mfrac><mo>ln</mo><mo>(</mo><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>)</mo><mo>+</mo><mi>C</mi></mtd></mtr></mtable></math></div>

因此稍微看一下html原始碼就能知道是使用何者，很明顯的第1種顯示方式最簡單漂亮，花了一個晚上嘗試，發現在安裝doit，docutils，mako等套件時，不能使用官方的套件，必須使用從nikola下載的套件，因為他們有針對nikola修改，因此最保險的方法就是將官方套件一個個移除後，重新使用::

    sudo pip install https://github.com/ralsina/nikola/archive/master.zip --upgrade

--upgrade參數會一個個檢查子套件並更新；更新後，重build一次rst文件就能夠以第一種型式顯示數學式子，在Chrome裡也完全正常!!推測其他瀏覽器應該也是OK!

.. 文章結尾

.. 超連結(URL)目的區

.. _MathJax for Chrome: https://chrome.google.com/webstore/detail/mathjax-for-chrome/elbbpgnifnallkilnkofjcgjeallfcfa?hl=zh-TW

.. 註腳(Footnote)與引用(Citation)區

