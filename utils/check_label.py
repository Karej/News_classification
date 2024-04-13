import json
import re

# Đọc file json chứa bài báo
with open('labeled_articles.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

# Biểu thức chính quy tìm các từ có 3 chữ cái bao quanh bởi dấu ngoặc tròn
pattern = r'\([a-zA-Z]{3}\)'

for article in data:
    # Lấy title của bài báo
    try:
        title = article['Label']
    except:
        #if title == None:
        print(article['Link'])
        
print(len(data))

            
            
        

# Ghi dữ liệu đã cập nhật vào file json mới
# with open('labeled_articles.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, ensure_ascii=False,indent=4)
