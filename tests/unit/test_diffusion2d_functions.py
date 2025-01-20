"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=20.,h=30.,dx=0.2,dy=0.4)

    assert solver.nx == 100, f"Expected nx=100, but got {solver.nx}"
    assert solver.ny == 75, f"Expected ny=75, but got {solver.ny}"


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.w = 20.
    solver.h = 30.
    solver.dx = 0.2
    solver.dy = 0.4
    solver.initialize_physical_parameters(d=2., T_cold=200., T_hot=500.)

    # Check the calculated dt value (assert with some tolerance)
    expected_dt = 0.008
    assert abs(solver.dt - expected_dt) < 1e-4, f"Expected dt={expected_dt}, but got {solver.dt}"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver = SolveDiffusion2D()
    solver.nx = 100
    solver.ny = 150
    solver.dx = 0.2
    solver.dy = 0.4
    solver.T_cold = 100.
    solver.T_hot = 400.

    u = solver.set_initial_condition()

    # Check the shape of the output matrix u (it should match nx, ny)
    assert u.shape == (solver.nx, solver.ny), f"Expected u.shape = ({solver.nx}, {solver.ny}), but got {u.shape}"

    # Check that corners are cold (boundary conditions)
    assert u[0, 0] == solver.T_cold, "Top-left corner should be cold."
    assert u[0, -1] == solver.T_cold, "Top-right corner should be cold."
    assert u[-1, 0] == solver.T_cold, "Bottom-left corner should be cold."
    assert u[-1, -1] == solver.T_cold, "Bottom-right corner should be cold."

    
