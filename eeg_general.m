% 改路徑
eeg_folder = 'eegevent/';
save_set_folder = 'eegset';

lct_sub = {'001','004','006'};
hct_sub = {'002','003'};
% 分析 h/lct general 表現 , event 2, 3 , alpha{8,12}, beta {12,40}訊號平均強度

% data preprocessing
% files = dir('eegevent/*test*.txt');
% for i = 1:length(files)
%     filename = extractBefore(files(i).name,'.txt');
%     fileinfo = split(filename,'_');
%     subID = fileinfo(2);
%     if any(strcmp(lct_sub,subID))
%         filename = strcat('lct_',filename);
%     else
%         filename = strcat('hct_',filename);
%     end
%     EEG = pop_importdata('dataformat','ascii','nbchan',0,'data',strcat(eeg_folder,files(i).name),'srate',250,'pnts',0,'xmin',0);
%     EEG = eeg_checkset( EEG );
%     EEG = pop_chanevent(EEG, 10,'edge','leading','edgelen',0);
%     EEG = eeg_checkset( EEG );
%     EEG = pop_select( EEG, 'channel',[2:9] );
%     EEG = eeg_checkset( EEG );
%     EEG = pop_eegfiltnew(EEG, 'locutoff',8,'hicutoff',40);
%     EEG = eeg_checkset( EEG );
%     EEG = pop_saveset( EEG, 'filename',strcat(filename,'.set'),'filepath',save_set_folder);
%     EEG = eeg_checkset( EEG );
% end
% data preprocessing done


% ch 改成要分析的 channel
files = dir('eegset/hct*test*.set');
event = {'2','2','3'};
event_sec = {[-5  0],[0  5]};
bandname = {'alpha_','lowbeta_','midbeta_','highbeta_'};
band = {8,12,12,15,15,20,18,40};
num = 0;
for b = 1:4
    num = 0;
    for n = 1:3
        eeg_topo_all = [];
        for i = 1:length(files)
            eeg_topo = zeros(1,7);
            for ch = 1:7
	            eegrobot = pop_loadset('filename', files(i).name, 'filepath', save_set_folder);
                e = pop_epoch( eegrobot, event, event_sec{mod(n+1,2)+1}, 'epochinfo', 'yes'); % 修改 event
                w = mean(e.data(ch,:,:),3);
                [S,F,T,P] = spectrogram(w,250,125,250,250);
                PP = mean(P, 2);
                eeg_topo(ch) = calcAvgBandPower(PP,band{1+(b-1)*2},band{2+(b-1)*2});
            end
            eeg_topo_all = cat(1,eeg_topo_all,eeg_topo);
        end
        topoplot(mean(eeg_topo_all), 'pilot_chan.loc','nosedir','+Y','electrodes','ptslabels');
        caxis([-20, 20]);
        num = num+1;
        saveas(gca,strcat('hct_',bandname{b})+string(num)+'.png');
    end
end

function avgbandpower = calcAvgBandPower(eeg_data,band_start,band_end)
    current = 0;
    for frequency = band_start:band_end
        current = current+eeg_data(frequency);
    end
    avgbandpower = current/5;
end
