function plotter(mat, fn, t)
    foo = figure();
    h=plot(mat(:,1), mat(:,2), 'x');%shading interp;camlight;
    set(h,'Color','red','LineWidth',1.5)
    %axis tight;
    set(get(h,'Parent'),'XScale', 'log');
    set(get(h,'Parent'),'YScale', 'log');
    %set(get(h,'Parent'),'ZScale', 'log');
    ylabel('Count');
    xlabel('Out degree');
    legend(t,'SouthWest');
    set(foo, 'Position', [400 320 400 320]);
    set(foo,'Visible','off');
    set(gcf, 'PaperPositionMode', 'auto');
    print(foo, fn, '-dpng');
end