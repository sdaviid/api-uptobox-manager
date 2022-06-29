import os
from typing import List
from sqlalchemy.orm import Session
from fastapi import(
    Depends,
    Response,
    status,
    APIRouter,
    File,
    UploadFile
)
from fastapi.responses import JSONResponse

from app.models.domain.account import(
    Account
)

from app.models.schemas.account import(
    AccountAdd,
    AccountDetail
)

from app.core.uptobox import uptobox



from app.core.database import get_db

from app.api.deps import(
    get_current_active_user
)



router = APIRouter()




@router.post(
    '/register',
    status_code=status.HTTP_200_OK
)
def register(
    data: AccountAdd,
    response: Response,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_active_user)
):
    temp = uptobox(data.api_key)
    if temp.status() != True:
        return {
            "error": True,
            "message": "Couldnt make login"
        }
    else:
        return Account.add(session=db, data=data)
