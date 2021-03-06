from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
from .youtube import youtube_parser
from .weather import weather_parser
from .cafeteria import cafeteria_parser
from article.models import Article
from board.models import Board
# Create your views here.

ARTICLE_NUM = 3


def main(request):
    datetime_now = datetime.now(tz=timezone.utc)
    datetime_past = datetime_now + timedelta(days=-7)
    
    # 메인 게시판

    board_cnt = 3
    boards = Board.objects.all().exclude(board_id = 'notice').order_by('-priority')[:board_cnt]
    for i in range(len(boards)):
        board_type = boards[i]
        boards[i].articles = Article.objects.filter(board_type=board_type, created_at__range=[datetime_past, datetime_now]).distinct().order_by('like_user_set')[:ARTICLE_NUM]

    article_popups = Article.objects.filter(is_popup = True)

    # 날씨 크롤링, 날씨객체 반환
    # weather = weather_parser()
    # 급식 크롤링, 3개의 급식객체가 들어있는 리스트 반환
    cafeteria_list = cafeteria_parser()
    # 유튜브 크롤링, 3개의 유튜브객체가 들어있는 리스트 반환
    youtube_list = youtube_parser()

    # 메뉴
    category = Board.objects.all().order_by('-priority')

    # 공지사항
    try:
        notice_cnt = 3
        board_notice_type = Board.objects.get(board_id='notice')
        notice = Article.objects.filter(board_type=board_notice_type).order_by('-created_at')[:notice_cnt]
    except:
        notice = None


    return render(request, 'main.html', {'notice': notice,'category': category,'boards': boards, 'cafeteria_list': cafeteria_list, 'youtube_list': youtube_list, 'article_popups' : article_popups})