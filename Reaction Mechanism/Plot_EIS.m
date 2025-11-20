load('Full_Mech3_Vac0_0.001.Rs_10.Vdc_0.3.b1_5.mat')

chirp_color = '#94dc7b'; 
conventional_color = '#003f5c'; 

%% Nyquist Plot
figure('Units','centimeters', 'Position', [2 2 7.5 6.5]);
plot(real(z_chirp), -imag(z_chirp), 'Color', chirp_color, 'LineWidth', 3); 
hold on;
plot(real(Z), -imag(Z), 'o-', 'Color', conventional_color, 'MarkerFaceColor', conventional_color, 'LineWidth', 1, 'MarkerSize', 3); % Conventional data
xlabel('Z_r(f) [\Omega]');
ylabel('-Z_j(f) [\Omega]');
grid on;
axis tight;
xticks = get(gca, 'XTick');
xticks = xticks(1:1:end); 
yticks = get(gca, 'YTick');
yticks = yticks(1:1:end); 
set(gca, 'XTick', xticks);
set(gca, 'YTick', yticks);
set(gca, 'FontSize', 10); 
fontname("CMU Serif")
