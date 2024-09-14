#include <iostream>


int main() {

    int n, mid;

    std::cin >> n;

    mid = n / 2;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j ++){
            if (abs(mid - j) + abs(mid - i) <= mid){
                std::cout << '+';
            } else {
                std::cout << ' ';
            }
        }
        std::cout << '\n';
    }

    return 0;
}