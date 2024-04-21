from domain import entities, usecases


class SQLAlchemy(usecases.interfaces.repositories.UserRepository):
    async def create_user(
        self,
        credentials: entities.user.Credentials,
    ) -> None:
        print(f"Created user new user: {credentials}")
