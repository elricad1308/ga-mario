import numpy as np
import random
import gym
import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

class Individuo:

    def __init__(self):
        self.genoma = np.zeros(6000)

        for i, value in enumerate(self.genoma):
            if random.random() > 0.5:
                self.genoma[i] = 1

    def fitness(self):
        # Creamos el entorno que nos 
        # permite ver hasta donde llega el individuo
        env = gym_super_mario_bros.make('SuperMarioBros-v0')

        # Esta línea define cuáles acciones podemos
        # realizar en el entorno
        env = JoypadSpace(env, SIMPLE_MOVEMENT)

        # Esta línea sirve para que el emulador pueda
        # decirnos si la simulación ya terminó
        terminated = True

        correr = 3
        saltar = 4

        # Este ciclo es el que toma la cadena del genoma
        # del individuo y la manda al emulador
        for i, value in enumerate(self.genoma):
            # Si mario se muere, prepara el simulador
            # para la siguiente corrida
            if terminated:
                env.reset()

            if value == 0:
                o, r, terminated, info = env.step(correr)
            else:
                o, r, terminated, info = env.step(saltar)

            env.render()

            if terminated:
                break

        env.close()
        distancia = info['x_pos']
        tiempo = 400 - info['time']

        print(f"velocidad: {distancia/tiempo}\tdistancia: {distancia}\ttiempo: {tiempo}")

