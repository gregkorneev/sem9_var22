#include <iostream>
#include <cmath>

using namespace std;

const int MAX_N = 15;
int N;
int colInRow[MAX_N];
long long solutions;
long long steps;

bool isSafe(int row, int col) {
    for (int prevRow = 0; prevRow < row; ++prevRow) {
        int prevCol = colInRow[prevRow];

        if (prevCol == col) {
            return false; // тот же столбец
        }

        if (abs(row - prevRow) == abs(col - prevCol)) {
            return false; // диагональ
        }
    }
    return true;
}

void placeQueen(int row) {
    steps++;

    if (row == N) {
        solutions++;
        return;
    }

    for (int col = 0; col < N; ++col) {
        if (isSafe(row, col)) {
            colInRow[row] = col;
            placeQueen(row + 1);
        }
    }
}

int main() {
    cout << "N  solutions       steps\n";

    for (int n = 4; n <= 14; ++n) {
        N = n;
        solutions = 0;
        steps = 0;

        placeQueen(0);

        cout << N << "  " << solutions << "        " << steps << "\n";
    }

    return 0;
}
