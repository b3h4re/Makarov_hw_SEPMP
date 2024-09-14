#include <iostream>


int main(){

    int n;

    unsigned long long res = 1;

    std::cin >> n;

    for (int i = 2; i <= n; i++)
        res *= i;

    std::cout << res;
    
    return 0;
}