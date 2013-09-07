function betweeness(mat, fn, t)
    
    leindex = find(mat(:,2));
    ofinterest = round(mat(leindex,2));
    [C, ia, ic] = unique(ofinterest);
    count = zeros(length(C), 1);
    
    for i = 1:length(ofinterest)
        count(ic(i)) = count(ic(i)) +1;
    end
    foo = figure();
    
    h=plot(C, count, 'x');%shading interp;camlight;
    set(h,'Color','blue','LineWidth',1.5)
    %axis tight;
    set(get(h,'Parent'),'XScale', 'log');
    set(get(h,'Parent'),'YScale', 'log');
    %set(get(h,'Parent'),'ZScale', 'log');
    ylabel('Count');
    xlabel('Betweeness');
    %colorbar;
    %caxis auto;%([0 600]);
    %view(-222,30);
    legend(t,'SouthWest');
    set(foo, 'Position', [400 320 400 320]);
    set(foo,'Visible','off');
    set(gcf, 'PaperPositionMode', 'auto'); 
    print(foo, fn, '-dpng');
end