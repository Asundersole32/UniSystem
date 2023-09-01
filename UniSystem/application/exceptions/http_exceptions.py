from fastapi import HTTPException, status


def bad_request():
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
