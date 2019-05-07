fid = fopen('miserables.mtx');
A = cell2mat(textscan(fid, '%d %d %d', 1));
data = cell2mat(textscan(fid, '%d %d', A(3)));
data_t = data(:, [2 1]);
data = [data;data_t];
data(:,3) = 1;
adj = edgeL2adj(data);
fclose(fid);
 
k = 11;
[m, mh, Q] = newmanGirvan(adj, k);

fid = fopen('result.txt','wt');
fprintf(fid, '%d %d\n', A(1), k);
for i=1:k
    fprintf(fid, '%d ', cell2mat(m(i)));
    fprintf(fid, '\n');
end
fclose(fid);
fid = fopen('edgel.txt', 'wt');
fprintf(fid, '%d %d %d\n', data');
fclose(fid);