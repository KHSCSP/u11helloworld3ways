import pygame, random

def graphics_hello(): 
    # Set up the drawing window
    pygame.init()
    w = 500
    h = 500
    screen = pygame.display.set_mode([w, h])
    
    # Fill the background with white
    screen.fill((255, 255, 255))

    my_font = pygame.font.Font('freesansbold.ttf', 32)

    name = ''
      
    
    # stay on screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    name = name + 'a'
                if event.key == pygame.K_b:
                    name = name + 'b'
                if event.key == pygame.K_c:
                    name = name + 'c'
                if event.key == pygame.K_d:
                    name = name + 'd'
                if event.key == pygame.K_e:
                    name = name + 'e'
                if event.key == pygame.K_f:
                    name = name + 'f'
                if event.key == pygame.K_g:
                    name = name + 'g'
                if event.key == pygame.K_h:
                    name = name + 'h'
                if event.key == pygame.K_i:
                    name = name + 'i'
                if event.key == pygame.K_j:
                    name = name + 'j'
                if event.key == pygame.K_k:
                    name = name + 'k'
                if event.key == pygame.K_l:
                    name = name + 'l'
                if event.key == pygame.K_m:
                    name = name + 'm'
                if event.key == pygame.K_n:
                    name = name + 'n'
                if event.key == pygame.K_o:
                    name = name + 'o'
                if event.key == pygame.K_p:
                    name = name + 'p'
                if event.key == pygame.K_q:
                    name = name + 'q'
                if event.key == pygame.K_r:
                    name = name + 'r'
                if event.key == pygame.K_s:
                    name = name + 's'
                if event.key == pygame.K_t:
                    name = name + 't'
                if event.key == pygame.K_u:
                    name = name + 'u'
                if event.key == pygame.K_v:
                    name = name + 'v'
                if event.key == pygame.K_w:
                    name = name + 'w'
                if event.key == pygame.K_x:
                    name = name + 'x'
                if event.key == pygame.K_y:
                    name = name + 'y'
                if event.key == pygame.K_z:
                    name = name + 'z'
            
        text1 = my_font.render("what's your name?", True, (0,0,0))
        screen.blit(text1, (10,10))
        
        text2 = my_font.render('hello ' + str(name), True, (0,0,0))
        screen.blit(text2, (10,50))
        pygame.display.flip()
    pygame.quit()