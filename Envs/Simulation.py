import random
import gym
from __init__ import env
from environment import pentestEnv

env = gym.make('pentestEnv-v0')
s = env.reset()

for _ in range(3):
    actions = list(range(env.action_space.n))  # Giả sử không gian hành động là Discrete
    env.render()

    action = random.choice(actions)
    s, r, done, info = env.step(action)

    print(f"Hành động có thể thực hiện: {actions}")
    print(f"Phần thưởng: {r}, Hoàn thành: {done}\n")
    input()
