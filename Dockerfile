FROM python:3.10

# Создаем директорию в которой будут храниться файлы, пакеты и модули
RUN mkdir /bewise

# Объявляем ее рабочей
WORKDIR /bewise

# Копируем в рабочую директорию файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем все файлы в рабочую директорию
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


# TODO докер работает, настраиваю компос и все чики бомбони