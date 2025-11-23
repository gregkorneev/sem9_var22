#include <iostream>
#include "nqueens.h"

int main() {
    std::cout << "Семинар 9. Перебор. Задача: N ферзей.\n";

    int n;
    std::cout << "Введите размер доски N (N x N): ";
    std::cin >> n;

    solveSingleN(n);

    std::cout << "\nТеперь проведём эксперименты для разных размеров.\n";
    std::cout << "Введите максимальное N для экспериментов: ";
    int maxN;
    std::cin >> maxN;

    runExperiments(maxN);

    std::cout << "\nРабота программы завершена.\n";
    return 0;
}
