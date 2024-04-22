import typing as t

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm


OAuth2PasswordRequestFormDependency = t.Annotated[OAuth2PasswordRequestForm, Depends()]
