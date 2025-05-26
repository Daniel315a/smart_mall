from fastapi import FastAPI
from app.routers import user_role, user, region, city, zone, store, coupon_type, mall, client, coupon, validation, gender

app = FastAPI()

app.include_router(user_role.router)
app.include_router(user.router)
app.include_router(region.router)
app.include_router(city.router)
app.include_router(zone.router)
app.include_router(coupon_type.router)
app.include_router(mall.router)
app.include_router(store.router)
app.include_router(client.router)
app.include_router(coupon.router)
app.include_router(validation.router)
app.include_router(gender.router)
