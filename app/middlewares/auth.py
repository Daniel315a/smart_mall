import os
from fastapi import Request
from jose import jwt, JWTError
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from app.database import SessionLocal
from app.models.user import User

JWT_SECRET = os.getenv("SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path == "/users/sync":
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse({"detail": "Token de autenticación requerido"}, status_code=401)

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            auth0_id = payload.get("sub")
        except JWTError:
            return JSONResponse({"detail": "Token inválido"}, status_code=401)

        if not auth0_id:
            return JSONResponse({"detail": "Token sin sub"}, status_code=401)

        db = SessionLocal()
        user = db.query(User).filter(User.auth0_id == auth0_id).first()
        db.close()

        if not user:
            return JSONResponse({"detail": "Usuario no encontrado"}, status_code=401)

        request.state.user = user
        return await call_next(request)
