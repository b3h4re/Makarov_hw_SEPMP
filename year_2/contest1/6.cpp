#include <iostream>


int main(){

    int n, m;

    std::cin >> n >> m;

    char filler = '+';

    for (int i = 0; i < n; i++) {
        if (i == 0 || i == n-1){
            filler = '+';
        } else {
            filler = ' ';
        }

        for (int j = 0; j < m; j++){
            if (j == 0 || j == m-1){
                std::cout << '+';
            } else{
                std::cout << filler;
            }
        }

        std::cout << "\n";
    }
    
    return 0;
}