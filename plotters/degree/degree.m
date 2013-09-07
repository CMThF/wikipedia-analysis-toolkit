function degree(degreemat, fn, t)
    degree = degreemat(find(degreemat(:,2)),2);
    [C, ia, ic] = unique(degree);
    count = zeros(length(C), 1);
    
    for i = 1:length(degree)
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
    xlabel('Degree');
    %colorbar;
    %caxis auto;%([0 600]);
    %view(-222,30);
    legend(t);
    set(foo, 'Position', [400 320 400 320]);
    set(foo,'Visible','off');
    set(gcf, 'PaperPositionMode', 'auto');
    set(foo,'Visible','off') 
    print(foo, fn, '-dpng');
end