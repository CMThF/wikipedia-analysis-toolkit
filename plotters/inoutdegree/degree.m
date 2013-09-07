function degree(InOutDeg, fn, t)
    l = length(InOutDeg);
    for i = 1:l
        if InOutDeg(i,1) == 0
            InOutDeg(i,1) = 1;
        end
        if InOutDeg(i,2) == 0
            InOutDeg(i,2) = 1;
        end
    end

    InOutDeg = log(InOutDeg);
    InOutDeg = round(InOutDeg);

    count = zeros(max(InOutDeg(:,1))+1,max(InOutDeg(:,2))+1); %zeile in, spalte out
    for i = 1:length(InOutDeg)
        count(InOutDeg(i,1)+1,InOutDeg(i,2)+1) = count(InOutDeg(i,1)+1,InOutDeg(i,2)+1)+ 1;
    end

    foo = figure();
    h=surf(count);shading interp;camlight;axis tight
    set(get(h,'Parent'),'XScale', 'log');
    set(get(h,'Parent'),'YScale', 'log');
    set(get(h,'Parent'),'ZScale', 'log');
    
    xlabel('Outdegree'); %x und y vertauscht
    ylabel('Indegree');
    
    colorbar('NorthOutside');
    caxis auto;%([0 600]);
    view(-222,30);
    title(t)
    set(foo, 'Position', [400 320 400 320]);
    set(foo,'Visible','off');
    set(gcf, 'PaperPositionMode', 'auto');
    print(foo, fn, '-dpng');
end