#include <iostream>


int main() {
    int size = 1000000;

    bool sieve[size];

    int n, count = 1;

    std::cin >> n;
    
    sieve[1] = true;
    sieve[2] = true;

    for (int i = 3; i < size; i++) sieve[i] = true;

    for (int i = 2; i < size; i++){
        if (sieve[i]){
            if (count == n){
                std::cout << i << '\n';
                break;
            }
            count++;
            for (int j = 2*i; j < size; j+=i){
                sieve[j] = false;
            }
        }
    }

    return 0;
}