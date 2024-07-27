class Config:
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:Vikasdatabase@localhost:5432/User_management_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:Vikasdatabase@localhost:5432/test_db"
    )
