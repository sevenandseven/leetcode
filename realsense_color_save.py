import pyrealsense2 as rs
import numpy as np
import cv2
import time
import os

def run():
    pipeline = rs.pipeline()

    #Create a config并配置要流​​式传输的管道
    config = rs.config()
    # config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

    align_to = rs.stream.color
    align = rs.align(align_to)

    # 按照日期创建文件夹
    # save_path = os.path.join(os.getcwd(), "out", time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
    # os.mkdir(save_path)
    save_path = r"E:\Project\shatong_jiance\SVM二分类\out"

    # 保存的图片和实时的图片界面
    cv2.namedWindow("live", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("save", cv2.WINDOW_AUTOSIZE)
    saved_count = 0

    pipeline.start(config)
    # 主循环
    try:
        while True:
            frames = pipeline.wait_for_frames()
            aligned_frames = align.process(frames)
            # 获取RGB图像
            color_frame = aligned_frames.get_color_frame()
            color_image = np.asanyarray(color_frame.get_data())
            # 获取深度图
            # aligned_depth_frame = aligned_frames.get_depth_frame()
            # depth_image = np.asanyarray(aligned_depth_frame.get_data()).astype(np.float32) / 1000.   # 单位为m
            # 可视化图像
            # depth_image = inpaint(depth_image)  # 补全缺失值
            # depth_image_color = depth2RGB(depth_image)
            cv2.imshow("live", color_image)
            key = cv2.waitKey(30)

            # s 保存图片
            if key & 0xFF == ord('s'):
                cv2.imwrite("{:04d}.jpg".format(saved_count+1), color_image)  # 保存RGB为png文件
                # imsave(os.path.join((save_path), "pcd{:04d}d.tiff".format(saved_count+1048)), depth_image)  # 保存深度图为tiff文件
                saved_count+=1
                cv2.imshow("save", color_image)

            # q 退出
            if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break
    finally:
        pipeline.stop()


if __name__ == '__main__':
    run()