import fastapi
import uvicorn
from views import home
from api import weather_api

# uvicorn  main:api --reload
# http://localhost:8000/
# 127.0.0.1:8000


api = fastapi.FastAPI()


def configure():
    api.include_router(home.router)
    api.include_router(weather_api.router)


# The following parts  are for development Not for Production
# uvicorn.run()
# uvicorn.run(api)

configure()
if __name__ == "__main__":
    uvicorn.run(api)
