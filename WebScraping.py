# # Web scraping is a general term for techniques involving automating the gathering of data from a website. In this
# # section we will learn how to use Python to conduct web scraping tasks, such as downloading images or info off a
# # website.
#
# # In order to web scrape with Python we need to understand the basic concepts of how a website works.
# # When a browser loads a website, the user gets to see what is known as the "front-end" of the website.
#
# # Main thing we need to understand
# # Rules of Web Scraping
# # Limitations of Web Scraping
# # Basic HTML and CSS
#
# # Rules of Web Scraping:
# # 1. Always try to ger permission before scraping!
# # 1.1 - If you make too many scraping attempts or requests your IP Address could get blocked!
# # 2.Some sites automatically block scraping software.
#
# # Scraping Limitation:
# # In general every website is unique, which means every web scraping script is unique!
# # A slight change or update to a website may completely break your web scraping script.
#
# import requests
# import lxml
# import bs4
#
# # _______________________________Grabbing a Title!__________________________
#
# result = requests.get("http://www.example.com")
# print(type(result))
#
# # print(result.text)
#
# soup = bs4.BeautifulSoup(result.text,"lxml")
#
# print(soup.select('title')[0].getText())
# site_paragraph = soup.select("p")
# print(site_paragraph[0].getText())
# print(site_paragraph[1].getText())
#



# import requests
# import bs4
#
# # Grabbing a class!
#
# # res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
#
# # soup = bs4.BeautifulSoup(res.text, 'lxml')
# # # print(soup)
# #
# # print(soup.select('.toctext')[0].getText())
# #
# # for item in soup.select('.toctext'):
# #    print(item.text)
#
#
# # Grabbing an image off of a website and saving it to your computer!
#
# res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
#
# soup = bs4.BeautifulSoup(res.text, 'lxml')
#
# # print(soup.select('.thumbimage'))
#
#
# computer = soup.select('.thumbimage')[0]
# print(computer)
# print(computer['src'])
#
# image_link = requests.get(
#     'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')
# # print(image_link.content)
#
# f = open('my_computer_image.jpg', 'wb')
#
# # wb - write binary because of image_ling.content gives out a binary
# # representation of an image in binary code!
#
# f.write(image_link.content)
# f.close()


# Real world - example project!
# ## We've seen how to grab elements one at a time, but realisically, we want to be able to grab multiple elements
# ## most likely across multiple pages
#
# ## This is where we can combine our prior python knowledge with the web scraping libraries to create powerful scripts!
#
# # We will use a website specifically designed for web scraping! : www.toscrape.com
# # We will practice grabbing elements across  multiple pages!
#
#
# # Goal: get the title of every book with a 2-star rating
# import bs4
# import requests
#
# # page_num = 1
# base_url = 'http://books.toscrape.com/catalogue/page-1.html'.format(1)
# # print(base_url)
#
# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# products = soup.select('.product_pod')
# # print(products[0])
# example = products[0]
# # print(example.select('.star-rating.Two'))
# # print(example.select('a')[1]['title'])
#
# two_star_titles = []
#
# for n in range(1,51):
#     scrape_url = base_url.format(n)
#     res = requests.get(scrape_url)
#
#     soup = bs4.BeautifulSoup(res.text, 'lxml')
#     books = soup.select(".product_pod")
#
#     for book in books:
#         if len(book.select('.star-rating.Two')) != 0:
#             book_title = book.select('a')[1]['title']
#             two_star_titles.append(book_title)
# print(two_star_titles)


# import bs4
# import requests
# import lxml
#
# # res = requests.get("https://quotes.toscrape.com/")
#
# # soup = bs4.BeautifulSoup(res.text, 'lxml')
#
# # authors = set()
# # # print(res.text)
# # get_title = soup.select('.author')
# #
# # for author in get_title:
# #     authors.add(author.text)
# # print(authors)
#
# # q_l = []
# # get_quote = soup.select('.text')
# # print(get_quote)
# #
# # for all_quotes in get_quote:
# #     q_l.append(all_quotes.text)
# # print(q_l)
# #
# # soup.select('.tag-item')
# #
# # for item in soup.select('.tag-item'):
# #     print(item.text)
#
# url = 'http://quotes.toscrape.com/page/'
# # url + str(10)
# # authors = set()
# #
# # for page in range(1,11):
# #     page_url = url + str(page)
# #
# #     res = requests.get(page_url)
# #     soup = bs4.BeautifulSoup(res.text, 'lxml')
# #     for name in soup.select('.author'):
# #         authors.add(name.text)
# # print(authors)
#
#
# page_url = url + str(999999)
# res = requests.get(page_url)
# soup1 = bs4.BeautifulSoup(res.text, 'lxml')
# # print(soup1)
# # print("No quotes found!" in res.text)
#
# page_still_valid = True
# authors = set()
# page = 1
# while page_still_valid:
#     page_url = url + str(page)
#     res = requests.get(page_url)
#
#     if "No quotes found!" in res.text:
#         break
#     soup1 = bs4.BeautifulSoup(res.text, 'lxml')
#
#     for name in soup1.select('.author'):
#         authors.add(name.text)
#
#     page = page + 1
# print(authors)

