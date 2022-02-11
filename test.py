import pygame
import time
pygame.init()


def main():
    running = True
    joysticks = [pygame.joystick.Joystick(
        i) for i in range(pygame.joystick.get_count())]
    for joy in joysticks:
        joy.init()
    i = 0
    while running:
        pygame.event.pump()
        time.sleep(0.08)
        print(f'{i}: {pygame.joystick.Joystick(0).get_axis(1)}')
        i += 1
    pygame.quit()


main()
