%Table data from id to t_inters is saved as csv and text files.
load('fine_database.mat');
cell_data = struct2cell(fine_database);
table_data = cell2table([cell_data(1,:); cell_data(2,:); cell_data(3,:); cell_data(4,:); cell_data(5,:); cell_data(6,:); cell_data(7,:)]', 'VariableNames',{'id' 'power' 'speed' 'angle' 'energy' 'depth' 't_inters'});
writetable(table_data, 'python_data.csv');
%writetable(table_data, 'python_data.txt');

%This part saves oct data as csv. When you open it in Excel, not all data
%will be visible. Text editor can be used.
for i = 1:630
    dlmwrite('oct_data.csv',fine_database(i).oct,'delimiter',',', '-append')
end