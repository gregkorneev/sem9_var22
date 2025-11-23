#!/usr/bin/env python3
import os
import csv
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

    data_rows = rows[1:]  # пропускаем заголовок

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


def plot_time(Ns, times):
    plt.figure()
    plt.plot(Ns, times, marker="o")
    plt.xlabel("N (размер доски)")
    plt.ylabel("Время, мс")
    plt.title("Время решения задачи N ферзей")
    plt.grid(True)
    out_path = os.path.join(PNG_DIR, "nqueens_time.png")
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()


def plot_states(Ns, states):
    plt.figure()
    plt.plot(Ns, states, marker="o")
    plt.xlabel("N (размер доски)")
    plt.ylabel("Рассмотрено позиций")
    plt.title("Количество рассмотренных позиций при решении задачи N ферзей")
    plt.grid(True)
    out_path = os.path.join(PNG_DIR, "nqueens_states.png")
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()


def plot_combined(Ns, states, times):
    fig, ax1 = plt.subplots()

    ax1.plot(Ns, times, marker="o")
    ax1.set_xlabel("N (размер доски)")
    ax1.set_ylabel("Время, мс")
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(Ns, states, marker="s")
    ax2.set_ylabel("Рассмотрено позиций")

    plt.title("Время и количество позиций для задачи N ферзей")
    out_path = os.path.join(PNG_DIR, "nqueens_combined.png")
    plt.savefig(out_path, bbox_inches="tight")
    plt.close(fig)


def main():
    ensure_dirs()

    if not os.path.exists(CSV_PATH):
        print(f"Файл {CSV_PATH} не найден.")
        return

    Ns, states, solutions, times = read_data(CSV_PATH)

    if not Ns:
        print("Нет данных в CSV.")
        return

    plot_time(Ns, times)
    plot_states(Ns, states)
    plot_combined(Ns, states, times)
    print("Графики nqueens_time.png, nqueens_states.png, nqueens_combined.png созданы.")


if __name__ == "__main__":
    main()
