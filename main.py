import pygame, sys
from random import randint
# from debugging import *
from settings import *
from quests import *
# from level import *


def make_quest():
        # Quests
        questChoices = ["Take %s minute shower" , "Sort %s bits of trash into recycle and compost" , "Use eco-friendly transporation %s times" 
                    , "Turn off faucet when not in use %s times" , "Get a smog check" , "Pick up %s pieces of trash", "Plant %s plants in your garden or yard" , "Use reusuable water bottle %s times" 
                    , "Buy %s groceries from local farms" , "Turn off lights when not in use %s times" , "Reduce AC usage by %s hours" , "Remove meat from %s meals"]
        questTypes = [0, 1, 3, 0, 3, 1, 3, 1, 3, 2, 2, 3] # 0 = water, 1 = garbage, 2 = energy, 3 = greenhouse gas
        quotas = [(3, 7), (5, 15), (1, 4), (1, 5), (-1, -1), (5, 15), (1, 3), (2, 5), (5, 20), (3, 10), (1, 5), (1, 3)] # Bounds for each quest, -1 representing not applicable
        quotaEXP = [10, 5, 20, 10, 25, 5, 25, 10, 5, 5, 10, 20] # EXP gained per 1 completion of the goal (1 trash, 1 plant, etc

        goalSelector = randint(0, len(questChoices)-1) # select which goal to use
        quotaLimits = quotas[goalSelector] # select which quota bounds to use
        questQuota = randint(quotaLimits[0], quotaLimits[1]) # pick a quota from those bounds
        questGoal = questChoices[goalSelector] # write the quest text in its entirety
        if questQuota > 0:
            questGoal = questGoal % questQuota
        chosenEXP = quotaEXP * questQuota
        questType = questTypes[goalSelector]
        quest_object = Quest(questType, questGoal, chosenEXP)
        return quest_object


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Magnolia')
        self.clock = pygame.time.Clock()
        # self.level = Level()


    def run(self):
        userData = open("userData.txt", "r").readlines()
        if len(userData) < 2:
            exp = 0
            quests = [make_quest(), make_quest(), make_quest()]
        else:
            exp = int(userData[0])
            quest1 = userData[1].split("_")
            quest2 = userData[2].split("_")
            quest3 = userData[3].split("_")
            quests = [Quest(int(quest1[0]), quest1[1], int(quest1[2]))
                    , Quest(int(quest2[0]), quest2[1], int(quest2[2]))
                    , Quest(int(quest3[0]), quest3[1], int(quest3[2]))]
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
            self.screen.fill(77, 77, 77)
            # self.level.run()

            pygame.display.flip()
            self.clock.tick(TICK_SPEED)



if __name__ == "__main__":
    game = Game()
    game.run()
