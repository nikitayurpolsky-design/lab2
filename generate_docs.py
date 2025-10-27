#!/usr/bin/env python3
"""
Скрипт для автоматической генерации документации
Запускается GitHub Actions при каждом коммите
"""

import os
import datetime
import subprocess
import ast
import inspect
from pathlib import Path

def get_file_info(filepath):
    """Получает информацию о файле"""
    stat = os.stat(filepath)
    return {
        'size': stat.st_size,
        'lines': sum(1 for _ in open(filepath, 'r', encoding='utf-8')),
        'modified': datetime.datetime.fromtimestamp(stat.st_mtime)
    }

def analyze_python_file(filepath):
    """Анализирует Python файл и извлекает информацию о функциях и классах"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        functions = []
        classes = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    'name': node.name,
                    'lineno': node.lineno,
                    'args': [arg.arg for arg in node.args.args]
                })
            elif isinstance(node, ast.ClassDef):
                classes.append({
                    'name': node.name,
                    'lineno': node.lineno
                })
        
        return {
            'functions': functions,
            'classes': classes,
            'file_info': get_file_info(filepath)
        }
    except Exception as e:
        return {'error': str(e)}

def generate_api_docs():
    """Генерирует документацию API"""
    api_dir = Path('docs/api')
    api_dir.mkdir(exist_ok=True)
    
    python_files = list(Path('.').glob('*.py')) + list(Path('.').glob('**/*.py'))
    
    for py_file in python_files:
        if py_file.name.startswith('test_') or py_file.name == 'generate_docs.py':
            continue
            
        analysis = analyze_python_file(py_file)
        
        if 'error' not in analysis:
            # Создаем Markdown файл для каждого Python файла
            md_content = f"""# {py_file.name}

##  Информация о файле
- **Размер:** {analysis['file_info']['size']} байт
- **Строк кода:** {analysis['file_info']['lines']}
- **Последнее изменение:** {analysis['file_info']['modified'].strftime('%Y-%m-%d %H:%M:%S')}

"""
            
            if analysis['classes']:
                md_content += "## Классы\n\n"
                for cls in analysis['classes']:
                    md_content += f"- `{cls['name']}` (строка {cls['lineno']})\n"
                md_content += "\n"
            
            if analysis['functions']:
                md_content += "## ⚙️ Функции\n\n"
                for func in analysis['functions']:
                    md_content += f"- `{func['name']}({', '.join(func['args'])})` (строка {func['lineno']})\n"
            
            # Сохраняем файл документации
            with open(api_dir / f"{py_file.stem}.md", 'w', encoding='utf-8') as f:
                f.write(md_content)

def generate_build_report(commit_hash, branch, run_id, run_number):
    """Генерирует отчет о сборке"""
    reports_dir = Path('docs/reports')
    reports_dir.mkdir(exist_ok=True)
    
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    # Получаем статистику тестов
    try:
        result = subprocess.run(['python', '-m', 'pytest', 'tests/', '--tb=short'], 
                              capture_output=True, text=True)
        test_output = result.stdout
        test_success = result.returncode == 0
    except Exception as e:
        test_output = f"Ошибка запуска тестов: {e}"
        test_success = False
    
    # Считаем метрики кода
    python_files = list(Path('.').glob('**/*.py'))
    total_lines = 0
    total_files = len(python_files)
    
    for py_file in python_files:
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                total_lines += len(f.readlines())
        except:
            pass
    
    build_report = f"""# Automated Build Report

##Информация о сборке
- **Дата сборки:** {current_time}
- **Коммит:** [{commit_hash[:8]}](https://github.com/${{GITHUB_REPOSITORY}}/commit/{commit_hash})
- **Ветка:** {branch}
- **Workflow Run:** [#{run_number}](https://github.com/${{GITHUB_REPOSITORY}}/actions/runs/{run_id})

## Статус тестов
{'ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!' if test_success else 'ТЕСТЫ НЕ ПРОЙДЕНЫ!'}

###Метрики кода
- **Файлов Python:** {total_files}
- **Всего строк кода:** {total_lines}
- **Файлов тестов:** {len(list(Path('tests').glob('*.py')))}
