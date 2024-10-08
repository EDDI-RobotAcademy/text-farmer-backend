from abc import ABC, abstractmethod


class AccountService(ABC):
    @abstractmethod
    def checkEmailDuplication(self, email):
        pass

    @abstractmethod
    def registerAccount(self, loginType, roleType, email):
        pass

    @abstractmethod
    def findAccountByEmail(self, email):
        pass

    @abstractmethod
    def findEmailByAccountId(self, accountId):
        pass
