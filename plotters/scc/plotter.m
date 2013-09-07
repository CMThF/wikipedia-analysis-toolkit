function plotter(mat, fn, t)
    foo = figure();
    h=plot(mat(:,1), mat(:,2), 'x-');%shading interp;camlight;
    set(h,'Color','red','LineWidth',1.5)
    %axis tight;
    set(get(h,'Parent'),'XScale', 'log');
    set(get(h,'Parent'),'YScale', 'log');
    %set(get(h,'Parent'),'ZScale', 'log');
    ylabel('Number of components');
    xlabel('Size of strongly connected component');
    legend(t);
    set(foo, 'Position', [400 320 400 320]);
    set(gcf, 'PaperPositionMode', 'auto');
    set(foo,'Visible','off'); 
    print(foo, fn, '-dpng');
end