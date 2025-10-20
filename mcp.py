import random
import math
import matplotlib.pyplot as plt

pi = math.pi
r = 1

def random_point():
    x = random.uniform(-r,r)
    y = random.uniform(-r,r)
    return x,y

def estimate_pi_visual(points):
    points_inside_circle , points_outside_circle = 0,0
    inside_x, inside_y, outside_x, outside_y = [],[],[],[]
    pi_estimations = []
    no_of_points = []

    for _ in range(points):
        x,y = random_point()
        placement = math.sqrt(x**2 + y**2)

        if placement <= r:
            points_inside_circle += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            points_outside_circle +=1
            outside_x.append(x)
            outside_y.append(y)

        total_points = points_inside_circle + points_outside_circle
        estimate_pi = 4 * points_inside_circle / total_points
        pi_estimations.append(estimate_pi)
        no_of_points.append(total_points)

    plt.figure(figsize=(12,6))

    plt.subplot(1,2,1)
    plt.scatter(inside_x, inside_y, color='green', s=1, label='Inside Circle')
    plt.scatter(outside_x, outside_y, color='red', s=1, label='Outside Circle')
    circle = plt.Circle((0,0), r, color='black', fill=False, linestyle='--')
    plt.gca().add_artist(circle)
    plt.xlim(-r-0.1, r+0.1)
    plt.ylim(-r-0.1, r+0.1)
    plt.title('Monte Carlo Pi simulation points')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid()
    plt.tight_layout()
    plt.legend()

    plt.subplot(1,2,2)
    plt.plot(no_of_points, pi_estimations, label="Estmated Pi", color='blue')
    plt.axhline(y=pi, color='black', linestyle='--', label='Actual Math Pi')
    plt.title('Monte Carlo Pi estimation')
    plt.xlabel('Number of Points')
    plt.ylabel('Estimated Pi Value')
    plt.grid()
    plt.tight_layout()
    plt.legend()

    plt.show()

if __name__ == "__main__":
    try:
        points = int(input("Enter number of points to estimate pi: "))
        estimate_pi_visual(points)

    except ValueError:
        print("Please enter number only, better go above 100")