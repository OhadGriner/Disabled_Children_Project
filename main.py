import pygame
pygame.init()
 
def main():
    running = True
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joy in joysticks:
        joy.init()
 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYAXISMOTION:
                print(event)
            elif event.type == pygame.JOYHATMOTION:
                print(event)
            elif event.type == pygame.JOYBUTTONDOWN:
                print(event)
 
    pygame.quit()
 
main()