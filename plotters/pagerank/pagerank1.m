function pagerank1(mat, fn)
    fn
    minimum = min(mat(:,6))
    maximum = max(mat(:,6))
    pr = sort(mat(:,6), 'descend');
    topelements = pr(1:5)
    range = maximum - minimum;
    prange = range/100 *1;
    foo = minimum + prange;
    
    indexes = find(pr < foo);
    
    bot1 = length(indexes)/length(mat(:,6))
    '====================================================='
end