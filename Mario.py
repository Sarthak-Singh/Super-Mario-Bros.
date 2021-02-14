# ===================================================================================================================== #
# ===========================================IMPORTS AND ASSIGNMENTS=================================================== #
# ===================================================================================================================== #

import pygame
import os
import sys

pygame.init()

# Display Window
win = pygame.display.set_mode((320, 224), pygame.FULLSCREEN)
pygame.display.set_caption('Super Mario Bros.')

# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------MARIO IMAGES-------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #

# background
bg = pygame.image.load(os.path.join('Images', 'World', 'World.png'))

# Mario Walk
walkLeftM1 = [pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1walking1.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1walking2.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1walking3.png'))]
walkLeftM2 = [pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2walking1.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2walking2.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2walking3.png'))]
walkLeftM3 = [pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3walking1.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3walking2.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3walking3.png'))]
walkLeftM4 = [pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4walking1.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4walking2.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4walking3.png'))]
walkRightM1 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1walking1.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1walking2.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1walking3.png'))]
walkRightM2 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2walking1.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2walking2.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2walking3.png'))]
walkRightM3 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3walking1.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3walking2.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3walking3.png'))]
walkRightM4 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4walking1.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4walking2.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4walking3.png'))]

# Mario Jump
jump_L_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1jumping.png'))
jump_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2jumping.png'))
jump_L_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3jumping.png'))
jump_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4jumping.png'))
jump_R_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1jumping.png'))
jump_R_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2jumping.png'))
jump_R_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3jumping.png'))
jump_R_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4jumping.png'))

# Mario Standing
stand_L_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1standing.png'))
stand_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2standing.png'))
stand_L_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3standing.png'))
stand_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4standing.png'))
stand_R_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1standing.png'))
stand_R_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2standing.png'))
stand_R_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3standing.png'))
stand_R_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4standing.png'))

# Mario Face_Switch
face_switch_L_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1switch.png'))
face_switch_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2switch.png'))
face_switch_L_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3switch.png'))
face_switch_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4switch.png'))
face_switch_R_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1switch.png'))
face_switch_R_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2switch.png'))
face_switch_R_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3switch.png'))
face_switch_R_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4switch.png'))

# Mario Death
death_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Mid', '1', '1death.png'))
death_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Mid', '3', '3death.png'))

# Mario Duck
duck_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2duck.png'))
duck_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4duck.png'))
duck_R_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2duck.png'))
duck_R_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4duck.png'))

# Mario Smaller
smaller_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2smaller.png'))
smaller_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4smaller.png'))
smaller_R_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2smaller.png'))
smaller_R_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4smaller.png'))

# Mario Flag Rappelling
rappelling_L_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'flag', 'l1flag1.png'))
rappelling_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'flag', 'l2flag1.png'))
rappelling_L_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'flag', 'l3flag1.png'))
rappelling_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'flag', 'l4flag1.png'))
rappelling_R_M1 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'flag', 'r1flag1.png')),
                   pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'flag', 'r1flag2.png'))]
rappelling_R_M2 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'flag', 'r2flag1.png')),
                   pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'flag', 'r2flag2.png'))]
rappelling_R_M3 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'flag', 'r3flag1.png')),
                   pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'flag', 'r3flag2.png'))]
rappelling_R_M4 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'flag', 'r4flag1.png')),
                   pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'flag', 'r4flag2.png'))]

# Mario Shooting
walkLeftM4_s = [pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'shoot', 'l4swalking1.png')),
                pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'shoot', 'l4swalking2.png')),
                pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'shoot', 'l4swalking3.png'))]
walkRightM4_s = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'shoot', 'r4swalking1.png')),
                 pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'shoot', 'r4swalking2.png')),
                 pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'shoot', 'r4swalking3.png'))]

jump_L_M4_s = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'shoot', 'l4sjumping.png'))
jump_R_M4_s = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'shoot', 'r4sjumping.png'))

face_switch_L_M4_s = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'shoot', 'l4sswitch.png'))
face_switch_R_M4_s = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'shoot', 'r4sswitch.png'))

# Mario Bullets
bullets = [pygame.image.load(os.path.join('Images', 'Items', 'Mario Bullets', 'b1.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'Mario Bullets', 'b2.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'Mario Bullets', 'b3.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'Mario Bullets', 'b4.png'))]

b_hits = [pygame.image.load(os.path.join('Images', 'Items', 'Bullet hit', 'bh1.png')),
          pygame.image.load(os.path.join('Images', 'Items', 'Bullet hit', 'bh2.png')),
          pygame.image.load(os.path.join('Images', 'Items', 'Bullet hit', 'bh3.png'))]

# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------ITEMS IMAGES------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #

# pipes
pipes = [pygame.image.load(os.path.join('Images', 'Items', 'pipes', 'p1.png')),
         pygame.image.load(os.path.join('Images', 'Items', 'pipes', 'p2.png')),
         pygame.image.load(os.path.join('Images', 'Items', 'pipes', 'p3.png'))]

# floor block
floor_blocks = pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'floor_block.png'))

# brick
bricks = pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'brick_block.png'))
brick_break_pieces = [pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'brick_block_break_p1.png')),
                      pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'brick_block_break_p2.png')),
                      pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'brick_block_break_p3.png')),
                      pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'brick_block_break_p4.png'))]

# mystery boxes
mystery_boxes = [pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'coin_box_1.png')),
                 pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'coin_box_2.png')),
                 pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'coin_box_3.png'))]

# empty box
empty_box = pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'empty_box.png'))

# coins
coins_i = [pygame.image.load(os.path.join('Images', 'Items', 'coins', 'coin_1.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'coins', 'coin_2.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'coins', 'coin_3.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'coins', 'coin_4.png'))]

# mushroom
mushroom = pygame.image.load(os.path.join('Images', 'Items', 'mushroom', 'mushroom.png'))

# 1up mushroom
l_mushroom = pygame.image.load(os.path.join('Images', 'Items', '1up', '1up.png'))

# flower
flowers = [pygame.image.load(os.path.join('Images', 'Items', 'flower', 'flower_1.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'flower', 'flower_2.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'flower', 'flower_3.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'flower', 'flower_4.png'))]

# flag
pole_i = pygame.image.load(os.path.join('Images', 'Items', 'flags', 'pole.png'))
cloth_i = pygame.image.load(os.path.join('Images', 'Items', 'flags', 'flag.png'))
victory_flag = pygame.image.load(os.path.join('Images', 'Items', 'flags', 'victory_flag.png'))

# castle
castle = pygame.image.load(os.path.join('Images', 'Items', 'castle', 'castle1.png'))

# --------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------SCREENS' IMAGES------------------------------------------------------ #
# --------------------------------------------------------------------------------------------------------------------- #

# Title for start_screen
title = pygame.image.load(os.path.join('Images', 'Title Screen', 'name.png'))

# Controls
ctrls = pygame.image.load(os.path.join('Images', 'Controls', 'Controls2.png'))

# Keys for start_screen
ctrls_i = pygame.image.load(os.path.join('Images', 'Title Screen', 'I2.png'))
play_enter = pygame.image.load(os.path.join('Images', 'Title Screen', 'Enter2.png'))

# Heading coin
t_coins_i = [pygame.image.load(os.path.join('Images', 'Items', 'coins', 'title coin icon', 't_coin_1.png')),
             pygame.image.load(os.path.join('Images', 'Items', 'coins', 'title coin icon', 't_coin_2.png')),
             pygame.image.load(os.path.join('Images', 'Items', 'coins', 'title coin icon', 't_coin_3.png'))]

# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------ENEMY IMAGES------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #

# goomba
goomba = [pygame.image.load(os.path.join('Images', 'Enemies', 'goomba', 'g1.png')),
          pygame.image.load(os.path.join('Images', 'Enemies', 'goomba', 'g2.png'))]
inv_goomba = pygame.transform.rotate(goomba[0], 180)
squished_goomba = pygame.image.load(os.path.join('Images', 'Enemies', 'goomba', 'dead.png'))

# koopa troopa
koopa_troopa_L = [pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'l1.png')),
                  pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'l2.png'))]
koopa_troopa_R = [pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'r1.png')),
                  pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'r2.png'))]
koopa_troopa_shell = [pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'shell_mid.png')),
                     pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'shell.png'))]
inv_koopa_troopa = pygame.transform.rotate(koopa_troopa_shell[1], 180)

# --------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------SOUNDS---------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #

# Sounds
s_1up = pygame.mixer.Sound(os.path.join('Sounds', '1-up.wav'))
s_breakblock = pygame.mixer.Sound(os.path.join('Sounds', 'breakblock.wav'))
s_bump = pygame.mixer.Sound(os.path.join('Sounds', 'bump.wav'))
s_coin = pygame.mixer.Sound(os.path.join('Sounds', 'coin.wav'))
s_fireball = pygame.mixer.Sound(os.path.join('Sounds', 'fireball.wav'))
s_flagpole = pygame.mixer.Sound(os.path.join('Sounds', 'flagpole.wav'))
s_gameover = pygame.mixer.Sound(os.path.join('Sounds', 'gameover.wav'))
s_jump_small = pygame.mixer.Sound(os.path.join('Sounds', 'jump-small.wav'))
s_jump_big = pygame.mixer.Sound(os.path.join('Sounds', 'jump-super.wav'))
s_kick = pygame.mixer.Sound(os.path.join('Sounds', 'kick.wav'))
s_mario_die = pygame.mixer.Sound(os.path.join('Sounds', 'mario-die.wav'))
s_pause = pygame.mixer.Sound(os.path.join('Sounds', 'pause.wav'))
s_powerdown = pygame.mixer.Sound(os.path.join('Sounds', 'powerdown.wav'))
s_powerup = pygame.mixer.Sound(os.path.join('Sounds', 'powerup.wav'))
s_powerup_appears = pygame.mixer.Sound(os.path.join('Sounds', 'powerup_appears.wav'))
s_stage_clear = pygame.mixer.Sound(os.path.join('Sounds', 'stage_clear.wav'))
s_stomp = pygame.mixer.Sound(os.path.join('Sounds', 'stomp.wav'))
s_warning = pygame.mixer.Sound(os.path.join('Sounds', 'warning.wav'))
s_world_clear = pygame.mixer.Sound(os.path.join('Sounds', 'world_clear.wav'))

# Theme
music = pygame.mixer.music.load(os.path.join('Sounds', 'Theme.mp3'))

# --------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------OTHERS---------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #

# Fonts
f_text = pygame.font.Font('Font.ttf', 16)
f_sign = pygame.font.Font('Font.ttf', 10)
f_points = pygame.font.Font('Font.ttf', 9)

# Parameters
bgX = 0
f_1_3 = 185                     # floor level - height for 1 & 3
f_2_4 = 169                     # floor level - height for 2 & 4
ground_level = 200
color = (255, 255, 255)
score = 0
coins = 0
time = 400
high_score = 0
pygame.mixer.music.play(-1)

# Clock
clock = pygame.time.Clock()


# ===================================================================================================================== #
# ===================================================CLASSES=========================================================== #
# ===================================================================================================================== #

# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------PIPE CLASS--------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class pipe:
    def __init__(self, x, level):
        self.x = x
        self.y = 168
        self.width = 32
        self.height = 32
        self.level = level
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        if self.level == 1:
            self.y = 168
            self.height = 32
            win.blit(pipes[0], (self.x + bgX, self.y))
        if self.level == 2:
            self.y = 152
            self.height = 48
            win.blit(pipes[1], (self.x + bgX, self.y))
        if self.level == 3:
            self.y = 136
            self.height = 64
            win.blit(pipes[2], (self.x + bgX, self.y))
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)


# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------HOLE CLASS--------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #

class hole:
    def __init__(self, x, width):
        self.x = x
        self.width = width


# --------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------FLOOR BLOCK CLASS----------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class floor_block:
    def __init__(self, x, y, hb):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.hb = hb
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(floor_blocks, (self.x + bgX, self.y))
        if self.hb == 1:
            self.hitBox = (self.x + bgX, self.y, self.width, self.height)
        elif self.hb == 4:
            self.hitBox = (self.x + bgX, self.y, self.width, self.height*4)
        elif self.hb == 8:
            self.hitBox = (self.x + bgX, self.y, self.width, self.height*8)
        #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)


# --------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------BRICK BLOCK CLASS----------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class brick:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.type = type
        self.empty = False
        self.coin_counter = 10
        self.block_push = False
        self.push_count = 4
        self.broken = False
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        if not self.broken and not self.type == 'c':
            win.blit(bricks, (self.x + bgX, self.y))
            self.hitBox = (self.x + bgX, self.y, self.width, self.height)
        if self.type == 'c':
            self.hitBox = (self.x + bgX, self.y, self.width, self.height)
            if not self.empty:
                win.blit(bricks, (self.x + bgX, self.y))
            else:
                win.blit(empty_box, (self.x + bgX, self.y))
        #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)


class broken_brick:
    def __init__(self, x, y, piece):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8
        self.piece = piece
        if self.piece == 0 or self.piece == 1:
            self.fall_u = 8
        elif self.piece == 2 or self.piece == 3:
            self.fall_u = 6
        self.fall_lr = 5
        self.fall_d = 4

    def draw(self, win):
        win.blit(brick_break_pieces[self.piece], (self.x + bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------MYSTERY BOX CLASS----------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class mystery_box:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.type = type
        self.empty = False
        self.block_push = False
        self.push_count = 3
        self.timer = 0
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)
        if not self.empty:
            if self.timer + 1 >= 45:
                self.timer = 0
            if self.timer <= 25:
                win.blit(mystery_boxes[0], (self.x + bgX, self.y))
            elif 25 < self.timer <= 35:
                win.blit(mystery_boxes[1], (self.x + bgX, self.y))
            elif 35 < self.timer <= 45:
                win.blit(mystery_boxes[2], (self.x + bgX, self.y))
            self.timer += 1
        else:
            win.blit(empty_box, (self.x + bgX, self.y))
        #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)


# --------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------INVISIBLE BOX CLASS---------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class invisible_box:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.type = type
        self.empty = False
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)
        if self.empty:
            win.blit(empty_box, (self.x + bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------FLAG CLASSES------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class pole:
    def __init__(self):
        self.x = 3173
        self.y = 32
        self.height = 152
        self. width = 8
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(pole_i, (self.x + bgX, self.y))
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)


class cloth:
    def __init__(self):
        self.x = 3160
        self.y = 40
        self.height = 16
        self. width = 16
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(cloth_i, (self.x + bgX, self.y))
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)


# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------CASTLE CLASS------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Castle:
    def __init__(self):
        self.x = 3232
        self.y = 120

    def draw(self, win):
        win.blit(castle, (self.x + bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------VIC FLAG CLASS------------------------------------------------------ #
# --------------------------------------------------------------------------------------------------------------------- #


class v_Flag:
    def __init__(self):
        self.x = 3264
        self.y = 125

    def draw(self, win):
        win.blit(victory_flag, (self.x + bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------COIN CLASS-------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 0
        self.jump_h = 9

    def draw(self, win):
        if self.timer + 1 >= 24:
            self.timer = 0
        win.blit(coins_i[self.timer//6], (self.x + bgX, self.y))
        self.timer += 1


class title_Coin:
    def __init__(self):
        self.x = 118
        self.y = 21
        self.timer = 0

    def draw(self, win):
        if self.timer + 1 >= 45:
            self.timer = 0
        if self.timer <= 25:
            win.blit(t_coins_i[0], (self.x, self.y))
        elif 25 < self.timer <= 35:
            win.blit(t_coins_i[1], (self.x, self.y))
        elif 35 < self.timer <= 45:
            win.blit(t_coins_i[2], (self.x, self.y))
        self.timer += 1


# --------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------MUSHROOM CLASS------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Mushroom:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.rise = True
        self.dir = 1
        self.switch = False
        self.fall_count = 1
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)
        win.blit(mushroom, (self.x + bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------1UP MUSHROOM CLASS---------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class L_Mushroom:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.rise = True
        self.fall_count = 1
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)
        win.blit(l_mushroom, (self.x + bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------FLOWER CLASS-------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Flower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.rise = True
        self.timer = 0
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)
        if self.timer + 1 >= 36:
            self.timer = 0
        win.blit(flowers[self.timer//9], (self.x + bgX, self.y))
        self.timer += 1


# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------BULLET CLASS-------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Bullet:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 9
        self.dir = dir
        self.bounce_h = 7
        self.bounce = False
        self.hit = False
        self.timer_b = 0
        self.timer_h = 0
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        if not self.hit:
            if self.timer_b >= 36:
                self.timer_b = 0
            win.blit(bullets[self.timer_b//9], (self.x + bgX, self.y))
            self.timer_b += 1
            self.hitBox = (self.x + bgX, self.y, self.width, self.height)
        else:
            if self.timer_h < 26:
                self.timer_h += 1
                if 0 <= self.timer_h < 9:
                    win.blit(b_hits[0], (self.x + bgX, self.y))
                elif 9 <= self.timer_h < 18:
                    win.blit(b_hits[1], (self.x - 2 + bgX, self.y - 3))
                elif 18 <= self.timer_h < 26:
                    win.blit(b_hits[2], (self.x - 4 + bgX, self.y - 4))


# --------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------GOOMBA CLASS------------------------------------------------------ #
# --------------------------------------------------------------------------------------------------------------------- #


class Goomba:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.move = False
        self.dir = -1
        self.switch = False
        self.fall_count = 1
        self.walkCount = 0
        self.hit = False
        self.squished = False
        self.dis_time = 0
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        if not self.hit and not self.squished:
            if self.walkCount + 1 >= 30:
                self.walkCount = 0
            win.blit(goomba[self.walkCount//15], (self.x + bgX, self.y))
            self.walkCount += 1
            self.hitBox = (self.x + bgX, self.y, self.width, self.height)
        else:
            if self.squished:
                win.blit(squished_goomba, (self.x + bgX, self.y))
            elif self.hit:
                win.blit(inv_goomba, (self.x + bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------KOOPA TROOPA CLASS--------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Koopa_Troopa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 24
        self.move = False
        self.dir = -1
        self.switch = False
        self.fall_count = 1
        self.walkCount = 0
        self.hit = False
        self.hole_coll = False
        self.shell = False
        self.shell_tr_timer = 0
        self.shell_stop = False
        self.shell_slide = False
        self.goom_domino = 0
        self.dis_time = 0
        self.hitBox = (self.x + bgX, self.y, self.width, self.height)

    def draw(self, win):
        if not self.hit and not self.shell:
            if self.walkCount + 1 >= 30:
                self.walkCount = 0
            win.blit(koopa_troopa_L[self.walkCount//15], (self.x + bgX, self.y))
            self.walkCount += 1
            self.hitBox = (self.x + bgX, self.y, self.width, self.height)
        else:
            self.hitBox = (self.x + bgX, self.y, self.width, 16)
            if self.shell and not self.hit:
                if self.shell_tr_timer <= 10:
                    win.blit(koopa_troopa_shell[0], (self.x + bgX, self.y + 1))
                    self.shell_tr_timer += 1
                else:
                    win.blit(koopa_troopa_shell[1], (self.x + bgX, self.y + 1))
            elif self.hit:
                win.blit(inv_koopa_troopa, (self.x + bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------MARIO CLASS-------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Mario:
    def __init__(self):
        self.x = 40
        self.y = 185
        self.width = 16
        self.height = 17
        self.ground_level = 185
        self.vel = 2.6
        self.pot_en = 0
        self.walkCount = 0
        self.jump_count_up = 10
        self.jump_count_down = 0
        self.falling_count = 1
        self.level = 1
        self.lives = 3
        self.face_switch_timer = 0
        self.grow_time = 0
        self.shrink_time = 0
        self.blink_timer = 0
        self.squish_streak = 0
        self.rap_count = 0
        self.right = True
        self.left = False
        self.standing = True
        self.collide_l = False
        self.collide_r = False
        self.game_over = False
        self.death = False
        self.hole_falling = False
        self.reset = False
        self.face_switch = False
        self.isJump = False
        self.duck = False
        self.grow = False
        self.shrink = False
        self.blink = False
        self.shoot = False
        self.rappelling = False
        self.rap_switch = False
        self.end_jump = False
        self.end_walk = False
        self.end_m = False
        self.dis = False
        self.hitBox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.rap_count + 1 >= 20:
            self.rap_count = 0

        if self.level == 1 or self.level == 3:
            self.ground_level = f_1_3
            if not self.isJump and self.pot_en == 0 and not self.death and not self.hole_falling and not self.end_m:
                self.y = f_1_3
            self.width = 16
            self.height = 17
            self.hitBox = (self.x, self.y, self.width, self.height - 1)
        else:
            self.ground_level = f_2_4
            if not self.isJump and self.pot_en == 0 and not self.hole_falling and not self.end_m:
                self.y = f_2_4
            self.width = 16
            self.height = 32
            self.hitBox = (self.x, self.y, self.width, self.height)

        if self.level == 1:
            if self.grow:
                if self.grow_time <= 100:
                    if self.left:
                        if 0 < self.grow_time <= 20 or 40 < self.grow_time <= 60 or 80 < self.grow_time <= 100:
                            win.blit(smaller_L_M2, (self.x, self.y - 16))
                        if 20 < self.grow_time <= 40 or 60 < self.grow_time <= 80:
                            win.blit(stand_L_M2, (self.x, self.y - 16))
                    elif self.right:
                        if 0 < self.grow_time <= 20 or 40 < self.grow_time <= 60 or 80 < self.grow_time <= 100:
                            win.blit(smaller_R_M2, (self.x, self.y - 16))
                        if 20 < self.grow_time <= 40 or 60 < self.grow_time <= 80:
                            win.blit(stand_R_M2, (self.x, self.y - 16))
                    self.grow_time += 2.5
                else:
                    self.level += 1
                    self.y -= 16
                    self.grow_time = 0
                    self.grow = False
            if self.rappelling:
                win.blit(rappelling_R_M1[self.rap_count//10], (self.x, self.y))
                self.rap_count += 1
            elif self.end_m:
                if not self.rap_switch:
                    win.blit(rappelling_R_M1[0], (self.x, self.y))
                else:
                    if not self.end_jump and not self.end_walk:
                        win.blit(rappelling_L_M1, (self.x, self.y))
                    else:
                        if not self.end_walk:
                            win.blit(jump_L_M1, (self.x, self.y))
                        else:
                            win.blit(walkRightM1[self.walkCount // 6], (self.x, self.y))
                            self.walkCount += 1
            else:
                if self.death:
                    win.blit(death_M1, (self.x, self.y))
                elif self.isJump and not self.grow:
                    if self.left:
                        win.blit(jump_L_M1, (self.x, self.y))
                    elif self.right:
                        win.blit(jump_R_M1, (self.x, self.y))
                else:
                    if not self.standing:
                        if self.face_switch and self.left:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_R_M1, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        elif self.face_switch and self.right:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_L_M1, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        if not self.face_switch:
                            if self.left:
                                win.blit(walkLeftM1[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                            elif self.right:
                                win.blit(walkRightM1[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                    elif not self.grow:
                        if self.right:
                            win.blit(stand_R_M1, (self.x, self.y))
                        else:
                            win.blit(stand_L_M1, (self.x, self.y))

        if self.level == 2:
            if self.shrink:
                if self.shrink_time <= 100:
                    if self.left:
                        if 0 < self.shrink_time <= 20 or 40 < self.shrink_time <= 60 or 80 < self.shrink_time <= 100:
                            win.blit(smaller_L_M2, (self.x, self.y))
                        if 20 < self.shrink_time <= 40 or 60 < self.shrink_time <= 80:
                            win.blit(stand_L_M1, (self.x, self.y + 16))
                    elif self.right:
                        if 0 < self.shrink_time <= 20 or 40 < self.shrink_time <= 60 or 80 < self.shrink_time <= 100:
                            win.blit(smaller_R_M2, (self.x, self.y))
                        if 20 < self.shrink_time <= 40 or 60 < self.shrink_time <= 80:
                            win.blit(stand_R_M1, (self.x, self.y + 16))
                    self.shrink_time += 3
                else:
                    self.level -= 1
                    self.y += 16
                    self.shrink_time = 0
                    self.shrink = False
            if self.rappelling:
                win.blit(rappelling_R_M2[self.rap_count//10], (self.x, self.y))
                self.rap_count += 1
            elif self.end_m:
                if not self.rap_switch:
                    win.blit(rappelling_R_M2[0], (self.x, self.y))
                else:
                    if not self.end_jump and not self.end_walk:
                        win.blit(rappelling_L_M2, (self.x, self.y))
                    else:
                        if not self.end_walk:
                            win.blit(jump_L_M2, (self.x, self.y))
                        else:
                            win.blit(walkRightM2[self.walkCount // 6], (self.x, self.y))
                            self.walkCount += 1
            else:
                if self.isJump and not self.duck:
                    if self.left:
                        win.blit(jump_L_M2, (self.x, self.y))
                    elif self.right:
                        win.blit(jump_R_M2, (self.x, self.y))
                elif not self.isJump and not self.duck:
                    if not self.standing:
                        if self.face_switch and self.left:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_R_M2, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        elif self.face_switch and self.right:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_L_M2, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        if not self.face_switch:
                            if self.left:
                                win.blit(walkLeftM2[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                            elif self.right:
                                win.blit(walkRightM2[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                    elif not self.shrink:
                        if self.right:
                            win.blit(stand_R_M2, (self.x, self.y))
                        else:
                            win.blit(stand_L_M2, (self.x, self.y))
                if self.duck:
                    self.standing = False
                    if self.left:
                        win.blit(duck_L_M2, (self.x, self.y))
                    elif self.right:
                        win.blit(duck_R_M2, (self.x, self.y))
                    self.duck = False

        if self.level == 3:
            if self.rappelling:
                win.blit(rappelling_R_M3[self.rap_count//10], (self.x, self.y))
                self.rap_count += 1
            elif self.end_m:
                if not self.rap_switch:
                    win.blit(rappelling_R_M3[0], (self.x, self.y))
                else:
                    if not self.end_jump and not self.end_walk:
                        win.blit(rappelling_L_M3, (self.x, self.y))
                    else:
                        if not self.end_walk:
                            win.blit(jump_L_M3, (self.x, self.y))
                        else:
                            win.blit(walkRightM3[self.walkCount // 6], (self.x, self.y))
                            self.walkCount += 1
            else:
                if self.death:
                    win.blit(death_M3, (self.x, self.y))
                elif self.isJump:
                    if self.left:
                        win.blit(jump_L_M3, (self.x, self.y))
                    elif self.right:
                        win.blit(jump_R_M3, (self.x, self.y))
                else:
                    if not self.standing:
                        if self.face_switch and self.left:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_R_M3, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        elif self.face_switch and self.right:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_L_M3, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        if not self.face_switch:
                            if self.left:
                                win.blit(walkLeftM3[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                            elif self.right:
                                win.blit(walkRightM3[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                    else:
                        if self.right:
                            win.blit(stand_R_M3, (self.x, self.y))
                        else:
                            win.blit(stand_L_M3, (self.x, self.y))

        if self.level == 4:
            if self.shrink:
                if self.shrink_time <= 100:
                    if self.left:
                        if 0 < self.shrink_time <= 20 or 40 < self.shrink_time <= 60 or 80 < self.shrink_time <= 100:
                            win.blit(smaller_L_M4, (self.x, self.y))
                        if 20 < self.shrink_time <= 40 or 60 < self.shrink_time <= 80:
                            win.blit(stand_L_M3, (self.x, self.y + 16))
                    elif self.right:
                        if 0 < self.shrink_time <= 20 or 40 < self.shrink_time <= 60 or 80 < self.shrink_time <= 100:
                            win.blit(smaller_R_M4, (self.x, self.y))
                        if 20 < self.shrink_time <= 40 or 60 < self.shrink_time <= 80:
                            win.blit(stand_R_M3, (self.x, self.y + 16))
                    self.shrink_time += 3
                else:
                    self.level -= 1
                    self.y += 16
                    self.shrink_time = 0
                    self.shrink = False
            if self.rappelling:
                win.blit(rappelling_R_M4[self.rap_count//10], (self.x, self.y))
                self.rap_count += 1
            elif self.end_m:
                if not self.rap_switch:
                    win.blit(rappelling_R_M4[0], (self.x, self.y))
                else:
                    if not self.end_jump and not self.end_walk:
                        win.blit(rappelling_L_M4, (self.x, self.y))
                    else:
                        if not self.end_walk:
                            win.blit(jump_L_M4, (self.x, self.y))
                        else:
                            win.blit(walkRightM4[self.walkCount // 6], (self.x, self.y))
                            self.walkCount += 1
            else:
                if self.isJump and not self.duck:
                    if self.left:
                        if self.shoot:
                            for x in range(300):
                                win.blit(jump_L_M4_s, (self.x, self.y))
                                pygame.display.update()
                            self.shoot = False
                        else:
                            win.blit(jump_L_M4, (self.x, self.y))
                    elif self.right:
                        if self.shoot:
                            for x in range(300):
                                win.blit(jump_R_M4_s, (self.x, self.y))
                                pygame.display.update()
                            self.shoot = False
                        else:
                            win.blit(jump_R_M4, (self.x, self.y))
                elif not self.isJump and not self.duck:
                    if not self.standing:
                        if self.face_switch and self.left:
                            if self.face_switch_timer + 1 <= 6:
                                if self.shoot:
                                    win.blit(face_switch_R_M4_s, (self.x, self.y))
                                else:
                                    win.blit(face_switch_R_M4, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                                self.shoot = False
                        elif self.face_switch and self.right:
                            if self.face_switch_timer + 1 <= 6:
                                if self.shoot:
                                    win.blit(face_switch_L_M4_s, (self.x, self.y))
                                else:
                                    win.blit(face_switch_L_M4, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                                self.shoot = False
                        if not self.face_switch:
                            if self.left:
                                if self.shoot:
                                    for x in range(200):
                                        win.blit(walkLeftM4_s[self.walkCount // 6], (self.x, self.y))
                                        pygame.display.update()
                                    self.shoot = False
                                else:
                                    win.blit(walkLeftM4[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                            elif self.right:
                                if self.shoot:
                                    for x in range(200):
                                        win.blit(walkRightM4_s[self.walkCount // 6], (self.x, self.y))
                                        pygame.display.update()
                                    self.shoot = False
                                else:
                                    win.blit(walkRightM4[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                    elif not self.shrink:
                        if self.right:
                            if self.shoot:
                                for x in range(500):
                                    win.blit(walkRightM4_s[2], (self.x, self.y))
                                    pygame.display.update()
                                self.shoot = False
                            else:
                                win.blit(stand_R_M4, (self.x, self.y))
                        else:
                            if self.shoot:
                                for x in range(500):
                                    win.blit(walkLeftM4_s[2], (self.x, self.y))
                                    pygame.display.update()
                                self.shoot = False
                            else:
                                win.blit(stand_L_M4, (self.x, self.y))
                if self.duck:
                    self.standing = False
                    if self.left:
                        win.blit(duck_L_M4, (self.x, self.y))
                    elif self.right:
                        win.blit(duck_R_M4, (self.x, self.y))
                    self.duck = False
        #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)

    def land(self, obj):
        self.pot_en = obj.hitBox[3]
        if self.hitBox[1] + self.hitBox[3] > obj.hitBox[1]:
            if self.level == 1 or self.level == 3:
                self.y = obj.hitBox[1] - self.height + 1
            else:
                self.y = obj.hitBox[1] - self.height
            self.collide_r = False
            self.collide_l = False
            self.isJump = False
            self.standing = True
            self.jump_count_up = 10
            self.jump_count_down = 0

    def collide(self, obj):
        if obj.hitBox[0] < self.hitBox[0] < obj.hitBox[0] + obj.hitBox[2]:
            self.collide_l = True
        elif obj.hitBox[0] + obj.hitBox[2] > self.hitBox[0] + self.hitBox[2] > obj.hitBox[0]:
            self.collide_r = True

    def fall(self):
        if self.pot_en and not self.isJump:
            if self.y < self.ground_level:
                self.y += (self.falling_count ** 2) / 10
                self.falling_count += 0.5
            else:
                self.pot_en = 0
                self.falling_count = 1

    def enemy_damage(self):
        if self.level == 1 or self.level == 3:
            s_mario_die.play()
            self.death = True
        elif self.level == 2 or self.level == 4:
            self.shrink = True

    def squish_jump(self):
        self.pot_en = 0
        self.isJump = True
        self.jump_count_up = 5
        self.jump_count_down = 0
        self.falling_count = 1


# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------POINTS TEXT CLASS-------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Points:
    def __init__(self, x, y, amount):
        self.x = x
        self.y = y
        self.amount = amount
        self.timer = 0

    def draw(self, win):
        if self.amount is not flag_score:
            win.blit(f_points.render(str(self.amount), 1, color), (self.x, self.y))
        else:
            win.blit(f_points.render(str(self.amount), 1, color), (self.x + bgX, self.y))


# ===================================================================================================================== #
# ======================================================FUNCTIONS====================================================== #
# ===================================================================================================================== #

# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------START PAGE FUNCTION------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


def start_page():
    # background
    win.blit(bg, (0, 0))

    # headings
    win.blit(text_mario, (40, 4))
    win.blit(text_score, (40, 15))
    t_c.draw(win)
    win.blit(text_x, (125, 15))
    win.blit(text_coins, (133, 15))
    win.blit(text_world, (172, 4))
    win.blit(text_world_c, (181, 15))
    win.blit(text_time, (240, 4))
    #win.blit(text_time_c, (248, 15))

    # title
    win.blit(title, (70, 30))

    # sign
    win.blit(text_sign, (75, 115))

    # keys
    win.blit(play_enter, (90, 130))
    win.blit(ctrls_i, (108, 151))

    # instruction text
    win.blit(text_start, (172, 130))
    win.blit(text_controls, (160, 150))

    # top score texts
    win.blit(text_top, (103, 170))
    win.blit(text_high_score, (169, 170))

    # player
    player.draw(win)

    # controls
    if controls:
        win.blit(ctrls, (28, 10))

    pygame.display.update()


# --------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------LOADING PAGE FUNCTION------------------------------------------------ #
# --------------------------------------------------------------------------------------------------------------------- #


def load_page():
    # background
    win.fill((0, 0, 0))

    # headings
    win.blit(text_mario, (40, 4))
    win.blit(text_score, (40, 15))
    t_c.draw(win)
    win.blit(text_x, (125, 15))
    win.blit(text_coins, (133, 15))
    win.blit(text_world, (172, 4))
    win.blit(text_world_c, (181, 15))
    win.blit(text_time, (240, 4))
    # win.blit(text_time_c, (248, 15))

    # mid texts
    win.blit(text_world, (106, 70))
    win.blit(text_world_c, (162, 70))

    # mario
    win.blit(stand_R_M1, (115, 100))

    # bottom texts
    win.blit(text_x, (142, 99))
    win.blit(text_lives, (170, 100))

    pygame.display.update()


# --------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------TIME UP PAGE FUNCTION------------------------------------------------ #
# --------------------------------------------------------------------------------------------------------------------- #


def time_up_page():
    # background
    win.fill((0, 0, 0))

    # headings
    win.blit(text_mario, (40, 4))
    win.blit(text_score, (40, 15))
    t_c.draw(win)
    win.blit(text_x, (125, 15))
    win.blit(text_coins, (133, 15))
    win.blit(text_world, (172, 4))
    win.blit(text_world_c, (181, 15))
    win.blit(text_time, (240, 4))
    # win.blit(text_time_c, (248, 15))

    # main text
    win.blit(text_time_up, (125, 100))

    pygame.display.update()


# --------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------GAME OVER PAGE FUNCTION----------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


def game_over_page():
    # background
    win.fill((0, 0, 0))

    # headings
    win.blit(text_mario, (40, 4))
    win.blit(text_score, (40, 15))
    t_c.draw(win)
    win.blit(text_x, (125, 15))
    win.blit(text_coins, (133, 15))
    win.blit(text_world, (172, 4))
    win.blit(text_world_c, (181, 15))
    win.blit(text_time, (240, 4))
    # win.blit(text_time_c, (248, 15))

    # main text
    win.blit(text_game_over, (115, 100))

    # new high score
    if score > high_score and player.x - bgX > 3173:
        win.blit(text_new_high_score, (94, new_high_height))

    pygame.display.update()


# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------MAIN REDRAW FUNCTION------------------------------------------------ #
# --------------------------------------------------------------------------------------------------------------------- #


def redrawWindow():
    # background
    win.blit(bg, (bgX, 0))

    # headings
    win.blit(text_mario, (40, 4))
    win.blit(text_score, (40, 15))
    t_c.draw(win)
    win.blit(text_x, (125, 15))
    win.blit(text_coins, (133, 15))
    win.blit(text_world, (172, 4))
    win.blit(text_world_c, (181, 15))
    win.blit(text_time, (240, 4))
    win.blit(text_time_c, (248, 15))

    # mushroom
    for x in m:
        x.draw(win)

    # 1up mushroom
    for x in lm:
        x.draw(win)

    # flower
    for x in f:
        x.draw(win)

    # Goombas
    for x in g:
        x.draw(win)

    # Koopa Troopas
    for x in kt:
        x.draw(win)

    # pipes
    for x in p:
        x.draw(win)

    # floor blocks
    for x in fb:
        x.draw(win)

    # brick blocks
    for x in bb:
        x.draw(win)
    for x in broken_bs:
        x.draw(win)

    # mystery boxes
    for x in mb:
        x.draw(win)

    # invisible box
    ib.draw(win)

    # coins
    for x in c:
        x.draw(win)

    # flag
    f_p.draw(win)
    f_c.draw(win)

    # victory flag
    f_v.draw(win)

    # castle
    cas.draw(win)

    # bullets
    for x in bul:
        x.draw(win)

    # points
    for x in pts:
        x.draw(win)

    # player
    if not player.dis:
        player.draw(win)

    pygame.display.update()


# --------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------INITIALIZATION FUNCTION---------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


def initialize():

    global player, bb, mb, ib, f_p, f_c, f_v, g, kt, run_inertia, flag_score, rap_start_timer, rap_switch_timer, \
        end_jump_timer, end_jump_impulse, v_flag_timer, bgX, score, coins, time

    # ------------------------------------------------INSTANCES------------------------------------------------------- #

    # Mario
    player = Mario()
    player.lives = 3
    player.level = 1
    player.dis = False
    player.x = 40
    player.y = 185
    player.pot_en = 0

    # Brick_Blocks
    bb = [brick(321, 136, 'n'), brick(353, 136, 'n'), brick(385, 136, 'n'), brick(1233, 136, 'n'), brick(1265, 136, 'n'),
          brick(1281, 72, 'n'), brick(1297, 72, 'n'), brick(1313, 72, 'n'), brick(1329, 72, 'n'), brick(1345, 72, 'n'),
          brick(1361, 72, 'n'), brick(1377, 72, 'n'), brick(1393, 72, 'n'), brick(1457, 72, 'n'), brick(1473, 72, 'n'),
          brick(1489, 72, 'n'), brick(1505, 136, 'c'), brick(1601, 136, 'n'), brick(1617, 136, 'n'), brick(1889, 136, 'n'),
          brick(1937, 72, 'n'), brick(1953, 72, 'n'), brick(1969, 72, 'n'), brick(2049, 72, 'n'), brick(2065, 136, 'n'),
          brick(2081, 136, 'n'), brick(2097, 72, 'n'), brick(2689, 136, 'n'), brick(2705, 136, 'n'), brick(2737, 136, 'n')]

    # Mystery boxes
    mb = [mystery_box(257, 136, 'c'), mystery_box(337, 136, 'p'), mystery_box(353, 72, 'c'), mystery_box(369, 136, 'c'),
          mystery_box(1249, 136, 'p'), mystery_box(1505, 72, 'c'), mystery_box(1697, 136, 'c'), mystery_box(1745, 72, 'p'),
          mystery_box(1745, 136, 'c'), mystery_box(1793, 136, 'c'), mystery_box(2065, 72, 'c'), mystery_box(2081, 72, 'c'),
          mystery_box(2721, 136, 'c')]

    # Invisible box
    ib = invisible_box(1025, 120, 'l')

    # Flag
    f_p = pole()
    f_c = cloth()

    # Victory Flag
    f_v = v_Flag()

    # Goombas
    g = [Goomba(353, 184), Goomba(641, 184), Goomba(817, 184), Goomba(841, 184), Goomba(1281, 56), Goomba(1313, 56),
         Goomba(1553, 184), Goomba(1577, 184), Goomba(1825, 184), Goomba(1849, 184), Goomba(1985, 184), Goomba(2009, 184),
         Goomba(2049, 184), Goomba(2073, 184), Goomba(2769, 184), Goomba(2793, 184)]

    # Koopa Troopas
    kt = [Koopa_Troopa(1713, 176)]

    # ------------------------------------------------VARIABLES------------------------------------------------------- #

    run_inertia = 0

    # end actions'
    flag_score = 0
    rap_start_timer = 0
    rap_switch_timer = 0
    end_jump_timer = 0
    end_jump_impulse = 2
    v_flag_timer = 0

    # master
    bgX = 0
    score = 0
    coins = 0
    time = 400
    pygame.mixer.music.load(os.path.join('Sounds', 'Theme.mp3'))


# ===================================================================================================================== #
# ====================================================INITIAL SETTINGS================================================= #
# ===================================================================================================================== #

# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------INSTANCES----------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #

# Mario
player = Mario()

# Bullets
bul = []

# Pipes
p = [pipe(449, 1), pipe(609, 2), pipe(737, 3), pipe(913, 3), pipe(2609, 1), pipe(2865, 1)]

# Holes
h = [hole(1103.5, 32.5), hole(1375.5, 48), hole(2447.5, 32.5)]

# Floor_Blocks
fb = [floor_block(2145, 184, 1), floor_block(2161, 168, 1), floor_block(2177, 152, 1), floor_block(2193, 136, 4),
      floor_block(2193, 152, 1), floor_block(2193, 168, 1), floor_block(2193, 184, 1), floor_block(2241, 184, 1),
      floor_block(2241, 168, 1), floor_block(2241, 152, 1), floor_block(2241, 136, 4), floor_block(2257, 152, 1),
      floor_block(2273, 168, 1), floor_block(2289, 184, 1), floor_block(2369, 184, 1), floor_block(2385, 168, 1),
      floor_block(2401, 152, 1), floor_block(2417, 136, 1), floor_block(2433, 136, 4), floor_block(2433, 152, 1),
      floor_block(2433, 168, 1), floor_block(2433, 184, 1), floor_block(2481, 184, 1), floor_block(2481, 168, 1),
      floor_block(2481, 152, 1), floor_block(2481, 136, 4), floor_block(2497, 152, 1), floor_block(2513, 168, 1),
      floor_block(2529, 184, 1), floor_block(2896, 184, 1), floor_block(2912, 168, 1), floor_block(2928, 152, 1),
      floor_block(2944, 136, 1), floor_block(2960, 120, 1), floor_block(2976, 104, 1), floor_block(2992, 88, 1),
      floor_block(3008, 72, 1), floor_block(3024, 72, 8), floor_block(3024, 88, 1), floor_block(3024, 104, 1),
      floor_block(3024, 120, 1), floor_block(3024, 136, 1), floor_block(3024, 152, 1), floor_block(3024, 168, 1),
      floor_block(3024, 184, 1), floor_block(3168, 184, 1)]

# Brick_Blocks
bb = [brick(321, 136, 'n'), brick(353, 136, 'n'), brick(385, 136, 'n'), brick(1233, 136, 'n'), brick(1265, 136, 'n'),
      brick(1281, 72, 'n'), brick(1297, 72, 'n'), brick(1313, 72, 'n'), brick(1329, 72, 'n'), brick(1345, 72, 'n'),
      brick(1361, 72, 'n'), brick(1377, 72, 'n'), brick(1393, 72, 'n'), brick(1457, 72, 'n'), brick(1473, 72, 'n'),
      brick(1489, 72, 'n'), brick(1505, 136, 'c'), brick(1601, 136, 'n'), brick(1617, 136, 'n'), brick(1889, 136, 'n'),
      brick(1937, 72, 'n'), brick(1953, 72, 'n'), brick(1969, 72, 'n'), brick(2049, 72, 'n'), brick(2065, 136, 'n'),
      brick(2081, 136, 'n'), brick(2097, 72, 'n'), brick(2689, 136, 'n'), brick(2705, 136, 'n'), brick(2737, 136, 'n')]

broken_bs = []

# Mystery boxes
mb = [mystery_box(257, 136, 'c'), mystery_box(337, 136, 'p'), mystery_box(353, 72, 'c'), mystery_box(369, 136, 'c'),
      mystery_box(1249, 136, 'p'), mystery_box(1505, 72, 'c'), mystery_box(1697, 136, 'c'), mystery_box(1745, 72, 'p'),
      mystery_box(1745, 136, 'c'), mystery_box(1793, 136, 'c'), mystery_box(2065, 72, 'c'), mystery_box(2081, 72, 'c'),
      mystery_box(2721, 136, 'c')]

# Invisible box
ib = invisible_box(1025, 120, 'l')

# Coins
c = []
t_c = title_Coin()

# Mushroom
m = []

# 1up Mushroom
lm = []

# Flower
f = []

# Flag
f_p = pole()
f_c = cloth()

# Castle
cas = Castle()

# Victory Flag
f_v = v_Flag()

# Goombas
g = [Goomba(353, 184), Goomba(641, 184), Goomba(817, 184), Goomba(841, 184), Goomba(1281, 56), Goomba(1313, 56),
     Goomba(1553, 184), Goomba(1577, 184), Goomba(1825, 184), Goomba(1849, 184), Goomba(1985, 184), Goomba(2009, 184),
     Goomba(2049, 184), Goomba(2073, 184), Goomba(2769, 184), Goomba(2793, 184)]

# Koopa Troopas
kt = [Koopa_Troopa(1713, 176)]

# Points
pts = []

# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------VARIABLES----------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #

# mario movement
run_inertia = 0

# mario deaths
death_height_count_up = 3
death_height_count_down = 0
hole_fall_height_count = 5
fall_timer = 0
time_up_fall = False

# for regulating bullets
bullet_buff = 0

# for referencing last mystery box
v_m = v_f = 1

# end actions'
flag_score = 0
rap_start_timer = 0
rap_switch_timer = 0
end_jump_timer = 0
end_jump_impulse = 2
v_flag_timer = 0
end_timer = 0

# universal constant texts
text_mario = f_text.render('MARIO', 1, color)
text_x = f_text.render('x', 1, color)
text_world = f_text.render('WORLD', 1, color)
text_world_c = f_text.render('1-1', 1, color)
text_time = f_text.render('TIME', 1, color)

text_pause = f_text.render('PAUSED', 1, color)

text_game_over = f_text.render('GAME OVER', 1, color)

text_time_up = f_text.render('TIME UP', 1, color)

text_new_high_score = f_text.render('NEW HIGH SCORE', 1, color)

# for start page
start_pg = True
controls = False
text_controls = f_text.render('CONTROLS', 1, color)
text_start = f_text.render('START', 1, color)
text_top = f_text.render('TOP -', 1, color)
text_sign = f_sign.render('By - Sarthak Singh aka GHOST', 1, (0, 0, 0))

# for loading pages
load = False
game_over = False
time_up = False
hold_timer = 0
new_high_height = 220

# for main loop
time_regulator = 0
speed = 65                              # fps
pause = False                           # for pausing
run = True
warning = False
warning_timer = 0


# ===================================================================================================================== #
# ===================================================MAIN LOOP========================================================= #
# ===================================================================================================================== #

while run:

    # ----------------------------------------UNIVERSAL CHANGING TEXTS------------------------------------------------ #

    text_score = f_text.render(str(score).zfill(6), 1, color)
    text_coins = f_text.render(str(coins).zfill(2), 1, color)
    text_time_c = f_text.render(str(time).zfill(3), 1, color)
    text_lives = f_text.render(str(player.lives), 1, color)
    text_high_score = f_text.render(str(high_score).zfill(6), 1, color)

    # ----------------------------------------------START LOOP-------------------------------------------------------- #

    while start_pg:
        pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    start_pg = False
                    load = True
                if event.key == pygame.K_i:
                    if not controls:
                        controls = True
                    else:
                        controls = False
        start_page()
        clock.tick(speed)

    # ----------------------------------------------PAUSE LOOP-------------------------------------------------------- #

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_p:
                    s_pause.play()
                    pause = False
        win.blit(text_pause, (132, 100))
        pygame.display.update()
        clock.tick(speed)

    # -----------------------------------------------TIME UP LOOP----------------------------------------------------- #

    if player.y >= 220:
        pygame.mixer.music.stop()
        while time_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            if hold_timer + 1 <= 200:
                hold_timer += 1
            else:
                time_up = False
                time = 400
                hold_timer = 0
            time_up_page()
            clock.tick(speed)

    # ---------------------------------------------------------------------------------------------------------------- #

    if player.game_over and player.y > 224 and not time_up:
        game_over = True
        s_gameover.play()
    if player.game_over and player.end_m:
        game_over = True
        if score > high_score:
            s_world_clear.play()

    # -----------------------------------------------GAME OVER LOOP--------------------------------------------------- #

    while game_over:
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if hold_timer + 1 <= 500:
            hold_timer += 1
            if score > high_score and player.x - bgX > 3173:
                new_high_height -= 0.2
        else:
            if score > high_score:
                high_score = score
            game_over = False
            new_high_height = 220
            initialize()
            start_pg = True
            hold_timer = 0
        game_over_page()
        clock.tick(speed)

    # ---------------------------------------------LOADING LOOP------------------------------------------------------- #

    while load:
        pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if hold_timer + 1 <= 150:
            hold_timer += 1
        else:
            load = False
            hold_timer = 0
        load_page()
        clock.tick(speed)

    # ----------------------------------------------THEME MUSIC------------------------------------------------------- #

    if not warning:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.play()
    else:
        if warning_timer + 1 <= 200:
            warning_timer += 1
        else:
            warning_timer = 0
            pygame.mixer.music.unpause()
            warning = False

    # --------------------------------ACTIVATION RANGE FROM INSTANTANEOUS POSITION------------------------------------ #

    x = 0                                                                           # #################
    if player.hitBox[0] + player.hitBox[2] - bgX < 490:                                               #
        x = 0                                                                                         #
    elif 600 < player.hitBox[0] + player.hitBox[2] - bgX < 680:                                       #
        x = 1                                                                                         #
    elif 720 < player.hitBox[0] + player.hitBox[2] - bgX < 800:                                       #
        x = 2                                                                                         # ####### for pipes
    elif 900 < player.hitBox[0] + player.hitBox[2] - bgX < 960:                                       #
        x = 3                                                                                         #
    elif 2590 < player.hitBox[0] + player.hitBox[2] - bgX < 2660:                                     #
        x = 4                                                                                         #
    elif 2800 < player.hitBox[0] + player.hitBox[2] - bgX < 2915:                                     #
        x = 5                                                                       # #################

    y = 0                                                                           # #################
    if player.hitBox[0] + player.hitBox[2] - bgX < 1150:                                              #
        y = 0                                                                                         #
    elif 1200 < player.hitBox[0] + player.hitBox[2] - bgX < 1500:                                     # ###### for holes
        y = 1                                                                                         #
    elif 2400 < player.hitBox[0] + player.hitBox[2] - bgX:                                            #
        y = 2                                                                       # #################

    z = 0                                                                           # #################
    if player.hitBox[0] + player.hitBox[2] - bgX < 2161:                                              #
        z = 0                                                                                         #
    elif 2161 < player.hitBox[0] + player.hitBox[2] - bgX < 2177:                                     #
        z = 1                                                                                         #
    elif 2177 < player.hitBox[0] + player.hitBox[2] - bgX < 2193:                                     #
        z = 2                                                                                         #
    elif 2193 < player.hitBox[0] + player.hitBox[2] - bgX < 2229:                                     #
        z = 3                                                                                         #
    elif 2241 < player.hitBox[0] - bgX < 2257:                                                        #
        z = 10                                                                                        #
    elif 2241 < player.hitBox[0] + player.hitBox[2] - bgX < 2257:                                     #
        z = 10                                                                                        #
    elif 2257 < player.hitBox[0] - bgX < 2273:                                                        #
        z = 11                                                                                        #
    elif 2273 < player.hitBox[0] - bgX < 2289:                                                        #
        z = 12                                                                                        #
    elif 2289 < player.hitBox[0] - bgX < 2310:                                                        #
        z = 13                                                                                        #
    elif 2365 < player.hitBox[0] + player.hitBox[2] - bgX < 2385:                                     #
        z = 14                                                                                        #
    elif 2385 < player.hitBox[0] + player.hitBox[2] - bgX < 2401:                                     #
        z = 15                                                                                        #
    elif 2401 < player.hitBox[0] + player.hitBox[2] - bgX < 2417:                                     #
        z = 16                                                                                        #
    elif 2417 < player.hitBox[0] + player.hitBox[2] - bgX < 2433:                                     #
        z = 17                                                                                        # ###### for floor blocks
    elif 2433 < player.hitBox[0] + player.hitBox[2] - bgX < 2465:                                     #
        z = 18                                                                                        #
    elif 2481 < player.hitBox[0] - bgX < 2497:                                                        #
        z = 25                                                                                        #
    elif 2481 < player.hitBox[0] + player.hitBox[2] - bgX < 2497:                                     #
        z = 25                                                                                        #
    elif 2497 < player.hitBox[0] - bgX < 2513:                                                        #
        z = 26                                                                                        #
    elif 2513 < player.hitBox[0] - bgX < 2529:                                                        #
        z = 27                                                                                        #
    elif 2529 < player.hitBox[0] - bgX < 2555:                                                        #
        z = 28                                                                                        #
    elif 2850 < player.hitBox[0] + player.hitBox[2] - bgX < 2912:                                     #
        z = 29                                                                                        #
    elif 2912 < player.hitBox[0] + player.hitBox[2] - bgX < 2928:                                     #
        z = 30                                                                                        #
    elif 2928 < player.hitBox[0] + player.hitBox[2] - bgX < 2944:                                     #
        z = 31                                                                                        #
    elif 2944 < player.hitBox[0] + player.hitBox[2] - bgX < 2960:                                     #
        z = 32                                                                                        #
    elif 2960 < player.hitBox[0] + player.hitBox[2] - bgX < 2976:                                     #
        z = 33                                                                                        #
    elif 2976 < player.hitBox[0] + player.hitBox[2] - bgX < 2992:                                     #
        z = 34                                                                                        #
    elif 2992 < player.hitBox[0] + player.hitBox[2] - bgX < 3008:                                     #
        z = 35                                                                                        #
    elif 3008 < player.hitBox[0] + player.hitBox[2] - bgX < 3024:                                     #
        z = 36                                                                                        #
    elif 3024 < player.hitBox[0] + player.hitBox[2] - bgX < 3060:                                     #
        z = 37                                                                                        #
    elif 3160 < player.hitBox[0] + player.hitBox[2] - bgX < 3200:                                     #
        z = 45                                                                      # #################

    w = 0                                                                           # #################
    if player.hitBox[0] + player.hitBox[2] - bgX < 345:                                               #
        w = 0                                                                                         #
    elif 345 < player.hitBox[0] + player.hitBox[2] - bgX < 377:                                       #
        w = 1                                                                                         #
    elif 377 < player.hitBox[0] + player.hitBox[2] - bgX < 459:                                       #
        w = 2                                                                                         #
    elif 1210 < player.hitBox[0] + player.hitBox[2] - bgX < 1257:                                     #
        w = 3                                                                                         #
    elif 1257 < player.hitBox[0] + player.hitBox[2] - bgX < 1281:                                     #
        w = 4                                                                                         #
    elif 1281 < player.hitBox[0] + player.hitBox[2] - bgX < 1297:                                     #
        w = 5                                                                                         #
    elif 1297 < player.hitBox[0] + player.hitBox[2] - bgX < 1313:                                     #
        w = 6                                                                                         #
    elif 1313 < player.hitBox[0] + player.hitBox[2] - bgX < 1329:                                     #
        w = 7                                                                                         #
    elif 1329 < player.hitBox[0] + player.hitBox[2] - bgX < 1345:                                     #
        w = 8                                                                                         #
    elif 1345 < player.hitBox[0] + player.hitBox[2] - bgX < 1361:                                     #
        w = 9                                                                                         #
    elif 1361 < player.hitBox[0] + player.hitBox[2] - bgX < 1377:                                     #
        w = 10                                                                                        #
    elif 1377 < player.hitBox[0] + player.hitBox[2] - bgX < 1393:                                     #
        w = 11                                                                                        #
    elif 1393 < player.hitBox[0] + player.hitBox[2] - bgX < 1427:                                     #
        w = 12                                                                                        #
    elif 1450 < player.hitBox[0] + player.hitBox[2] - bgX < 1473:                                     #
        w = 13                                                                                        #
    elif 1473 < player.hitBox[0] + player.hitBox[2] - bgX < 1489:                                     #
        w = 14                                                                                        # ###### for brick blocks
    elif 1489 < player.hitBox[0] + player.hitBox[2] - bgX < 1505:                                     #
        w = 15                                                                                        #
    elif 1505 < player.hitBox[0] + player.hitBox[2] - bgX < 1539:                                     #
        w = 16                                                                                        #
    elif 1593 < player.hitBox[0] + player.hitBox[2] - bgX < 1617:                                     #
        w = 17                                                                                        #
    elif 1617 < player.hitBox[0] + player.hitBox[2] - bgX < 1651:                                     #
        w = 18                                                                                        #
    elif 1881 < player.hitBox[0] + player.hitBox[2] - bgX < 1923:                                     #
        w = 19                                                                                        #
    elif 1929 < player.hitBox[0] + player.hitBox[2] - bgX < 1953:                                     #
        w = 20                                                                                        #
    elif 1953 < player.hitBox[0] + player.hitBox[2] - bgX < 1969:                                     #
        w = 21                                                                                        #
    elif 1969 < player.hitBox[0] + player.hitBox[2] - bgX < 2003:                                     #
        w = 22                                                                                        #
    elif 2041 < player.hitBox[0] + player.hitBox[2] - bgX < 2065:                                     #
        w = 23                                                                                        #
    elif 2065 < player.hitBox[0] + player.hitBox[2] - bgX < 2081:                                     #
        w = 24                                                                                        #
    elif 2081 < player.hitBox[0] + player.hitBox[2] - bgX < 2097:                                     #
        w = 25                                                                                        #
    elif 2097 < player.hitBox[0] + player.hitBox[2] - bgX < 2131:                                     #
        w = 26                                                                                        #
    elif 2681 < player.hitBox[0] + player.hitBox[2] - bgX < 2705:                                     #
        w = 27                                                                                        #
    elif 2705 < player.hitBox[0] + player.hitBox[2] - bgX < 2737:                                     #
        w = 28                                                                                        #
    elif 2737 < player.hitBox[0] + player.hitBox[2] - bgX < 2771:                                     #
        w = 29                                                                      # #################

    v = 0                                                                           # #################
    if player.hitBox[0] + player.hitBox[2] - bgX < 273:                                               #
        v = 0                                                                                         #
    elif 337 < player.hitBox[0] + player.hitBox[2] - bgX < 353:                                       #
        v = 1                                                                                         #
    elif 353 < player.hitBox[0] + player.hitBox[2] - bgX < 369:                                       #
        v = 2                                                                                         #
    elif 369 < player.hitBox[0] + player.hitBox[2] - bgX < 410:                                       #
        v = 3                                                                                         #
    elif 1235 < player.hitBox[0] + player.hitBox[2] - bgX < 1280:                                     #
        v = 4                                                                                         #
    elif 1490 < player.hitBox[0] + player.hitBox[2] - bgX < 1540:                                     #
        v = 5                                                                                         #
    elif 1680 < player.hitBox[0] + player.hitBox[2] - bgX < 1725:                                     # ###### for mystery boxes
        v = 6                                                                                         #
    elif 1735 < player.hitBox[0] + player.hitBox[2] - bgX < 1775:                                     #
        if player.hitBox[1] < 103:                                                                    #
            v = 7                                                                                     #
        elif player.hitBox[1] > 103:                                                                  #
            v = 8                                                                                     #
    elif 1780 < player.hitBox[0] + player.hitBox[2] - bgX < 1820:                                     #
        v = 9                                                                                         #
    elif 2055 < player.hitBox[0] + player.hitBox[2] - bgX < 2081:                                     #
        v = 10                                                                                        #
    elif 2081 < player.hitBox[0] + player.hitBox[2] - bgX < 2110:                                     #
        v = 11                                                                                        #
    elif 2710 < player.hitBox[0] + player.hitBox[2] - bgX < 2750:                                     #
        v = 12                                                                      # #################

    for goom in g:                                                                  # #################
        if 0 < goom.x < 1100 and 0 < player.x < 1100 + bgX:                                           #
            goom.move = True                                                                          #
        elif 1000 <= goom.x < 1500 and 1000 <= player.x - bgX < 1500:                                 #
            goom.move = True                                                                          # ###### for goombas
        elif 1300 <= goom.x < 1900 and 1300 <= player.x - bgX < 1900:                                 #
            goom.move = True                                                                          #
        elif 1600 <= goom.x < 2010 and 1600 <= player.x - bgX < 2010:                                 #
            goom.move = True                                                        # #################
        elif 1800 <= goom.x < 3300 and 1800 <= player.x - bgX < 3300:
            goom.move = True

    for koopa in kt:                                                                # #################
        if 0 < koopa.x < 1100 and 0 < player.x < 1100 + bgX:                                          #
            koopa.move = True                                                                         #
        elif 1000 <= koopa.x < 1500 and 1000 <= player.x - bgX < 1500:                                #
            koopa.move = True                                                                         # ###### for koopa troopas
        elif 1300 <= koopa.x < 2010 and 1300 <= player.x - bgX < 2010:                                #
            koopa.move = True                                                                         #
        elif 1800 <= koopa.x < 3300 and 1800 <= player.x - bgX < 3300:                                #
            koopa.move = True                                                       # #################

    # -----------------------------------------------INTERACTION LOGIC------------------------------------------------ #

    if player.hitBox[1] + player.hitBox[3] > p[x].hitBox[1] and (player.hitBox[0] < p[x].hitBox[0] + p[x].hitBox[2] or     # #########
       player.hitBox[0] + player.hitBox[2] > p[x].hitBox[0]):                                                                        #
        player.collide(p[x])                                                                                                         #
                                                                                                                                     #
    if player.hitBox[1] + player.hitBox[3] > fb[z].hitBox[1] and (player.hitBox[0] < fb[z].hitBox[0] + fb[z].hitBox[2] or            #
       player.hitBox[0] + player.hitBox[2] > fb[z].hitBox[0]):                                                                       #
        player.collide(fb[z])                                                                                                        #
                                                                                                                                     #
    if (player.hitBox[1] < bb[w].hitBox[1] + bb[w].hitBox[3] and player.hitBox[1] + player.hitBox[3] > bb[w].hitBox[1] and           #
            not bb[w].broken):                                                                                                       #
        player.collide(bb[w])                                                                                                        # ###### collision detection
                                                                                                                                     #
    if player.hitBox[1] < mb[v].hitBox[1] + mb[v].hitBox[3] and player.hitBox[1] + player.hitBox[3] > mb[v].hitBox[1]:               #
        player.collide(mb[v])                                                                                                        #
                                                                                                                                     #
    if (player.hitBox[1] < ib.hitBox[1] + ib.hitBox[3] and player.hitBox[1] + player.hitBox[3] > ib.hitBox[1] and                    #
        ib.empty and (not lm or not lm[0].rise)):                                                                                    #
        player.collide(ib)                                                                                                           #
                                                                                                                                     #
    if player.hitBox[0] + player.hitBox[2] > f_p.hitBox[0] + 3:                                                                      #
        player.end_m = True                                                                                                # #########

    if ((p[x].hitBox[0] + p[x].hitBox[2] - 3 > player.hitBox[0] + player.hitBox[2] > p[x].hitBox[0] + 3 or                 # #########
        p[x].hitBox[0] + 3 < player.hitBox[0] < p[x].hitBox[0] + p[x].hitBox[2] - 3) and not player.death):                          #
        player.land(p[x])                                                                                                            #
                                                                                                                                     #
    elif ((fb[z].hitBox[0] + fb[z].hitBox[2] > player.hitBox[0] + player.hitBox[2] > fb[z].hitBox[0] + 3 or                          #
            fb[z].hitBox[0] < player.hitBox[0] < fb[z].hitBox[0] + fb[z].hitBox[2] - 3) and                                          #
            player.hitBox[1] + player.hitBox[3] > fb[z].hitBox[1] - 1 > player.hitBox[1] and not player.death):                      #
        player.land(fb[z])                                                                                                           #
    elif (fb[z-1].hitBox[0] + fb[z-1].hitBox[2] > player.hitBox[0] > fb[z-1].hitBox[0] and                                           #
            player.hitBox[1] + player.hitBox[3] > fb[z-1].hitBox[1] - 1 > player.hitBox[1] and not player.death):                    #
        player.land(fb[z-1])                                                                                                         #
    elif (z != 45 and fb[z+1].hitBox[0] + fb[z+1].hitBox[2] > player.hitBox[0] + player.hitBox[2] > fb[z+1].hitBox[0] and            #
            player.hitBox[1] + player.hitBox[3] > fb[z+1].hitBox[1] - 1 > player.hitBox[1] and not player.death):                    #
        player.land(fb[z+1])                                                                                                         #
                                                                                                                                     #
    elif ((bb[w].hitBox[0] + bb[w].hitBox[2] > player.hitBox[0] + player.hitBox[2] > bb[w].hitBox[0] + 3 or                          #
            bb[w].hitBox[0] < player.hitBox[0] < bb[w].hitBox[0] + bb[w].hitBox[2] - 3) and                                          #
            bb[w].hitBox[1] - 1 < player.hitBox[1] + player.hitBox[3] < bb[w].hitBox[1] + bb[w].hitBox[3] and                        #
            not bb[w].broken and not player.death):                                                                                  # ###### landing logic
        player.land(bb[w])                                                                                                           #
    elif (bb[w-1].hitBox[0] < player.hitBox[0] < bb[w-1].hitBox[0] + bb[w-1].hitBox[2] and                                           #
            bb[w-1].hitBox[1] - 1 < player.hitBox[1] + player.hitBox[3] < bb[w-1].hitBox[1] + bb[w-1].hitBox[3] and                  #
            not bb[w-1].broken and not player.death):                                                                                #
        player.land(bb[w-1])                                                                                                         #
                                                                                                                                     #
    elif ((mb[v].hitBox[0] + mb[v].hitBox[2] > player.hitBox[0] + player.hitBox[2] > mb[v].hitBox[0] + 3 or                          #
           mb[v].hitBox[0] < player.hitBox[0] < mb[v].hitBox[0] + mb[v].hitBox[2] - 3) and                                           #
           mb[v].hitBox[1] + mb[v].hitBox[3] > player.hitBox[1] + player.hitBox[3] > mb[v].hitBox[1] - 1 and                         #
           not player.death):                                                                                                        #
        player.land(mb[v])                                                                                                           #
    elif (mb[v - 1].hitBox[0] < player.hitBox[0] < mb[v - 1].hitBox[0] + mb[v - 1].hitBox[2] and                                     #
          mb[v - 1].hitBox[1] - 1 < player.hitBox[1] + player.hitBox[3] < mb[v - 1].hitBox[1] + mb[v - 1].hitBox[3] and              #
          not player.death):                                                                                                         #
        player.land(mb[v - 1])                                                                                                       #
                                                                                                                                     #
    elif ((ib.hitBox[0] + ib.hitBox[2] > player.hitBox[0] + player.hitBox[2] > ib.hitBox[0] + 3 or                                   #
           ib.hitBox[0] < player.hitBox[0] < ib.hitBox[0] + ib.hitBox[2] - 3) and                                                    #
           ib.hitBox[1] + ib.hitBox[3] > player.hitBox[1] + player.hitBox[3] > ib.hitBox[1] - 1 and ib.empty):                       #
        player.land(ib)                                                                                                    # #########

    elif ((bb[w].hitBox[0] + bb[w].hitBox[2] > player.hitBox[0] + player.hitBox[2] > bb[w].hitBox[0] + 3 or                # #########
           bb[w].hitBox[0] < player.hitBox[0] < bb[w].hitBox[0] + bb[w].hitBox[2] - 3) and                                           #
           player.hitBox[1] < bb[w].hitBox[1] + bb[w].hitBox[3] < player.hitBox[1] + player.hitBox[3] and                            #
           not bb[w].broken and not player.death):                                                                                   #
            player.jump_count_up = -10                                                                                               #
            player.y += 3                                                                                                            #
            player.collide_r = False                                                                                                 #
            player.collide_l = False                                                                                                 #
            s_bump.play()                                                                                                            #
            if bb[w].type == 'n':                                                                                                    #
                if player.level == 1 or player.level == 3:                                                                           #
                    bb[w].block_push = True                                                                                          #
                elif player.level == 2 or player.level == 4:                                                                         #
                    s_breakblock.play()                                                                                              #
                    bb[w].broken = True                                                                                              #
                    score += 50                                                                                                      #
                    broken_bs.append(broken_brick(bb[w].x, bb[w].y, 0))                                                              #
                    broken_bs.append(broken_brick(bb[w].x + 8, bb[w].y, 1))                                                          #
                    broken_bs.append(broken_brick(bb[w].x, bb[w].y + 8, 2))                                                          #
                    broken_bs.append(broken_brick(bb[w].x + 8, bb[w].y + 8, 3))                                                      #
            elif bb[w].type == 'c':                                                                                                  #
                if bb[w].coin_counter > 0:                                                                                           #
                    if not bb[w].block_push:                                                                                         #
                        s_coin.play()                                                                                                #
                        c.append(Coin(bb[w].x + 4, bb[w].y))                                                                         #
                        coins += 1                                                                                                   #
                        score += 200                                                                                                 #
                        bb[w].coin_counter -= 1                                                                                      #
                        bb[w].block_push = True                                                                                      #
                if bb[w].coin_counter == 0:                                                                                          #
                    bb[w].empty = True                                                                                               # ###### brick functions' logic
    elif ((bb[w-1].hitBox[0] + bb[w-1].hitBox[2] > player.hitBox[0] + player.hitBox[2] > bb[w-1].hitBox[0] + 3 or                    #
           bb[w-1].hitBox[0] < player.hitBox[0] < bb[w-1].hitBox[0] + bb[w-1].hitBox[2] - 3) and                                     #
           player.hitBox[1] < bb[w-1].hitBox[1] + bb[w-1].hitBox[3] < player.hitBox[1] + player.hitBox[3] and                        #
           not bb[w-1].broken and not player.death):                                                                                 #
            player.jump_count_up = -10                                                                                               #
            player.y += 3                                                                                                            #
            player.collide_r = False                                                                                                 #
            player.collide_l = False                                                                                                 #
            s_bump.play()                                                                                                            #
            if bb[w-1].type == 'n':                                                                                                  #
                if player.level == 1 or player.level == 3:                                                                           #
                    bb[w-1].block_push = True                                                                                        #
                elif player.level == 2 or player.level == 4:                                                                         #
                    s_breakblock.play()                                                                                              #
                    bb[w-1].broken = True                                                                                            #
                    score += 50                                                                                                      #
                    broken_bs.append(broken_brick(bb[w-1].x, bb[w-1].y, 0))                                                          #
                    broken_bs.append(broken_brick(bb[w-1].x + 8, bb[w-1].y, 1))                                                      #
                    broken_bs.append(broken_brick(bb[w-1].x, bb[w-1].y + 8, 2))                                                      #
                    broken_bs.append(broken_brick(bb[w-1].x + 8, bb[w-1].y + 8, 3))                                                  #
            elif bb[w-1].type == 'c':                                                                                                #
                if bb[w-1].coin_counter > 0:                                                                                         #
                    if not bb[w-1].block_push:                                                                                       #
                        s_coin.play()                                                                                                #
                        c.append(Coin(bb[w-1].x + 4, bb[w-1].y))                                                                     #
                        coins += 1                                                                                                   #
                        score += 200                                                                                                 #
                        bb[w-1].coin_counter -= 1                                                                                    #
                        bb[w-1].block_push = True                                                                                    #
                if bb[w-1].coin_counter == 0:                                                                                        #
                    bb[w-1].empty = True                                                                                   # #########

    elif ((mb[v].hitBox[0] + mb[v].hitBox[2] > player.hitBox[0] + player.hitBox[2] > mb[v].hitBox[0] + 3 or                # #########
           mb[v].hitBox[0] < player.hitBox[0] < mb[v].hitBox[0] + mb[v].hitBox[2] - 3) and                                           #
           player.hitBox[1] < mb[v].hitBox[1] + mb[v].hitBox[3] < player.hitBox[1] + player.hitBox[3] and                            #
           not player.death):                                                                                                        #
            player.jump_count_up = -10                                                                                               #
            player.y += 3                                                                                                            #
            player.collide_r = False                                                                                                 #
            player.collide_l = False                                                                                                 #
            s_bump.play()                                                                                                            #
            if not mb[v].empty:                                                                                                      #
                mb[v].block_push = True                                                                                              #
                if mb[v].type == 'c':                                                                                                #
                    s_coin.play()                                                                                                    #
                    c.append(Coin(mb[v].x + 4, mb[v].y))                                                                             #
                    coins += 1                                                                                                       #
                    score += 200                                                                                                     #
                elif mb[v].type == 'p' and player.level == 1:                                                                        #
                    s_powerup_appears.play()                                                                                         #
                    m.append(Mushroom(mb[v].x, mb[v].y))                                                                             #
                    v_m = v                                                                                                          #
                elif mb[v].type == 'p':                                                                                              #
                    s_powerup_appears.play()                                                                                         #
                    f.append(Flower(mb[v].x, mb[v].y))                                                                               #
                    v_f = v                                                                                                          #
                mb[v].empty = True                                                                                                   # ###### mystery box functions' logic
    elif ((mb[v-1].hitBox[0] + mb[v-1].hitBox[2] > player.hitBox[0] + player.hitBox[2] > mb[v-1].hitBox[0] + 3 or                    #
           mb[v-1].hitBox[0] < player.hitBox[0] < mb[v-1].hitBox[0] + mb[v-1].hitBox[2] - 3) and                                     #
           player.hitBox[1] < mb[v-1].hitBox[1] + mb[v-1].hitBox[3] < player.hitBox[1] + player.hitBox[3] and                        #
           not player.death):                                                                                                        #
            player.jump_count_up = -10                                                                                               #
            player.y += 3                                                                                                            #
            player.collide_r = False                                                                                                 #
            player.collide_l = False                                                                                                 #
            s_bump.play()                                                                                                            #
            if not mb[v-1].empty:                                                                                                    #
                mb[v-1].block_push = True                                                                                            #
                if mb[v-1].type == 'c':                                                                                              #
                    s_coin.play()                                                                                                    #
                    c.append(Coin(mb[v-1].x + 4, mb[v-1].y))                                                                         #
                    coins += 1                                                                                                       #
                    score += 200                                                                                                     #
                elif mb[v-1].type == 'p' and player.level == 1:                                                                      #
                    s_powerup_appears.play()                                                                                         #
                    m.append(Mushroom(mb[v-1].x, mb[v-1].y))                                                                         #
                    v_m = v-1                                                                                                        #
                elif mb[v-1].type == 'p':                                                                                            #
                    s_powerup_appears.play()                                                                                         #
                    f.append(Flower(mb[v-1].x, mb[v-1].y))                                                                           #
                    v_f = v-1                                                                                                        #
                mb[v-1].empty = True                                                                                       # #########

    elif ((ib.hitBox[0] + ib.hitBox[2] > player.hitBox[0] + player.hitBox[2] > ib.hitBox[0] + 3 or                         # #########
           ib.hitBox[0] < player.hitBox[0] < ib.hitBox[0] + ib.hitBox[2] - 3) and                                                    #
           player.hitBox[1] < ib.hitBox[1] + ib.hitBox[3] < player.hitBox[1] + player.hitBox[3] and not player.jump_count_down):     #
            player.jump_count_up = -10                                                                                               #
            player.y += 3                                                                                                            #
            player.collide_r = False                                                                                                 #
            player.collide_l = False                                                                                                 # ###### invisible box functions' logic
            s_bump.play()                                                                                                            #
            if not ib.empty:                                                                                                         #
                if ib.type == 'l':                                                                                                   #
                    s_powerup_appears.play()                                                                                         #
                    lm.append(L_Mushroom(ib.x, ib.y))                                                                                #
                ib.empty = True                                                                                            # #########

    elif not player.death:                                                                                                 # #########
        player.fall()                                                                                                                #
                                                                                                                                     #
    if (h[y].x + h[y].width + bgX + 3 > player.hitBox[0] + player.hitBox[2] > h[y].x + bgX and                                       # ###### fall functions
        h[y].x + bgX - 1 < player.hitBox[0] < h[y].x + h[y].width + bgX) and not player.isJump and not player.pot_en:                #
        if not player.hole_falling:                                                                                                  #
            s_mario_die.play()                                                                                                       #
        player.hole_falling = True                                                                                         # #########

    for mush in m:                                                                                                         # #########
        if ((player.hitBox[0] + player.hitBox[2] > mush.hitBox[0] > player.hitBox[0] or                                              #
            player.hitBox[0] < mush.hitBox[0] + mush.hitBox[2] < player.hitBox[0] + player.hitBox[2]) and                            #
            (player.hitBox[1] + player.hitBox[3] > mush.hitBox[1] >= player.hitBox[1] or                                             #
            player.hitBox[1] < mush.hitBox[1] + mush.hitBox[3] <= player.hitBox[1] + player.hitBox[3]) and                           #
            not mush.rise and not player.death):                                                                                     # ###### for mushroom consumption
            s_powerup.play()                                                                                                         #
            player.grow = True                                                                                                       #
            score += 1000                                                                                                            #
            pts.append(Points(mush.x + bgX, mush.y - 8, 1000))                                                                       #
            m.remove(mush)                                                                                                 # #########

    for mush in lm:                                                                                                        # #########
        if ((player.hitBox[0] + player.hitBox[2] > mush.hitBox[0] > player.hitBox[0] or                                              #
            player.hitBox[0] < mush.hitBox[0] + mush.hitBox[2] < player.hitBox[0] + player.hitBox[2]) and                            #
            (player.hitBox[1] + player.hitBox[3] > mush.hitBox[1] >= player.hitBox[1] or                                             #
            player.hitBox[1] < mush.hitBox[1] + mush.hitBox[3] <= player.hitBox[1] + player.hitBox[3]) and                           # ###### for 1up mushroom consumption
            not mush.rise and not player.death):                                                                                     #
            s_1up.play()                                                                                                             #
            player.lives += 1                                                                                                        #
            pts.append(Points(mush.x + bgX, mush.y - 8, '1UP'))                                                                      #
            lm.remove(mush)                                                                                                # #########

    for fl in f:                                                                                                           # #########
        if ((player.hitBox[0] + player.hitBox[2] > fl.hitBox[0] > player.hitBox[0] or                                                #
            player.hitBox[0] < fl.hitBox[0] + fl.hitBox[2] < player.hitBox[0] + player.hitBox[2]) and                                #
            (player.hitBox[1] + player.hitBox[3] > fl.hitBox[1] >= player.hitBox[1] or                                               #
            player.hitBox[1] < fl.hitBox[1] + fl.hitBox[3] <= player.hitBox[1] + player.hitBox[3]) and                               #
            not fl.rise and not player.death):                                                                                       # ###### for flower consumption
            s_powerup.play()                                                                                                         #
            if player.level == 1 or player.level == 2:                                                                               #
                player.level += 2                                                                                                    #
            score += 1000                                                                                                            #
            pts.append(Points(fl.x + bgX, fl.y - 8, 1000))                                                                           #
            f.remove(fl)                                                                                                   # #########

    for bullet in bul:                                                                                                     # #########
        for pip in p:                                                                                                                #
            if (bullet.hitBox[0] < pip.hitBox[0] + pip.hitBox[2] - 3 < bullet.hitBox[0] + bullet.hitBox[2] or                        #
                bullet.hitBox[0] + bullet.hitBox[2] > pip.hitBox[0] + 3 > bullet.hitBox[0]):                                         #
                if bullet.hitBox[1] > pip.hitBox[1] and not bullet.hit:                                                              #
                    s_bump.play()                                                                                                    #
                    bullet.hit = True                                                                                                #
                    break                                                                                                            #
                elif bullet.hitBox[1] + bullet.hitBox[3] > pip.hitBox[1]:                                                            #
                    bullet.bounce = True                                                                                             #
                                                                                                                                     #
        for block in fb:                                                                                                             #
            if (bullet.hitBox[0] < block.hitBox[0] + block.hitBox[2] < bullet.hitBox[0] + bullet.hitBox[2] or                        #
                bullet.hitBox[0] + bullet.hitBox[2] > block.hitBox[0] > bullet.hitBox[0]):                                           #
                if bullet.hitBox[1] > block.hitBox[1] and not bullet.hit:                                                            #
                    s_bump.play()                                                                                                    #
                    bullet.hit = True                                                                                                #
                    break                                                                                                            #
                if bullet.hitBox[1] + bullet.hitBox[3] > block.hitBox[1]:                                                            #
                    bullet.bounce = True                                                                                             #
                                                                                                                                     #
        for br in bb:                                                                                                                #
            if (bullet.hitBox[0] < br.hitBox[0] + br.hitBox[2] < bullet.hitBox[0] + bullet.hitBox[2] or                              #
                bullet.hitBox[0] + bullet.hitBox[2] > br.hitBox[0] > bullet.hitBox[0]) and not br.broken:                            #
                if ((bullet.hitBox[1] < br.hitBox[1] + br.hitBox[3] < bullet.hitBox[1] + bullet.hitBox[3] or                         #
                    (bullet.hitBox[1] > br.hitBox[1] and bullet.hitBox[1] + bullet.hitBox[3] < br.hitBox[1] + br.hitBox[3]))         #
                    and not bullet.hit):                                                                                             #
                    s_bump.play()                                                                                                    #
                    bullet.hit = True                                                                                                #
                    break                                                                                                            #
                if bullet.hitBox[1] + bullet.hitBox[3] > br.hitBox[1] > bullet.hitBox[1]:                                            #
                    bullet.bounce = True                                                                                             #
                                                                                                                                     #
        for box in mb:                                                                                                               #
            if (bullet.hitBox[0] < box.hitBox[0] + box.hitBox[2] < bullet.hitBox[0] + bullet.hitBox[2] or                            #
                bullet.hitBox[0] + bullet.hitBox[2] > box.hitBox[0] > bullet.hitBox[0]):                                             #
                if ((bullet.hitBox[1] < box.hitBox[1] + box.hitBox[3] < bullet.hitBox[1] + bullet.hitBox[3] or                       #
                    (bullet.hitBox[1] > box.hitBox[1] and bullet.hitBox[1] + bullet.hitBox[3] < box.hitBox[1] + box.hitBox[3]))      #
                    and not bullet.hit):                                                                                             #
                    s_bump.play()                                                                                                    #
                    bullet.hit = True                                                                                                #
                    break                                                                                                            #
                if bullet.hitBox[1] + bullet.hitBox[3] > box.hitBox[1] > bullet.hitBox[1]:                                           #
                    bullet.bounce = True                                                                                             #
                                                                                                                                     #
        for goom in g:                                                                                                               #
            if ((bullet.hitBox[0] + bullet.hitBox[2] > goom.hitBox[0] > bullet.hitBox[0] or                                          # ###### bullet collisions
                bullet.hitBox[0] < goom.hitBox[0] + goom.hitBox[2] < bullet.hitBox[0] + bullet.hitBox[2]) and                        #
                (bullet.hitBox[1] + bullet.hitBox[3] > goom.hitBox[1] >= bullet.hitBox[1] or                                         #
                bullet.hitBox[1] < goom.hitBox[1] + goom.hitBox[3] <= bullet.hitBox[1] + bullet.hitBox[3] or                         #
                (bullet.hitBox[1] > goom.hitBox[1] and bullet.hitBox[1] + bullet.hitBox[3] < goom.hitBox[1] + goom.hitBox[3]))       #
                and goom.move and not goom.hit and not goom.squished):                                                               #
                s_kick.play()                                                                                                        #
                bullet.hit = True                                                                                                    #
                goom.hit = True                                                                                                      #
                score += 100                                                                                                         #
                pts.append(Points(goom.x + bgX, goom.y - 8, 100))                                                                    #
                break                                                                                                                #
                                                                                                                                     #
        for koopa in kt:                                                                                                             #
            if ((bullet.hitBox[0] + bullet.hitBox[2] > koopa.hitBox[0] > bullet.hitBox[0] or                                         #
                bullet.hitBox[0] < koopa.hitBox[0] + koopa.hitBox[2] < bullet.hitBox[0] + bullet.hitBox[2]) and                      #
                (bullet.hitBox[1] + bullet.hitBox[3] > koopa.hitBox[1] >= bullet.hitBox[1] or                                        #
                bullet.hitBox[1] < koopa.hitBox[1] + koopa.hitBox[3] <= bullet.hitBox[1] + bullet.hitBox[3] or                       #
                (bullet.hitBox[1] > koopa.hitBox[1] and bullet.hitBox[1] + bullet.hitBox[3] < koopa.hitBox[1] + koopa.hitBox[3]))    #
                and koopa.move and not koopa.hit):                                                                                   #
                s_kick.play()                                                                                                        #
                bullet.hit = True                                                                                                    #
                koopa.hit = True                                                                                                     #
                score += 200                                                                                                         #
                pts.append(Points(koopa.x + bgX, koopa.y - 8, 200))                                                                  #
                break                                                                                                                #
                                                                                                                                     #
        for hol in h:                                                                                                                #
            if (hol.x + hol.width > bullet.hitBox[0] - bgX > hol.x and                                                               #
                hol.x < bullet.hitBox[0] + bullet.hitBox[2] - bgX < hol.x + hol.width):                                              #
                if bullet.hitBox[1] + bullet.hitBox[3] > ground_level:                                                               #
                    bullet.bounce = False                                                                                            #
                    break                                                                                                            #
            elif (bullet.hitBox[1] + bullet.hitBox[3] > ground_level + 2 and                                                         #
                (bullet.hitBox[0] < hol.x + bgX < bullet.hitBox[0] + bullet.hitBox[2] or                                             #
                bullet.hitBox[0] < hol.x + hol.width + bgX < bullet.hitBox[0] + bullet.hitBox[2]) and not bullet.hit):               #
                s_bump.play()                                                                                                        #
                bullet.hit = True                                                                                                    #
                break                                                                                                                #
            elif bullet.hitBox[1] + bullet.hitBox[3] > ground_level:                                                                 #
                bullet.bounce = True                                                                                                 #
                                                                                                                                     #
        if f_p.hitBox[0] + 2 < bullet.hitBox[0] + bullet.hitBox[2] < f_p.hitBox[0] + f_p.hitBox[2] and not bullet.hit:               #
            s_bump.play()                                                                                                            #
            bullet.hit = True                                                                                                        #
                                                                                                                                     #
        if bullet.timer_h == 26 or bullet.x + bullet.width < -bgX - 100:                                                             #
            bul.remove(bullet)                                                                                             # #########

    for i in range(len(g) - 1):                                                                                            # #########
        if (g[i].hitBox[0] + g[i].hitBox[2] > g[i+1].hitBox[0] and not g[i].squished and not g[i+1].squished and                     #
            not g[i].hit and not g[i+1].hit):                                                                                        #
            g[i].switch = True                                                                                                       #
            g[i+1].switch = True                                                                                                     #
                                                                                                                                     #
    for goom in g:                                                                                                                   #
        for pip in p:                                                                                                                #
            if (goom.hitBox[0] < pip.hitBox[0] + pip.hitBox[2] - 2 < goom.hitBox[0] + goom.hitBox[2] or                              #
                goom.hitBox[0] + goom.hitBox[2] > pip.hitBox[0] + 2 > goom.hitBox[0]) and goom.hitBox[1] > pip.hitBox[1]:            #
                goom.switch = True                                                                                                   #
                                                                                                                                     #
        if ((player.hitBox[0] + player.hitBox[2] > goom.hitBox[0] > player.hitBox[0] or                                              # ###### goomba collisions
            player.hitBox[0] < goom.hitBox[0] + goom.hitBox[2] < player.hitBox[0] + player.hitBox[2])                                #
            and not goom.squished and not goom.hit and not player.death and not player.hole_falling):                                #
            if (player.hitBox[1] + player.hitBox[3] > goom.hitBox[1] + 8 and player.hitBox[1] < goom.hitBox[1] + goom.hitBox[3] and  #
                not player.blink):                                                                                                   #
                if player.level == 2 or player.level == 4:                                                                           #
                    s_powerdown.play()                                                                                               #
                player.enemy_damage()                                                                                                #
            if (player.hitBox[1] < goom.hitBox[1] < player.hitBox[1] + player.hitBox[3] <= goom.hitBox[1] + 8 and                    #
                (player.falling_count != 1 or player.jump_count_down != 0)):                                                         #
                s_stomp.play()                                                                                                       #
                goom.squished = True                                                                                                 #
                player.squish_streak += 1                                                                                            #
                score += 100 * player.squish_streak                                                                                  #
                pts.append(Points(goom.x + bgX, goom.y - 8, 100 * player.squish_streak))                                             #
                player.squish_jump()                                                                                                 #
                                                                                                                                     #
    if player.y == player.ground_level:                                                                                              #
        player.squish_streak = 0                                                                                           # #########

    for koopa in kt:                                                                                                       # #########
        if (koopa.hitBox[0] < fb[0].hitBox[0] + fb[0].hitBox[2] < koopa.hitBox[0] + koopa.hitBox[2] or                               #
            koopa.hitBox[0] + koopa.hitBox[2] > fb[0].hitBox[0] > koopa.hitBox[0]):                                                  #
            s_bump.play()                                                                                                            #
            koopa.switch = True                                                                                                      #
        elif(h[1].x < koopa.hitBox[0] + koopa.hitBox[2] - bgX < h[1].x + h[1].width and                                              #
             h[1].x + h[1].width > koopa.hitBox[0] - bgX > h[1].x):                                                                  #
            if ((koopa.hitBox[0] - bgX < h[1].x + 4 or                                                                               #
                koopa.hitBox[0] + koopa.hitBox[2] - bgX > h[1].x + h[1].width - 4) and                                               #
                koopa.hitBox[1] + koopa.hitBox[3] > ground_level):                                                                   #
                s_bump.play()                                                                                                        #
                koopa.switch = True                                                                                                  #
                                                                                                                                     #
        if koopa.shell_slide:                                                                                                        #
            for goom in g:                                                                                                           #
                if ((koopa.hitBox[0] + koopa.hitBox[2] > goom.hitBox[0] > koopa.hitBox[0] or                                         #
                    koopa.hitBox[0] < goom.hitBox[0] + goom.hitBox[2] < koopa.hitBox[0] + koopa.hitBox[2]) and                       #
                    (koopa.hitBox[1] + koopa.hitBox[3] > goom.hitBox[1] >= koopa.hitBox[1] or                                        #
                    koopa.hitBox[1] < goom.hitBox[1] + goom.hitBox[3] <= koopa.hitBox[1] + koopa.hitBox[3] or                        #
                    (koopa.hitBox[1] > goom.hitBox[1] and koopa.hitBox[1] + koopa.hitBox[3] < goom.hitBox[1] +                       #
                    goom.hitBox[3])) and goom.move and not goom.hit and not goom.squished):                                          #
                    s_kick.play()                                                                                                    #
                    goom.hit = True                                                                                                  #
                    koopa.goom_domino += 1                                                                                           #
                    score += koopa.goom_domino * 100                                                                                 #
                    pts.append(Points(goom.x + bgX, goom.y - 8, koopa.goom_domino * 100))                                            #
                                                                                                                                     #
        if ((player.hitBox[0] + player.hitBox[2] > koopa.hitBox[0] > player.hitBox[0] or                                             #
            player.hitBox[0] < koopa.hitBox[0] + koopa.hitBox[2] < player.hitBox[0] + player.hitBox[2])                              #
            and not koopa.hit and not player.death and not player.hole_falling):                                                     #
            if (player.hitBox[1] + player.hitBox[3] > koopa.hitBox[1] + 8 and                                                        #
                player.hitBox[1] < koopa.hitBox[1] + koopa.hitBox[3] and not player.blink):                                          #
                if (koopa.shell_slide and not koopa.shell_stop) or not koopa.shell:                                                  #
                    if player.level == 2 or player.level == 4:                                                                       #
                        s_powerdown.play()                                                                                           #
                    player.enemy_damage()                                                                                            #
                elif koopa.shell_stop:                                                                                               # ###### koopa troopa collisions
                    s_kick.play()                                                                                                    #
                    koopa.shell_slide = True                                                                                         #
                    score += 100                                                                                                     #
                    pts.append(Points(koopa.x + bgX, koopa.y - 8, 100))                                                              #
                    if player.hitBox[0] + player.hitBox[2] > koopa.hitBox[0] > player.hitBox[0]:                                     #
                        koopa.dir = 1                                                                                                #
                    elif player.hitBox[0] < koopa.hitBox[0] + koopa.hitBox[2] < player.hitBox[0] + player.hitBox[2]:                 #
                        koopa.dir = -1                                                                                               #
            if (player.hitBox[1] < koopa.hitBox[1] < player.hitBox[1] + player.hitBox[3] <= koopa.hitBox[1] + 8 and                  #
                (player.falling_count != 1 or player.jump_count_down != 0)):                                                         #
                s_stomp.play()                                                                                                       #
                player.squish_jump()                                                                                                 #
                if not koopa.shell:                                                                                                  #
                    koopa.shell = True                                                                                               #
                    koopa.y += 8                                                                                                     #
                    koopa.shell_stop = True                                                                                          #
                    score += 100                                                                                                     #
                    pts.append(Points(koopa.x + bgX, koopa.y - 8, 100))                                                              #
                else:                                                                                                                #
                    if koopa.shell_slide:                                                                                            #
                        koopa.shell_stop = True                                                                                      #
                        koopa.shell_slide = False                                                                                    #
                        score += 100                                                                                                 #
                        pts.append(Points(koopa.x + bgX, koopa.y - 8, 100))                                                          #
                    elif koopa.shell_stop:                                                                                           #
                        koopa.shell_stop = False                                                                                     #
                        koopa.shell_slide = True                                                                                     #
                        score += 100                                                                                                 #
                        pts.append(Points(koopa.x + bgX, koopa.y - 8, 100))                                                          #
                        if player.hitBox[0] + player.hitBox[2] > koopa.hitBox[0] > player.hitBox[0]:                                 #
                            koopa.dir = 1                                                                                            #
                        elif player.hitBox[0] < koopa.hitBox[0] + koopa.hitBox[2] < player.hitBox[0] + player.hitBox[2]:             #
                            koopa.dir = -1                                                                                 # #########

    # ----------------------------------------------------------------------------------------------------------------- #
    # ---------------------------------------------CONTINUOUS FUNCTIONS------------------------------------------------ #

    if bullet_buff > 0:           # ##
        bullet_buff += 1             # ### for regulating bullet intervals
    if bullet_buff > 10:             #
        bullet_buff = 0           # ##

    if player.death:                                                    # ###############
        if death_height_count_up < 8:                                                   #
            player.y -= (death_height_count_up ** 2) / 10                               #
            death_height_count_up += 0.5                                                #
        else:                                                                           #
            if player.y < 226:                                                          #
                player.y += (death_height_count_down ** 2) / 50                         #
                death_height_count_down += 0.5                                          #
            else:                                                                       #
                if not time_up_fall and fall_timer + 1 <= 200:                          #
                    fall_timer += 1                                                     # #### for death fall due to enemy damage
                else:                                                                   #
                    fall_timer = 0                                                      #
                    death_height_count_down = 0                                         #
                    death_height_count_up = 3                                           #
                    if player.lives == 1:                                               #
                        player.game_over = True                                         #
                    else:                                                               #
                        player.lives -= 1                                               #
                        player.reset = True                                             #
                        player.death = False                            # ###############

    if player.hole_falling:                                             # ###############
        if player.y <= 225:                                                             #
            player.y += (hole_fall_height_count ** 2) / 10                              #
            hole_fall_height_count += 1                                                 #
        else:                                                                           #
            if fall_timer + 1 <= 200:                                                   #
                fall_timer += 1                                                         #
            else:                                                                       # #### for hole fall
                fall_timer = 0                                                          #
                hole_fall_height_count = 5                                              #
                if player.lives == 1:                                                   #
                    player.game_over = True                                             #
                else:                                                                   #
                    player.hole_falling = False                                         #
                    player.reset = True                                                 #
                    player.lives -= 1                                   # ###############

    if player.shrink or player.blink:                                   # ###############
        player.blink = True                                                             #
        if player.blink_timer <= 100:                                                   #
            if player.blink_timer % 3 == 0:                                             #
                player.dis = True                                                       #
            else:                                                                       # #### for blinking from damage
                player.dis = False                                                      #
            player.blink_timer += 1                                                     #
        else:                                                                           #
            player.blink_timer = 0                                                      #
            player.dis = False                                                          #
            player.blink = False                                        # ###############

    # -------------------------------------------------BUTTON CONTROLS------------------------------------------------- #

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:                              # #######
            pygame.quit()                                                                           # ##### for quitting
            sys.exit()                                                                      # #######
        if not player.grow and not player.shrink:
            if event.type == pygame.KEYDOWN:                                                # #######
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:                           #
                    player.face_switch = True                                                       #
                    player.left = True                                                              #
                    player.right = False                                                            # ##### for face switching
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:                        #
                    player.face_switch = True                                                       #
                    player.left = False                                                             #
                    player.right = True                                                     # #######
                if event.key == pygame.K_p:                                                 # #######
                    pygame.mixer.music.pause()                                                      # ##### for pausing
                    s_pause.play()                                                                  #
                    pause = True                                                            # #######

    if not player.end_m:                                                                            # #######
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (player.level == 2 or player.level == 4):          # ##### for ducking
            player.duck = True                                                                      # #######

        if not player.death and not player.hole_falling:                                    # #######
            if not player.isJump:                                                                   #
                if keys[pygame.K_UP] or keys[pygame.K_w]:                                           #
                    if player.level == 1 or player.level == 3:                                      #
                        s_jump_small.play()                                                         #
                    elif player.level == 2 or player.level == 4:                                    #
                        s_jump_big.play()                                                           #
                    player.isJump = True                                                            #
                    walkCount = 0                                                                   #
            elif not player.grow:                                                                   #
                if player.jump_count_up >= 0:                                                       #
                    player.y -= (player.jump_count_up ** 2) / 10                                    # ##### for jumping
                    player.jump_count_up -= 0.5                                                     #
                else:                                                                               #
                    if player.y < player.ground_level or player.y < 255:                            #
                        if player.y + (player.jump_count_down ** 2) / 10 > player.ground_level:     #
                            player.y = player.ground_level                                          #
                            player.jump_count_down = 0                                              #
                            player.isJump = False                                                   #
                            player.jump_count_up = 10                                               #
                        else:                                                                       #
                            player.y += (player.jump_count_down ** 2) / 10                          #
                            player.jump_count_down += 0.5                                   # #######

        if ((keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x > player.vel and not player.duck and         # #######
                not player.collide_l and not player.death and not player.grow and not player.shrink and                 #
                not player.hole_falling):                                                                               #
            if run_inertia <= player.vel:                                                                               #
                run_inertia += 0.1                                                                                      # ##### for left
            player.x -= run_inertia                                                                                     #
            player.left = True                                                                                          #
            player.right = False                                                                                        #
            player.standing = False                                                                                     #
            player.collide_r = False                                                                            # #######

        elif ((keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not player.duck and not player.collide_r and       # #######
              not player.death and not player.grow and not player.shrink and not player.hole_falling):                  #
            if run_inertia <= player.vel:                                                                               #
                run_inertia += 0.1                                                                                      #
            if player.x + player.width < 150 - player.vel:                                                              #
                player.x += run_inertia                                                                                 # ###### for right
            elif player.x + player.width >= 150 - player.vel:            # for background scrolling                     #
                bgX -= run_inertia                                                                                      #
            player.right = True                                                                                         #
            player.left = False                                                                                         #
            player.standing = False                                                                                     #
            player.collide_l = False                                                                            # #######

        elif not player.death:                                                                                  # #######
            if run_inertia - 1 >= 0:                                                                                    #
                if player.right and player.x + player.width <= 200 - player.vel and not player.collide_r:               #
                    run_inertia -= 0.3                                                                                  #
                    player.x += run_inertia                                                                             # ###### for inertia
                elif player.left and player.x > player.vel and not player.collide_l:                                    #
                    run_inertia -= 0.3                                                                                  #
                    player.x -= run_inertia                                                                             #
            player.standing = True                                                                                      #
            player.walkCount = 0                                                                                # #######

        if ((keys[pygame.K_SPACE] or keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]) and bullet_buff == 0 and   # #######
            (player.level == 3 or player.level == 4) and not player.shrink and not player.grow and                      #
            not player.hole_falling):                                                                                   #
            if player.left:                                                                                             #
                dir = -1                                                                                                #
            else:                                                                                                       # ###### for shooting
                dir = 1                                                                                                 #
            if len(bul) < 2:                                                                                            #
                s_fireball.play()                                                                                       #
                bul.append(Bullet(player.x + player.width//2 - 4 - bgX, player.y + player.height//2 - 3, dir))          #
                player.shoot = True                                                                                     #
            bullet_buff = 1                                                                                     # #######

    # ----------------------------------------CONTINUOUS OBJECT MOVEMENTS---------------------------------------------- #

    else:                                                                                                       # #######
        pygame.mixer.music.stop()                                                                                       #
        pygame.mixer.music.load(os.path.join('Sounds', 'time_count.wav'))                                               #
        if not flag_score:                                          # #######                                           #
            if f_p.y + f_p.height - player.y < 20:                          #                                           #
                flag_score = 100                                            #                                           #
            elif 20 <= f_p.y + f_p.height - player.y < 40:                  #                                           #
                flag_score = 400                                            #                                           #
            elif 40 <= f_p.y + f_p.height - player.y < 80:                  #                                           #
                flag_score = 800                                            # #### scoring ranges for flag              #
            elif 80 <= f_p.y + f_p.height - player.y < 100:                 #                                           #
                flag_score = 1000                                           #                                           #
            elif 100 <= f_p.y + f_p.height - player.y < 120:                #                                           #
                flag_score = 3000                                           #                                           #
            elif 120 <= f_p.y + f_p.height - player.y < 130:                #                                           #
                flag_score = 4000                                           #                                           #
            elif 130 <= f_p.y + f_p.height - player.y:                      #                                           #
                flag_score = 5000                                   # #######                                           #
        if not pts:                                                                                                     #
            pts.append(Points(fb[-1].x + 12, fb[-1].y - 12, flag_score))                                                #
        if rap_start_timer == 5:                                                                                        #
            s_flagpole.play()                                                                                           #
            player.rappelling = True                                                                                    #
            rap_start_timer += 1                                                                                        #
        elif rap_start_timer < 7:                                                                                       #
            rap_start_timer += 1                                                                                        #
        if (player.hitBox[1] + player.hitBox[3] < fb[45].hitBox[1] - 1 or                                               #
            f_c.hitBox[1] + f_c.hitBox[3] < fb[45].hitBox[1] - 1):                                                      #
            if player.hitBox[1] + player.hitBox[3] < fb[45].hitBox[1] - 1:                                              #
                player.y += 1                                                                                           #
            if f_c.hitBox[1] + f_c.hitBox[3] < fb[45].hitBox[1] - 1:                                                    #
                f_c.y += 1                                                                                              #
                pts[0].y -= 1                                                                                           #
        else:                                                                                                           #
            if player.rappelling:                                                                                       #
                score += flag_score                                                                                     #
            player.rappelling = False                                                                                   #
            if rap_switch_timer == 20:                                                                                  # ###### end actions
                player.rap_switch = True                                                                                #
            elif rap_switch_timer == 19:                                                                                #
                player.x += player.width                                                                                #
                rap_switch_timer += 1                                                                                   #
            else:                                                                                                       #
                rap_switch_timer += 1                                                                                   #
        if player.rap_switch:                                                                                           #
            if end_jump_timer == 20:                                                                                    #
                player.end_jump = True                                                                                  #
                if player.y < player.ground_level:                                                                      #
                    player.y += 0.5                                                                                     #
                    player.x += end_jump_impulse ** 2 // 50                                                             #
                    end_jump_impulse -= 1                                                                               #
                else:                                                                                                   #
                    player.y = player.ground_level                                                                      #
                    player.end_jump = False                                                                             #
                    if not player.end_walk:                                                                             #
                        s_stage_clear.play()                                                                            #
                    player.end_walk = True                                                                              #
                    if player.hitBox[0] + player.hitBox[2] - bgX < 3280:                                                #
                        player.x += 0.5                                                                                 #
                        bgX -= 0.2                                                                                      #
                    else:                                                                                               #
                        player.dis = True                                                                               #
                        if time:                                                                                        #
                            time -= 1                                                                                   #
                            score += 100                                                                                #
                            pygame.mixer.music.play(-1)                                                                 #
                        else:                                                                                           #
                            pygame.mixer.music.stop()                                                                   #
                            if v_flag_timer == 60:                                                                      #
                                if f_v.y > 106:                                                                         #
                                    f_v.y -= 1                                                                          #
                                else:                                                                                   #
                                    if end_timer + 1 <= 200:                                                            #
                                        end_timer += 1                                                                  #
                                    else:                                                                               #
                                        end_timer = 0                                                                   #
                                        player.game_over = True                                                         #
                            elif v_flag_timer == 59:                                                                    #
                                score += player.lives * 2000                                                            #
                                pts.append(Points(f_v.x + bgX, f_v.y - 15, player.lives*2000))                          #
                                v_flag_timer += 1                                                                       #
                            else:                                                                                       #
                                v_flag_timer += 1                                                                       #
            else:                                                                                                       #
                end_jump_timer += 1                                                                             # #######

    for x in bb:                                                     # #######
        if x.block_push:                                                     #
            if x.push_count >= -4:                                           #
                mul = -1                                                     #
                if x.push_count > 0:                                         #
                    mul = 1                                                  #
                x.y -= mul*(x.push_count ** 2 / 10)                          #
                x.push_count -= 0.5                                          #
            else:                                                            #
                x.push_count = 4                                             #
                x.block_push = False                                         #
                                                                             #
    for b in broken_bs:                                                      #
        if b.y < 224:                                                        # #### brick movement functions
            if b.fall_lr != 0:                                               #
                mul = -1                                                     #
                if b.piece == 0 or b.piece == 2:                             #
                    mul = 1                                                  #
                b.x -= mul * (b.fall_lr ** 2 / 10)                           #
                b.fall_lr -= 0.1                                             #
            if b.fall_u != 0:                                                #
                b.y -= b.fall_u ** 2 / 10                                    #
                b.fall_u -= 0.5                                              #
            else:                                                            #
                b.y += b.fall_d ** 2 / 10                                    #
                b.fall_d += 0.5                                              #
        else:                                                                #
            broken_bs.remove(b)                                      # #######

    for box in mb:                                                   # #######
        if box.block_push:                                                   #
            if box.push_count >= -3:                                         #
                mul = -1                                                     #
                if box.push_count > 0:                                       #
                    mul = 1                                                  # #### mystery box movement function
                box.y -= mul*(box.push_count ** 2 / 10)                      #
                box.push_count -= 0.5                                        #
            else:                                                            #
                box.push_count = 3                                           #
                box.block_push = False                               # #######

    for coin in c:                                                   # #######
        if coin.jump_h >= -9:                                                #
            mul = -1                                                         #
            if coin.jump_h > 0:                                              #
                mul = 1                                                      # #### coin jump function
            coin.y -= mul*(coin.jump_h ** 2 / 10)                            #
            coin.jump_h -= 0.5                                               #
        else:                                                                #
            pts.append(Points(coin.x + bgX, coin.y - 8, 200))                #
            c.remove(coin)                                           # #######

    for mush in m:                                                                              # #######
        if mush.hitBox[1] + mush.hitBox[3] > mb[v_m].hitBox[1] and mush.rise:                           #
            mush.y -= 0.5                                                                               #
        else:                                                                                           #
            mush.rise = False                                                                           #
            if ((mush.hitBox[0] + mush.hitBox[2] > p[0].hitBox[0] and v_m == 1) or                      #
                (mush.hitBox[0] + mush.hitBox[2] > fb[0].hitBox[0] and v_m == 7)):                      #
                mush.switch = True                                                                      #
            if mush.switch:                                                                             #
                mush.dir *= -1                                                                          #
                mush.switch = False                                                                     #
            mush.x += mush.dir                                                                          #
            if ((mush.hitBox[0] > bb[2].hitBox[0] + bb[2].hitBox[2] and v_m == 1) or                    #
                (mush.hitBox[0] > bb[4].hitBox[0] + bb[4].hitBox[2] and v_m == 4) or                    #
                (mush.hitBox[0] > mb[7].hitBox[0] + mb[7].hitBox[2] and v_m == 7)):                     # ##### Mushroom movement functions
                if mush.y < f_1_3:                                                                      #
                    if mush.y + (mush.fall_count ** 2 / 10) > f_1_3:                                    #
                        mush.y = f_1_3                                                                  #
                        mush.fall_count = 1                                                             #
                    else:                                                                               #
                        mush.y += mush.fall_count ** 2 / 10                                             #
                        mush.fall_count += 0.5                                                          #
            if (h[1].x < mush.hitBox[0] + mush.hitBox[2] - bgX < h[1].x + h[1].width and                #
                    h[1].x + h[1].width > mush.hitBox[0] - bgX > h[1].x):                               #
                if mush.y < 224:                                                                        #
                    mush.y += mush.fall_count ** 2 / 10                                                 #
                    mush.fall_count += 0.5                                                              #
        if mush.x + mush.width < 0 or mush.y > 223:                                                     #
            m.remove(mush)                                                                      # #######

    for mush in lm:                                                                             # #######
        if mush.hitBox[1] + mush.hitBox[3] > ib.hitBox[1] and mush.rise:                                #
            mush.y -= 0.5                                                                               #
        else:                                                                                           #
            mush.rise = False                                                                           #
            mush.x += 1                                                                                 #
            if mush.hitBox[0] > ib.hitBox[0] + ib.hitBox[2]:                                            #
                if mush.y < f_1_3:                                                                      #
                    if mush.y + (mush.fall_count ** 2 / 10) > f_1_3:                                    #
                        mush.y = f_1_3                                                                  #
                        mush.fall_count = 1                                                             # ##### 1up Mushroom movement functions
                    else:                                                                               #
                        mush.y += mush.fall_count ** 2 / 10                                             #
                        mush.fall_count += 0.5                                                          #
            if (h[0].x < mush.hitBox[0] + mush.hitBox[2] - bgX < h[0].x + h[0].width and                #
                    h[0].x + h[0].width > mush.hitBox[0] - bgX > h[0].x):                               #
                if mush.y < 224:                                                                        #
                    mush.y += mush.fall_count ** 2 / 10                                                 #
                    mush.fall_count += 0.5                                                              #
        if mush.y > 223:                                                                                #
            lm.remove(mush)                                                                     # #######

    for fl in f:                                                                                # #######
        if fl.hitBox[1] + fl.hitBox[3] > mb[v_f].hitBox[1] and fl.rise:                                 #
            fl.y -= 0.5                                                                                 #
        else:                                                                                           # ##### Flower movement functions
            fl.rise = False                                                                             #
        if fl.x + fl.width < -bgX:                                                                      #
            f.remove(fl)                                                                        # #######

    for bullet in bul:                                                                          # #######
        if not bullet.hit:                                                                              #
            bullet.x += 4 * bullet.dir                                                                  #
            if not bullet.bounce:                                                                       #
                bullet.y += 2.5                                                                         #
            else:                                                                                       # ##### Bullet movement functions
                if bullet.bounce_h > 0:                                                                 #
                    bullet.y -= 1                                                                       #
                    bullet.bounce_h -= 1                                                                #
                else:                                                                                   #
                    bullet.bounce_h = 7                                                                 #
                    bullet.bounce = False                                                       # #######

    for goom in g:                                                                              # #######
        if goom.move and not goom.squished and not goom.hit:                                            #
            if goom.switch:                                                                             #
                goom.dir *= -1                                                                          #
                goom.switch = False                                                                     #
            goom.x += goom.dir * 0.5                                                                    #
            if goom.hitBox[0] + goom.hitBox[2] < bb[5].hitBox[0]:                                       #
                if goom.hitBox[1] + goom.hitBox[3] < bb[4].hitBox[1]:                                   #
                    if goom.y + (goom.fall_count ** 2 / 10) > bb[4].hitBox[1] - goom.height:            #
                        goom.y = bb[4].hitBox[1] - goom.height                                          #
                        goom.fall_count = 1                                                             #
                    else:                                                                               #
                        goom.y += goom.fall_count ** 2 / 10                                             #
                        goom.fall_count += 0.5                                                          #
            if bb[3].broken:                                                                            #
                if goom.hitBox[0] + goom.hitBox[2] < mb[4].hitBox[0]:                                   #
                    if goom.y < f_1_3:                                                                  #
                        if goom.y + (goom.fall_count ** 2 / 10) > f_1_3:                                #
                            goom.y = f_1_3                                                              #
                            goom.fall_count = 1                                                         #
                        else:                                                                           #
                            goom.y += goom.fall_count ** 2 / 10                                         #
                            goom.fall_count += 0.5                                                      #
            else:                                                                                       #
                if goom.hitBox[0] + goom.hitBox[2] < bb[3].hitBox[0]:                                   # ##### Goomba movement functions
                    if goom.y < f_1_3:                                                                  #
                        if goom.y + (goom.fall_count ** 2 / 10) > f_1_3:                                #
                            goom.y = f_1_3                                                              #
                            goom.fall_count = 1                                                         #
                        else:                                                                           #
                            goom.y += goom.fall_count ** 2 / 10                                         #
                            goom.fall_count += 0.5                                                      #
            if ((h[0].x < goom.hitBox[0] + goom.hitBox[2] - bgX < h[0].x + h[0].width and               #
                    h[0].x + h[0].width > goom.hitBox[0] - bgX > h[0].x) or                             #
                    (h[1].x < goom.hitBox[0] + goom.hitBox[2] - bgX < h[1].x + h[1].width and           #
                    h[1].x + h[1].width > goom.hitBox[0] - bgX > h[1].x)):                              #
                if goom.y < 224:                                                                        #
                    goom.y += goom.fall_count ** 2 / 10                                                 #
                    goom.fall_count += 0.5                                                              #
        if goom.squished:                                                                               #
            if goom.dis_time < 60:                                                                      #
                goom.dis_time += 1                                                                      #
            else:                                                                                       #
                g.remove(goom)                                                                          #
        if goom.hit:                                                                                    #
            goom.y -= 2                                                                                 #
            if goom.y < 224:                                                                            #
                goom.y += goom.fall_count ** 2 / 10                                                     #
                goom.fall_count += 0.5                                                                  #
        if goom.x + goom.width < 0 or goom.y > 223:                                                     #
            g.remove(goom)                                                                      # #######

    for koopa in kt:                                                                            # #######
        if koopa.move and not koopa.hit:                                                                #
            if not koopa.shell:                                                                         #
                koopa.x += koopa.dir * 0.5                                                              #
            if (h[1].x < koopa.hitBox[0] + koopa.hitBox[2] - bgX < h[1].x + h[1].width and              #
                    h[1].x + h[1].width > koopa.hitBox[0] - bgX > h[1].x):                              #
                if koopa.y < 224:                                                                       #
                    koopa.y += koopa.fall_count ** 2 / 10                                               #
                    koopa.fall_count += 0.5                                                             #
        if koopa.shell:                                                                                 #
            if koopa.shell_slide and not koopa.hit:                                                     # ##### Koopa Troopa Movements
                if koopa.switch:                                                                        #
                    koopa.dir *= -1                                                                     #
                    koopa.switch = False                                                                #
                koopa.x += koopa.dir * 3.5                                                              #
        if koopa.hit:                                                                                   #
            koopa.y -= 2                                                                                #
            if koopa.y < 224:                                                                           #
                koopa.y += koopa.fall_count ** 2 / 10                                                   #
                koopa.fall_count += 0.5                                                                 #
        if koopa.y > 223:                                                                               #
            kt.remove(koopa)                                                                    # #######

    for pt in pts:                                                   # #######
        if pt.amount is not flag_score:                                      #
            if pt.timer + 1 <= 150:                                          #
                pt.timer += 2                                                # #### for floating points' text
                pt.y -= 0.5                                                  #
            else:                                                            #
                pts.remove(pt)                                       # #######

    if player.reset and player.y >= 225:                             # #######
        player.x = 40                                                        #
        player.blink = True                                                  #
        bgX = 0                                                              #
        player.jump_count_up = 10                                            #
        player.jump_count_down = 0                                           #
        run_inertia = 0                                                      # #### for resetting the position after death
        player.level = 1                                                     #
        player.collide_r = False                                             #
        player.collide_l = False                                             #
        player.right = True                                                  #
        player.left = False                                                  #
        player.reset = False                                                 #
        load = True                                                  # #######

    if not player.end_m and not player.death:                              # ########
        if time_regulator < speed:                                                  #
            time_regulator += 3                                                     #
        else:                                                                       #
            time -= 1                                                               #
            time_regulator = 0                                                      #
        if time == 0:                                                               #
            player.level = 1                                                        #
            time_up_fall = True                                                     # #### game time logic
            player.enemy_damage()                                                   #
            time_up = True                                                          #
        else:                                                                       #
            time_up_fall = False                                                    #
        if time == 100 and time_regulator == 0:                                     #
            pygame.mixer.music.pause()                                              #
            s_warning.play()                                                        #
            warning = True                                                 # ########

    clock.tick(speed)
    redrawWindow()
