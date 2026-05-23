from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#instance of fastapi
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"],
)

#testing if back end is connected
@app.get("/test")
def test():
    return{"message": "Backend successfully connected"}
#commit now, and now commit again
#some more comments man 