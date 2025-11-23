#!/usr/bin/env python3
import os
import csv
import matplotlib.pyplot as plt

CSV_PATH = "data/csv/nqueens_results.csv"
PNG_DIR = "data/png"


def read_rows(path):
    rows = []
    with open(path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    return rows


def ensure_dirs():
    os.makedirs(PNG_DIR, exist_ok=True)


def main():
    ensure_dirs()

    if not os.path.exists(CSV_PATH):
        print(f"Файл {CSV_PATH} не найден.")
        return

    rows = read_rows(CSV_PATH)
    if len(rows) <= 1:
        print("Недостаточно данных в CSV для таблицы.")
        return

    header = rows[0]
    data = rows[1:]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis("off")

    table = ax.table(
        cellText=data,
        colLabels=header,
        cellLoc="center",
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.4)

    ax.set_title("Результаты экспериментов для задачи N ферзей", pad=20)

    out_path = os.path.join(PNG_DIR, "nqueens_table.png")
    plt.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    print("Таблица nqueens_table.png создана.")


if __name__ == "__main__":
    main()
