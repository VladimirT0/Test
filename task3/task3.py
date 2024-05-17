import json
import sys


def fill_report(values, tests):
    for test in tests:
        # Если тест является листом, значит это конечный тест, для которого нужно заполнить значение
        if isinstance(test, dict) and 'id' in test:
            # Находим значение для данного теста по его id из values
            test_id = test['id']
            if test_id in values:
                test['value'] = values[test_id]
            else:
                test['value'] = None
        # Если тест не является листом, значит он содержит вложенные тесты, рекурсивно запускаем fill_report
        elif isinstance(test, list):
            fill_report(values, test)


def main():
    if len(sys.argv) != 4:
        print("Wrong params!")
        return
    
    values_filename = sys.argv[1]
    tests_filename = sys.argv[2]
    report_filename = sys.argv[3]
    
    with open(values_filename, 'r') as values_file:
        values = json.load(values_file)

    with open(tests_filename, 'r') as tests_file:
        tests = json.load(tests_file)

    # Заполняем отчет значениями из values
    fill_report(values, tests)

    # Записываем результат в report.json
    with open(report_filename, 'w') as report_file:
        json.dump(tests, report_file, indent=4)


if __name__ == "__main__":
    main()
    