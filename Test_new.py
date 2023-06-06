import pytest
from selene.support.shared import browser
from selene import be, have
@pytest.fixture()
def before_each():
    print("called before each test")
def test_first(before_each):
    assert 1 == 1

def test_two(before_each):
    assert 1 == 1 ,'ошибОчка'

def test_three(before_each):
    pass
browser.open('https://google.com')
browser.element('[type="search"]').should(be.blank).type('https://www.dota2.com').press_enter()
browser.element('[id="search"]').should(have.text('dota2.com'))

def test_big_test():
    assert 5==5




