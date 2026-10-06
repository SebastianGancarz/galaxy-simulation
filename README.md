# 🌌 Galaxy Simulation

A Python-based galaxy simulation project created to explore **procedural galaxy generation, numerical simulation, and gravitational physics**.

The project started as a simple visualization of randomly generated stars and is gradually evolving into a physics-based simulation where a test particle moves under the gravitational influence of individual stars.

> 🚧 **Work in Progress** — this project is actively being developed and used as a learning project.

---

## ✨ Current Features

* Procedurally generated spiral galaxy
* Two spiral arms
* Exponential radial star distribution
* Randomized star brightness
* 3D galaxy structure with vertical star distribution
* Dense visual galactic center
* Test particle with simulated movement
* Gravitational force calculated from individual stars
* Numerical integration of velocity and position
* Configurable simulation timestep
* 10,000 simulation steps
* Gravitational force tracking over time
* Analysis of maximum gravitational force
* Detection of the closest star during maximum force

---

## 🧠 What I'm Learning

This project is helping me practice and understand:

* Python
* NumPy
* Matplotlib
* Vector mathematics
* Arrays and matrix operations
* 3D coordinate systems
* Numerical integration
* Newtonian gravity
* Procedural generation
* Data analysis and visualization
* Git & GitHub

The main goal is not just to make the simulation work, but to understand **why it works** and gradually improve the underlying model.

---

## ⚙️ How It Works

### 1. Galaxy Generation

Stars are generated using polar coordinates:

```text
x = r · cos(θ)
y = r · sin(θ)
```

The radial distance is generated using an exponential distribution, while the angle is influenced by the radial distance to create spiral arms.

Random noise is added to the angle to give the galaxy a less artificial appearance.

### 2. 3D Structure

Each star receives a small random `z` coordinate, creating a thin three-dimensional galactic disk instead of a completely flat 2D structure.

### 3. Gravitational Simulation

A test particle is placed inside the galaxy.

For every simulation step, the distance between the particle and every star is calculated. The gravitational force from each star is then calculated and combined into a single net force.

The basic gravitational relationship used is:

```text
F = G · m / r²
```

The resulting acceleration is used to update the particle's velocity and position.

### 4. Numerical Integration

The simulation updates the particle using a small timestep:

```text
velocity = velocity + acceleration · dt
position = position + velocity · dt
```

Currently, the simulation uses:

```text
dt = 0.001
```

and runs for:

```text
10,000 steps
```

---

## 📊 Force Analysis

The simulation records the gravitational force acting on the test particle at every timestep.

This allows the simulation to be analyzed after it finishes rather than only visualized.

For example, the project can determine:

* Maximum gravitational force
* The timestep where it occurred
* The particle's position at that moment
* Distance to the closest star
* Mass of the closest star
* Estimated gravitational contribution of that star

This is an important part of the project because it turns the simulation into a small **data analysis experiment**, rather than only a graphical visualization.

---

## 🛠️ Technologies

| Technology | Purpose                                      |
| ---------- | -------------------------------------------- |
| Python     | Core programming language                    |
| NumPy      | Numerical calculations and vector operations |
| Matplotlib | 2D/3D visualization                          |
| Git        | Version control                              |
| GitHub     | Project hosting and version history          |

---

## 🚀 Running the Project

Clone the repository:

```bash
git clone https://github.com/555seba/galaxy-simulation.git
cd galaxy-simulation
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the simulation:

```bash
python main.py
```

---

## 🔭 Planned Improvements

The project is still in development. Possible future improvements include:

* [ ] Make the galactic center gravitationally active
* [ ] Give stars physically meaningful masses
* [ ] Improve gravitational softening
* [ ] Simulate multiple moving stars
* [ ] Implement a more complete N-body simulation
* [ ] Add orbital velocity calculations
* [ ] Add animation
* [ ] Improve galaxy morphology
* [ ] Add interactive parameters
* [ ] Analyze orbital stability
* [ ] Compare different galaxy configurations
* [ ] Improve numerical integration methods

---

## 📚 Project Goal

This project is part of my journey into **Python, data science, and computational simulation**.

Rather than following a finished tutorial, I am building the simulation incrementally and documenting the concepts I learn along the way.

The long-term goal is to turn the initial visualization into a more realistic and computationally interesting galaxy simulation.

---

## 👤 Author

**Sebastian Gancarz**

Information Technology Student — Data Science & AI

GitHub: [@SebastianGancarz](https://github.com/SebastianGancarz)
