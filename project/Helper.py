CONSOLESTART = "Welcome to Tower Defense!"

# gamestates
STATESELECT = 0  # if left click into field
STATETOWER1 = 1  # if left click on tower1 button
STATETOWER2 = 2  # if left click on tower2 button
STATETOWER3 = 3
STATEGO = 4
STATEDELETE = 5
STATEUPGRADE = 6

FIELDSIZE = 29
FIELDSTART = 3
FIELDEND = 5

GOAL = FIELDSIZE + FIELDEND - 1

FIELDOFFSETX = 84
FIELDOFFSETY = 74
FIELDCELLWIDTH = 12
FIELDCELLHEIGHT = 12

SHOOTDURATION = 20

FIELDDATA = {"offsetX": FIELDOFFSETX,
             "cellW": FIELDCELLWIDTH,
             "offsetY": FIELDOFFSETY,
             "cellH": FIELDCELLHEIGHT}

FIELDUIDATA = {"offsetX": FIELDOFFSETX,
               "offsetY": FIELDOFFSETY,
               "width": FIELDSIZE * FIELDCELLWIDTH,
               "height": FIELDSIZE * FIELDCELLHEIGHT,
               "statechange": STATESELECT}

PLAYERDATA = {"lifes": 20,
              "money": 50}

TOWER1DATA = {"cost": 5,
              "cooldown": 60,
              "damage": 10,
              "freeze": 1,
              "freezeduration": 0,
              "range": 5,
              "image": "Images/Tower1.png",
              "size": 2}

TOWER2DATA = {"cost": 5,
              "cooldown": 60,
              "damage": 2,
              "range": 5,
              "freeze": 2,
              "freezeduration": 50,
              "image": "Images/Tower2.png",
              "size": 2}

TOWER1BUTTON = {"x": 550,
                "y": 200,
                "w": 75,
                "h": 75,
                "imp": "Images/Button_Tower1_Normal.png",
                "ima": "Images/Button_Tower1_Clicked.png",
                "statechange": STATETOWER1}

TOWER2 = {"x": 650,
          "y": 200,
          "w": 75,
          "h": 75,
          "imp": "Images/Button_Tower2_Normal.png",
          "ima": "Images/Button_Tower2_Clicked.png",
          "statechange": STATETOWER2}

TOWER3 = {"x": 530,
          "y": 300,
          "w": 75,
          "h": 75,
          "imp": "Images/Button_Tower2_Normal.png",
          "ima": "Images/Button_Tower2_Clicked.png",
          "statechange": STATETOWER3}
GO = {"x": 399,
      "y": 508,
      "w": 75,
      "h": 75,
      "imp": "Images/Button_NextWave.png",
      "ima": "Images/Button_NextWave_Clicked.png",
      "statechange": STATEGO}

DELETE = {"x": 530,
      "y": 480,
      "w": 75,
      "h": 75,
      "imp": "Images/Button_Delete.png",
      "ima": "Images/Button_Delete_Clicked.png",
      "statechange": STATEDELETE}

UPGRADE = {"x": 640,
           "y": 480,
           "w": 75,
           "h": 75,
          "imp": "Images/Button_Upgrade.png",
          "ima": "Images/Button_Upgrade_Clicked.png",
           "statechange": STATEUPGRADE}
WAVES = {0: {"hp": 0,
             "count": 0,
             "speed": 0,
             "score": 0,
             "goal": GOAL,
             "spawnrate": 20,
             "im": "Images/minion.bmp"},
         1: {"hp": 50,
             "count": 10,
             "speed": 20,
             "score": 5,
             "goal": GOAL,
             "spawnrate": 20,
             "im": "Images/minion.bmp"},
         2: {"hp": 70,
             "count": 10,
             "speed": 20,
             "score": 5,
             "goal": GOAL,
             "spawnrate": 20,
             "im": "Images/minion.bmp"},
         3: {"hp": 120,
             "count": 10,
             "speed": 30,
             "score": 10,
             "goal": GOAL,
             "spawnrate": 20,
             "im": "Images/minion.bmp"},
         4: {"hp": 120,
             "count": 10,
             "speed": 30,
             "score": 10,
             "goal": GOAL,
             "spawnrate": 20,
             "im": "Images/minion.bmp"},
         5: {"hp": 120,
             "count": 50,
             "speed": 30,
             "score": 10,
             "goal": GOAL,
             "spawnrate": 20,
             "im": "Images/minion.bmp"},
         6: {"hp": 120,
             "count": 50,
             "speed": 30,
             "score": 10,
             "goal": GOAL,
             "spawnrate": 20,
             "im": "Images/minion.bmp"}}

LABELPOS = {"score": (681, 74),
            "lifes": (587, 113),
            "money": (681, 113),
            "console": (57, 525),
            "info": (600, 400),
            "level": (587, 74)}


def postocoord(pos):
    return (pos[0] - FIELDOFFSETX) / FIELDCELLWIDTH, (pos[1] - FIELDOFFSETY) / FIELDCELLHEIGHT


def animations(pygame, path):
    sprites = {}
    for i in range(0, 4):
        anim = []
        for j in range(0, 4):
            rect = pygame.Rect(25 * j, 25 * i, 25, 25)
            image = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
            image = image.convert_alpha()
            image.blit(pygame.image.load(path), (0, 0), rect)
            anim.append(image)
        sprites.update({i: anim})
    return sprites


