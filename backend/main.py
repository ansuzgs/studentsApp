from fastapi import FastAPI #type: ignore
from routers import students
#from fastapi.middleware.cors import CORSMiddleware #type: ignore

origins = [
    "http://localhost:3000",
]

app = FastAPI()
app.include_router(students.router)
""" app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 """

@app.get("/")
async def root():
    return {'message': 'Hello world'}