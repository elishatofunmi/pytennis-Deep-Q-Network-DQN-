import time
import numpy as np
import pygame
import sys, os
from keras import Sequential, layers
from keras.optimizers import Adam
from keras.layers import Dense
from collections import deque



from DQNetwork import DQN
from BallRegression import Network 
from PyTennis import pytennis


from pygame.locals import *
pygame.init()


#initialize the 2 agents.
AgentA = DQN()
AgentB = DQN()


if __name__ == "__main__":
    tennis = pytennis(fps = 50)
    tennis.reset()
    tennis.render()



