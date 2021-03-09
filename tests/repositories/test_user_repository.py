import unittest

from app.repositories import user_repository
from app.schemas.address_schema import Address
from app.schemas.user_schema import UserRequest


class UserRepositoryTest(unittest.TestCase):

    def setUp(self) -> None:
        self.user = UserRequest(
            email='email@email.com',
            name='name',
            cpf='05270520001',
            pis='54233492215',
            password='1234asdf',
            addresses=Address(
                country='BRASIL',
                state='SP',
                city='Piquete',
                street='Alguma',
                zip_code='12345-00',
                number=1,
                complement='casa'
            )
        )

    def test_create_user(self):
        """when receive an UserRequest returns an UserModel"""
        user = user_repository.create(user=self.user)
        self.assertNotEqual(user.id, None)
        self.assertEqual(user.email, 'email@email.com')
        self.assertNotEqual(user.addresses.id, None)
        self.user_model = user
        user_repository.db.delete(self.user_model)
        user_repository.db.commit()



