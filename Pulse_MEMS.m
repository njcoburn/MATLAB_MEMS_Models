clear
clc

%system variables%
e0 = 8.85418782e-12;
V = 42; %biasing voltage
g0 = 3e-6; %beam to electrode gap
Q = 0.5;
l = 300e-6; %length of beam
E = 50e9; %Au Young's ########changed here
t = 0.8e-6; %thickness of beam
w = 100e-6; %width of beam
k = 10.0; %spring constant , N/m
%ks = (pi^4*E*w*t)/(8*l^3); %ks factor
%ks = (55e-6-k*g0)/(g0^3); %from python script
ks = 0;
m = 0.35*(w)*(l)*(t)*(19320); %mass , Kg for Au
freq = 39.5e3;
C1 = 1e-80;
C2 = 1e-75;
A = w*w; %w*l*0.75;
t_d = 150e-9;
e_r = 7.6;
y_x = 0.06e-6;%lambda

for v = [40 50]

   Period = 100e-6 %20e-6; %time, (sec)
   Pulse_Width = v; %Percentage

    %%%%%%%%%%%%%%%%%%%%%
   outp = sim('MXXX',100e-6);

   data = outp.simout.Data;
   t = outp.tout(1:end-1);
   pos = data(1:end-1,1);
   Vplot = data(1:end-1,2);

   %hold on
   %hold (ax, 'on')

%    yyaxis left
%    plot(t,pos)
%    yyaxis right
%    plot(t,Vplot)
   
   figure(5)
   subplot(2,1,1);
   plot(t,pos,'LineWidth',5)
   xlabel('Time, (s)') 
   ylabel('Gap Height, (m)') 
   hold('on')
   subplot(2,1,2); 
   plot(t,Vplot,'LineWidth',5)
   xlabel('Time, (s)') 
   ylabel('Voltage, (V)') 
   hold('on')
end
