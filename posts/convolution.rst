.. title: Convolution(摺積)的物理意義
.. slug: convolution
.. date: 2013-05-24 14:38:55
.. tags: mathjax
.. link: 
.. description: Created at 2013-05-24 13:37:06

.. 請記得加上slug，會以slug名稱產生副檔名為.html的文章
.. 同時，別忘了加上tags喔!

******************************************
Convolution(摺積)的物理意義
******************************************

.. 文章起始

========
問題
========

假設一個黑盒子(black box)是一個線性系統(LTI,Linear time invariant)，已知他的operator特性為\ :math:`g(t"), t"=0 \rightarrow \infty`\ ，亦即當我們用隨時間輸出的單位脈衝電流\ :math:`\delta(t")`\ 輸入這個black box(因為是單位脈衝unit impulse，所以每個脈衝大小均為1)，所量到的輸出對應電流即為\ :math:`g(t")`\ 。


.. 部落格分頁(Teaser)標籤
.. TEASER_END

現在我們已經知道這個黑盒子對時間的operator特性，如今我們要量測一個待測物體，他的輸入電流是\ :math:`f(\tau)`\ ，其中\ :math:`\tau=0\rightarrow t`\ 則他的輸出電流\ :math:`y(t)`\ 會是如何呢?

首先，線性系統在時間t前的輸出是具有疊加性的，也就是t時間前的電流輸出疊加起來，假設f的時間尺度0到t的t時剛好和g(t")的t"時相同，即t"=t，因此\ :math:`y(t)`\ 相當於在t"的時間\ :math:`(t-\tau)\rightarrow t`\ 的訊號疊加，因為f可能是從g的某一段插入進去的，因此以t=t"時為參考點倒推 ,在\ :math:`t"=t-\tau`\ 時的電流輸出應該為\ :math:`\delta(t")`\ 的\ :math:`f(\tau)g(t-\tau)\Delta\tau`\ 倍，也因為這個\ :math:`\Delta\tau`\ 的出現(即計算面積)，故回到t時間前的訊號疊加，可以寫成積分式

.. math::
   y(t)\equiv{f*g}=\int^{t}_{0}f(\tau)g(t-\tau)d\tau

由此可以知道convolution有moving integral的概念，同時也是藉由輸入單位衝量函數以預測一個線性系統下任意函數的輸出值!

f(t)與g(t)的convolution寫成f(t)*g(t)，其Fourier Transformation為其個別Fourier transformation的product

f(t)*g(t)==>Fourier Trans==>F(w)G(w)

===================
Convolution Theorem
===================

如果寫成\ :math:`Corr(f,g)\equiv \int^{t}_0 f(\tau+t)g(\tau)d\tau`\ 則為Correlation:

Corr(f,g)的Fourier Trans==>\ :math:`F(\omega)G^*(\omega)`\

===================
Correlation Theorem
===================

如果f=g就是autocorrelation
  
Corr(g,g)的Fourier Trans==>\ :math:`|G(\omega)|^2`\ ，即是Power Spectral Density(PSD)
        
=======================
Wiener-Khinchin Theorem
=======================

Parseval's theorem(怕什麼定理)說，對所有時域跟頻域的積分所得的total power應該要一樣。

即Total Power :math:`\equiv \int^{\infty}_{-\infty}|g(t)|^2 dt=\int^{\infty}_{-\infty}|G(\omega)|^2 d\omega`\ 。

大致上是這樣。

.. 文章結尾

.. 超連結(URL)目的區

.. 註腳(Footnote)與引用(Citation)區

