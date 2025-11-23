#include "nqueens.h"

#include <iostream>
#include <chrono>
#include <iomanip>
#include <vector>
#include <cmath>

using long_long = long long;

// -------------------------------------------------------
// Вспомогательные функции для задачи N ферзей
// -------------------------------------------------------

// Проверка, можно ли поставить ферзя в клетку (row, col),
// чтобы он не бил уже расставленных ферзей.
static bool isSafe(const std::vector<int> &cols, int row, int col) {
    for (int r = 0; r < row; ++r) {
        int c = cols[r];
        if (c == col) {
            return false; // тот же столбец
        }
        if (std::abs(c - col) == std::abs(r - row)) {
            return false; // диагональ
        }
    }
    return true;
}

// Печать одной расстановки ферзей в виде доски.
static void printBoard(const std::vector<int> &cols, int n, long_long solutionIndex) {
    std::cout << "Решение " << solutionIndex << ":\n";
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            if (cols[r] == c) {
                std::cout << "Q ";
            } else {
                std::cout << ". ";
            }
        }
        std::cout << "\n";
    }
    std::cout << "\n";
}

// Рекурсивный перебор расстановок ферзей.
// row         — текущая строка, в которую пытаемся поставить ферзя
// n           — размер доски (N x N) и количество ферзей
// cols[row]   — в каком столбце размещён ферзь в строке row
// states      — счётчик рассмотренных позиций (кандидатных установок)
// solutions   — число корректных расстановок
// print       — печатать ли найденные решения
static void solveNQueensRecursive(int row,
                                  int n,
                                  std::vector<int> &cols,
                                  long_long &states,
                                  long_long &solutions,
                                  bool print) {
    if (row == n) {
        // Удалось расставить ферзей во все строки — найдено решение
        ++solutions;
        if (print) {
            printBoard(cols, n, solutions);
        }
        return;
    }

    // Перебираем все столбцы в текущей строке
    for (int col = 0; col < n; ++col) {
        ++states; // считаем каждую попытку поставить ферзя
        if (isSafe(cols, row, col)) {
            cols[row] = col;
            solveNQueensRecursive(row + 1, n, cols, states, solutions, print);
            // cols[row] можно не сбрасывать: следующая попытка просто перезапишет значение
        }
    }
}

// -------------------------------------------------------
// Публичная функция: один эксперимент для заданного N
// (используется в runExperiments в другом файле).
// -------------------------------------------------------
void runExperimentForN(int n, long_long &states, long_long &solutions, double &ms) {
    states = 0;
    solutions = 0;
    ms = 0.0;

    if (n <= 0) {
        return;
    }

    std::vector<int> cols(n, -1);

    auto start = std::chrono::steady_clock::now();
    solveNQueensRecursive(0, n, cols, states, solutions, false);
    auto end = std::chrono::steady_clock::now();

    ms = std::chrono::duration<double, std::milli>(end - start).count();
}

// -------------------------------------------------------
// Решение задачи для одного N.
// Для малых N выводим найденные расстановки,
// для больших N только считаем их количество и время.
// -------------------------------------------------------
void solveSingleN(int n) {
    if (n <= 0) {
        std::cout << "N должно быть положительным.\n";
        return;
    }

    bool printSolutions = (n <= 6); // чтобы не захламлять вывод при больших N

    std::cout << "\n=== Задача расстановки N ферзей для N = " << n << " ===\n";
    if (printSolutions) {
        std::cout << "Выводим все найденные корректные расстановки:\n\n";
    } else {
        std::cout << "N довольно велико, вывод расстановок отключён (считаем только количество).\n\n";
    }

    long_long states = 0;
    long_long solutions = 0;
    std::vector<int> cols(n, -1);

    auto start = std::chrono::steady_clock::now();
    solveNQueensRecursive(0, n, cols, states, solutions, printSolutions);
    auto end = std::chrono::steady_clock::now();

    double ms = std::chrono::duration<double, std::milli>(end - start).count();

    std::cout << std::fixed << std::setprecision(6);
    std::cout << "Рассмотрено позиций (кандидатных установок ферзя): " << states << "\n";
    std::cout << "Число корректных расстановок: " << solutions << "\n";
    std::cout << "Время работы: " << ms << " мс\n";

    std::cout << "\nКомментарий по сложности:\n";
    std::cout << "• Алгоритм использует полный перебор с возвратом (backtracking).\n";
    std::cout << "• Количество рассматриваемых позиций растёт экспоненциально с увеличением N.\n";
    std::cout << "• Для больших N такой перебор становится практически неприемлем по времени.\n";
}
