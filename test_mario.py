import gym
import ppaquette_gym_super_mario
import time

def main():
    env = gym.make('ppaquette/SuperMarioBros-1-1-v0')
    env.reset()
    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample())  # take a random action
        time.sleep(0.1)  # Add a small delay to make the rendering visible
    env.close()

if __name__ == "__main__":
    main()
