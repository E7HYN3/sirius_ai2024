import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard
import ollama


# Функция для выполнения запроса к модели Ollama
def summarize_with_ollama(text, model_name, compression_level):
    """
    Выполняет запрос к Ollama для сжатия текста.

    Args:
        text (str): Текст для сжатия.
        model_name (str): Название модели Ollama.
        compression_level (str): Уровень сжатия ("Сильное" или "Слабое").

    Returns:
        str: Сжатый текст.
    """
    prompt_template = "Сократи текст строго до {}:\n{}"
    if compression_level == "Сильное":
        prompt = prompt_template.format("одного или двух коротких предложений", text)
    else:
        prompt = prompt_template.format("одного краткого абзаца", text)
    response = ollama.generate(model=model_name, prompt=prompt)
    return response["response"]


# Интерфейс Streamlit
st.title("Приложение для сжатия и суммаризации текста")

# Поле ввода текста
input_text = st.text_area("Введите текст")

# Список моделей для выбора
available_models = [model["name"] for model in ollama.list()["models"]]
selected_model = st.selectbox("Выберите модель для сжатия", available_models)

# Выбор уровня сжатия
compression_type = st.radio("Выберите уровень сжатия", ("Сильное", "Слабое"))

# Кнопка запуска
if st.button("Сжать текст"):
    result = summarize_with_ollama(input_text, selected_model, compression_type)
    # Вывод результата
    st.title("Результат")
    st.write(result)
    st_copy_to_clipboard(
        result, before_copy_label="Копировать", after_copy_label="Скопировано!"
    )

# CSS для динамического изменения высоты поля ввода текста
st.html("""
    <style>
    .stTextArea textarea {
        resize: vertical;
        min-height: 100px;
    }
    </style>
""")
