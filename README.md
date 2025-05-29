# GAIA Agent Demo
Интерактивный пример интеллектуального агента на базе
smol-agent, способный решать задачи из бенчмарка GAIA.

## Возможности
* мультишаговый агент (`smolagents.CodeAgent`) с инструментами:
  ­- веб-поиск, Python-exec, (при желании) собственные LlamaIndex-RAG-запросы;
* скрипт скачивания поднабора GAIA и оценка точности (≥ 30 % на level-1).

## Установка
```bash
git clone https://github.com/papafranchesco/agent_hf.git
cd agent_hf
pip install -r requirements.txt
```


## Использование
№ 1 Скачать валидационный сплит GAIA-L1 (download_gaia.py)                                     
№ 2 Посчитать accuracy, посмотротеть процесс рассуждений с помощью evaluate.py                                           


## Оценка

На сплите *2023\_level1 validation* (53 задач) агент показывает
≈ 32 % точности (17/53) при 6 шагах на запрос.

## Nota bene
Репозиторий **не содержит** копий вопросов/ответов GAIA.
Для оценки нужно принять условия доступа на HF и загрузить сплит
скриптом `download_gaia.py`.


