import cv2 as cv
import numpy as np
import collections

file_name = 'webcam_video.mp4'
fourcc = cv.VideoWriter_fourcc(*'mp4v')

webcam = cv.VideoCapture(0)

if webcam.isOpened():
    fps = webcam.get(cv.CAP_PROP_FPS) or 30  # FPS 기본값 설정
    wait_msec = int(1000 / fps)
    record = False
    blur_mode = False  # 블러 모드 ON/OFF
    blur_level = 5  # 블러 강도 (이전 프레임 개수)
    frame_queue = collections.deque(maxlen=blur_level)  # 이전 프레임 저장용 큐

    video_writer = None

    while True:
        valid, img = webcam.read()
        if not valid:
            break

        display_img = img.copy()

        # 블러 모드 적용
        if blur_mode and len(frame_queue) > 0:
            blended_img = np.mean(np.array(frame_queue), axis=0).astype(np.uint8)
            display_img = blended_img.copy()

        # 현재 프레임을 큐에 추가
        frame_queue.append(img)

        key = cv.waitKey(wait_msec) & 0xFF

        if key == ord(' '):  # Space 키로 녹화 시작/중지
            record = not record
            if record:
                if not video_writer:
                    h, w, _ = img.shape
                    video_writer = cv.VideoWriter(file_name, fourcc, fps, (w, h))
                print("🎥 녹화 시작")
            else:
                print("🛑 녹화 중지")

        elif key == 98:  # B 키로 블러 모드 ON/OFF
            blur_mode = not blur_mode
            frame_queue.clear()  # 모드 변경 시 프레임 초기화
            status = "ON" if blur_mode else "OFF"
            print(f"🔵 블러 모드: {status}")

        elif key == ord('['):  # [ 키로 블러 정도 감소
            if blur_level > 2:
                blur_level -= 1
                frame_queue = collections.deque(frame_queue, maxlen=blur_level)  # 프레임 개수 변경
                print(f"🔽 블러 강도 감소: {blur_level}")

        elif key == ord(']'):  # ] 키로 블러 정도 증가
            if blur_level < 10:
                blur_level += 1
                frame_queue = collections.deque(frame_queue, maxlen=blur_level)  # 프레임 개수 변경
                print(f"🔼 블러 강도 증가: {blur_level}")

        elif key == 27:  # ESC 키로 종료
            break

        if record:
            cv.circle(display_img, (50, 50), radius=30, color=(0, 0, 255), thickness=-1)
            video_writer.write(display_img)  # 블러 처리된 프레임을 녹화

        cv.imshow('Webcam', display_img)

    # 자원 해제
    webcam.release()
    if video_writer:
        video_writer.release()
    cv.destroyAllWindows()
    print("✅ 프로그램 종료 및 녹화 파일 저장")
