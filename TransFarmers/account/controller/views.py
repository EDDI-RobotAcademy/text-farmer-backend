from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.serializers import AccountSerializer
from account.service.account_service_impl import AccountServiceImpl


class AccountView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()

    def checkEmailDuplication(self, request):
        try:
            email = request.data.get('email')
            isDuplicate = self.accountService.checkEmailDuplication(email)

            return Response({'isDuplicate': isDuplicate, 'message': 'Email이 이미 존재' \
                             if isDuplicate else 'Email 사용 가능'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("이메일 중복 체크 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def findEmailByAccountId(self, request):
        try:
            accountId = request.data.get("accountId")
            email = self.accountService.findEmailByAccountId(accountId)

            return Response({"email": email}, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error occured in findEmail : ", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def registerAccount(self, request):
        try:
            email = request.data.get('email')

            account = self.accountService.registerAccount(
                loginType='KAKAO',
                roleType='NORMAL',
                email=email
            )

            serializer = AccountSerializer(account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("계정 생성 중 에러 발생:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
