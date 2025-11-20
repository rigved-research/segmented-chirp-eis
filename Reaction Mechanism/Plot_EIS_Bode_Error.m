load('Mech2_Vac0_0.001.Rs_10.Vdc_0.3.b1_5.f0_0.001Hz.ff_1Hz.tf_5400s.Idx_5.mat')

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


%% Bode Plots
figure('Units','centimeters', 'Position', [2 2 7.5 8]);
% Bode Magnitude Plot
subplot(2, 1, 1);
semilogx(f, abs(z_chirp), 'Color', chirp_color, 'LineWidth', 3); 
hold on;
semilogx(F, abs(Z), 'o-', 'Color', conventional_color, 'MarkerFaceColor', conventional_color, 'LineWidth', 1, 'MarkerSize', 3); 
ylabel('|Z(f)| [\Omega]');
grid on;
axis tight;
set(gca, 'XMinorGrid', 'off');
set(gca, 'FontSize', 10);

% Bode Phase Plot
subplot(2, 1, 2);
semilogx(f, (180/pi) * angle(z_chirp), 'Color', chirp_color, 'LineWidth', 3); 
hold on;
semilogx(F, (180/pi) * angle(Z), 'o-', 'Color', conventional_color, 'MarkerFaceColor', conventional_color, 'LineWidth', 1, 'MarkerSize', 3); 
xlabel('Frequency [Hz]');
ylabel('\angle Z(f)°');
grid on;
axis tight;
set(gca, 'XMinorGrid', 'off');
set(gca, 'FontSize', 10);


%% Error
% z_chirp_interpolated = interp1(f, z_chirp, F, 'pchip');
% error = (abs(Z - z_chirp_interpolated) ./ abs(Z))*100;

figure('Units','centimeters', 'Position', [2 2 12 6.5]);
semilogx(F, error, 'o-', 'LineWidth', 1.5, 'Color', '#04938c', 'MarkerFaceColor', '#04938c', 'LineWidth', 1.5);
grid on;
xlabel('Frequency [Hz]', 'FontSize', 12);
ylabel('Abs. Relative Error [%]', 'FontSize', 12);
set(gca, 'FontSize', 12);
set(gca, 'XMinorGrid', 'off');
fontname("CMU Serif")
hold on
