# __init__.py 
# 파일이 위치한 경로를 패키지 모듈처럼 사용할 수 있도록 해주는 기능을 수행
from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views