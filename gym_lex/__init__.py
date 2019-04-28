from gym.envs.registration import register

register(
    id='lex-v0',
    entry_point='gym_lex.envs:LexEnv',
)