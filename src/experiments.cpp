#include "nqueens.h"

#include <iostream>
#include <fstream>
#include <filesystem>
#include <iomanip>

using long_long = long long;
namespace fs = std::filesystem;

// -------------------------------------------------------
// Серия экспериментов для N = 1..maxN.
//
// Пишем:
//   data/csv/nqueens_results.csv
//   data/nqueens_report.md
// -------------------------------------------------------
void runExperiments(int maxN) {
    if (maxN <= 0) {
        std::cout << "maxN должно быть положительным.\n";
        return;
    }

    // Создаём папки data и data/csv
    try {
        fs::create_directories("data/csv");
    } catch (...) {
        std::cout << "Не удалось создать папки data/csv.\n";
        return;
    }

    const std::string csvPath = "data/csv/nqueens_results.csv";
    const std::string mdPath  = "data/nqueens_report.md";

    std::ofstream csv(csvPath);
    if (!csv.is_open()) {
        std::cout << "Не удалось открыть файл " << csvPath << " для записи.\n";
        return;
    }

    // Заголовок CSV
    csv << "N,Рассмотрено позиций,Число решений,Время, мс\n";

    std::cout << "\n=== Эксперименты: рост сложности для задачи N ферзей ===\n";
    std::cout << "Результаты таблицы будут сохранены в файле " << csvPath << "\n\n";
    std::cout << "N\tРассмотрено позиций\tЧисло решений\tВремя, мс\n";
    std::cout << "--------------------------------------------------------------\n";

    std::cout << std::fixed << std::setprecision(6);

    for (int n = 1; n <= maxN; ++n) {
        long_long states = 0;
        long_long solutions = 0;
        double ms = 0.0;

        // Один эксперимент для данного N
        runExperimentForN(n, states, solutions, ms);

        // Вывод в терминал
        std::cout << n << "\t"
                  << states << "\t\t"
                  << solutions << "\t\t"
                  << ms << "\n";

        // Строка CSV
        csv << n << ','
            << states << ','
            << solutions << ','
            << std::setprecision(10) << ms << '\n';
    }

    csv.close();

    // Формируем краткий Markdown-отчёт
    std::ofstream md(mdPath);
    if (!md.is_open()) {
        std::cout << "\nНе удалось создать файл " << mdPath << "\n";
        return;
    }

    md << "# Анализ экспериментов по задаче N ферзей\n\n";
    md << "Исходные данные измерений находятся в файле "
          "`data/csv/nqueens_results.csv`.\n\n";

    md << "## Вывод по экспериментам\n\n";
    md << "- Количество рассмотренных позиций растёт очень быстро при увеличении N.\n";
    md << "- Время работы алгоритма также растёт близко к экспоненциальному закону.\n";
    md << "- Уже при сравнительно небольших N полный перебор становится заметно тяжёлым по времени.\n\n";

    md << "## Сравнение подходов\n\n";
    md << "1. В программе реализован классический рекурсивный алгоритм с возвратом "
          "(backtracking), который перебирает варианты расстановки ферзей, "
          "отбрасывая заведомо конфликтные позиции.\n";
    md << "2. Полный перебор всех возможных конфигураций доски без отсечений имел бы "
          "количество вариантов порядка 2^(N^2), что абсолютно неприемлемо уже при "
          "малых размерах.\n";
    md << "3. Алгоритм с отсечениями существенно уменьшает число рассматриваемых позиций, "
          "но в худшем случае трудоёмкость всё равно растёт экспоненциально.\n";

    md.close();

    std::cout << "\nТаблица сохранена в: " << csvPath << "\n";
    std::cout << "Текстовый отчёт сохранён в: " << mdPath << "\n";
}
