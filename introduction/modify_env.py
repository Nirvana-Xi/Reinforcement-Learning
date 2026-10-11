import warnings
import gymnasium as gym
from gymnasium.wrappers import FlattenObservation

warnings.filterwarnings("ignore")

# Start with a complex observation space
env = gym.make("CarRacing-v2")
print(env.observation_space.shape)  # 96x96 RGB image

# Wrap it to flatten the observation into a 1D array
wrapped_env = FlattenObservation(env)
print(wrapped_env.observation_space.shape)  # All pixels in a single array

# This makes it easier to use with some algorithms that expect 1D input

# wrapped_env.unwrapped
# access the original environment underneath all the layers of wrappers
