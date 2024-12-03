# GitGraphViz

**GitGraphViz** — инструмент командной строки для анализа зависимостей между коммитами в Git-репозитории. Он позволяет строить граф зависимостей в формате Graphviz (`dot`) на основе указанных условий.

## Описание

Этот инструмент:
- Загружает конфигурацию из JSON-файла.
- Извлекает зависимости между коммитами в указанном Git-репозитории до заданной даты.
- Генерирует граф в формате Graphviz.
- Сохраняет сгенерированный граф в выходной файл.
- Печатает хронологически упорядоченную информацию о коммитах.

### Возможности:
- Гибкая настройка через конфигурационный файл.
- Использование стандартных инструментов Git для извлечения информации.
- Генерация графа для визуализации с помощью совместимых инструментов (например, Graphviz).

---

## Описание функций и настроек

**1. `load_config(config_path)`:**

* **`config_path` (str):** Путь к JSON-файлу с конфигурационными данными.

Загружает файл конфигурации и проверяет наличие всех обязательных параметров.

**2. `get_commits(repo_path, date_limit)`:**

Извлекает коммиты и их родителей из Git-репозитория до указанной даты.

**3. `generate_graphviz_code(dependencies)`:**

Генерирует код Graphviz для представления графа зависимостей между коммитами.

**4. `write_output(output_path, dot_code)`:**

Сохраняет сгенерированный код Graphviz в файл.

**5. `main(config_path)`:**

Основная функция, объединяющая все этапы работы программы.

## Результаты прогона тестов

Тесты для эмулятора написаны с использованием pytest. 

Результаты успешного прогона тестов:

![Результат прогона тестов](https://github.com/skufirovan/GitGraphViz/blob/main/img/pytest.png?raw=true)

Пример выходного файла:

![Скриншот работы](https://github.com/skufirovan/GitGraphViz/blob/main/img/output.png?raw=true)



