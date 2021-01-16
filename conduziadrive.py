import gym
gym.logger.set_level(32)

from stable_baselines3 import PPO
from stable_baselines3.ppo import MlpPolicy
from stable_baselines3.common.env_util import make_vec_env

def train():
    #Recebe e cria o ambiente
    env = make_vec_env('CarRacing-v0', n_envs=6)
    #Cria o agent
    drive = PPO(MlpPolicy, env, gamma=0.9997, gae_lambda=1, ent_coef=0.01, vf_coef=1, batch_size=256, learning_rate=5e-6, clip_range=0.1, n_steps=64, n_epochs=20, verbose=1)
    # Treina o agent
    drive = drive.learn(total_timesteps=500000)
    # Salva o treino feito pelo agent
    drive.save("conduziadrive")

    #del drive
    # Faz load automatico dos argumentos
    #drive = PPO.load("conduziadrive")

    # Executa o agent
    #score = 0
    #obs = env.reset()
    #while True:
    #    action, _states = drive.predict(obs)
    #    obs, reward, done, info = env.step(action)
    #    score += reward
    #    env.render()

train()
