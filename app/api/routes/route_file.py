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
from app.models.domain.file import(
    File
)
from app.models.schemas.file import(
    FileAddUpload,
    FileAdd,
    FileDetail
)

from app.core.uptobox import uptobox



from app.core.database import get_db



router = APIRouter()




@router.post(
    '/upload',
    status_code=status.HTTP_200_OK
)
def upload(data: FileAddUpload, response: Response, db: Session = Depends(get_db)):
    temp_account = Account.find_upload_api(session=db)
    if temp_account:
        temp_uptobox = uptobox(temp_account.api_key)
        url_uptobox = temp_uptobox.upload_remote(data.origin)
        if url_uptobox:
            temp_fileadd = FileAdd
            temp_fileadd.origin = data.origin
            temp_fileadd.url = url_uptobox
            return File.add(session=db, data=temp_fileadd)
        else:
            return {
                "error": True,
                "message": "Failed upload uptobox"
            }
    else:
        return {
            "error": True,
            "message": "Couldnt get api key"
        }


@router.get(
    '/detail/{md5_key}',
    status_code=status.HTTP_200_OK
)
def detail(md5_key: str, response: Response, db: Session = Depends(get_db)):
    temp_response = File.find_by_md5(session=db, md5_key=md5_key)
    if temp_response:
        return temp_response
    else:
        return {
            "error": True,
            "message": "No results"
        }



@router.get(
    '/download/{md5_key}',
    status_code=status.HTTP_200_OK
)
def download(md5_key: str, response: Response, db: Session = Depends(get_db)):
    temp_response = File.find_by_md5(session=db, md5_key=md5_key)
    if temp_response:
        temp_account = Account.find_premium_api(session=db)
        if temp_account:
            temp_uptobox = uptobox(temp_account.api_key)
            url_code = temp_response.url[temp_response.url.rindex('/')+1:]
            temp_direct_link = temp_uptobox.generate_download_link(url_code)
            if temp_direct_link:
                return {
                    "download": temp_direct_link
                }
            else:
                return {
                    "error": True,
                    "message": "Couldnt generate download link"
                }
        else:
            return {
                "error": True,
                "message": "No account avalaible"
            }
    else:
        return {
            "error": True,
            "message": "Failed find file"
        }
        