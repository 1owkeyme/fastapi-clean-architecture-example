from enum import StrEnum, unique


@unique
class TableName(StrEnum):
    USERS = "users"
    REVIEWS = "reviews"
    MOVIES = "movies"
