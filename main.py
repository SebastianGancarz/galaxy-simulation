import numpy as np


#PHYSICS
trajectory = []
num_stars = 500
mass = np.random.uniform(0.5, 2.0, num_stars * 2)
total_mass = np.sum(mass)
orbit_radius = 8.0
G = 1.0 #G-Force aka gravity, not real world.
velocity = np.array([0.0, 10.0, 0.0])
particle_mass = 1.0
position = np.array([orbit_radius, 0.0, 0.0])


brightness = np.random.uniform(0.2, 1.0, num_stars)
brightness2 = np.random.uniform(0.2, 1.0, num_stars)

r = np.random.exponential(5,num_stars)
angle = r * 0.5 + np.random.normal(0,0.15,num_stars)


center_r = np.random.exponential(0.7,1000)
center_angle = np.random.uniform(0,2 * np.pi, 1000)

x = r * np.cos(angle)
y = r * np.sin(angle)
z = np.random.normal(0, 0.15, 500)

x2 = r * np.cos(angle + np.pi)
y2 = r * np.sin(angle + np.pi)
z2 = np.random.normal(0, 0.15, 500)

center_x = center_r * np.cos(center_angle)
center_y = center_r * np.sin(center_angle)
center_z = np.random.normal(0, 0.15, 1000)


star_positions = np.column_stack((x,y,z))
star_positions2 = np.column_stack((x2,y2,z2))
star_positions = np.vstack((star_positions, star_positions2))

force_history = []
for _ in range(10000):
    distances = np.linalg.norm(star_positions - position, axis=1) + 0.1
    directions = (star_positions - position) / distances[:, np.newaxis]
    forces = (G * mass[:, np.newaxis]) / distances[:, np.newaxis]**2 * directions
    net_force = np.sum(forces, axis=0)
    force_magnitude = np.linalg.norm(net_force)
    force_history.append(force_magnitude)
    acceleration = net_force / particle_mass
    dt = 0.001 #Interval between calculations
    velocity = velocity + acceleration * dt #New velocity equals old velocity plus acceleration times interval
    position = position + velocity * dt #New position equals old position plus new velocity times interval
    trajectory.append(position.copy())

force_history = np.array(force_history)
max_force_index = np.argmax(force_history)
position_at_max_force = trajectory[max_force_index]
distances_at_max_force = np.linalg.norm(star_positions - position_at_max_force, axis=1)
min_distance = np.min(distances_at_max_force)
closest_star_index = np.argmin(distances_at_max_force)
closest_star_mass = mass[closest_star_index]
closest_star_force = (G * closest_star_mass) / min_distance**2
print("Max force index:", np.argmax(force_history)) #Which index was the maximum value reached at
print("Maximum force:", force_history[max_force_index]) #Maximum value reached
print("Minimum distance:", min_distance) #The distance of the closest star to the center
print("Closest star force:", closest_star_force) #The force of the closest star to the center
print("Closest star mass:", closest_star_mass) #The mass of the closest star to the center
#print(len(force_history))


trajectory = np.array(trajectory)
trajectory_x = trajectory[:,0]
trajectory_y = trajectory[:,1]
trajectory_z = trajectory[:,2]

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")
ax.scatter(x,y,z,s=2, alpha=brightness)
ax.scatter(x2,y2,z2,s=2, alpha=brightness2)
ax.view_init(elev=20, azim=45)
#ax.view_init(elev=90, azim=0) Incase I want to see it from above
ax.scatter(center_x, center_y, center_z, s=4, alpha=0.4)
ax.scatter(center_x, center_y, center_z, s=12, alpha=0.05)
ax.plot(trajectory_x, trajectory_y, trajectory_z) #Able to see how it moved under the influence of gravity
plt.show()
plt.figure()
plt.plot(force_history)
plt.show()