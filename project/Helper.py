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

MAXLEVEL = 50

FIELDOFFSETX = 84
FIELDOFFSETY = 74
FIELDCELLWIDTH = 12
FIELDCELLHEIGHT = 12

SHOOTDURATION = 20

PROJETILE = {0: "Images/Projectile_Normal.png",
             1: "Images/Projectile_Freeze.png"}

FIELDDATA = {"offsetX": FIELDOFFSETX,
             "cellW": FIELDCELLWIDTH,
             "offsetY": FIELDOFFSETY,
             "cellH": FIELDCELLHEIGHT}

FIELDUIDATA = {"offsetX": FIELDOFFSETX,
               "offsetY": FIELDOFFSETY,
               "width": FIELDSIZE * FIELDCELLWIDTH,
               "height": FIELDSIZE * FIELDCELLHEIGHT,
               "statechange": STATESELECT}

PLAYERDATA = {"lives": 20,
              "money": 50}

TOWER1DATA = {"cost": 5,
              "cooldown": 60,
              "damage": 10,
              "freeze": 1,
              "freezeduration": 0,
              "range": 5,
              "image": "Images/Tower1.png",
              "imp": "Images/Tower1_Red.png",
              "poss": "Images/Tower1_White.png",
              "size": 2,
              "projectile": 0}

TOWER2DATA = {"cost": 5,
              "cooldown": 60,
              "damage": 2,
              "range": 5,
              "freeze": 2,
              "freezeduration": 50,
              "image": "Images/Tower2.png",
              "imp": "Images/Tower2_Red.png",
              "poss": "Images/Tower2_White.png",
              "size": 2,
              "projectile": 1}

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

GO = {"x": 408,
      "y": 518,
      "w": 60,
      "h": 60,
      "imp": "Images/Button_NextWave.png",
      "ima": "Images/Button_NextWave_Clicked.png",
      "statechange": STATEGO}

DELETE = {"x": 545,
      "y": 450,
      "w": 75,
      "h": 75,
      "imp": "Images/Button_Delete.png",
      "ima": "Images/Button_Delete_Clicked.png",
      "statechange": STATEDELETE}

UPGRADE = {"x": 645,
           "y": 450,
           "w": 75,
           "h": 75,
          "imp": "Images/Button_Upgrade.png",
          "ima": "Images/Button_Upgrade_Clicked.png",
           "statechange": STATEUPGRADE}

LABELPOS = {"score": (681, 74),
            "lives": (587, 113),
            "money": (681, 113),
            "console": (57, 525),
            "info": (550, 324),
            "level": (587, 74),
            "upgrade": (650, 324)}


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

WAVES = {0: {"hp": 0,
             "count": 0,
             "speed": 0,
             "score": 0,
             "goal": GOAL,
             "spawnrate": 0,
             "im": "Images/GenericEnemy.png",
             "type": 0}}

for i in range(1, MAXLEVEL + 1):
    WAVES.update({i: {"hp": 20 + int(i * 20 * 1.2),
                      "count": 15,
                      "speed": 20,
                      "score": 2,
                      "goal": GOAL,
                      "spawnrate": 30,
                      "im": "Images/GenericEnemy.png",
                      "type": "generic"}})
    if i % 2 == 0:
        WAVES[i].update({"im": "Images/FastEnemy.png"})
        WAVES[i].update({"speed": 10})
        WAVES[i].update({"type": "fast"})
    if i % 5 == 0:
        WAVES[i].update({"im": "Images/SlowEnemy.png"})
        WAVES[i].update({"speed": 30})
        WAVES[i].update({"count": 20})
        WAVES[i].update({"spawnrate": 60})
        WAVES[i].update({"hp": 50 + int(i * 40 * 1.4)})
        WAVES[i].update({"type": "slow"})
WAVES[MAXLEVEL].update({"count": 50})
WAVES[MAXLEVEL].update({"count": 50})
