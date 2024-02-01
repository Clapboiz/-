import sys

import gym
import numpy as np
import gym.spaces
import tensorflow as tf

from io import StringIO

from generateMap import generateMap

class pentestEnv(gym.Env):
    metadata = {'render.modes': ['human', 'ansi']}
    # MAP = np.loadtxt('../processdata/newmap.txt')
    webVulnerability = open('D:/Users/Desktop/Reinforcement-Learning-for-Automating-Pentest/Data/Web_vulnerability.csv', 'r')
    webVulnerabilityData = webVulnerability.readlines()
    # webVulnerabilityData = webVulnerability.readlines()

    # endLine = webVulnerabilityData[-1]
    # line = int(float(endLine.split(',')[0]))
    
    line = len(webVulnerabilityData)

    MAP = -(np.ones((line, line), dtype=np.float))
    line = len(MAP)
    observation_map = np.zeros((line, line), dtype=float)    

    def __init__(self):
        super().__init__()
        self.action_space = gym.spaces.Discrete(self.line) 
        self.reset()

    def reset(self):
        # parameters initialize
        self.pos = 0
        self.goal = self.line - 1
        self.done = False
        self.steps = 0
        return self._observe(self.pos)

    def step(self, action):
        global next_state
        self.next_state = action
        self.state = [self.pos, self.next_state]

        self.pos = self.next_state
        self.steps = self.steps + 1

        observation = self._observe(self.next_state)
        reward = self._get_reward(self.state)

        self.done = self._is_done()
        total_steps = self.steps

        return observation, reward, self.done, total_steps

    def _close(self):
        pass

    def _seed(self, seed=None):
        pass

    def _get_reward(self, state):
        self.reward = self.MAP[tuple(state)]
        return self.reward

    def _observe(self, state):
        self.observation = state

        return self.observation

    def _is_done(self):
        if (self.pos == self.goal):
            return True
        else:
            return False

    def _start_state(self):
        return self._find_pos('S')[0]
        
    def render(self, mode='human', close=False):
        if mode == 'human':
            # Implement code để hiển thị trạng thái môi trường khi mode là 'human'
            print(f"Current position: {self.pos}, Goal position: {self.goal}")
            print(f"Observation map:\n{self.observation_map}")
        elif mode == 'ansi':
            # Implement code để trả về trạng thái môi trường dưới dạng ANSI khi mode là 'ansi'
            return f"Current position: {self.pos}, Goal position: {self.goal}\nObservation map:\n{self.observation_map}"