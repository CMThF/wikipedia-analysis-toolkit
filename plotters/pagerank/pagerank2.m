function pagerank2(mat, fn)
    fn
    minimum = min(mat(:,2))
    maximum = max(mat(:,2))
    pr = sort(mat(:,2));
    pr = sort(mat(:,2), 'descend');
    topelements = pr(1:5)
    range = maximum - minimum;
    prange = range/100 *1;
    foo = minimum + prange;
    
    indexes = find(pr < foo);
    
    bot1 = length(indexes)/length(mat(:,2))
    '====================================================='
end