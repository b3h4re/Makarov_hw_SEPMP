#include <iostream>


int main() {

    int n, index;

    std::cin >> n;

    double r, h, rho, m, max_m = 0;

    for (int i = 0; i < n; i++){
        std::cin >> r >> h >> rho;

        m = r*r*h*rho;
        if (m > max_m) {
            max_m = m;
            index = i;
        }
    }

    std::cout << index << '\n';

    return 0;
}