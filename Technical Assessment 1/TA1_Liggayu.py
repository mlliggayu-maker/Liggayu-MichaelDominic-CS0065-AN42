import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------- Get user input --------
num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
num_steps = int(input("Enter number of steps: "))


# -------- Agent Definition --------
class RandomWalker(ap.Agent):

    def setup(self):
        # Random starting position
        self.position = (
            random.randint(0, self.model.p.grid_size[0] - 1),
            random.randint(0, self.model.p.grid_size[1] - 1)
        )

        # Record the path
        self.path = [self.position]

    def step(self):
        # Possible movements
        directions = [
            (1, 0),    # Right
            (-1, 0),   # Left
            (0, 1),    # Up
            (0, -1)    # Down
        ]

        # Randomize the order of directions
        random.shuffle(directions)

        # Try each direction
        for direction in directions:

            x = self.position[0] + direction[0]
            y = self.position[1] + direction[1]

            # Check grid boundaries
            if (
                0 <= x < self.model.p.grid_size[0]
                and 0 <= y < self.model.p.grid_size[1]
            ):

                new_position = (x, y)

                # Check if another agent is there
                occupied = False

                for other in self.model.agents:
                    if other != self and other.position == new_position:
                        occupied = True
                        break

                # Move if the position is free
                if not occupied:
                    self.position = new_position
                    break

        # Record the new position
        self.path.append(self.position)


# -------- Model Definition --------
class RandomWalkModel(ap.Model):

    def setup(self):
        # Create agents
        self.agents = ap.AgentList(
            self,
            self.p.agents,
            RandomWalker
        )

    def step(self):
        # Move all agents
        for agent in self.agents:
            agent.step()


# -------- Parameters --------
parameters = {
    "agents": num_agents,
    "grid_size": (grid_size, grid_size),
    "steps": num_steps
}


# -------- Create Model --------
model = RandomWalkModel(parameters)
model.setup()


# -------- Create Animation --------
fig, ax = plt.subplots(figsize=(7, 7))

ax.set_xlim(-0.5, grid_size - 0.5)
ax.set_ylim(-0.5, grid_size - 0.5)

ax.set_xticks(range(grid_size))
ax.set_yticks(range(grid_size))

ax.grid(True)

ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
ax.set_title("Random Walk - Agent Movement")


# Get starting positions
x = [agent.position[0] for agent in model.agents]
y = [agent.position[1] for agent in model.agents]

# Create moving dots
scat = ax.scatter(x, y, s=100)


# Create path lines
lines = []

for agent in model.agents:
    line, = ax.plot([], [])
    lines.append(line)


# -------- Update Animation --------
def update(frame):

    # Move agents
    model.step()

    # Get new positions
    x = [agent.position[0] for agent in model.agents]
    y = [agent.position[1] for agent in model.agents]

    # Move the dots
    scat.set_offsets(list(zip(x, y)))

    # Draw each agent's path
    for i, agent in enumerate(model.agents):

        path_x = [position[0] for position in agent.path]
        path_y = [position[1] for position in agent.path]

        lines[i].set_data(path_x, path_y)

    return [scat] + lines


# -------- Start Animation --------
ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_steps,
    interval=300,
    repeat=False
)

plt.show()


# -------- Display Final Positions --------
print("\n--- Final Positions ---")

for i, agent in enumerate(model.agents):
    print(f"Agent {i + 1}: {agent.position}")
