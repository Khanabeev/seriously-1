import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, repository):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, repository):
        raise NotImplementedError

    @abc.abstractmethod
    def show_all(self):
        raise NotImplementedError
