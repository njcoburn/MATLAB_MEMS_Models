clear
clc

%system variables%
e0 = 8.85418782e-12;
V = 30; %biasing voltage
g0 = 3e-6; %beam to electrode gap
Q = 0.5;
l = 300e-6; %length of beam
E = 79e9; %Au Young's 
t = 0.8e-6; %thickness of beam
w = 100e-6; %width of beam
k = 10.0; %spring constant , N/m
ks = ((pi^4)*E*w*t)/(8*(l^3)); %ks factor
m = 0.35*(w)*(l)*(t)*(19320); %mass , Kg for Au
freq = 39.5e3;
C1 = 1e-80;
C2 = 1e-75;
A = w*w; %w*l*0.75;
t_d = 150e-9;
e_r = 7.6;
y_x = 0.06e-6;%lambda

%%%%%%%%%%%%%%%%%%%%%
outp = sim('MEMS_Switch',100e-6);

data = outp.simout;
ti = outp.tout(1:end-1);
pos = data.Data(1:end-1);
hold on
plot(ti,pos);
