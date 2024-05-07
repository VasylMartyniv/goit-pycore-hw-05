import sys
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    parts = line.strip().split(' ', maxsplit=3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("Файл логів не знайдено.")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count:<10}")


def main():
    if len(sys.argv) < 2:
        print("Введіть шлях до файлу логів.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        logs_of_type = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level}':")
        for log in logs_of_type:
            print(f"{log['date']} {log['time']} - {log['message']}")
        print()


if __name__ == "__main__":
    main()
