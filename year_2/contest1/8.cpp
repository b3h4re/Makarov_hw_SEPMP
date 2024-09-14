#include <iostream>


int main(){

    int n;

    std::cin >> n;

    for (int i = 1; i <= n; i++){
        if (n % i == 0) {
            std::cout << i;

            if (i == n)
                std::cout << '\n';
            else
                std::cout << ' ';
        }
    }
    
    return 0;
}