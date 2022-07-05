from utills import load_posts


class TestUtills:
    def test_posts(self):
        posts_data = load_posts()
        assert type(posts_data) == list
        assert len(posts_data) != 0
