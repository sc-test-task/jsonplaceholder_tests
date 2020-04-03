import allure
import requests as r
from config import JSONPLACEHOLDER_HOST


class Client:

    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    @allure.step
    def get_posts(self, post_id: int = None):
        return self._get(path=f"/posts/{post_id if post_id else ''}")
