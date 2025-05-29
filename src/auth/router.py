from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.schemas import UserSchema
from src.auth.service import registration_user
from src.database import get_session

router = APIRouter(prefix="/auth", tags=["Auth 🔐"])


@router.post("/register")
async def register_user(
    user_schema: UserSchema, db: AsyncSession = Depends(get_session)
):
    return await registration_user(db, user_schema)
