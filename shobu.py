import pygame
from Board import Board
from sys import exit

#todo: clean up magic code, work on separating movement logic into the correct areas, start building stone class if needed, implement move check logic
#TODO add board history

BACKGROUND = 'assets/ramin.jpg'
BOARD_SIZE = (810, 810)

def main():
    while True:
        pygame.display.update()
        pygame.time.wait(250)
        passive_stone = board.get_square()
        passive_stone_move = board.get_square()
        aggro_stone = board.get_square()
        if passive_stone != None:
            #add board history 
            board.update_board(board.player, passive_stone[0], passive_stone_move[0], aggro_stone[0])
            board.clear()
            board.draw()
            board.player = 'w' if board.player == 'b' else 'b'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()              

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Shobu')
    screen = pygame.display.set_mode(BOARD_SIZE, 0, 32)
    background = pygame.image.load(BACKGROUND).convert()
    board = Board(background, screen)
    board.draw() 
    main()