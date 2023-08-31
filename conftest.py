import pytest
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    login = data['login']
    title = data['title']

@pytest.fixture()
def x_selector1():
    return """/html/body/div/main/div/div/div/form/div[1]/label/input"""


@pytest.fixture()
def x_selector2():
    return """/html/body/div/main/div/div/div/form/div[2]/label/input"""


@pytest.fixture()
def btn_selector():
    return 'button'


@pytest.fixture()
def x_selector3():
    return """/html/body/div/main/div/div/div[2]/h2"""


@pytest.fixture()
def expected_result_1():
    return '401'


@pytest.fixture()
def x_selector4():
    return """/html/body/div[1]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def expected_result_2():
    return f'Hello, {login}'


@pytest.fixture()
def new_post_btn_selector():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def title_selector():
    return """/html/body/div/main/div/div/form/div/div/div[1]/div/label/input"""


@pytest.fixture()
def description_selector():
    return """/html/body/div/main/div/div/form/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def content_selector():
    return """/html/body/div/main/div/div/form/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def post_btn_selector():
    return """/html/body/div/main/div/div/form/div/div/div[7]/div/button/span"""


@pytest.fixture()
def expected_title():
    return f'{title}'


@pytest.fixture()
def x_selector5():
    return """/html/body/div[1]/main/div/div[1]/h1"""
