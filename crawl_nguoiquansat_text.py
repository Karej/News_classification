import json
import requests
from bs4 import BeautifulSoup

# Đọc file json chứa link


# Danh sách để lưu nội dung từ các link
data_all =[]
contents = []

    # Lấy link từ từng item
with open('news_links_tinnhanhchungkhoan.json', 'r', encoding='utf-8-sig') as file:  # Thêm '-sig' để tự động loại bỏ BOM
    data = json.load(file)
#a=0
for item in data:
    
    link = item['Link']
    response = requests.get(link)

    # Sử dụng BeautifulSoup để phân tích nội dung HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Tìm tất cả thẻ <p> có class "Headlines" và biến đổi thành text
    p_tags = soup.find('div', class_='article__sapo cms-desc')
    headlines = []
    if p_tags:
        headlines = p_tags.get_text().replace(u'\ufeff', '').replace('\n', '')
    
    # Lấy article
    articles = soup.find('h1', class_='article__header cms-title')
    title = []
    if articles:
    
        title = articles.get_text().replace(u'\ufeff', '').replace('\n', '')
    
    #Lấy tag cũng như đoạn text chính
    
    
    content = []
    #key_words = []    
    
    keys_tabs = soup.find('div', class_="article__tag")
    key =[]
    if keys_tabs:
        keys = keys_tabs.find_all('a')
        key = [a.get_text().replace('\n', '') for a in keys]
        
    div_tags = soup.find('div', class_ = 'article__body cms-body')
    if div_tags:

        # highlight_tags =  div_tags.find_all('a', href=True, attrs={'target': '_blank'})
        # highlight_tags = [a.get_text().replace(u'\ufeff', '') for a in highlight_tags]
        # if highlight_tags:
        #     if len(highlight_tags) !=1:
        #         highlight_tags.pop()
      
      
      
        #for a in div_tags.find_all('p', href=True, attrs={'target': '_blank'}):
        #    a.unwrap()

        div_tag = div_tags.find_all('p')
        content = [p.get_text().replace(u'\ufeff', '').replace('\n', '')  for p in div_tag]
        content.pop()
        
    else:
        content = []
    
    # Thêm nội dung vào danh sách
    contents.append({
        'Link': link,
        'Title':title,
        'Headlines': headlines,
        'Content': ''.join(content),
        'Tag': key
    })
    
    # a+=1
    # if a >=10:
    #     break
    
    
    
data_all.extend(contents)

# Ghi nội dung đã lấy được vào file json mới
with open('text_nguoiquansat.json', 'w', encoding='utf-8') as file:
    json.dump(data_all, file,ensure_ascii=False,indent=4)
