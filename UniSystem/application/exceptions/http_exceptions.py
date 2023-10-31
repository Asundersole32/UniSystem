from fastapi import HTTPException, status


def bad_request(error):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=str(error)
    )


def credentials_exception():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )


def unauthorized_access():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid user Type'
    )
