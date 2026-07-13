from repositories.temple_repository_impl import TempleRepositoryImpl
from schemas.temple_schema import TempleResponse


class TempleServiceImpl:

    def __init__(self, repository: TempleRepositoryImpl):

        self.repository = repository

    def get_all_temples(self):

        temples = self.repository.get_all_temples()

        return [
            TempleResponse.model_validate(t)
            for t in temples
        ]
    
# NOTE : Business logic goes here.