"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import unittest

class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        """Initialize the solver with default values for tests."""
        self.solver = SolveDiffusion2D()

        # Set up the domain and physical parameters for the tests
        self.solver.w = 20.  # Width of the domain
        self.solver.h = 30.  # Height of the domain
        self.solver.dx = 0.2  # Grid step size in x direction
        self.solver.dy = 0.4  # Grid step size in y direction
        self.solver.T_cold = 100.  # Initial cold temperature
        self.solver.T_hot = 400.  # Initial hot temperature
        self.solver.initialize_domain(self.solver.w, self.solver.h, self.solver.dx, self.solver.dy)

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=20., h=30., dx=0.2, dy=0.4)

        # nx and ny should be based on w/dx and h/dy
        self.assertEqual(self.solver.nx, 100, f"Expected nx=100, but got {self.solver.nx}")
        self.assertEqual(self.solver.ny, 75, f"Expected ny=75, but got {self.solver.ny}")
    



    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_physical_parameters(d=2., T_cold=200., T_hot=500.)

        # Check the calculated dt value (assert with some tolerance)
        expected_dt = 0.008
        self.assertAlmostEqual(self.solver.dt, expected_dt, places=4, msg=f"Expected dt={expected_dt}, but got {self.solver.dt}")
       


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # Initialize physical parameters for this test
        self.solver.nx = 100
        self.solver.ny = 150
        self.solver.T_cold = 100.
        self.solver.T_hot = 400.
        u = self.solver.set_initial_condition()

        # Check the shape of the output matrix u (it should match nx, ny)
        self.assertEqual(u.shape, (self.solver.nx, self.solver.ny),f"Expected u.shape = ({self.solver.nx}, {self.solver.ny}), but got {u.shape}")

        # Check that corners are cold (boundary conditions)
        self.assertEqual(u[0, 0], self.solver.T_cold, "Top-left corner should be cold.")
        self.assertEqual(u[0, -1], self.solver.T_cold, "Top-right corner should be cold.")
        self.assertEqual(u[-1, 0], self.solver.T_cold, "Bottom-left corner should be cold.")
        self.assertEqual(u[-1, -1], self.solver.T_cold, "Bottom-right corner should be cold.")

        # Check if some of the center values are hot (inside the circle, should be equal to T_hot)
        # Based on the implementation, we know that the center will have T_hot values.
        r, cx, cy = 2, 5, 5  # Circle parameters used in set_initial_condition
        for i in range(self.solver.nx):
            for j in range(self.solver.ny):
                # Calculate distance from the center (cx, cy)
                dist = (i * self.solver.dx - cx) ** 2 + (j * self.solver.dy - cy) ** 2
                if dist < r**2:
                    # The points within the radius of the circle should have T_hot
                    self.assertEqual(u[i, j], self.solver.T_hot,f"Expected T_hot={self.solver.T_hot} inside the circle, but got {u[i,j]} at ({i},{j})")
                else:
                    # Points outside the circle should remain at T_cold
                    self.assertEqual(u[i, j], self.solver.T_cold, f"Expected T_cold={self.solver.T_cold} outside the circle, but got {u[i,j]} at ({i},{j})")

           

