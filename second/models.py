from django.db import models

# Create your models here.
class Save_place(models.Model):
    '''id(PK)는 인스턴스 생성과 함께 자동부여'''
    place_name = models.CharField(max_length=200)  # 식당명
    lat = models.FloatField()  # 위도
    lng = models.FloatField()  # 경도
    road_address = models.CharField(max_length=500)  # 주소(도로명)
    jibun_address = models.CharField(max_length=500)  # 주소(지번)
    phone = models.CharField(max_length=13)  # 전화번호
    category = models.CharField(max_length=3)  # 카테고리
    register = models.CharField(max_length=20)  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)  # 등록시각
