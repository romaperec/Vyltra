from email_validator import EmailNotValidError, validate_email
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import UserModel
from src.auth.schemas import UserSchema
from src.auth.utils import hash_password, verify_password


async def registration_user(db: AsyncSession, user: UserSchema):
    try:
        email_info = validate_email(user.email, allow_empty_local=False)

        normalized_email = email_info.normalized

        user_in_db = await db.execute(
            select(UserModel).where(UserModel.email == normalized_email)
        )
        user_in_db = user_in_db.scalar_one_or_none()

        if user_in_db:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password = hash_password(user.password)
        new_user = UserModel(email=normalized_email, password=hashed_password)

        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        return {"message": "OK"}

    except EmailNotValidError:
        raise HTTPException(status_code=400, detail="Invalid email")


async def login_in_account(db: AsyncSession, user: UserSchema):
    user_in_db = await db.execute(
        select(UserModel).where(UserModel.email == user.email)
    )
    user_in_db = user_in_db.scalar_one_or_none()

    if not user_in_db:
        raise HTTPException(status_code=400, detail="Email not found")

    if verify_password(user.password, user_in_db.password):
        return {"message": "OK"}

    raise HTTPException(status_code=400, detail="Invalid password")
