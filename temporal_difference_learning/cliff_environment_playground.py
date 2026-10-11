import sys
import numpy as np
import gymnasium as gym
from lib.envs.cliff_walking import CliffWalkingEnv

env = CliffWalkingEnv()

print(env.reset())
env.render()

print(env.step(0))
env.render()

print(env.step(1))
env.render()

print(env.step(1))
env.render()

print(env.step(2))
env.render()
