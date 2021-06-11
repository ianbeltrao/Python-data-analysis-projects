from bs4 import BeautifulSoup
import requests

webpage = requests.get("http://books.toscrape.com")
soup = BeautifulSoup(webpage.content, "html.parser")


#Separating the book categories
a = soup.find_all("a")
lst = []
for i in a[3:53]:
    lst.append(i.string)
categories = []
for cat_raw in lst:
    categories.append(cat_raw.strip())

#Separating links per category
links = []
for link in a[3:53]:
    links.append(link.get("href"))

#Getting all the books
pages = []
all_books = []
for index in range(len(links)):
    wp_per_cat = requests.get(f"http://books.toscrape.com/{links[index]}")
    soup_per_cat = BeautifulSoup(wp_per_cat.content, "html.parser")
    num_pages_html = soup_per_cat.select(".current")
    num_pages = 0
    for html in num_pages_html:
        cleaned = html.get_text().strip()
        num_pages += int(cleaned[-1])
    

    if num_pages == 0:
        books_html = soup_per_cat.select("h3")
        for i in books_html:
            for a in i.find_all("a"):
                if 'title' in a.attrs:
                    all_books.append(a['title'])
    else:
        link_per_page = links[index].replace("index.html", "page-")
        for num in range(num_pages):
            page_num = num + 1
            wp_per_page_num = requests.get(f"http://books.toscrape.com/{link_per_page}{page_num}.html")
            soup_per_page_num = BeautifulSoup(wp_per_page_num.content, "html.parser")
            books_html_per_page = soup_per_page_num.select("h3")
            for i in books_html_per_page:
                for a in i.find_all("a"):
                    if 'title' in a.attrs:
                        all_books.append(a['title'])

books_dict = {}
for i in range(len(categories)):
    books_dict[categories[i]] = all_books[i]

print(books_dict)

    

    


    





