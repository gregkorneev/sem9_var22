#!/usr/bin/env python3
import os
import csv
import matplotlib.pyplot as plt

CSV_PATH = "data/csv/nqueens_results.csv"
PNG_DIR = "data/png"


def read_data(path):
    Ns = []
    states = []
    times = []

    with open(path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if len(rows) <= 1:
        return [], [], []

    data_rows = rows[1:]

    for row in data_rows:
        if len(row) < 4:
            continue
        try:
            n = int(row[0])
            s = int(row[1])
            t = float(row[3])
        except ValueError:
            continue

        Ns.append(n)
        states.append(s)
        times.append(t)

    return Ns, states, times


def ensure_dirs():
    os.makedirs(PNG_DIR, exist_ok=True)


def main():
    ensure_dirs()

    if not os.path.exists(CSV_PATH):
        print(f"Файл {CSV_PATH} не найден.")
        return

    Ns, states, times = read_data(CSV_PATH)
    if len(Ns) < 2:
        print("Недостаточно точек для анализа роста.")
        return

    growth_states = []
    growth_times = []
    growth_Ns = []

    for i in range(1, len(Ns)):
        if states[i - 1] > 0 and times[i - 1] > 0:
            growth_Ns.append(Ns[i])
            growth_states.append(states[i] / states[i - 1])
            growth_times.append(times[i] / times[i - 1])

    if not growth_Ns:
        print("Не удалось вычислить коэффициенты роста.")
        return

    fig, ax1 = plt.subplots()

    ax1.plot(growth_Ns, growth_states, marker="o")
    ax1.set_xlabel("N")
    ax1.set_ylabel("Рост числа позиций (ratio)")
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(growth_Ns, growth_times, marker="s")
    ax2.set_ylabel("Рост времени (ratio)")

    plt.title("Коэффициенты роста для задачи N ферзей")
    out_path = os.path.join(PNG_DIR, "nqueens_growth.png")
    plt.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    print("График nqueens_growth.png создан.")


if __name__ == "__main__":
    main()
