from pico2d import *

# Energy_Wave.png 파일만 사용하여 애니메이션 실행
CHARACTER_SHEET = 'Energy_Wave.png'  # 캐릭터 애니메이션 시트
CHARACTER_FRAME_WIDTH = 128
CHARACTER_FRAME_HEIGHT = 128
CHARACTER_NUM_FRAMES = 7  # 첨부 이미지 기준 프레임 수

open_canvas()

SCALE = 1.5
CENTER_X, CENTER_Y = 400, 300

character = load_image(CHARACTER_SHEET)

while True:
    # 캐릭터 애니메이션 5회 반복
    for repeat in range(5):
        for frame in range(CHARACTER_NUM_FRAMES):
            clear_canvas()
            character.clip_draw(
                frame * CHARACTER_FRAME_WIDTH, 0, CHARACTER_FRAME_WIDTH, CHARACTER_FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(CHARACTER_FRAME_WIDTH * SCALE), int(CHARACTER_FRAME_HEIGHT * SCALE)
            )
            update_canvas()
            delay(0.12)
    delay(1.0)

close_canvas()

# 커멘트:
# - Energy_Wave.png 파일만 사용
# - 캐릭터 애니메이션 7프레임 반복
# - 5회 반복 후 1초 정지, 무한 반복
# - 캐릭터는 확대되어 중앙에 출력
# - 프레임 수/크기는 실제 이미지에 맞게 설정
