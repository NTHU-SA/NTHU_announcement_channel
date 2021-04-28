import json
from time import sleep

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from backend.models import News
from backend.MSG import line, tg


def gen_dep_cname():
    with open(f"{settings.BASE_DIR}/backend/crawler/url_list.json", "r") as f:
        schools = json.loads(f.read())
    return schools


class Command(BaseCommand):
    help = "Send message which is not published."

    def handle(self, *args, **options):
        """ Not complete!!! """
        news_list = News.objects.get_not_published()
        schools = gen_dep_cname()
        for news in news_list:
            # "學校 系所 公告類別" => "清大 資工 演講"
            dep = (
                schools[news.school]["abbr"]
                + " "
                + schools[news.school]["dep"][news.dep]["abbr"]
                + " "
                + news.category
            )
            tg.send_msg(dep, news.title, news.url)
            # line.send_msg(news.dep, news.title, news.url)
            # 將該筆資料改成已傳送
            news.published = True
            news.save()
            # 避免太頻繁發送被 ban
            sleep(5)
