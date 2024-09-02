# Diffusion1D
Simple 1D diffusion code solving it numerically using finite differences approach

Solving for 1D diffusion equation 

$$\frac{\partial{C}}{\partial{t}} = D\frac{\partial^2{C}}{\partial{x^2}} $$

This applies to all diffusion-like problems like heat diffusion where we would have Temperature instead of C.

$$\frac{\partial{T}}{\partial{t}} = D\frac{\partial^2{T}}{\partial{x^2}} $$

where D is in that case thermal diffusivity kappa

$$ D = \kappa = \frac{k}{\rho C_p} $$

The file Diffusion1D.m is MATLAB code that simulates consecutive timestep evaluations of concentration from initial conditions.
The initial concentration distribution is set to be Gaussian distribution centered around x=0

https://github.com/user-attachments/assets/eee3bbe7-6f1e-4c57-b9b1-85de21fdbebf

Diffusion1D.py is the Python file that makes the same simulation from the same equation. The video of Python version is below

![movie](https://github.com/user-attachments/assets/ecc5c3cc-f1ec-4219-af76-f7c854665918)
