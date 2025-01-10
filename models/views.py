from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel, ChechingModel, Came, Gone
from .serializers import UserModelSerializer, ChechingModelSerializer, ChechingModelCreateSerializer
from .bot import send_message_to_telegram
from datetime import datetime

# UserModel uchun APIView
class UserModelListCreateView(APIView):
    def get(self, request):
        users = UserModel.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserModelDetailView(APIView):
#     def get_object(self, user_id):
#         try:
#             return UserModel.objects.get(user_id=user_id)
#         except UserModel.DoesNotExist:
#             return None

#     def check_user_status(self, user):
#         if user.status != Active:  
#             return False
#         return True

#     def get(self, request, user_id):
#         user = self.get_object(user_id)
#         if user is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         if not self.check_user_status(user):
#             return Response({"error": "User status is not Active."}, status=status.HTTP_403_FORBIDDEN)

#         serializer = UserModelSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, user_id):
#         user = self.get_object(user_id)
#         if user is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         if not self.check_user_status(user):
#             return Response({"error": "User status is not Active."}, status=status.HTTP_403_FORBIDDEN)

#         serializer = UserModelSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, user_id):
#         user = self.get_object(user_id)
#         if user is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         if not self.check_user_status(user):
#             return Response({"error": "User status is not Active."}, status=status.HTTP_403_FORBIDDEN)

#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class ComeChechingModelListCreateView(APIView):
    # def get(self, request):
    #     checkings = ChechingModel.objects.all()
    #     serializer = ChechingModelSerializer(checkings, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = ChechingModelCreateSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data['checking_status'] = Came
            current_time = datetime.now()  
            formatted_time = current_time.strftime('%d-%m %H:%M')
            validated_data['time'] = formatted_time  
            
            serializer.save(checking_status=validated_data['checking_status'])
            send_message_to_telegram(validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GoneChechingModelListCreateView(APIView):
    def post(self, request):
        serializer = ChechingModelCreateSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data['checking_status'] = Gone
            current_time = datetime.now()  
            formatted_time = current_time.strftime('%d-%m %H:%M')
            validated_data['time'] = formatted_time  
            
            serializer.save(checking_status=validated_data['checking_status'])
            send_message_to_telegram(validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
