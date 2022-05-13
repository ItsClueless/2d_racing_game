from game_classes import *

def start_game():
    main_menu = pygame_menu.Menu('Welcome', 800, 600, theme=pygame_menu.themes.THEME_DARK,onclose=game_scene)
    main_menu.add.button('Play', pygame_menu.events.CLOSE)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    main_menu.mainloop(screen)

def game_scene():
    screen.fill((0, 0, 0))
    pygame.display.flip()
    camera_group = CameraGroup()
    player = Player((660, 360), camera_group)
    computer1 = Computer((630, 360), camera_group, 'computer1.png')
    computer2 = Computer((690, 360), camera_group, 'computer2.png') 
    computer3 = Computer((720, 360), camera_group, 'computer3.png')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if player.laps == 2 or computer1.laps == 6 or computer2.laps == 6 or computer3.laps == 6: ## MAX LAPS IS 6
                player.laps = 0
                player.check_points = 0
                computer1.path = 1
                computer1.laps = 1
                end_scene1()
            


            # Key Input For Rotations And Boost
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.rotation_direction += 1
                if event.key == pygame.K_LEFT:
                    player.rotation_direction -= 1
                if event.key == pygame.K_SPACE:
                    player.speed *= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.rotation_direction -= 1
                if event.key == pygame.K_LEFT:
                    player.rotation_direction += 1
                if event.key == pygame.K_SPACE:
                    player.speed *= 1 / 2

            

        screen.fill('#56AF27')

        camera_group.update()
        camera_group.custom_draw(player)

        pygame.display.update()

        # USING PATH MASKS CENTROID AND COMPUTER RECT CENTER FOR COLLISION ON PATH
        if computer1.path == 1 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path1_mask.centroid())
        elif computer1.path == 2 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path2_mask.centroid())
        elif computer1.path == 3 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path3_mask.centroid())
        elif computer1.path == 4 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path4_mask.centroid())
        elif computer1.path == 5 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path5_mask.centroid())
        elif computer1.path == 6 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path6_mask.centroid())
        elif computer1.path == 7 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path7_mask.centroid())
        elif computer1.path == 8 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path8_mask.centroid())
        elif computer1.path == 9 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path9_mask.centroid())
        elif computer1.path == 10 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path10_mask.centroid())
        elif computer1.path == 11 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path11_mask.centroid())
        elif computer1.path == 12 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path12_mask.centroid())
        elif computer1.path == 13 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path13_mask.centroid())
        elif computer1.path == 14 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path14_mask.centroid())
        elif computer1.path == 15 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path15_mask.centroid())
        elif computer1.path == 16 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path16_mask.centroid())
        elif computer1.path == 17 and computer1.collide(camera_group.track_border_mask) == None:
            computer1.rotate(computer1.rect.center, camera_group.path17_mask.centroid())
        elif computer1.path == 18:
            computer1.update_lap()
            computer1.path = 1
        else:
            computer1.speed = 0

        
        if computer1.rect.center[0] == camera_group.path1_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path1_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path2_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path2_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path3_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path3_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path4_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path4_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path5_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path5_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path6_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path6_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path7_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path7_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path8_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path8_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path9_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path9_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path10_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path10_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path11_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path11_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path12_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path12_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path13_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path13_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path14_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path14_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path15_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path15_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path16_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path16_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path17_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path17_mask.centroid()[1]-2:
                computer1.update_path()
        elif computer1.rect.center[0] == camera_group.path18_mask.centroid()[0]:
            if computer1.rect.center[1] == camera_group.path18_mask.centroid()[1]-2:
                computer1.update_path()

                
        if computer2.path == 1 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path1_mask.centroid())
        elif computer2.path == 2 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path2_mask.centroid())
        elif computer2.path == 3 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path3_mask.centroid())
        elif computer2.path == 4 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path4_mask.centroid())
        elif computer2.path == 5 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path5_mask.centroid())
        elif computer2.path == 6 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path6_mask.centroid())
        elif computer2.path == 7 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path7_mask.centroid())
        elif computer2.path == 8 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path8_mask.centroid())
        elif computer2.path == 9 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path9_mask.centroid())
        elif computer2.path == 10 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path10_mask.centroid())
        elif computer2.path == 11 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path11_mask.centroid())
        elif computer2.path == 12 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path12_mask.centroid())
        elif computer2.path == 13 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path13_mask.centroid())
        elif computer2.path == 14 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path14_mask.centroid())
        elif computer2.path == 15 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path15_mask.centroid())
        elif computer2.path == 16 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path16_mask.centroid())
        elif computer2.path == 17 and computer2.collide(camera_group.track_border_mask) == None:
            computer2.rotate(computer2.rect.center, camera_group.path17_mask.centroid())
        elif computer2.path == 18:
            computer2.update_lap()
            computer2.path = 1
        else:
            computer2.speed = 0

        
        if computer2.rect.center[0] == camera_group.path1_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path1_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path2_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path2_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path3_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path3_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path4_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path4_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path5_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path5_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path6_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path6_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path7_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path7_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path8_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path8_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path9_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path9_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path10_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path10_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path11_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path11_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path12_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path12_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path13_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path13_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path14_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path14_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path15_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path15_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path16_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path16_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path17_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path17_mask.centroid()[1]-2:
                computer2.update_path()
        elif computer2.rect.center[0] == camera_group.path18_mask.centroid()[0]:
            if computer2.rect.center[1] == camera_group.path18_mask.centroid()[1]-2:
                computer2.update_path()



        if computer3.path == 1 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path1_mask.centroid())
        elif computer3.path == 2 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path2_mask.centroid())
        elif computer3.path == 3 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path3_mask.centroid())
        elif computer3.path == 4 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path4_mask.centroid())
        elif computer3.path == 5 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path5_mask.centroid())
        elif computer3.path == 6 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path6_mask.centroid())
        elif computer3.path == 7 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path7_mask.centroid())
        elif computer3.path == 8 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path8_mask.centroid())
        elif computer3.path == 9 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path9_mask.centroid())
        elif computer3.path == 10 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path10_mask.centroid())
        elif computer3.path == 11 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path11_mask.centroid())
        elif computer3.path == 12 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path12_mask.centroid())
        elif computer3.path == 13 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path13_mask.centroid())
        elif computer3.path == 14 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path14_mask.centroid())
        elif computer3.path == 15 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path15_mask.centroid())
        elif computer3.path == 16 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path16_mask.centroid())
        elif computer3.path == 17 and computer3.collide(camera_group.track_border_mask) == None:
            computer3.rotate(computer3.rect.center, camera_group.path17_mask.centroid())
        elif computer3.path == 18:
            computer3.update_lap()
            computer3.path = 1
        else:
            computer3.speed = 0

        
        if computer3.rect.center[0] == camera_group.path1_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path1_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path2_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path2_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path3_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path3_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path4_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path4_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path5_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path5_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path6_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path6_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path7_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path7_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path8_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path8_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path9_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path9_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path10_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path10_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path11_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path11_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path12_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path12_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path13_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path13_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path14_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path14_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path15_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path15_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path16_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path16_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path17_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path17_mask.centroid()[1]-2:
                computer3.update_path()
        elif computer3.rect.center[0] == camera_group.path18_mask.centroid()[0]:
            if computer3.rect.center[1] == camera_group.path18_mask.centroid()[1]-2:
                computer3.update_path()
        


        if player.collide(camera_group.track_border_mask) != None:
            print("Collison")
            end_scene2()
        
        if player.collide(camera_group.finish_mask) != None:
            player.update_lap()
        
        if player.collide(camera_group.checkpoint_one_mask) != None:
            if player.check_points == 0:
                player.update_checkpoint()
        if player.collide(camera_group.checkpoint_two_mask) != None:
            if player.check_points == 1:
                player.update_checkpoint()
        if player.collide(camera_group.checkpoint_three_mask) != None:
            if player.check_points == 2:
                player.update_checkpoint()
        if player.collide(camera_group.checkpoint_four_mask) != None:
            if player.check_points == 3:
                player.update_checkpoint()
        if player.collide(camera_group.checkpoint_five_mask) != None:
            if player.check_points == 4:
                player.update_checkpoint()

        clock.tick(60)



def end_scene1():
    end_menu = pygame_menu.Menu('Thank You for Playing', 800, 600, theme=pygame_menu.themes.THEME_DARK,onclose=start_game)
    end_menu.add.label('You finished the game')
    end_menu.add.button('Play Again', pygame_menu.events.CLOSE)
    end_menu.add.button('Quit', pygame_menu.events.EXIT)
    end_menu.mainloop(screen)

def end_scene2():
    end_menu = pygame_menu.Menu('Thank You for Playing', 800, 600, theme=pygame_menu.themes.THEME_DARK,onclose=start_game)
    end_menu.add.label('You Crashed, Game Over')
    end_menu.add.button('Play Again', pygame_menu.events.CLOSE)
    end_menu.add.button('Quit', pygame_menu.events.EXIT)
    end_menu.mainloop(screen)

# setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('TD Racer')
clock = pygame.time.Clock()

# start the game (runs the game loop functions)
start_game()