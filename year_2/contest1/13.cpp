#include <iostream>


int main() {

    int n, size = 0;

    std::cin >> n;

    if (n == 0)
        std::cout << 0;
    
    bool out[1000];

    while (n > 0) {
        out[size] = n % 2;
        n /= 2;
        size++;
    }

    for (int j = size - 1; j >= 0; j--) 
        std::cout << out[j];

    std::cout << '\n';

    return 0;
}