from pico2d import *

# 첫 번째 애니메이션: Energy_Wave.png
FIRST_SHEET = 'Energy_Wave.png'
FIRST_FRAME_WIDTH = 128
FIRST_FRAME_HEIGHT = 128
FIRST_NUM_FRAMES = 7

# 두 번째 애니메이션: Energy_Charge.png (첨부 이미지)
SECOND_SHEET = 'Light_Emission.png'
SECOND_FRAME_WIDTH = 128
SECOND_FRAME_HEIGHT = 128
SECOND_NUM_FRAMES = 5

# Teleport 애니메이션: 첨부한 두 파일 사용
TELEPORT_IN_SHEET = 'Teleport_Character_1.png'   # 텔레포트 등장 애니메이션
TELEPORT_OUT_SHEET = 'Teleport_Character_2.png'  # 텔레포트 퇴장 애니메이션
FRAME_WIDTH = 128
FRAME_HEIGHT = 128
NUM_FRAMES = 6

open_canvas()

SCALE = 1.5
CENTER_X, CENTER_Y = 400, 300

first = load_image(FIRST_SHEET)
second = load_image(SECOND_SHEET)
teleport_in = load_image(TELEPORT_IN_SHEET)
teleport_out = load_image(TELEPORT_OUT_SHEET)

while True:
    # 첫 번째 애니메이션 5회 반복
    for repeat in range(5):
        for frame in range(FIRST_NUM_FRAMES):
            clear_canvas()
            first.clip_draw(
                frame * FIRST_FRAME_WIDTH, 0, FIRST_FRAME_WIDTH, FIRST_FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(FIRST_FRAME_WIDTH * SCALE), int(FIRST_FRAME_HEIGHT * SCALE)
            )
            update_canvas()
            delay(0.12)
    delay(1.0)
    # 두 번째 애니메이션 5회 반복
    for repeat in range(5):
        for frame in range(SECOND_NUM_FRAMES):
            clear_canvas()
            second.clip_draw(
                frame * SECOND_FRAME_WIDTH, 0, SECOND_FRAME_WIDTH, SECOND_FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(SECOND_FRAME_WIDTH * SCALE), int(SECOND_FRAME_HEIGHT * SCALE)
            )
            update_canvas()
            delay(0.12)
    delay(1.0)
    # 텔레포트 등장-퇴장 애니메이션을 1회 이어서 실행
    for frame in range(NUM_FRAMES):
        clear_canvas()
        teleport_in.clip_draw(
            frame * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT,
            CENTER_X, CENTER_Y,
            int(FRAME_WIDTH * SCALE), int(FRAME_HEIGHT * SCALE)
        )
        update_canvas()
        delay(0.12)
    for frame in range(NUM_FRAMES):
        clear_canvas()
        teleport_out.clip_draw(
            frame * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT,
            CENTER_X, CENTER_Y,
            int(FRAME_WIDTH * SCALE), int(FRAME_HEIGHT * SCALE)
        )
        update_canvas()
        delay(0.12)
    delay(1.0)
    # 텔레포트 등장-퇴장 애니메이션을 4회 반복
    for repeat in range(4):
        for frame in range(NUM_FRAMES):
            clear_canvas()
            teleport_in.clip_draw(
                frame * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(FRAME_WIDTH * SCALE), int(FRAME_HEIGHT * SCALE)
            )
            update_canvas()
            delay(0.12)
        for frame in range(NUM_FRAMES):
            clear_canvas()
            teleport_out.clip_draw(
                frame * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(FRAME_WIDTH * SCALE), int(FRAME_HEIGHT * SCALE)
            )
            update_canvas()
            delay(0.12)
        delay(1.0)

close_canvas()

# 커멘트:
# - 첫 번째 애니메이션: Energy_Wave.png(7프레임)
# - 두 번째 애니메이션: Energy_Charge.png(5프레임)
# - 텔레포트 애니메이션: Teleport_Character_1.png(등장), Teleport_Character_2.png(퇴장) 사용
# - 각 애니메이션 5회 반복 후 1초 정지, 무한 반복
# - 캐릭터는 확대되어 중앙에 출력
# - 프레임 수/크기는 실제 이미지에 맞게 설정
