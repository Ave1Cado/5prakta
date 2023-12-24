import pandas as pd

# Загрузка датасета (предположим, что файл CSV используется)
df = pd.read_csv('C:\\Users\Кырылюк Артём\Desktop\gk\spotify_songs.csv')

# Проверка на совпадения и их удаление
dr = df.drop_duplicates()

# Вывод информации о датасете
print("Исходный размер датасета:", df.shape)
print("Размер датасета после удаления дубликатов:", dr.shape)

# Вывод наименований колонок
print("Наименования колонок:", df.columns.tolist())

# Вывод уникальных значений для каждой колонки
for column in df.columns:
    print(f"Уникальные значения для {column}:", df[column].nunique())

# Отображение информации о датасете
df.info()

# Отображение статистического описания датасета
df.describe(include='all')

# Отсортировать датасет по определенным параметрам 
sorted_df = dr.sort_values(by='track_popularity', ascending=False)

# Удаление ненужных столбцов
reduced_df = sorted_df.drop(columns=['track_album_id'])

# Замена пустых значений 
cleaned_df = reduced_df.fillna({'country': 'Unknown'})

# Выборка данных  в моём случае первых 10
sampled_data = cleaned_df.head(10)[['track_name', 'track_popularity']]

# Вывод примера выборки
print(sampled_data)

# Сохранение нового датасета
newDataset = 'C:\\Users\Кырылюк Артём\Desktop\gk\dataset.csv'
cleaned_df.to_csv(newDataset, index=False)