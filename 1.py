import random
import time
import pygame
pygame.init()


win = pygame.display.set_mode((500, 500))
win.fill((255, 255, 255))
pygame.display.set_caption('tic tac toe')


class BoardDisplay:
    def __init__(self , x , y , width , height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.open1 = False
        self.open2 = False
        self.use  = False

    def draw(self , win):
        if menu.clicked_menu:
            pygame.draw.rect(win , (255,255,255) , (self.x, self.y, self.width, self.height), 3)
            pygame.display.update()




class Player:
    def __init__(self):
        self.turn = True
        self.contain = []
        self.win = False


class StartMenu:
    def __init__(self):
        self.clicked_menu = False
        self.muli = False
        self.single = False



    def menudraw(self , win):
        font = pygame.font.SysFont('comicsans', 40, True)
        global text_multi
        global text_single
        text_single = font.render('single player', 1, (255, 255, 255))
        text_multi = font.render('multiplayer', 1, (255, 255, 255))
        if not self.clicked_menu:
            win.fill((0, 0, 0))
            pygame.draw.rect(win, (255, 255, 255), (170, 100, text_multi.get_width() + 10, text_multi.get_height() + 10), 2)
            win.blit(text_multi, (180, 110))
            pygame.display.update()
            pygame.draw.rect(win, (255, 255, 255), (160, 300, text_single.get_width() + 10, text_single.get_height() + 10), 2)
            win.blit(text_single, (170, 306))
            pygame.display.update()


def comp_move(win , run):
    for box in boxes:
        if box.use == False:
            player2.contain.append(box)
            check_win(win , run)

            if player2.win == True and box.use == False:
                player2.contain.pop()
                set_turn(boxes.index(box))
                box.use = True
                break
            else:
                player2.contain.pop()
    if not player2.win and player2.turn:
        for box in boxes:
            if box.use == False:
                player1.contain.append(box)
                check_win(win , run)

                if player1.win == True:
                    player1.contain.pop()
                    set_turn(boxes.index(box))
                    box.use = True
                    break
                else:
                    player1.contain.pop()

    player2.win = False
    player1.win = False
    while player2.turn:
        random.seed(time.time())
        choice = random.randint(0,8)
        if boxes[choice].use == False:
            set_turn(choice)
            boxes[choice].use = True
            break




def check_win(win , run):

    font = pygame.font.SysFont('comicsans' , 50 , True)
    countX1 = 0
    countY1 = 0
    countZ1 = 0
    countT1 = 0
    countX2 = 0
    countY2 = 0
    countZ2 = 0
    countT2 = 0
    if len(player1.contain) >= 3:
        for i in range(len(player1.contain)):
            countX1 = 0
            countY1 = 0
            for j in range(len(player1.contain)):
                if player1.contain[i].x == player1.contain[j].x:
                    countX1 += 1
                if player1.contain[i].y == player1.contain[j].y:
                    countY1 += 1

        for i in range(len(player1.contain)):
            if player1.contain[i] == boxes[0] or player1.contain[i] == boxes[4] or player1.contain[i] == boxes[8] :
                countZ1 += 1
            if player1.contain[i] == boxes[2] or player1.contain[i] == boxes[4] or player1.contain[i] == boxes[6]:
                countT1 += 1

        if countX1 == 3 or countY1 == 3 or countZ1 == 3 or countT1 == 3:
            player1.win = True


    if len(player2.contain) >= 3:
        for i in range(len(player2.contain)):
            countX2 = 0
            countY2 = 0
            for j in range(len(player2.contain)):
                if player2.contain[i].x == player2.contain[j].x:
                    countX2 += 1
                if player2.contain[i].y == player2.contain[j].y:
                    countY2 += 1

        for i in range(len(player2.contain)):
            if player2.contain[i] == boxes[0] or player2.contain[i] == boxes[4] or player2.contain[i] == boxes[8]:
                countZ2 += 1
            if player2.contain[i] == boxes[2] or player2.contain[i] == boxes[4] or player2.contain[i] == boxes[6]:
                countT2 += 1

        if countX2 == 3 or countY2 == 3 or countZ2 == 3 or countT2 ==3:
            player2.win = True

    count = 0
    for box in boxes:
        if box.use:
            count += 1
    if count == 9:
        player1.win = True
        player2.win = True


def set_turn(index):
    if player1.turn:
            boxes[index].open1 = True
            player1.turn = False
            player2.turn = True
            player1.contain.append(boxes[index])

    elif player2.turn:
            boxes[index].open2 = True
            player2.turn = False
            player1.turn = True
            player2.contain.append(boxes[index])





def maindraw(win , run):
    menu.menudraw(win)
    font = pygame.font.SysFont('comicsans' , 50 , True)
    win.fill((0, 0, 0))
                                                                    #win check:
    check_win(win, run)


    if player2.win == True and player1.win == True:
        text3 = font.render('equal ', 1, (255, 0, 0))
        win.fill((0, 0, 0))
        win.blit(text3, (200, 200))
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.quit()
    elif player1.win == True:
        text1 = font.render('player 1 won ', 1, (255, 0, 0))
        win.fill((0, 0, 0))
        win.blit(text1, (100, 200))
        pygame.display.update()
        pygame.time.delay(1000)
        run = False
        pygame.quit()
    elif player2.win == True:
        text2 = font.render('player 2 won ', 1, (255, 0, 0))
        win.fill((0, 0, 0))
        win.blit(text2, (100, 200))
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.quit()

                                                                    #board draw:
    for box in boxes:
        box.draw(win)
        if box.open1:
            pygame.draw.line(win, (0, 255, 255), (box.x + 20, box.y + 20 ),
                     (box.x + box.width - 20 , box.y + box.height - 20), 4)
            pygame.draw.line(win, (0, 255, 255), (box.x + 20, box.y + box.height - 20),
                             (box.x + box.width - 20, box.y  + 20), 4)
            pygame.display.update()
        if box.open2:
            pygame.draw.circle(win, (0, 0, 255), (
             box.x + box.width // 2, box.y + box.height // 2),
                           box.width // 4, 4)
            pygame.display.update()





boxes = [BoardDisplay(50, 50, 400 // 3, 400//3),BoardDisplay(50 + 400//3, 50, 400 // 3, 400//3),
         BoardDisplay(50 + 400//3 *2, 50 , 400 // 3, 400//3),BoardDisplay(50 , 50 + 400//3, 400 // 3, 400//3),
         BoardDisplay(50 + 400 //3, 50 + 400//3 , 400 // 3, 400//3),BoardDisplay(50 + 400//3*2, 50 + 400//3 , 400 // 3, 400//3),
         BoardDisplay(50, 50 + 400//3*2, 400 // 3, 400//3),BoardDisplay(50 + 400//3, 50 + 400//3 * 2, 400 // 3, 400//3),
         BoardDisplay(50 + 400//3 * 2, 50 + 400//3 * 2, 400 // 3, 400//3)]




player1 = Player()
player2 = Player()
player1.turn = True
player2.turn = False
#board = BoardDisplay(50, 50, 400, 400)

menu = StartMenu()




run = True
while run:                       #main loop
    pygame.time.delay(300)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if (170 < pos[0] < text_multi.get_width() + 180) and (100 < pos[1] < text_multi.get_height() + 110 ) and not menu.clicked_menu:
                menu.clicked_menu = True
                menu.muli = True
            elif (170 < pos[0] < text_multi.get_width() + 180) and (300 < pos[1] < text_single.get_height() + 310) and not menu.clicked_menu:
                menu.clicked_menu = True
                menu.single = True

            elif menu.clicked_menu:
                for box in boxes:
                    if menu.muli:
                        if (box.x < pos[0] < box.x + box.width) and (box.y < pos[1] < box.y + box.height) and box.use == False:
                            set_turn(boxes.index(box))
                            box.use = True
                    elif menu.single:
                        if player1.turn:
                            if (box.x < pos[0] < box.x + box.width) and (box.y < pos[1] < box.y + box.height) and box.use == False:
                                set_turn(boxes.index(box))
                                box.use = True



    maindraw(win , run)

    if menu.single and player2.turn:
        comp_move(win, run)

pygame.quit()



