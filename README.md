### Обновленный README для установки и запуска приложения

# Установка и запуск приложения для сжатия текста

Данное приложение на **Streamlit** позволяет пользователю вводить текст, выбирать модель и уровень сжатия, а затем получать сжатый текст. Для установки и запуска приложения выполните следующие шаги.

## Установка Python и Ollama

Перед началом убедитесь, что Python и Ollama установлены на вашем устройстве.

### Установка Python

1. **Linux**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
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
   Ознакомьтесь с официальной документацией Ollama для конкретных шагов по установке, так как поддержка может варьироваться.
   ```bash
   curl -o ollama-installer.sh https://ollama.com/download
   sudo bash ollama-installer.sh
   ```

2. **macOS**:
   С использованием Homebrew:
   ```bash
   brew install ollama
   ```

3. **Windows**:
   - Скачайте и установите Ollama с [официального сайта Ollama](https://ollama.com/download). Убедитесь, что путь к `ollama` добавлен в системные переменные среды PATH.

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

Теперь ваше приложение готово к использованию.
