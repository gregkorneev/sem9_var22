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
    if not Ns:
        print("Нет данных в CSV.")
        return

    eps = 1e-9
    log_states = [math.log10(s + eps) for s in states]
    log_times = [math.log10(t + eps) for t in times]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 8), sharex=True)

    ax1.plot(Ns, log_times, marker="o")
    ax1.set_ylabel("log10(время, мс)")
    ax1.set_title("Логарифм времени решения задачи N ферзей")
    ax1.grid(True)

    ax2.plot(Ns, log_states, marker="s")
    ax2.set_xlabel("N (размер доски)")
    ax2.set_ylabel("log10(кол-во позиций)")
    ax2.set_title("Логарифм количества рассмотренных позиций")
    ax2.grid(True)

    fig.suptitle("Дашборд по задаче N ферзей", fontsize=12)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])

    out_path = os.path.join(PNG_DIR, "nqueens_dashboard.png")
    plt.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    print("График nqueens_dashboard.png создан.")


if __name__ == "__main__":
    main()
