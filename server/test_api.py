import unittest
import requests


class TestApi(unittest.TestCase):
    get_url = 'http://0.0.0.0:8000/get_posts?query=давай'
    delete_url = 'http://0.0.0.0:8000/delete_post?id=100'

    def test_is_deleted(self):
        response = requests.delete(self.delete_url)
        self.assertTrue(response.status_code == 200)

    def test_deleted_id_check(self):
        response = requests.delete(self.delete_url)
        d = {
            "deleted": 100
        }

        self.assertEqual(d, response.json())

    def test_status_get_posts(self):
        response = requests.get(self.get_url)
        self.assertEqual(response.status_code, 200)

    def test_match_ids(self):
        response = requests.get(self.get_url)
        r = response.json()
        id_lst = [el.get('id') for key, value in r.items() for el in value]
        self.assertEqual(id_lst, [151, 175, 201, 215])
