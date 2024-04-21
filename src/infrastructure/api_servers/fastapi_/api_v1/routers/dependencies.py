import typing as t

from fastapi import Depends

from domain import usecases


auth_usecases_builder: usecases.auth.AuthUsecasesBuilder | None = None


def __get_auth_usecases_builder() -> usecases.auth.AuthUsecasesBuilder:
    if auth_usecases_builder is None:
        raise RuntimeError  # TODO: raise HTTPException or smth
    return auth_usecases_builder


def __get_sign_up_usecase() -> usecases.auth.SignUpUsecase:
    return __get_auth_usecases_builder().create_sign_up_usecase()


SignUpDependency = t.Annotated[
    usecases.auth.SignUpUsecase, Depends(__get_sign_up_usecase)
]
