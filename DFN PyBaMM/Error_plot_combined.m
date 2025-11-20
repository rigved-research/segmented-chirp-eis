clc;
clear;

load("Full_SoC_0.2.Temp_263.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat")

% z_chirp_interpolated = interp1(f, z_chirp, F, 'pchip');
% error = (abs(Z - z_chirp_interpolated) ./ abs(Z))*100;

color1 = '#045970';
figure('Units','centimeters', 'Position', [2 2 12 6.5]);
semilogx(F, error, 'o-', 'LineWidth', 1.5, 'Color', color1 , 'MarkerFaceColor', color1 ,  'MarkerSize',3);
grid on;
xlabel('Frequency [Hz]');
ylabel('Abs. Relative Error [%]');
set(gca, 'FontSize', 12);
set(gca, 'XMinorGrid', 'off');
axis tight;
fontname("CMU Serif")
hold on

if F(1) == 0.01
    xticks = [1e-2, 1e-1, 1e0, 1e1, 1e2, 1e3, 1e4];
    xlim([1e-2, 1e4]);
else
    xticks = [1e-3, 1e-2, 1e-1, 1e0, 1e1, 1e2, 1e3, 1e4];
    xlim([1e-3, 1e4]);
end
set(gca, 'XTick', xticks);
set(gca, 'XTickLabelRotation', 0)



%%
color2 = '#04938c';
semilogx(F, error, 'o-', 'LineWidth', 1.5, 'Color', color2, 'MarkerFaceColor', color2, 'MarkerSize',3);
grid on;
hold on

%%
color3 = '#2cb688';
semilogx(F, error, 'o-', 'LineWidth', 1.5, 'Color', color3, 'MarkerFaceColor', color3, 'MarkerSize',3);
grid on;
hold on

%%
color4 = '#90e075';
semilogx(F, error, 'o-', 'LineWidth', 1.5, 'Color', color4, 'MarkerFaceColor', color4, 'MarkerSize',3);
grid on;
hold on

%%
color5 = '#003f61';
semilogx(F, error, 'o-', 'LineWidth', 1.5, 'Color', color5, 'MarkerFaceColor', color5, 'MarkerSize',3);
grid on;
hold on

%%
color6 = '#75a4cf';
semilogx(F, error, 'o-', 'LineWidth', 1.5, 'Color', color6, 'MarkerFaceColor', color6, 'MarkerSize',3);
grid on;
hold on

%%
color7 = '#366fab';
semilogx(F, error, 'o-', 'LineWidth', 1.5, 'Color', color7, 'MarkerFaceColor', color7, 'MarkerSize',3);
grid on;
hold on

%%


legend({'-10°C', ...
    '10°C', ...
    '25°C', ...
    '40°C'},...
    'Location', 'north', 'NumColumns',4);







