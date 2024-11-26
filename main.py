import json
import subprocess

def load_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Проверка обязательных параметров
    required_keys = ["visualizer_path", "repository_path", "output_path", "date_limit"]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing '{key}' in config file.")
    return config

def get_commits(repo_path, date_limit):
    command = [
        "git", "-C", repo_path, "log", "--before", date_limit, "--pretty=format:%H %P",  "--reverse"
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        commits = result.stdout.strip().split('\n')
        dependencies = {}
        for line in commits:
            parts = line.split()
            commit = parts[0]
            parents = parts[1:]
            dependencies[commit] = parents
        return dependencies
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды git: {e}")
        return {}

def generate_graphviz_code(dependencies):
    dot_code = "digraph G {\n"
    for commit, parents in dependencies.items():
        for parent in parents:
            dot_code += f'    "{parent}" -> "{commit}";\n'
    dot_code += "}"
    return dot_code

def write_output(output_path, dot_code):
    with open(output_path, 'w') as f:
        f.write(dot_code)

def print_commits_and_dates(repo_path, date_limit):
    # Убедитесь, что git доступен
    git_command = "git"  # Это должно работать, если git доступен в PATH
    command = [
        git_command, 
        "-C", repo_path, 
        "log", 
        "--before=" + date_limit,  # Коммиты до заданной даты
        "--format=%h %cd",  # Формат вывода: хеш коммита и дата
         "--reverse"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        commits_info = result.stdout.splitlines()  # Разделяем вывод по строкам
        for commit in commits_info:
            print(f"Коммит: {commit}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды: {e}")

def main(config_path):
    try:
        config = load_config(config_path)
        repo_path = config["repository_path"]
        date_limit = config["date_limit"]
        output_path = config["output_path"]

        print("Загружаем и обрабатываем коммиты...")
        dependencies = get_commits(repo_path, date_limit)
        if not dependencies:
            print("Не удалось получить коммиты.")
            return
        
        dot_code = generate_graphviz_code(dependencies)
        write_output(output_path, dot_code)
        print("Граф зависимостей записан в файл:", output_path)
        
        # Вывод информации о коммитах и датах
        print_commits_and_dates(repo_path, date_limit)
    except ValueError as e:
        print(f"Ошибка конфигурации: {e}")
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    config_path = "config.json"  # Укажите путь к вашему конфигурационному файлу
    main(config_path)
