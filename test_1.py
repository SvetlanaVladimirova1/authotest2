import yaml
import time
from module import Site

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata['address'])


def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, expected_result_1):
    input1 = site.find_element('xpath', x_selector1)
    input1.send_keys('test')
    input2 = site.find_element('xpath', x_selector2)
    input2.send_keys('test')
    btn = site.find_element('css', btn_selector)
    btn.click()
    err_label = site.find_element('xpath', x_selector3)
    result = err_label.text
    assert result == expected_result_1, 'Test failed.'


def test_step2(x_selector1, x_selector2, x_selector4, btn_selector, expected_result_2):
    input1 = site.find_element('xpath', x_selector1)
    input1.clear()
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', x_selector2)
    input2.clear()
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', btn_selector)
    btn.click()
    link1 = site.find_element('xpath', x_selector4)
    result = link1.text
    assert result == expected_result_2, 'Test failed.'


def test_step3(new_post_btn_selector, title_selector,  expected_title, description_selector,
               content_selector, post_btn_selector, x_selector5):
    new_post_btn = site.find_element('xpath', new_post_btn_selector)
    new_post_btn.click()
    time.sleep(testdata['sleep_time'])
    title = site.find_element('xpath', title_selector)
    title.send_keys(testdata['title'])
    description = site.find_element('xpath', description_selector)
    description.send_keys(testdata['description'])
    content = site.find_element('xpath', content_selector)
    content.send_keys(testdata['content'])
    post_button = site.find_element('xpath', post_btn_selector)
    post_button.click()
    time.sleep(testdata['sleep_time'])

    post_title = site.find_element('xpath', x_selector5)
    result = post_title.text
    assert result == expected_title, 'Test failed.'

