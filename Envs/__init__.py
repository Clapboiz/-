import gym
from gym.envs.registration import register

register(
    id='pentestEnv-v0',
    entry_point='Envs.envs:pentestEnv'
)

env = gym.make('pentestEnv-v0')