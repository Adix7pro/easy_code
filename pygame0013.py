import pygame # type: ignore
import sys
"""
pygame.draw.rect( Sirt , rang , to'g'ri , kenglik = 0 )
pygame.draw.line( Sirt , rang , start_post , end_pos , width=1 )

"""
pygame.init()

screen = pygame.display.set_mode((1000, 800))
r = pygame.Rect(100, 100, 50, 100)
pygame.draw.rect(screen, (255, 0, 0), r, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()