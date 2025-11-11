
x = 1:11;
y = f(x);

sumErr = 0;

for i = 1:10
    P = polyfit(x(1:i),y(1:i),i-1);
    op_1 = polyval(P,i+1);
    if round(op_1) ~= round(y(i+1))
        
        sumErr = sumErr + op_1
    end
end