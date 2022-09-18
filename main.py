import pygame, sys
from random import randint
# from debugging import *
from settings import *
from quests import *
# from level import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Magnolia')
        self.clock = pygame.time.Clock()
        # self.level = Level()

    
    def make_quest(self):
        # Quests
        questType = randint(0,2) # 0 = water, 1 = garbage, 2 = energy

        questChoices = ["Take %s minute shower" , "Sort %s bits of trash into recycle and compost" , "Use eco-friendly transporation %s times" 
                    , "Turn off faucet when not in use %s times" , "Get a smog check" , "Pick up %s pieces of trash", "Plant %s plants in your garden or yard" , "Use reusuable water bottle %s times" 
                    , "Buy %s groceries from local farms" , "Turn off lights when not in use %s times" , "Reduce AC usage by %s hours" , "Remove meat from %s meals"]
        quotas = [(3, 7), (5, 15), (1, 4), (1, 5), (-1, -1), (5, 15), (1, 3), (2, 5), (5, 20), (3, 10), (1, 5), (1, 3)] # Bounds for each quest, -1 representing not applicable
        quotaEXP = [10, 5, 20, 10, 25, 5, 25, 10, 5, 5, 10, 20] # EXP gained per 1 completion of the goal (1 trash, 1 plant, etc)

        goalSelector = randint(0, len(questChoices)-1) # select which goal to use
        quotaLimits = quotas[goalSelector] # select which quota bounds to use
        questQuota = randint(quotaLimits[0], quotaLimits[1]) # pick a quota from those bounds
        questGoal = questChoices[goalSelector] # write the quest text in its entirety
        if questQuota > 0:
            questGoal = questGoal % questQuota
        chosenEXP = quotaEXP * questQuota
        
        return Quest(questType, questGoal, chosenEXP)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
            self.screen.fill((0, 0, 0))
            # self.level.run()
            pygame.display.flip()
            self.clock.tick(TICK_SPEED)

            # generate quest if there's an empty slot
            


if __name__ == "__main__":
    game = Game()
    game.run()

    # take x minute shower
    # sort trash into recycle and compost
    # use eco-friendly transsportant to a location
    # turn off faucet when not in use
    # close faucet all the way to prevent leaks
    # pick up x pieces of trash
    # smog check