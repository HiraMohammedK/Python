import numpy as np
import random

grid_size = 4
goal_state = (3, 3)
actions = ["up", "down", "left", "right"]

q_table = np.zeros((grid_size, grid_size, len(actions)))

learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.2
episodes = 500

def get_next_state(state, action):
    x, y = state
    if action == "up":
        x = max(x - 1, 0)
    elif action == "down":
        x = min(x + 1, grid_size - 1)
    elif action == "left":
        y = max(y - 1, 0)
    elif action == "right":
        y = min(y + 1, grid_size - 1)
    return x, y

for episode in range(episodes):
    state = (0, 0)
    while state != goal_state:
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)
        else:
            action = actions[np.argmax(q_table[state[0], state[1]])]

        next_state = get_next_state(state, action)
        reward = 1 if next_state == goal_state else -0.01

        action_idx = actions.index(action)
        best_next_action = np.max(q_table[next_state[0], next_state[1]])
        q_table[state[0], state[1], action_idx] += learning_rate * (
            reward + discount_factor * best_next_action - q_table[state[0], state[1], action_idx]
        )

        state = next_state

print("Q-learning training completed!")
