from canvasapi import Canvas
import markdownify as md



class Scraper:
    def __init__(self,api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url 
        self.course = ""
        self.canvas = Canvas(self.api_url,self.api_key)

    def set_course(self, course):
        self.course = course
    
    def get_course(self):
        return self.course
    
    def convert_pages_to_markdown(self,pathname):
        cur_class = self.canvas.get_course(self.course)

        pages = cur_class.get_pages()
        for page in pages:
            new_page = cur_class.get_page(page.url)
            cleaned_up_page = md.markdownify(new_page.body)
            f = open(pathname+page.title, "w")
            f.write(cleaned_up_page)

# Grab your Canvas api key from user settings
API_KEY = ""
# Specify your base canvas url i.e https://canvas.uni.edu/
API_URL = ""

# Setup a Scrapper object and specify course you'd like to pull from.
csci5117 = Scraper(API_KEY,API_URL)

# The course id can be found in the url after clicking on the course page i.e https://canvas.uni.edu/courses/123456
csci5117.set_course(123456)

# Pass the location you'd like to write to, files names will be specified by page name.
csci5117.convert_pages_to_markdown("/example/path/Desktop")