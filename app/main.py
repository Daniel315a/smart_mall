from fastapi import FastAPI
from app.routers import user_role, user, region, city, client, coupon, validation,gender

app = FastAPI()

app.include_router(user_role.router)
app.include_router(user.router)
app.include_router(region.router)
app.include_router(city.router)
app.include_router(client.router)
app.include_router(coupon.router)
app.include_router(validation.router)
app.include_router(gender.router)
