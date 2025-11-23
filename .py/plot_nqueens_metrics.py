#!/usr/bin/env python3
import os
import csv
import math
import matplotlib.pyplot as plt

CSV_PATH = "data/csv/nqueens_results.csv"
PNG_DIR = "data/png"


def read_data(path):
    Ns = []
    states = []
    solutions = []
    times = []

    with open(path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if len(rows) <= 1:
        return [], [], [], []

    data_rows = rows[1:]

    for row in data_rows:
        if len(row) < 4:
            continue
        try:
            n = int(row[0])
            s = int(row[1])
            sol = int(row[2])
            t = float(row[3])
        except ValueError:
            continue

        Ns.append(n)
        states.append(s)
        solutions.append(sol)
        times.append(t)

    return Ns, states, solutions, times


def ensure_dirs():
    os.makedirs(PNG_DIR, exist_ok=True)


def main():
    ensure_dirs()

    if not os.path.exists(CSV_PATH):
        print(f"Файл {CSV_PATH} не найден.")
        return

    Ns, states, solutions, times = read_data(CSV_PATH)
    if not Ns:
        print("Нет данных в CSV.")
        return

    # Время на одну проверку
    time_per_state = []
    for s, t in zip(states, times):
        if s > 0:
            time_per_state.append(t / s)
        else:
            time_per_state.append(0.0)

    # log10(числа решений + 1)
    log_solutions = [math.log10(sol + 1) for sol in solutions]

    fig, ax1 = plt.subplots()

    ax1.plot(Ns, time_per_state, marker="o")
    ax1.set_xlabel("N")
    ax1.set_ylabel("Время на одну позицию (мс)", color="black")
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(Ns, log_solutions, marker="s")
    ax2.set_ylabel("log10(число решений + 1)", color="black")

    plt.title("Дополнительные метрики для задачи N ферзей")
    out_path = os.path.join(PNG_DIR, "nqueens_metrics.png")
    plt.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    print("График nqueens_metrics.png создан.")


if __name__ == "__main__":
    main()
