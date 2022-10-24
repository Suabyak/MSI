import pygame

pygame.display.set_mode((1240, 800))
run = True

def quit():
    run = False

operatable_events = {
    pygame.constants.QUIT: quit,
}


def operate_events():
    for event in pygame.event.get():
        if event.type in operatable_events.keys():
            operatable_events[event.type](event)
        else:
            print(event)



while run:
    operate_events()
