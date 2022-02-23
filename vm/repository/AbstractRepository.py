import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def show_all(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, obj):
        raise NotImplementedError
