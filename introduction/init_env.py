import gymnasium as gym
import warnings

warnings.filterwarnings("ignore")

# Create a simple environment perfect for beginners
env = gym.make('CartPole-v1')
print(env)

# Show all environments you can create
print(gym.pprint_registry())
