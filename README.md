# Приложение для сжатия текста 
[![GitHub](https://img.shields.io/badge/github-100000?style=flat&logo=GitHub&logoColor=white&labelColor=black&color=black)](https://github.com/E7HYN3/sirius_ai2024) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1j-FdgRfbcW3zYJEJRwUT_oVaL-eiLuNm?usp=sharing) <br>
Данное приложение на **Streamlit** и **Ollama** позволяет пользователю вводить текст, выбирать модель и уровень сжатия, а затем получать сжатый текст. 
> Реализовано в рамках дополнительного задания проектной задачи "Приложение для чтения книг с AI-ассистентом" [программы Сириус ИИ](https://sochisirius.ru/obuchenie/distant/smena1894/8753)
___
# Запуск в Google Colab


https://github.com/user-attachments/assets/27bc1f50-ae45-4115-a6bc-c940899cb89c


| Colab | 
| --- |
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1j-FdgRfbcW3zYJEJRwUT_oVaL-eiLuNm?usp=sharing) |

# Локальная установка и запуск


https://github.com/user-attachments/assets/d4513c4c-e7cc-4a0f-bafb-c2a8472f9d98


## Установка Python и Ollama

Перед началом убедитесь, что Python и Ollama установлены на вашем устройстве.

### Установка Python

1. **Linux (Ubuntu/Debian)**:
   ```bash
   sudo apt install -y python3 python3-venv python3-pip
   ```
   **Linux (Febora)**:
   ```bash
   sudo dnf install python3 python3-virtualenv python3-pip
   ```
   **Linux (Arch)**:
   ```bash
   sudo pacman -S python3 python-virtualenv python-pip
   ```


2. **macOS**:
   Убедитесь, что установлен Homebrew:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   Затем установите Python:
   ```bash
   brew install python
   ```

3. **Windows**:
   - Скачайте установочный файл Python с [официального сайта Python](https://www.python.org/downloads/) и установите его, отметив опцию "Add Python to PATH".

### Установка Ollama

1. **Linux**:
   Ознакомьтесь с официальной [документацией Ollama](https://github.com/ollama/ollama/blob/main/docs/linux.md) для конкретных шагов по установке вручную, так как поддержка разных дистрибутивов может отличаться.
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **macOS**:
   С использованием Homebrew:
   ```bash
   brew install ollama
   ```

3. **Windows**:
   - Скачайте и установите Ollama с [официального сайта Ollama](https://ollama.com/download). Убедитесь, что путь к `ollama` добавлен в системные переменные среды PATH.

### Загрузка моделей

   - Для загрузки языковых моделей используйте `ollama pull название_модели`, полный список языковых моделей можно найти на [сайте Ollama](https://ollama.com/library). 
   - Мы рекомендуем использовать модель [gemma2:9b](https://ollama.com/library/gemma2:9b). Для её загрузки воспользуйтесь следующей командой:
   ```bash
   ollama pull gemma2:9b
   ```

## Установка приложения

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/E7HYN3/sirius_ai2024.git
   ```

2. **Перейдите в каталог проекта:**
   ```bash
   cd sirius_ai2024
   ```

3. **Создайте виртуальное окружение:**
   ```bash
   python -m venv venv
   ```

4. **Активируйте виртуальное окружение:**
   - Для Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - Для Windows:
     ```bash
     venv\Scripts\activate.bat
     ```

5. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

## Запуск приложения

1. **Запустите приложение Streamlit:**
   ```bash
   streamlit run app.py
   ```

## Примечания
- Убедитесь, что у вас установлен Python версии 3.7 или выше.
- Проверьте, что Ollama успешно установлен и настроен для работы с локальными моделями.
- Убедитесь, что все зависимости, указанные в `requirements.txt`, успешно установлены.

Теперь приложение готово к использованию.
