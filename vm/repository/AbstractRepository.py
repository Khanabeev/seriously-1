import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, obj):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, obj_id):
        raise NotImplementedError

    @abc.abstractmethod
    def show_all(self):
        raise NotImplementedError
