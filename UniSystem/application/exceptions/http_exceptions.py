from fastapi import HTTPException, status


def bad_request(Error):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail= Error
    )

def credentials_exeption():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )
