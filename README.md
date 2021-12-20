# converter_tts

Clone this repo, move into src
Install pdm with pip 
```
pip install pdm
```
Then, install packages in src

```
pdm install
```

Get API json with keys from google, and set your env variable GOOGLE_APPLICATION_CREDENTIALS=<path_to_api_keys.json>

https://cloud.google.com/text-to-speech

Run app
```
pdm run uvicorn app.main:app --port 8000 --reload
```

Or move to app and execute
```
pdm run uvicorn main:app --port 8000 --reload
```

Application accept txt files with following format:
```
Chapter 1
TextTextText

Chapter 2
TextText
```
Or on Russian
```
Глава 1
ТекстТекстТекст
ТекстТекст

Глава 2
Еще какой-нибудь текст
```
Then send post request to endpoint /converter, with attached txt file
Here some request params:
Text will be translated and voiced to specified language. By default language="ru"
  
