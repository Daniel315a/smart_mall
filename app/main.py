from fastapi import FastAPI
from app.routers import user_role, user, region, city

app = FastAPI()

app.include_router(user_role.router)
app.include_router(user.router)
app.include_router(region.router)
app.include_router(city.router)
