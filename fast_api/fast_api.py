from fastapi import FastAPI
app=FastAPI()

@app.get('/ping')
def check_ping(message:str):
    if message.lower()=="ping":
        return {"reponse":"pong"}
    else:
        return {"reponse":"Invalid inputs"}
