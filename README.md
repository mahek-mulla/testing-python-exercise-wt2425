# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)
For all the tests, the following changes were made :

**Changing `self.nx = int(w / dx)` to `self.nx = int(h / dx)` in initialize_domain**

**Changing to `dx2, dy2 = self.dx * self.dy, self.dy * self.dy` in initialize_physical_parameters**

**Changing to `u = self.T_hot * np.ones((self.nx, self.ny))` in set_initial_condition**


### pytest log

#### unit 

<img width="1154" alt="Screenshot 2025-01-20 at 7 23 06 PM" src="https://github.com/user-attachments/assets/485bb3bb-8de6-47dc-bc72-4fe212211aca" />

<img width="1159" alt="Screenshot 2025-01-20 at 7 23 19 PM" src="https://github.com/user-attachments/assets/52935532-50b4-4f10-a1ee-2144f2e00938" />

<img width="1151" alt="Screenshot 2025-01-20 at 7 23 29 PM" src="https://github.com/user-attachments/assets/5f9ca867-be58-48dd-a7da-43a761b96e9a" />

#### integration

<img width="1161" alt="Screenshot 2025-01-20 at 7 46 05 PM" src="https://github.com/user-attachments/assets/5e65809a-5d7c-49d2-9350-589580559f89" />

<img width="1167" alt="Screenshot 2025-01-20 at 7 46 13 PM" src="https://github.com/user-attachments/assets/0e1f99c5-7bf7-44e8-a754-ccae710941f2" />


### unittest log

<img width="1152" alt="Screenshot 2025-01-20 at 7 40 00 PM" src="https://github.com/user-attachments/assets/754dc869-8b36-42ac-8846-07525eb16b73" />

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
