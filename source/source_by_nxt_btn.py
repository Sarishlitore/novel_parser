from source.source import *
from selenium.webdriver.support.select import Select


class SourceByNextButton(Source, ABC):
    def __init__(self, book_url: str, book_name_xpath: str, book_author_xpath: str,
                 first_chapter_url: str, first_chapter_next_button_xpath: str, last_chapter_url: str,
                 chapter_title_xpath: str, chapter_content_xpath: str, next_button_xpath: str):
        super().__init__(book_url, book_name_xpath, book_author_xpath)
        self._first_chapter_url = first_chapter_url
        self._first_chapter_next_button_xpath = first_chapter_next_button_xpath
        self._last_chapter_url = last_chapter_url
        self._chapter_title_xpath = chapter_title_xpath
        self._chapter_content_xpath = chapter_content_xpath
        self._next_button_xpath = next_button_xpath

    @abstractmethod
    def _get_chapter_title(self, driver: uc) -> str:
        pass

    def _scrape_chapter(self, driver: uc, sleep_time) -> (str, list[str]):
        time.sleep(sleep_time)
        chapter_title = self._get_chapter_title(driver)
        chapter_content = driver.find_element(By.XPATH, self._chapter_content_xpath).text.split('\n')
        return chapter_title, chapter_content

    def _scrape_chapters(self, driver: uc, book: Book, sleep_time=5):
        while True:
            chapter_title, chapter_content = self._scrape_chapter(driver, sleep_time=sleep_time)
            book.add_chapter(chapter_title, chapter_content)
            print(f'{chapter_title} scraped')
            if driver.current_url == self._last_chapter_url:
                break
            driver.find_element(By.XPATH, self._next_button_xpath).click()

    def _scrape_first_chapter(self, driver: uc, book: Book, sleep_time=5):
        driver.get(self._first_chapter_url)
        first_chapter_title, first_chapter_content = self._scrape_chapter(driver, sleep_time)
        driver.find_element(By.XPATH, self._first_chapter_next_button_xpath).click()
        book.add_chapter(first_chapter_title, first_chapter_content)
        print(f'{first_chapter_title} scraped')

    def scrape(self, sleep_time=5) -> Book:
        driver = uc.Chrome(driver_executable_path='chromedriver.exe')
        book = self._form_book(driver, sleep_time)
        self._scrape_first_chapter(driver, book, sleep_time)
        self._scrape_chapters(driver, book, sleep_time)
        driver.quit()
        print(f'{book.name} scraped')
        return book


class Fanfiction(SourceByNextButton):
    @classmethod
    def form_source(cls, book_url: str, first_chapter_url: str, last_chapter_url: str):
        return cls(book_url=book_url,
                   book_name_xpath='//*[@id="profile_top"]/b',
                   book_author_xpath='//*[@id="profile_top"]/a[1]',
                   first_chapter_url=first_chapter_url,
                   first_chapter_next_button_xpath='//*[@id="content_wrapper_inner"]/span/button',
                   last_chapter_url=last_chapter_url,
                   chapter_title_xpath='//*[@id="chap_select"]',
                   chapter_content_xpath='//*[@id="storytext"]',
                   next_button_xpath='//*[@id="content_wrapper_inner"]/span/button[2]')

    def _get_chapter_title(self, driver: uc) -> str:
        return Select(driver.find_element(By.XPATH, self._chapter_title_xpath)).first_selected_option.text


class Scribblehub(SourceByNextButton):
    @classmethod
    def form_source(cls, book_url: str, first_chapter_url: str, last_chapter_url: str):
        return cls(book_url=book_url,
                   book_name_xpath='//*[@id="page"]/div/div[4]/div/div[1]/div[1]',
                   book_author_xpath='//*[@id="page"]/div/div[4]/div/div[4]/div[1]/div/div[3]/span/a/span',
                   first_chapter_url=first_chapter_url,
                   first_chapter_next_button_xpath='//*[@id="chp_contents"]/div[1]/div/a[2]',
                   last_chapter_url=last_chapter_url,
                   chapter_title_xpath='//*[@id="main read chapter"]/div[1]',
                   chapter_content_xpath='//*[@id="chp_raw"]',
                   next_button_xpath='//*[@id="chp_contents"]/div[1]/div/a[2]')

    def _get_chapter_title(self, driver: uc) -> str:
        return driver.find_element(By.XPATH, self._chapter_title_xpath).text


class Mtlnovel(SourceByNextButton):
    @classmethod
    def form_source(cls, book_url: str, first_chapter_url: str, last_chapter_url: str):
        return cls(book_url=book_url,
                   book_name_xpath='/html/body/main/article/div[1]/h1',
                   book_author_xpath='//*[@id="author"]/a',
                   first_chapter_url=first_chapter_url,
                   first_chapter_next_button_xpath='/html/body/main/article/div/div[2]/div[1]/a[1]',
                   last_chapter_url=last_chapter_url,
                   chapter_title_xpath='/html/body/main/article/div/h1',
                   chapter_content_xpath='/html/body/main/article/div/div[2]/div[4]',
                   next_button_xpath='/html/body/main/article/div/div[2]/div[1]/a[2]')

    def _get_chapter_title(self, driver: uc) -> str:
        return driver.find_element(By.XPATH, self._chapter_title_xpath).text


class Tlrulate(SourceByNextButton):
    @classmethod
    def form_source(cls, book_url: str, first_chapter_url: str, last_chapter_url: str):
        return cls(book_url=book_url,
                   book_name_xpath='/html/body/div[2]/div/div[1]/h1',
                   book_author_xpath='//*[@id="Info"]/div[1]/div[2]/p[4]/em/a',
                   first_chapter_url=first_chapter_url,
                   first_chapter_next_button_xpath='//*[@id="text-container"]/ul/li[2]/a',
                   last_chapter_url=last_chapter_url,
                   chapter_title_xpath='//*[@id="reader"]/header/nav/div[2]/select',
                   chapter_content_xpath='//*[@id="scroll_chapter_1905317"]/div/div[1]',
                   next_button_xpath='//*[@id="text-container"]/ul/li[2]/a')

    def _get_chapter_title(self, driver: uc) -> str:
        return Select(driver.find_element(By.XPATH, self._chapter_title_xpath)).first_selected_option.text


class Novelnext(SourceByNextButton):
    @classmethod
    def form_source(cls, book_url: str, first_chapter_url: str, last_chapter_url: str):
        return cls(book_url=book_url,
                   book_name_xpath='//*[@id="novel"]/div[1]/div[1]/div[3]/h3',
                   book_author_xpath='//*[@id="novel"]/div[1]/div[1]/div[3]/ul/li[1]/a',
                   first_chapter_url=first_chapter_url,
                   first_chapter_next_button_xpath='//*[@id="next_chap"]',
                   last_chapter_url=last_chapter_url,
                   chapter_title_xpath='//*[@id="chapter"]/div/div/h2/a/span',
                   chapter_content_xpath='//*[@id="chr-content"]',
                   next_button_xpath='//*[@id="next_chap"]')

    def _get_chapter_title(self, driver: uc) -> str:
        return driver.find_element(By.XPATH, self._chapter_title_xpath).text
