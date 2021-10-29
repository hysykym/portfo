# import 開啟Flask檔, 開啟.html檔, request檔案, redirect to .html
from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

# root
@app.route('/')
def root():
    # 打開index.html
    return render_template('index.html')

# 其他頁面 <使用者輸入，若有則開啟，若無則錯誤>
@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name)

# 存成txt
# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email},{subject}, {message}')

# 把資料存成csv
def write_to_csv(data):
    # 開csv檔 mode a(append) 空一行(因為標題已經打好了)
    with open('database.csv', newline='', mode='a') as database:
        # 讀contact資料中的資料
        email = data['email']
        subject = data['subject']
        message = data['message']
        # 寫進去 分隔是,
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject, message])

# contact頁面用的傳送資料func (GET內容會顯示在網址 所以用POST)
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # data = request.form['email']
            # 讀資料並轉成dict
            data = request.form.to_dict()
            write_to_csv(data)
            # 完成 並轉到感謝的頁面
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something is wrong'


# @app.route('/blog/<username>')
# def blog(username=None):
#     return f'These are my thoughs of blog {username}'