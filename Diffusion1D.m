clear all, close all, clc

% Physics
Lx = 10; % length of domain in x direction, m
D = 1; % Diffusion coefficient
tt = 1; % total time of simulation in s

% Preprocessing
nx = 100; % number of grid points
dx = Lx/(nx-1); % spacing between points, m
X = -Lx/2:dx:Lx/2; % vectorized positions of gridpoints
dt = 1e-3; % time interval 
nt = tt/dt; % number of time intervals

% Initial conditions
C0 = 1; % Concentration amplitude
w = 1; % Concentration width
cx = 0; % Location of amplitude center in x direction
C = C0 * exp(-(X-cx).^2/w);
time = 0; % initial time, s
% Action
for it = 1:nt
    dCdt = D * diff(diff(C)/dx)/dx;
    C(2:end-1) = C(2:end-1) + dCdt * dt;
    time = time + dt;
    %postprocessing
    plot(X,C,'LineWidth',2,'Color','#129823')
    title(["One dimensional diffusion after ", num2str(time)," seconds"])
    xlabel("x(m)")
    ylabel("Concentration")
    axis([-Lx/2 Lx/2 0 1])
    drawnow
end
