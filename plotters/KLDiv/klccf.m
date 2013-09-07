function klccf(A, B, fn, sp1, sp2)
    countA = A(:,sp1);
    countB = B(:,sp2);
    
    countA = cutthatshit(countA);
    countB = cutthatshit(countB);
    
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

function M = cutthatshit(X)
    I = find(X>0);
    M = X(I);
end