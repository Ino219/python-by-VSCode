import numpy as np
import cv2
from matplotlib import pyplot as plt

#画像の読み込み
#カラー
img=cv2.imread("c56.jpg")
#グレースケール
#img=cv2.imread("c56.jpg",0)
#BGRからRGBへ変換し、正しいカラーで表示されるようにする
img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#画像の表示
#ウィンドウをサイズ変更可能に
#cv2.namedWindow("img",cv2.WINDOW_NORMAL)
#グレースケールでの表示
#plt.imshow(img,cmap='gray',interpolation='bicubic')
#カラー表示
plt.imshow(img2,interpolation='bicubic')
#画像の周囲の目盛りを表示するかどうかの指定
plt.xticks([]),plt.yticks([])
#表示
plt.show()
#cv2でのキーイベントと画像表示
"""cv2.imshow("img",img)
k=cv2.waitKey(0)&0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("new56.png",img)
    cv2.destroyWindow("img")"""
"""mat = np.random.rand(10, 10)

fig, ax = plt.subplots()
ax.matshow(mat)

plt.show()"""