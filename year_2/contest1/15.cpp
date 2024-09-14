#include <iostream>


int main() {
    int n, d1 = 0, d0 = 0;

    std::cin >> n;

    if (n == 0)
        std::cout << 0;

    while (n > 0) {
        if (n % 2 == 0)
            d0++;
        else
            d1++;
        n /= 2;
    }

    for (int i = 0; i < d1; i++) std::cout << 1;
    for (int i = 0; i < d0; i++) std::cout << 0;
    std::cout << '\n';

    return 0;
}