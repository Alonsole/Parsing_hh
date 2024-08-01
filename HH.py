from selenium import webdriver
import time
import json
driver = webdriver.Chrome()


class Parsing_go:
    def __init__(self, first_criterion, second_criterion, url_parsing):
        self.first_criterion = first_criterion
        self.second_criterion = second_criterion
        self.get_url = url_parsing

    def letsgodance(self):
        """Функция парсинга"""
        driver.get(self.get_url)
        time.sleep(2)
        get_urls = driver.find_elements(
            'xpath', "(//div [@data-qa='vacancy-serp__results']//"
                     "div[contains(@class, 'vacancy-card--z')])//h2//a")
        result_final = []
        i = 1
        urls = [url.get_attribute('href') for url in get_urls]
        for go_url in urls:
            result = {}
            driver.get(go_url)
            time.sleep(2)
            job_vacancy_text = driver.find_element(
                'xpath', "(//div [@class='vacancy-section'])[1]").text
            money = driver.find_element(
                'xpath', "//div [@class='vacancy-title']//span[contains(@class, 'magritte-text')]").text
            company = driver.find_element(
                'xpath', "//span [@class='vacancy-company-name']").text
            try:
                address = driver.find_element(
                    'xpath', "(//span [@data-qa='vacancy-view-raw-address'])[1]").text
            except:
                address = "Адрес не указан"
            if self.first_criterion in job_vacancy_text and self.second_criterion in job_vacancy_text:
                result['Вакансия № ' + str(i)] = go_url
                result['Зарплата'] = money
                result['Компания'] = company
                result['Адрес'] = address
                i += 1
                result_final.append(result)
            else:
                print('Увы это объявление нам не подходит по критериям')

        if i > 1:
            print('Записываю результаты, подождите пожалуйста')
            with open('jobs.json', 'w', encoding='utf-8') as f:
                json.dump(result_final, f, ensure_ascii=False, indent=4)
            print('Запись результатов завершена')
        else:
            print('Увы по критериям нет совпадений')


first_criterion = "Django"
second_criterion = "Flask"
url_parsing = "https://****************************/*********/*********?text=python&area=1&area=2"
if __name__ == '__main__':
    hh_parsing = Parsing_go(first_criterion, second_criterion, url_parsing)
    hh_parsing.letsgodance()
