import gym
import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

def main():
    env = gym_super_mario_bros.make('SuperMarioBros-v0')
    env = JoypadSpace(env, SIMPLE_MOVEMENT)
    terminated = True

    for step in range(5000):
        if terminated:
            state = env.reset()
        observation, reward, terminated, info = env.step(env.action_space.sample())
        env.render()

    env.close()

if __name__ == "__main__":
    main()