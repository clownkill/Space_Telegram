# Space_Telegram
Скрипт для скачивания фото космоса NASA и пусков ракет SpaceX и публикации их в Telegram канале.
Фото скачиваются в каталог images. Фото публикуются с задержкой (устанавливается в переменной окружения `SLEEP_TIME`,
по умолчанию 1 сутки). 

### Как установить
Python3 должен быть уже установлен. Затем используйте 'pip' (или 'pip3', если есть конфликт с Python2) для установки
зависимостей.

```
pip install -r requirements.txt
```

### Объявление переменных окружения
Перед запуском скрипта в одном каталоге с файлом `main.py` необходимо создать файл для хранения переменных окружения
с именем `.env` со следующим содержимым:
```
NASA_API = [TOKEN]
TELEGRAM_API = [TOKEN]
SLEEP_TIME = '18600'
```
В переменной `NASA_API` хранится API-токен, полученный от [nasa.gov](https://api.nasa.gov/).

В переменной `TELEGRAM_API` хранится API-токен Telegram-бота.

В переменной `SLEEP_TIME` хранится время задержки публикации фото в секундах.

### Инструкция
Для запуска скрипта используйте `python main.py`

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
 
