from game_classes import *


def racing_test():
    pygame.init()
    player = Player((660, 360), None)

    if player.laps != 0:
        raise Exception("Fail: Laps should be 0 but were " + str(player.laps))

    player.update_lap()

    if player.laps != 1:
        raise Exception("Fail: Laps should be 1 but were " + str(player.laps))

    player.update_checkpoint()

    if player.check_points != 1:
        raise Exception("Fail: Check points should be 1 but were " + str(player.check_points))

    player.update_lap()

    if player.laps != 1:
        raise Exception("Fail: Laps should be 1 but were " + str(player.laps))

    player.update_checkpoint()
    player.update_checkpoint()
    player.update_checkpoint()
    player.update_checkpoint()

    if player.check_points != 5:
        raise Exception("Fail: Check points should be 5 but were " + str(player.check_points))

    player.update_lap()

    if player.laps != 2:
        raise Exception("Fail: Laps should be 2 but were " + str(player.laps))

    player.update_checkpoint()
    player.update_lap()

    if player.laps != 2:
        raise Exception("Fail: Laps should be 2 but were " + str(player.laps))


racing_test()
print("All test cases passed")
