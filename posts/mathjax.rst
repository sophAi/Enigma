.. title: 測試mathjax與Latex數學
.. slug: mathjax
.. date: 2013-05-24 15:45:20
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

.. 文章結尾

.. 超連結(URL)目的區

.. 註腳(Footnote)與引用(Citation)區

