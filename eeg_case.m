% alpha = readtable('case2_case3.xlsx','Range','C3:I6');
% alpha = table2array(alpha);
alpha = readtable('case2_case3.xlsx','Range','C31:I32');
alpha = table2array(alpha);
% lowbeta = readtable('case2_case3.xlsx','Range','C10:I13');
% lowbeta = table2array(lowbeta);
lowbeta = readtable('case2_case3.xlsx','Range','C36:I37');
lowbeta = table2array(lowbeta);
% midbeta = readtable('case2_case3.xlsx','Range','C17:I20');
% midbeta = table2array(midbeta);
midbeta = readtable('case2_case3.xlsx','Range','C41:I42');
midbeta = table2array(midbeta);
% highbeta = readtable('case2_case3.xlsx','Range','C24:I27');
% highbeta = table2array(highbeta);
highbeta = readtable('case2_case3.xlsx','Range','C46:I47');
highbeta = table2array(highbeta);

topoplot(alpha(1,:), 'pilot_chan.loc','nosedir','+Y','electrodes','ptslabels');
caxis([-20, 20]);
saveas(gca,'case2_alpha_phase3.png');

topoplot(alpha(2,:), 'pilot_chan.loc','nosedir','+Y','electrodes','ptslabels');
saveas(gca,'case3_alpha_phase3.png');

% topoplot(highbeta(3,:), 'pilot_chan.loc','nosedir','+Y','electrodes','ptslabels');
% saveas(gca,'case3_highbeta_phase1.png');
% 
% topoplot(highbeta(4,:), 'pilot_chan.loc','nosedir','+Y','electrodes','ptslabels');
% saveas(gca,'case3_highbeta_phase2.png');