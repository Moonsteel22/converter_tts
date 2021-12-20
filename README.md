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
Then send post request to endpoint __/convert__, with attached txt file
Here some query params:
--- language: ru, en

Example:
Russian text translated into Russian and voiced

Text:

![image](https://user-images.githubusercontent.com/60964414/146820657-78d4025e-47e6-4775-abb8-159d20bffcc0.png)

Request:

![image](https://user-images.githubusercontent.com/60964414/146820789-a9387ab5-047b-4d0b-b482-7e07fed8edee.png)
Result:

You will get tar file with splitted by chapters audio files


![image](https://user-images.githubusercontent.com/60964414/146820615-062eabe4-9f9d-4e95-8bb2-90ae47d3cfc2.png)

  
