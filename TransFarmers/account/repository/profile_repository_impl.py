from account.entity.profile import Profile
from account.entity.account import Account
from account.repository.profile_repository import ProfileRepository


class ProfileRepositoryImpl(ProfileRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def findByEmail(self, email):
        try:
            profile = Profile.objects.get(email=email)
            return profile
        except Profile.DoesNotExist:
            print(f"email로 profile 찾을 수 없음: {email}")
            return None
        except Exception as e:
            print(f"이메일 중복 검사 중 에러 발생: {e}")
            return None

    def findEmail(self, accountId):
        try:
            account = Account.objects.get(id=accountId)
            profile = Profile.objects.get(account=account)
            email = profile.email

            return email
        except Exception as e:
            print("Error occured in findEmail : ", e)
            return None

    def create(self, email, account):
        profile = Profile.objects.create(email=email, account=account)
        return profile


