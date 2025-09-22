from pico2d import *

# 첫 번째 애니메이션: Energy_Wave.png (프레임마다 크기가 다른 sprite sheet)
FIRST_SHEET = 'Energy_Wave.png'
FIRST_FRAME_WIDTH = 128
FIRST_FRAME_HEIGHT = 128
FIRST_NUM_FRAMES = 7 # 이미지 기준 프레임 수
FIRST_FRAME_INFO = [
    {'x': i * FIRST_FRAME_WIDTH, 'y': 0, 'w': FIRST_FRAME_WIDTH, 'h': FIRST_FRAME_HEIGHT} for i in range(FIRST_NUM_FRAMES)
]
FIRST_SCALE_LIST = [0.5, 0.7, 1.0, 1.2, 1.5, 1.8, 2.0]  # 프레임별 커지는 효과

# 두 번째 애니메이션: Light_Emission.png
SECOND_SHEET = 'Light_Emission.png'
SECOND_FRAME_WIDTH = 128
SECOND_FRAME_HEIGHT = 128
SECOND_NUM_FRAMES = 5 # 이미지 기준 프레임 수

# Teleport 애니메이션: Teleport_Character_1.png, Teleport_Character_2.png, Teleport.png
TELEPORT_IN_SHEET = 'Teleport_Character_1.png'
TELEPORT_OUT_SHEET = 'Teleport_Character_2.png'
TELEPORT_FRAME_WIDTH = 128
TELEPORT_FRAME_HEIGHT = 128
TELEPORT_NUM_FRAMES = 6 # 이미지 기준 프레임 수
EFFECT_SHEET = 'Teleport.png'
EFFECT_FRAME_WIDTH = 100
EFFECT_FRAME_HEIGHT = 100
EFFECT_NUM_FRAMES = 16 # 이미지 기준 프레임 수

# 마지막 첨부 애니메이션: Attack_From_Cover.png
ATTACK_FROM_COVER_SHEET = 'Aerial_Strike.png'
ATTACK_FROM_COVER_FRAME_WIDTH = 128
ATTACK_FROM_COVER_FRAME_HEIGHT = 128
ATTACK_FROM_COVER_NUM_FRAMES = 9  # 이미지 기준 프레임 수

open_canvas(800, 600)

SCALE = 1.5
CENTER_X, CENTER_Y = 400, 300

first = load_image(FIRST_SHEET)
second = load_image(SECOND_SHEET)
teleport_in = load_image(TELEPORT_IN_SHEET)
teleport_out = load_image(TELEPORT_OUT_SHEET)
effect = load_image(EFFECT_SHEET)
attack_from_cover = load_image(ATTACK_FROM_COVER_SHEET)

while True:
    # 첫 번째 애니메이션 5회 반복 (프레임마다 크기가 같은 sprite sheet, SCALE로 커지는 효과)
    for repeat in range(5):
        for frame in range(FIRST_NUM_FRAMES):
            info = FIRST_FRAME_INFO[frame]
            scale = FIRST_SCALE_LIST[frame]
            clear_canvas()
            draw_x = CENTER_X - int((info['w'] * scale) // 2)
            draw_y = CENTER_Y - int((info['h'] * scale) // 2)
            first.clip_draw(
                info['x'], info['y'], info['w'], info['h'],
                draw_x + int((info['w'] * scale) // 2), draw_y + int((info['h'] * scale) // 2),
                int(info['w'] * scale), int(info['h'] * scale)
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
    for frame in range(TELEPORT_NUM_FRAMES):
        clear_canvas()
        teleport_in.clip_draw(
            frame * TELEPORT_FRAME_WIDTH, 0, TELEPORT_FRAME_WIDTH, TELEPORT_FRAME_HEIGHT,
            CENTER_X, CENTER_Y,
            int(TELEPORT_FRAME_WIDTH * SCALE), int(TELEPORT_FRAME_HEIGHT * SCALE)
        )
        effect_frame = int(frame * (EFFECT_NUM_FRAMES / TELEPORT_NUM_FRAMES))
        effect.clip_draw(
            effect_frame * EFFECT_FRAME_WIDTH, 0, EFFECT_FRAME_WIDTH, EFFECT_FRAME_HEIGHT,
            CENTER_X, CENTER_Y,
            int(EFFECT_FRAME_WIDTH * SCALE), int(EFFECT_FRAME_HEIGHT * SCALE)
        )
        update_canvas()
        delay(0.12)
    for frame in range(TELEPORT_NUM_FRAMES):
        clear_canvas()
        teleport_out.clip_draw(
            frame * TELEPORT_FRAME_WIDTH, 0, TELEPORT_FRAME_WIDTH, TELEPORT_FRAME_HEIGHT,
            CENTER_X, CENTER_Y,
            int(TELEPORT_FRAME_WIDTH * SCALE), int(TELEPORT_FRAME_HEIGHT * SCALE)
        )
        effect_frame = EFFECT_NUM_FRAMES - 1 - int(frame * (EFFECT_NUM_FRAMES / TELEPORT_NUM_FRAMES))
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
        for frame in range(TELEPORT_NUM_FRAMES):
            clear_canvas()
            teleport_in.clip_draw(
                frame * TELEPORT_FRAME_WIDTH, 0, TELEPORT_FRAME_WIDTH, TELEPORT_FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(TELEPORT_FRAME_WIDTH * SCALE), int(TELEPORT_FRAME_HEIGHT * SCALE)
            )
            effect_frame = int(frame * (EFFECT_NUM_FRAMES / TELEPORT_NUM_FRAMES))
            effect.clip_draw(
                effect_frame * EFFECT_FRAME_WIDTH, 0, EFFECT_FRAME_WIDTH, EFFECT_FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(EFFECT_FRAME_WIDTH * SCALE), int(EFFECT_FRAME_HEIGHT * SCALE)
            )
            update_canvas()
            delay(0.12)
        for frame in range(TELEPORT_NUM_FRAMES):
            clear_canvas()
            teleport_out.clip_draw(
                frame * TELEPORT_FRAME_WIDTH, 0, TELEPORT_FRAME_WIDTH, TELEPORT_FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(TELEPORT_FRAME_WIDTH * SCALE), int(TELEPORT_FRAME_HEIGHT * SCALE)
            )
            effect_frame = EFFECT_NUM_FRAMES - 1 - int(frame * (EFFECT_NUM_FRAMES / TELEPORT_NUM_FRAMES))
            effect.clip_draw(
                effect_frame * EFFECT_FRAME_WIDTH, 0, EFFECT_FRAME_WIDTH, EFFECT_FRAME_HEIGHT,
                CENTER_X, CENTER_Y - 100,
                int(EFFECT_FRAME_WIDTH * SCALE), int(EFFECT_FRAME_HEIGHT * SCALE)
            )
            update_canvas()
            delay(0.12)
        delay(1.0)
    # Attack_From_Cover 애니메이션 5회 반복
    for repeat in range(5):
        for frame in range(ATTACK_FROM_COVER_NUM_FRAMES):
            clear_canvas()
            attack_from_cover.clip_draw(
                frame * ATTACK_FROM_COVER_FRAME_WIDTH, 0, ATTACK_FROM_COVER_FRAME_WIDTH, ATTACK_FROM_COVER_FRAME_HEIGHT,
                CENTER_X, CENTER_Y,
                int(ATTACK_FROM_COVER_FRAME_WIDTH * SCALE), int(ATTACK_FROM_COVER_FRAME_HEIGHT * SCALE)
            )
            update_canvas()
            delay(0.12)
    delay(1.0)

close_canvas()
