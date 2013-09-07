clear all;
close all;
addpath('..\jsonlab');
langs = cellstr(['de';'es';'fr';'it';'ru';'en']);
mat_sorted_diffs_frac = [];

for i = 1:length(langs)
    language = langs{i};
    path = strcat(strcat('..\..\Pagecounts_to_Degree\',language),'_stripped.json');
    json2data=loadjson(path);

    titles = fieldnames(json2data); %beacuas matlab so gay
    datamat = [];
    for i = 1:numel(titles)
        datamat = [datamat;json2data.(titles{i})(1,:), json2data.(titles{i})(2,:), json2data.(titles{i})(3,:)]; %fancy addressing, because cells
    end

    % datamat nach schema Difference Competitive(1), Difference Fractional(2),
    % Competitive rank von A aus(3), Fractional rank von A aus(4), Competitive
    % rank von B aus(5), Fractional rank von B aus(6)
    % A ->pc, B ->degree
   

    diff_competitive_mean = mean(datamat(:,1));
    diff_competitive_median = median(datamat(:,1));
    diff_fractional_mean = mean(datamat(:,2));
    diff_fractional_median = median(datamat(:,2));

%     h=figure('visible','off');
%     loglog(datamat(:,3),datamat(:,5), '.')
%     title('Pagecounts vs Degree (Competition Ranking)')
%     xlabel('Pagecount Rank')
%     ylabel('Degree Rank')
%     hold off;
%     grid on;
%     saveas(h, strcat(language, '_PCvsDEG_comp'), 'png');
    
    h2=figure('visible','off');
    loglog(datamat(:,4),datamat(:,5), '.');
    title('Pagecounts vs Degree (Fractional Ranking)');
    xlabel('Pagecount Rank');
    ylabel('Degree Rank');
    legend(language, 'Location', 'NorthWest')
    hold off;
    grid on;
    saveas(h2, strcat(language, '_PCvsDEG_frac'), 'png');

    sorted_diffs_comp = sort(datamat(:,1));
    sorted_diffs_frac = sort(datamat(:,2));

    mat_sorted_diffs_frac = [mat_sorted_diffs_frac, sorted_diffs_frac];

%     i=figure('visible','off');
%     plot(sorted_diffs_comp)
%     title('Differences (Competition Ranking)')
%     xlabel('Count')
%     ylabel('Difference')
%     grid on;
%     saveas(i, strcat(language, '_PCvsDEG_compdif'), 'png');
    


%     k=figure('visible','off');
%     plot(sorted_diffs_comp(sorted_diffs_comp < 10000))
%     title('Differences below a value of 10000 (Competition Ranking)')
%     xlabel('Count')
%     ylabel('Difference')
%     grid on;
%     saveas(k, strcat(language, '_PCvsDEG_compdifbelow10k'), 'png');
    


    %spearman rank correlation
    mean_x = mean(datamat(:,4));
    mean_y = mean(datamat(:,6));
    foo = 0;
    bar1 = 0;
    bar2 = 0;
    for i = 1:length(datamat)
        foo = foo + ((datamat(i,4) - mean_x)*(datamat(i,6) - mean_y));
        bar1 = bar1 + (datamat(i,4) - mean_x)^2;
        bar2 = bar2 + (datamat(i,6) - mean_y)^2;
    end
    spearmans = foo/sqrt(bar1*bar2);
    
    fid = fopen(strcat(language, '_results.txt'), 'w');
    fprintf(fid, 'Language: %s\n', language);
    fprintf(fid, 'Competitive Difference Mean: %d\n', diff_competitive_mean);
    fprintf(fid, 'Competitive Difference Median: %d\n', diff_competitive_median);
    fprintf(fid, 'Fractional Difference Mean: %d\n', diff_fractional_mean);
    fprintf(fid, 'Fractional Difference Median: %d\n', diff_fractional_median);
    fprintf(fid, 'Spearman Rank Correlation: %d\n', spearmans);
    fclose(fid);  
end

i2=figure('visible','off');
for i=1:(length(langs))
    plot(mat_sorted_diffs_frac(:,i), 'LineWidth', 2);
    hold all; 
end
title('Differences (Fractional Ranking)')
xlabel('Index')
ylabel('Difference')
legend('de','es','fr','it','ru','en', 'Location', 'Northwest');
grid on;
hold off;
saveas(i2, 'PCvsDEG_fracdif', 'png');

k2=figure('visible','off');
for i=1:(length(langs))
    x = mat_sorted_diffs_frac(:,i);
    plot(x(x < 10000), 'LineWidth', 2);
    hold all; 
end
title('Differences below a value of 10000 (Fractional Ranking)')
xlabel('Index')
ylabel('Difference')
legend('de','es','fr','it','ru','en', 'Location', 'Northwest');
grid on;
hold off;
saveas(k2, 'PCvsDEG_fracdifbelow10k', 'png');


