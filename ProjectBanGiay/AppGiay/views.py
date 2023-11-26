from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Chitietdonhang,ChitiethoadonNhapHang,HoadonNhapHang,Donhang
from .models import Danhmucgiay,Chitietgiay,Khachhang,TaikhoanKhachhang,Reviewsanpham
from .models import UserHethong,Role
from .serializers import ChitietDHSerializer,ChitietHDNHSerializer,HDNhapHangSerializer,DonHangSerializer
from .serializers import DanhMucGiaySerializer,ChitietGiaySerializer,KhachhangSerializer,TaiKhoanKGSerializer,ReviewSPSerializer
from .serializers import UserHeThongSerializer,RoleSerializer
from django.contrib.auth import get_user_model
import traceback
import random, string
import datetime

# Create your views here.
def home(request) :
    return HttpResponse("Hello there")

def id_generator (size = 5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#Class quan li he thong
def insert_user(requested_data, email, password, fullName):
    usename = email
    password = password
    tennhanvien = fullName
    gioitinh = requested_data['sex']
    ngaysinh = requested_data['ngaysinh']
    idrole = requested_data['role']
    createday = requested_data['date']
    
    user = UserHethong(usename = usename, password = password, tennhanvien = tennhanvien, gioitinh = gioitinh, ngaysinh=ngaysinh, idrole= idrole, createday = createday)
    user.save()

    return user

class CreateAccout(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        try:
            data = request.data
            
            usename = data['email']
            usename = usename.lower()
            password = data['password']
            tennhanvien = data['fullName']
            gioitinh = data['gioitinh']
            ngaysinh = data['ngaysinh']
            idrole = data['role']
            createday = datetime.date.today()

            re_password = data['re_password']
            
            # TODO: the logic in the signup
            is_teacher = data['is_teacher']
            
            if password ==  re_password:
                if len(password) >= 8:
                    if not UserHethong.objects.filter(email=usename).exists():
                        return Response(
                            {"success": "User successfully created"},
                            status= status.HTTP_201_CREATED
                        )
                    else:
                        return Response(
                        {'error': 'Email already exist'},
                        status= status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                    {'error': 'Password must have more than 8 character'},
                    status= status.HTTP_400_BAD_REQUEST
                    )
                    
            else:
                return Response(
                    {'error': 'Password do not match'},
                    status= status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            traceback.print_exc()
            return Response(
                {'error': 'Something went wrong!'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def insert_danhmucgiay(requested_data, fullName, cost):
    tendanhmuc = fullName
    loaigiay = requested_data['loaigiay']
    hangsanxuat = requested_data['hangsanxuat']
    giatien = cost
    doituong = requested_data['doituong']
    
    danhmucgiay = Danhmucgiay(tendanhmuc = tendanhmuc, loaigiay = loaigiay, hangsanxuat = hangsanxuat, giatien = giatien, doituong = doituong)
    danhmucgiay.save()
    
    return danhmucgiay

def Danhmucgiay_list (request):
    giay = Danhmucgiay.objects.all()
    serialized = DanhMucGiaySerializer(giay, many=True)
    return JsonResponse(serialized.data, safe= False)

def ChitietgiayView(request, pk):
    try :
        view = Chitietgiay.objects.filter(iddanhmuc = pk).values()
    except view.doesnotExits :
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized = ChitietGiaySerializer(view, many= False)
    return JsonResponse(serialized.data, safe=False)