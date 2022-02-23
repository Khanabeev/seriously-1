import abc

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, repository):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, repository):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self, repository):
        raise NotImplementedError
