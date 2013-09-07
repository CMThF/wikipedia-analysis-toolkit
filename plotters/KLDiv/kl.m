function kl(A, B, fn, sp1, sp2)
    
    [C, ia, ic] = unique(A(:,sp1));
    countA = zeros(length(C), 1);
    
    for i = 1:length(A(:,sp1))
        countA(ic(i)) = countA(ic(i)) +1;
    end
    
    [C, ia, ic] = unique(B(:,sp2));
    countB = zeros(length(C), 1);
    
    for i = 1:length(B(:,sp2))
        countB(ic(i)) = countB(ic(i)) +1;
    end
    [m, n] = size(countA);
    [x,y] = size(countB);
    if m < x
%         countA = [countA; zeros(x-m, 1)];
          countB = countB(1:m,:);
    end
    if x < m
%         countB = [countB; zeros(m-x, 1)];
          countA = countA(1:x,:);
    end
    size(countA);
    size(countB);
    dist = KLDiv(countA', countB');
    dlmwrite(fn, dist);
end