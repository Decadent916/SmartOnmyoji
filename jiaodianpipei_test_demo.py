import numpy as np
import cv2
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10

img1 = cv2.imread('img/adb_img/yuhun/3.jpg', 1)
img2 = cv2.imread('screen_img/screen_pic.jpg', 1)

# 使用SIFT检测角点
# sift = cv2.xfeatures2d.SIFT_create()
sift = cv2.SIFT_create()
# 获取关键点和描述符
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# 定义FLANN匹配器
index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
# 使用KNN算法匹配
matches = flann.knnMatch(des1, des2, k=2)

# 去除错误匹配
good = []
for m, n in matches:
    if m.distance <= 0.7 * n.distance:
        good.append(m)

# 单应性
if len(good) > MIN_MATCH_COUNT:
    # 改变数组的表现形式，不改变数据内容，数据内容是每个关键点的坐标位置
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    # findHomography 函数是计算变换矩阵
    # 参数cv2.RANSAC是使用RANSAC算法寻找一个最佳单应性矩阵H，即返回值M
    # 返回值：M 为变换矩阵，mask是掩模
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    # ravel方法将数据降维处理，最后并转换成列表格式
    matchesMask = mask.ravel().tolist()
    # 获取img1的图像尺寸
    h, w, dim = img1.shape
    # pts是图像img1的四个顶点
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    # 计算变换后的四个顶点坐标位置
    dst = cv2.perspectiveTransform(pts, M)

    # 根据四个顶点坐标位置在img2图像画出变换后的边框
    img2 = cv2.polylines(img2, [np.int32(dst)], True, (0, 0, 255), 3, cv2.LINE_AA)

else:
    # print("Not enough matches are found - %d/%d") % (len(good), MIN_MATCH_COUNT)
    matchesMask = None

# 显示匹配结果
draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                   singlePointColor=None,
                   matchesMask=matchesMask,  # draw only inliers
                   flags=2)
img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)
plt.figure(figsize=(20, 20))
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.show()




# import cv2
# import os
# from matplotlib import pyplot as plt
#
#
# def FLANN():
#     # flags=0
#     # 灰色读入目标图像
#     targetPath = r'\img\pc_img\yuhun\end_win_0.jpg'
#     trainingImage = cv2.imread(targetPath, flags=0)
#     # 灰色读所有模板图片
#     templatePath = 'screen_img/'
#     icons = os.listdir(templatePath)
#     iconMatch = dict({'name': '未识别', 'value': 0})
#     for icon in icons:
#         queryImage = cv2.imread(templatePath + icon, 0)
#         # 使用SIFT 检测角点
#         sift = cv2.SIFT_create()
#         kp1, des1 = sift.detectAndCompute(queryImage, None)
#         kp2, des2 = sift.detectAndCompute(trainingImage, None)
#         # 设置FLANN匹配器参数，定义FLANN匹配器，使用 KNN 算法实现匹配
#         indexParams = dict(algorithm=0, trees=5)
#         searchParams = dict(checks=50)
#         flann = cv2.FlannBasedMatcher(indexParams, searchParams)
#         matches = flann.knnMatch(des1, des2, k=2)
#
#         # 根据matches生成相同长度的matchesMask列表，列表元素为[0,0]
#         matchesMask = [[0, 0] for i in range(len(matches))]
#         matchNumber = 0
#         # 去除错误匹配, 此处阈值设定为0.7
#         for i, (m, n) in enumerate(matches):
#             if m.distance < 0.7 * n.distance:
#                 matchesMask[i] = [1, 0]
#                 matchNumber = matchNumber + 1
#
#         # 将图像显示
#         # matchColor是两图的匹配连接线，连接线与matchesMask相关
#         # singlePointColor是勾画关键点
#         drawParams = dict(matchColor=(0, 255, 0), matchesMask=matchesMask[:50], flags=0)
#         resultImage = cv2.drawMatchesKnn(queryImage, kp1, trainingImage, kp2, matches[:50], None, **drawParams)
#
#         if matchNumber > iconMatch['value']:
#             iconMatch['name'] = icon.split('_')[0]
#             iconMatch['value'] = matchNumber
#
#     return resultImage, iconMatch
#
#
# if __name__ == '__main__':
#     resultImage, res = FLANN()
#     plt.imshow(resultImage)
#     plt.show()