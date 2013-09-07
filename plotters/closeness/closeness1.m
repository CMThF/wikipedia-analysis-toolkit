function closeness1(mat, fn, t)
    
    leindex = find(mat(:,3));
    ofinterest = round(mat(leindex,3)*100);
    [C, ia, ic] = unique(ofinterest);
    count = zeros(length(C), 1);
    
    for i = 1:length(ofinterest)
        count(ic(i)) = count(ic(i)) +1;
    end
    foo = figure();
    h=bar(C/100, count);%shading interp;camlight;
    %axis tight;
    %set(get(h,'Parent'),'XScale', 'log');
    %set(get(h,'Parent'),'YScale', 'log');
    %set(get(h,'Parent'),'ZScale', 'log');
    ylabel('Count');
    xlabel('Closeness');
    %colorbar;
    %caxis auto;%([0 600]);
    %view(-222,30);
    legend(t,'SouthWest');
    set(foo, 'Position', [400 320 400 320]);
    set(foo,'Visible','off');
    set(gcf, 'PaperPositionMode', 'auto');
    print(foo, fn, '-dpng');
end