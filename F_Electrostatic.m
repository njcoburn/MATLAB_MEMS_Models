function y = F_Electrostatic(u)

%system parameters%
e0 = 8.85418782e-12;
V = 42; %biasing voltage
g0 = 3e-6; %beam to electrode gap
Q = 2.0;
l = 300e-6; %length of beam
t = 0.8e-6; %thickness of beam
w = 100e-6; %width of beam
k = 10.0; %spring constant , N/m
k_3 = 974.1e9*w*t/l^3; %spring constant cubic term (971.1 = 80GPa*pi^4/8)
m = 0.35*(w)*(l)*(t)*(19320); %mass , Kg
freq = 39.5e3;
C1 = 1e-80;
C2 = 1e-75;
A = w^2;
t_d = 150e-9;
e_r = 7.6;
y = 0.06e-6;%lambda

y = ((g0+(t_d/e_r)+u)^2);