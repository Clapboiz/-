# import random
# import gym
# from __init__ import env
# from environment import pentestEnv

# env = gym.make('pentestEnv-v0')
# s = env.reset()

# for _ in range(3):
#     actions = list(range(env.action_space.n))  # Giả sử không gian hành động là Discrete
#     env.render()

#     action = random.choice(actions)
#     s, r, done, info = env.step(action)

#     print(f"Hành động có thể thực hiện: {actions}")
#     print(f"Phần thưởng: {r}, Hoàn thành: {done}\n")
#     input()


import random
import gym
from __init__ import env
from environment import pentestEnv

env = gym.make('pentestEnv-v0')
s = env.reset()

# Loop through a number of timesteps for testing
for _ in range(10):
    # Take a random action
    action = env.action_space.sample()

    # Make a move and get the new status, reward, end status and number of steps taken
    observation, reward, done, total_steps = env.step(action)

    # Print out the information
    print(f"Step: {total_steps}")
    print(f"Action: {action}")
    print(f"Observation: {observation}")
    print(f"Reward: {reward}")
    print(f"Done: {done}")
    print("")

    # Check if finished
    if done:
        print("Environment is done!")
        break

# Close the environment upon completion
env.close()
