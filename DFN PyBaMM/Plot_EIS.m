load('Full_SoC_0.5.Temp_298.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat')

chirp_color = '#94dc7b'; 
conventional_color = '#003f5c'; 

%% Nyquist Plot
figure('Units','centimeters', 'Position', [2 2 7.5 6.5]);
plot(real(z_chirp)*1e3, -imag(z_chirp)*1e3, 'Color', chirp_color, 'LineWidth', 3); 
hold on;
plot(real(Z)*1e3, -imag(Z)*1e3, 'o-', 'Color', conventional_color, 'MarkerFaceColor', conventional_color, 'LineWidth', 1, 'MarkerSize', 3); % Conventional data
xlabel('Z_r(f) [m\Omega]');
ylabel('-Z_j(f) [m\Omega]');
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
