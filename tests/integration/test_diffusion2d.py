"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w = 20., h = 30., dx = 0.2, dy = 0.4)
    solver.initialize_physical_parameters(d=2., T_cold=200., T_hot=500.)
    assert round(solver.dt, 3) == 0.008


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    # Set domain and physical parameters
    w, h = 10.0, 11.0  # Width and height of the domain
    dx, dy = 0.1, 0.2  # Grid spacing in x and y directions
    T_cold, T_hot = 301.0, 701.0  # Cold and hot temperatures

    # Initialize the domain and physical parameters
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(T_cold=T_cold, T_hot=T_hot)

    # Set the initial condition
    res = solver.set_initial_condition()

    # Test each grid point
    radius_squared = 2**2  # Radius of the circle squared
    center_x, center_y = 5.0, 5.0  # Center of the hot circle
    nx, ny = solver.nx, solver.ny  # Number of grid points in x and y directions

    for i in range(nx):
        for j in range(ny):
            # Calculate the squared distance from the center of the circle
            x, y = i * dx, j * dy
            distance_squared = (x - center_x) ** 2 + (y - center_y) ** 2

            # Check if the point is inside or outside the circle
            if distance_squared < radius_squared:
                # Inside the circle, temperature should be T_hot
                assert res[i, j] == T_hot, f"Expected T_hot={T_hot} at ({i},{j}), got {res[i, j]}"
            else:
                # Outside the circle, temperature should be T_cold
                assert res[i, j] == T_cold, f"Expected T_cold={T_cold} at ({i},{j}), got {res[i, j]}"
