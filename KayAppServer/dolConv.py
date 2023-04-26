import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой
global Cur;
# Основной класс
class Currency:
    # Ссылка на нужную страницу
    DOLLAR_RUB="https://nbu.uz/en/exchange-rates/"
    # Заголовки для передачи вместе с URL
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    current_converted_price = 0
    difference = 5 # Разница после которой будет отправлено сообщение на почту

    def __init__(self):
        # Установка курса валюты при создании объекта
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

    # Метод для получения курса валюты
    def get_currency_price(self):
        global Cur
        # Парсим всю страницу
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("tr")
        file=open("curBuf.html","w");
        file.write(str(convert[1].text));
        file.close();
        file=open("curBuf.html","r");
        data=file.readlines();
        file.close();

        Cur=data[2].replace("\n","").replace(" ","");
        return data[2]
 
    # Проверка изменения валюты
    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            print("Курс сильно вырос, может пора что-то делать?")
            self.send_mail()
        elif currency <= self.current_converted_price - self.difference:
            print("Курс сильно упал, может пора что-то делать?")
            self.send_mail()

        print("Сейчас курс: 1 доллар = " + str(currency))
        time.sleep(3) # Засыпание программы на 3 секунды
        self.check_currency()
        return currency

    # Отправка почты через SMTP
    def send_mail(self):
        pass

# Создание объекта и вызов метода
def get_dol():
    global Cur
    currency = Currency()
    return Cur;

print(get_dol())