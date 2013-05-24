.. title: 使用mathjax與Latex數學
.. slug: mathjax
.. date: 2013-05-24 20:14:21
.. tags: mathjax
.. link: 
.. description: Created at 2013-05-24 13:45:28

.. 請記得加上slug，會以slug名稱產生副檔名為.html的文章
.. 同時，別忘了加上tags喔!

************
mathjax測試
************

.. 文章起始

只要記得在tags裡加入mathjax即可自動載入mathjax JAVA scripts。

例如::

    The first equation using mathjax is as following :math:`\alpha=\beta+\gamma`

會顯示 
    
The first equation using mathjax is as following :math:`\alpha=\beta+\gamma`

或是使用以下語法::

    .. math::
      
       \int \frac{dx}{1+ax}=\frac{1}{a}\ln(1+ax)+C

則如下

.. math::

   \int \frac{dx}{1+ax}=\frac{1}{a}\ln(1+ax)+C

可惜的是Vst (VIM)還無法支援，轉PDF時的數學式子方案還要再研究一下。

FireFox原生支援MathJax所使用的MathML，但是無論其他瀏覽器就沒有，以至於數學式子只有FireFox表現最為正常，在Google Chrome還沒原生支援MathML之前，請先安裝\ `MathJax for Chrome`_\ ,就可以正常顯示數學式子了，IE，safari, opera的使用者可能就得多擔待一下，目前知道，如果要在所有的瀏覽器正常使用MathJax，則html必須包含::

	<div class="math">
	\begin{equation*}
	\int \frac{dx}{1+ax}=\frac{1}{a}\ln(1+ax)+C
	\end{equation*}
	</div>

這段，而我所產生的html檔裡，卻是這樣::

	<div>
	<math xmlns="http://www.w3.org/1998/Math/MathML" mode="display"><mtable><mtr><mtd><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>a</mi></mrow></mfrac><mo>ln</mo><mo>(</mo><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>)</mo><mo>+</mo><mi>C</mi></mtd></mtr></mtable></math></div>

這就是問題所在，問題應該是出在template與生成mathjax程式碼的區塊，很明顯的也是第1種顯示方式最簡單漂亮，總之我會找時間解決這個問題。

.. 文章結尾

.. 超連結(URL)目的區

.. _MathJax for Chrome: https://chrome.google.com/webstore/detail/mathjax-for-chrome/elbbpgnifnallkilnkofjcgjeallfcfa?hl=zh-TW

.. 註腳(Footnote)與引用(Citation)區

