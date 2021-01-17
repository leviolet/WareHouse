import numpy  as np
import cv2

src         = cv2.imread("./src.png"     , cv2.IMREAD_GRAYSCALE)
flag        = cv2.imread("./flag.png"    , cv2.IMREAD_GRAYSCALE)

fftsrc      = np.fft.fft2(src)         # 频域

# 获取中点 xc,yc
center = np.asarray(src.shape, dtype=int) / 2
xc,yc = center
xc,yc = int(xc),int(yc)

# 写入flag
for i in range(flag.shape[0]) :
    for j in range(flag.shape[1]):
        fftsrc[xc+i][yc+j] +=  10**(abs(flag[i][j]) / 40) 
        fftsrc[xc-i][yc-j] +=  10**(abs(flag[i][j]) / 40) 
        # 保证隐写后频谱仍然对称，这样逆变换后不会出现虚部，从而能正常显示图片

result      = np.fft.ifft2(fftsrc)     # 反变换结果

cv2.imwrite("./question.png"     ,np.real(result))

# 频谱
#fftsrcshift = np.log (abs(np.fft.fftshift(fftsrc))) * 20
# spectrum   = np.log (abs(fftsrc)) * 20
# cv2.imwrite("./answer.png",spectrum)
# cv2.imwrite("./question_real.png",np.real(result))
# cv2.imwrite("./question_imag.png",np.imag(result))