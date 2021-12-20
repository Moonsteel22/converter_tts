# converter_tts

Clone this repo
Move to src
Install pdm with pip 
```
pip install pdm
```
Then, install packages in src

```
pdm install
```

Get API json with keys from google, and set your env variable GOOGLE_APPLICATION_CREDENTIALS=<path_to_api_keys.json>

Run app

pdm run uvicorn main:app --port 8000 --reload
