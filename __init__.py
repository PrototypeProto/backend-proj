from typing import Optional, Union, Annotated
'''
    Optional[type(s)]
    Union() or (type | None)
    Annotated[type, "annotation textr"]
'''
from fastapi import FastAPI, Header
from .code.user_routes import router

api_version = "v1"

app = FastAPI(version=api_version)

app.include_router(router=router, prefix=f"/{api_version}/user")