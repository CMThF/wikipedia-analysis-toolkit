function plotter(mat, fn, t)
    foo = figure();
    h=plot(mat(:,1), mat(:,2), 'x');%shading interp;camlight;
    %axis tight;
    set(h,'Color','green','LineWidth',1.5)
    set(get(h,'Parent'),'XScale', 'log');
    set(get(h,'Parent'),'YScale', 'log');
    %set(get(h,'Parent'),'ZScale', 'log');
    ylabel('Count');
    xlabel('In degree');
    legend(t,'SouthWest');
    set(foo, 'Position', [400 320 400 320]);
    set(foo,'Visible','off');
    set(gcf, 'PaperPositionMode', 'auto');
    print(foo, fn, '-dpng');
end