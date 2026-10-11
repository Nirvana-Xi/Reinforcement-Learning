import numpy as np
import gymnasium as gym
from lib.envs.windy_gridworld import WindyGridworldEnv

env = WindyGridworldEnv()

print(env.reset())
env.render()

print(env.step(1))
env.render()

print(env.step(1))
env.render()

print(env.step(1))
env.render()

print(env.step(2))
env.render()

print(env.step(1))
env.render()

print(env.step(1))
env.render()
