class Solution {
public:
    int divide(int dividend, int divisor) {
        int quotient=0;
        if(divisor==0 || (dividend == INT_MIN && divisor == -1)) return INT_MAX;
        //判定结果正负
        int sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;
        long long dvd = labs(dividend);
        long long dvs = labs(divisor);
        //把一个数表示为2的阶乘和
        while(dvd >= dvs)
        {
            long long tmp = dvs;
            long long multiple = 1;
            while(dvd >= (tmp << 1))
            {
                tmp <<= 1;
                multiple <<= 1;
            }
            dvd -= tmp;
            quotient += multiple;
        }
        return sign == 1 ? quotient : -quotient;
    }
};