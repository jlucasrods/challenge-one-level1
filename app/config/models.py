from app.config.db import engine
from app.models import address, user


def create_all_models():
    address.AddressModel.metadata.create_all(engine)
    user.UserModel.metadata.create_all(engine)
