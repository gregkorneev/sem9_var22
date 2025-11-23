#ifndef NQUEENS_H
#define NQUEENS_H

// Решение задачи для одного N с (возможно) выводом расстановок
void solveSingleN(int n);

// Серия экспериментов для N = 1..maxN
void runExperiments(int maxN);

// Один эксперимент: для заданного N
// states    — количество рассмотренных позиций (кандидатных установок ферзя)
// solutions — количество корректных расстановок
// ms        — время работы в миллисекундах
void runExperimentForN(int n, long long &states, long long &solutions, double &ms);

#endif // NQUEENS_H
