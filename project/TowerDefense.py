import pygame
import Helper
import UI
import Path
import math
import Player
import GameObject


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('TowerDefense.py - Grundkurs Python WS15/16')

    state = Helper.STATESELECT

    # Initialise Field
    fields = Path.Field(Helper.FIELDSIZE, Helper.FIELDSTART, Helper.FIELDEND)
    pathdict = fields.getpath()

    player = Player.Player(Helper.PLAYERDATA)

    # Initialise UI
    ui = initUI()

    background = pygame.image.load("Images/background.png").convert()
    screen.blit(background, pygame.Rect(0, 0, 600, 800))

    pygame.display.flip()

    clock = pygame.time.Clock()
    FPS = 60
    speed = 1

    turrets = []
    projectiles = []
    wave = GameObject.Wave(Helper.WAVES[0], Helper.animations(pygame, "Images/GenericEnemy.png"),
                           pathdict, (Helper.FIELDSIZE / 2, -Helper.FIELDSTART))

    preview = None
    shift = False

    info = None

    console_text = [Helper.CONSOLESTART]

    level = 0

    myfont = pygame.font.SysFont("Verdana", 11)

    label_score = UI.Text(Helper.LABELPOS["score"], myfont)
    label_lives = UI.Text(Helper.LABELPOS["lives"], myfont)
    label_money = UI.Text(Helper.LABELPOS["money"], myfont)
    label_level = UI.Text(Helper.LABELPOS["level"], myfont)
    label_console = UI.Text(Helper.LABELPOS["console"], myfont)
    label_info = UI.Text(Helper.LABELPOS["info"], myfont)
    label_upgrade = UI.Text(Helper.LABELPOS["upgrade"], myfont)

    # Event loop
    while 1:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                shift = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
                speed = 10

            if event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT:
                shift = False

            if event.type == pygame.KEYUP and event.key == pygame.K_LCTRL:
                speed = 1

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    click = ui.click(event.pos)

                    if click == Helper.STATESELECT:
                        pos = Helper.postocoord(event.pos)

                        if state == Helper.STATETOWER1:
                            if not outsideoffield(pos):
                                image = pygame.image.load(Helper.TOWER1DATA["image"]).convert_alpha()
                                image = pygame.transform.scale(image,
                                                               (Helper.FIELDCELLWIDTH * 2, Helper.FIELDCELLHEIGHT * 2))
                                imagew = pygame.image.load(Helper.TOWER1DATA["poss"]).convert_alpha()
                                imagew = pygame.transform.scale(imagew,
                                                                (Helper.FIELDCELLWIDTH * 2, Helper.FIELDCELLHEIGHT * 2))
                                turret = GameObject.Tower(image, imagew, pos, Helper.TOWER1DATA)
                                if fields.available(pos, turret.size()) and player.getMoney() >= turret.getCost():
                                    turrets.append(turret)
                                    player.addMoney(turret.getCost() * -1)
                                    for i in range(0, turret.size()):
                                        for j in range(0, turret.size()):
                                            fields.deactivate((pos[0] + i, pos[1] + j), turret)
                                    pathdict = fields.getpath()
                                    preview = getPreview(player, fields, event.pos, Helper.TOWER1DATA)
                                    if info is not None:
                                        info.deselect()
                                    info = turret

                        if state == Helper.STATETOWER2:
                            if not outsideoffield(pos):
                                image = pygame.image.load(Helper.TOWER2DATA["image"]).convert_alpha()
                                image = pygame.transform.scale(image,
                                                               (Helper.FIELDCELLWIDTH * 2, Helper.FIELDCELLHEIGHT * 2))
                                imagew = pygame.image.load(Helper.TOWER2DATA["poss"]).convert_alpha()
                                imagew = pygame.transform.scale(imagew,
                                                                (Helper.FIELDCELLWIDTH * 2, Helper.FIELDCELLHEIGHT * 2))
                                turret = GameObject.Tower(image, imagew, pos, Helper.TOWER2DATA)
                                if fields.available(pos, turret.size()) and player.getMoney() >= turret.getCost():
                                    turrets.append(turret)
                                    player.addMoney(turret.getCost() * -1)
                                    for i in range(0, turret.size()):
                                        for j in range(0, turret.size()):
                                            fields.deactivate((pos[0] + i, pos[1] + j), turret)
                                    pathdict = fields.getpath()
                                    preview = getPreview(player, fields, event.pos, Helper.TOWER2DATA)
                                    if info is not None:
                                        info.deselect()
                                    info = turret

                        if state == Helper.STATESELECT:
                            if info is not None:
                                info.deselect()
                            info = fields.getTower(pos)

                    if click is not None:
                        if not shift:
                            state = click
                            preview = None

                    if click == Helper.STATEGO and wave.done():
                        if level < Helper.MAXLEVEL:
                            level += 1
                            wave = GameObject.Wave(Helper.WAVES[level],
                                                   Helper.animations(pygame, Helper.WAVES[level]["im"]),
                                                   pathdict, (Helper.FIELDSIZE / 2, -Helper.FIELDSTART))
                            state = Helper.STATESELECT
                            console_text.append(
                                "Level " + str(level) + ": " + str(Helper.WAVES[level]["type"]) + " enemies - "
                                + str(Helper.WAVES[level]["hp"]) + " hp, worth " + str(
                                    Helper.WAVES[level]["score"]) + "g each.")
                        if level == Helper.MAXLEVEL:
                            console_text.append("You did it! Last Level incoming.")

                    if click == Helper.STATEDELETE and info is not None:
                        player.addMoney(info.sell())
                        turrets.remove(info)
                        for i in range(0, info.size()):
                            for j in range(0, turret.size()):
                                fields.activate((info.pos()[0] + i, info.pos()[1] + j))
                        info = None
                        pathdict = fields.getpath()
                        state = Helper.STATESELECT

                    if click == Helper.STATEUPGRADE and info is not None:
                        if player.getMoney() >= info.getCost():
                            player.addMoney(-info.getCost())
                            info.upgrade()
                            state = Helper.STATESELECT

                    if click == Helper.STATETOWER1:
                        if info is not None:
                            info.deselect()
                        info = GameObject.Tower(None, None, (None, None), Helper.TOWER1DATA)

                    if click == Helper.STATETOWER2:
                        if info is not None:
                            info.deselect()
                        info = GameObject.Tower(None, None, (None, None), Helper.TOWER2DATA)

                if event.button == 3:
                    if info is not None:
                        info.deselect()
                    info = None
                    state = Helper.STATESELECT
                    preview = None

            if event.type == pygame.MOUSEMOTION:
                ui.update(event.pos)
                if state == Helper.STATETOWER1:
                    preview = getPreview(player, fields, event.pos, Helper.TOWER1DATA)
                if state == Helper.STATETOWER2:
                    preview = getPreview(player, fields, event.pos, Helper.TOWER2DATA)

        if player.getLives() > 0:
            lives = wave.update(pathdict, speed)
            if lives > 0:
                player.removeLives(lives)
                console_text.append("Lives remaining: " + str(player.getLives()))
            elif lives == -1:
                console_text.append("You are blocking every possible path!")
                console_text.append("Better sell a tower and rework your maze.")

            minionpos = wave.minionpositions()
            for t in turrets:
                for m in minionpos:
                    if math.sqrt(math.pow((t.pos()[0] + 1 - m[0]), 2) + math.pow((t.pos()[1] + 1 - m[1]),
                                                                                 2)) <= t.getRange():
                        shoot = t.shoot()
                        if shoot[0]:
                            value = wave.hit(minionpos.index(m), shoot[1], shoot[2], shoot[3])
                            player.addScore(value)
                            player.addMoney(value)
                            p = GameObject.projectile(t.pos(),
                                                      m, Helper.FIELDDATA, Helper.SHOOTDURATION,
                                                      pygame.image.load(
                                                          Helper.PROJETILE[t.projectile()]).convert_alpha())
                            projectiles.append(p)
                            break
                t.update(speed)

        else:
            console_text.append("Game over! You got wrecked, sorry.")

        draw(screen, ui, turrets, wave, background, preview, projectiles, speed)

        if console_text.__len__() > 3:
            label_console.setText([console_text[console_text.__len__() - 3],
                                   console_text[console_text.__len__() - 2],
                                   console_text[console_text.__len__() - 1]]).draw(screen)
        else:
            label_console.setText(console_text).draw(screen)

        if info is not None:
            if info.pos()[0] is not None:
                info.select()
                pos = info.pos()
                pos = ((pos[0] + 1) * Helper.FIELDCELLWIDTH + Helper.FIELDOFFSETX,
                       (pos[1] + 1) * Helper.FIELDCELLHEIGHT + Helper.FIELDOFFSETY)
                pygame.draw.circle(screen, (255, 255, 255), pos, info.getRange() * Helper.FIELDCELLWIDTH, 1)
                upgrade_text = info.getUpgrade()
                label_upgrade.setText(upgrade_text).draw(screen)
                ui.activ()
            else:
                ui.deactiv()
            info_text = info.getInfo()
            label_info.setText(info_text).draw(screen)
        else:
            ui.deactiv()

        if level == Helper.MAXLEVEL and wave.done():
            console_text.append("Congratulations! You won.")

        label_score.setText([str(player.getScore())]).draw(screen)
        label_lives.setText([str(player.getLives())]).draw(screen)
        label_money.setText([str(player.getMoney())]).draw(screen)
        label_level.setText([str(level)]).draw(screen)

        pygame.display.flip()


def initUI():
    ui = UI.Handler(UI.Field(Helper.FIELDUIDATA))

    ui.addButton(UI.Button(Helper.TOWER1BUTTON, pygame.image.load(Helper.TOWER1BUTTON["imp"]).convert_alpha(),
                           pygame.image.load(Helper.TOWER1BUTTON["ima"]).convert_alpha(), True))

    ui.addButton(UI.Button(Helper.TOWER2, pygame.image.load(Helper.TOWER2["imp"]).convert_alpha(),
                           pygame.image.load(Helper.TOWER2["ima"]).convert_alpha(), True))

    ui.addButton(UI.Button(Helper.GO, pygame.image.load(Helper.GO["imp"]).convert_alpha(),
                           pygame.image.load(Helper.GO["ima"]).convert_alpha(), True))

    ui.addButton(UI.Button(Helper.DELETE, pygame.image.load(Helper.DELETE["imp"]).convert_alpha(),
                           pygame.image.load(Helper.DELETE["ima"]).convert_alpha(), False))

    ui.addButton(UI.Button(Helper.UPGRADE, pygame.image.load(Helper.UPGRADE["imp"]).convert_alpha(),
                           pygame.image.load(Helper.UPGRADE["ima"]).convert_alpha(), False))

    return ui


def draw(screen, ui, turrets, wave, background, preview, projectiles, speed):
    screen.blit(background, (0, 0))

    ui.draw(screen)
    wave.draw(screen, Helper.FIELDDATA)
    for t in turrets:
        t.draw(screen, Helper.FIELDDATA)
    if preview is not None:
        preview.draw(screen, Helper.FIELDDATA)
        pos = preview.pos()
        pos = ((pos[0] + 1) * Helper.FIELDCELLWIDTH + Helper.FIELDOFFSETX,
               (pos[1] + 1) * Helper.FIELDCELLHEIGHT + Helper.FIELDOFFSETY)
        pygame.draw.circle(screen, (255, 255, 255), pos, preview.getRange() * Helper.FIELDCELLWIDTH, 1)
    for p in projectiles:
        if p.update(speed):
            p.draw(screen)
        else:
            projectiles.remove(p)


def outsideoffield(tpos):
    return tpos[0] > Helper.FIELDSIZE - 2 or tpos[1] > Helper.FIELDSIZE - 2 or tpos[0] < 0 or tpos[1] < 0


def getPreview(player, fields, mousepos, data):
    tpos = Helper.postocoord(mousepos)
    image = pygame.image.load(data["image"]).convert_alpha()
    image = pygame.transform.scale(image, (Helper.FIELDCELLHEIGHT * 2, Helper.FIELDCELLWIDTH * 2))
    imagew = pygame.image.load(data["poss"]).convert_alpha()
    imagew = pygame.transform.scale(imagew, (Helper.FIELDCELLHEIGHT * 2, Helper.FIELDCELLWIDTH * 2))
    turret = GameObject.Tower(image, imagew, tpos, data)
    turret.setImage(imagew)
    if not (fields.available(tpos, turret.size()) and player.getMoney() >= turret.getCost()):
        image = pygame.transform.scale(pygame.image.load(data["imp"]).convert_alpha(),
                                       (Helper.FIELDCELLWIDTH * 2, Helper.FIELDCELLHEIGHT * 2))
        turret.setImage(image)
    preview = turret
    if outsideoffield(tpos):
        preview = None
    return preview


if __name__ == '__main__': main()
