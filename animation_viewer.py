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
EFFECT_SHEET = 'Teleport.png'  # 첨부 이펙트 애니메이션 시트
FRAME_WIDTH = 128
FRAME_HEIGHT = 128
NUM_FRAMES = 6
EFFECT_FRAME_WIDTH = 100
EFFECT_FRAME_HEIGHT = 100
EFFECT_NUM_FRAMES = 16

# 무기 소환 애니메이션: Weapon_Summon.png
WEAPON_SUMMON_SHEET = 'Weapon_Summon.png'  # 무기 소환 애니메이션 시트
WEAPON_1_SHEET = 'Weapon_3.png'            # 무기 이미지
WEAPON_SUMMON_FRAME_WIDTH = 128
WEAPON_SUMMON_FRAME_HEIGHT = 128
WEAPON_SUMMON_NUM_FRAMES = 8  # 예시: 8프레임 (이미지에 따라 조정)

open_canvas()

SCALE = 1.5
CENTER_X, CENTER_Y = 400, 300

first = load_image(FIRST_SHEET)
second = load_image(SECOND_SHEET)
teleport_in = load_image(TELEPORT_IN_SHEET)
teleport_out = load_image(TELEPORT_OUT_SHEET)
effect = load_image(EFFECT_SHEET)
weapon_summon = load_image(WEAPON_SUMMON_SHEET)
weapon_1 = load_image(WEAPON_1_SHEET)

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
    # 텔레포트 등장-퇴장 애니메이션을 1회 이어서 실행 (이펙트 오버레이)
    for frame in range(NUM_FRAMES):
        clear_canvas()
        teleport_in.clip_draw(
            frame * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT,
            CENTER_X, CENTER_Y,
            int(FRAME_WIDTH * SCALE), int(FRAME_HEIGHT * SCALE)
        )
        # 이펙트 애니메이션 오버레이 (프레임에 맞춰서)
        effect_frame = int(frame * (EFFECT_NUM_FRAMES / NUM_FRAMES))
        effect.clip_draw(
            effect_frame * EFFECT_FRAME_WIDTH, 0, EFFECT_FRAME_WIDTH, EFFECT_FRAME_HEIGHT,
            CENTER_X, CENTER_Y,
            int(EFFECT_FRAME_WIDTH * SCALE), int(EFFECT_FRAME_HEIGHT * SCALE)
        )
        update_canvas()
        delay(0.12)
    for frame in range(NUM_FRAMES):
        clear_canvas()
        teleport_out.clip_draw(
            frame * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT,
            CENTER_X, CENTER_Y ,
            int(FRAME_WIDTH * SCALE), int(FRAME_HEIGHT * SCALE)
        )
        # 이펙트 애니메이션 오버레이 (역방향)
        effect_frame = EFFECT_NUM_FRAMES - 1 - int(frame * (EFFECT_NUM_FRAMES / NUM_FRAMES))
        effect.clip_draw(
            effect_frame * EFFECT_FRAME_WIDTH, 0, EFFECT_FRAME_WIDTH, EFFECT_FRAME_HEIGHT,
            CENTER_X, CENTER_Y - 100,
            int(EFFECT_FRAME_WIDTH * SCALE), int(EFFECT_FRAME_HEIGHT * SCALE)
        )
        update_canvas()
        delay(0.12)
    delay(1.0)
    # 텔레포트 등장-퇴장 애니메이션을 4회 반복 (이펙트 오버레이)
    for repeat in range(4):
        for frame in range(NUM_FRAMES):
            clear_canvas()
            teleport_in.clip_draw(
                frame * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(FRAME_WIDTH * SCALE), int(FRAME_HEIGHT * SCALE)
            )
            effect_frame = int(frame * (EFFECT_NUM_FRAMES / NUM_FRAMES))
            effect.clip_draw(
                effect_frame * EFFECT_FRAME_WIDTH, 0, EFFECT_FRAME_WIDTH, EFFECT_FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(EFFECT_FRAME_WIDTH * SCALE), int(EFFECT_FRAME_HEIGHT * SCALE)
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
            effect_frame = EFFECT_NUM_FRAMES - 1 - int(frame * (EFFECT_NUM_FRAMES / NUM_FRAMES))
            effect.clip_draw(
                effect_frame * EFFECT_FRAME_WIDTH, 0, EFFECT_FRAME_WIDTH, EFFECT_FRAME_HEIGHT,
                CENTER_X, CENTER_Y - 100,
                int(EFFECT_FRAME_WIDTH * SCALE), int(EFFECT_FRAME_HEIGHT * SCALE)
            )
            update_canvas()
            delay(0.12)
        delay(1.0)
    # 무기 소환 애니메이션 5회 반복 (속도 느리게)
    for repeat in range(5):
        for frame in range(WEAPON_SUMMON_NUM_FRAMES):
            clear_canvas()
            # 무기 소환 애니메이션 프레임 출력
            weapon_summon.clip_draw(
                frame * WEAPON_SUMMON_FRAME_WIDTH, 0, WEAPON_SUMMON_FRAME_WIDTH, WEAPON_SUMMON_FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(WEAPON_SUMMON_FRAME_WIDTH * SCALE), int(WEAPON_SUMMON_FRAME_HEIGHT * SCALE)
            )
            # 무기 이미지(Weapon_1.png)는 소환 마지막 프레임에만 오버레이
            if frame == WEAPON_SUMMON_NUM_FRAMES - 1:
                weapon_1.draw(
                    CENTER_X, CENTER_Y + 40,
                    int(WEAPON_SUMMON_FRAME_WIDTH * SCALE), int(WEAPON_SUMMON_FRAME_HEIGHT * SCALE)
                )
            update_canvas()
            delay(0.25)  # 기존 0.12에서 0.25로 느리게 변경
    delay(1.0)

close_canvas()
