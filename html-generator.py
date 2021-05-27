# Генератор стартового html шаблона
import os
import shutil
import requests

name = input('Введите название нового проекта: ')  # Получаем от пользователя название проекта
font = input('Выберите шрифт первым параментром и его плотность остальными (шрифт, 500, 600): ')  # Получаем от пользователя желаемый шрифт из Google Fonts


# Обработка шрифта
font = font.replace(', ', ',')
font = font.split(',')
if font == [''] or font == [' ']:
    font = ['Roboto']
print('Выбран шрифт ' + font[0])
print('Идёт загрузка шаблона...')

# Создание папки с указанным названием и перезапись в случае её существования
if os.path.exists(name):
    shutil.rmtree(name)
if os.path.exists('remove_' + name + '.py'):
    os.remove('remove_' + name + '.py')
os.mkdir(name)

# Создание скрипта для удаления шаблона
with open('remove_' + name + '.py', 'w') as remover:
    remover.write('# Removing template\n')
    remover.write('import os\n')
    remover.write('import shutil\n\n')
    remover.write('shutil.rmtree("' + name + '")\n')
    remover.write('os.remove("remove_' + name + '.py")')

# Создание папок для проекта
os.makedirs(name + '/css')
os.makedirs(name + '/js')
os.makedirs(name + '/img')

# Создание пояснительного файла
with open(name + '/README.txt', 'w') as readme:
    readme.write('Чтобы запустить локальный сервер,\n')
    readme.write('нажмите правой кнопкой мыши с зажатой клавишей Shift в любое место в этой папке,\n')
    readme.write('и нажмите "открыть окно команд",\n')
    readme.write('потом напишите "py server.py" и нажмите клавишу Enter.\n')
    readme.write('Приятной работы!)')

# Создание и наполнение html страницы
with open(name + '/index.html', 'w') as index_html:
    index_html.write('<!DOCTYPE html>' + '\n')
    index_html.write('<html lang="en">' + '\n')
    index_html.write('\t' + '<head>' + '\n')
    index_html.write('\t\t' + '<meta charset="UTF-8">' + '\n')
    index_html.write('\t\t' + '<meta name="viewport" content="width=device-width, initial-scale=1.0">' + '\n')
    index_html.write('\t\t' + '<title>' + name + '</title>' + '\n')
    index_html.write('\t\t' + '<!-- Connecting stylesheet -->' + '\n')
    index_html.write('\t\t' + '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">' + '\n')
    index_html.write('\t\t' + '<link rel="stylesheet" href="css/style.css">' + '\n')
    index_html.write('\t' + '</head>' + '\n')
    index_html.write('\t' + '<body>' + '\n\n')
    index_html.write('\t\t' + '<!-- Main code -->' + '\n')
    index_html.write('\t\t' + name + '\n')
    index_html.write('\t\t' + '<!-- /Main code -->' + '\n\n')
    index_html.write('\t\t' + '<!-- Connecting scripts -->' + '\n')
    index_html.write('\t\t' + '<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>' + '\n')
    index_html.write('\t\t' + '<script src="js/script.js"></script>' + '\n')
    index_html.write('\t' + '</body>' + '\n')
    index_html.write('</html>' + '\n')

# Создание и наполнение style.css
with open(name + '/css/style.css', 'w') as style_css:
    # Подключение шрифтов
    font[0] = font[0].replace(' ', '+')
    if len(font) == 1:
        style_css.write("@import url('https://fonts.googleapis.com/css2?family=" + font[0] + "&display=swap');" + '\n\n')
    else:
        style_css.write("@import url('https://fonts.googleapis.com/css2?family=" + font[0] + ":wght@" + ';'.join(font[1::]) + "&display=swap');" + '\n\n')
    style_css.write('body{' + '\n')
    font[0] = font[0].replace('+', ' ')
    style_css.write('\t' + 'font-family: ' + "'" + font[0] + "';" + '\n')
    style_css.write('}' + '\n')

# Создание и наполнение script.js
with open(name + '/js/script.js', 'w') as script_js:
    script_js.write('$(function(){' + '\n\t\n')
    script_js.write('});')

# Создание и наполнение файла для запуска локального сервера
with open(name + '/server.py', 'w') as server_py:
    server_py.write('# Local server for ' + name + '\n')
    server_py.write('from http.server import HTTPServer, CGIHTTPRequestHandler' + '\n')
    server_py.write('import webbrowser' + '\n')
    server_py.write('from livereload import Server, shell' + '\n\n')
    server_py.write("webbrowser.open('http://localhost:8080/')" + '\n\n')
    server_py.write("server = Server()" + '\n')
    server_py.write("server.watch('index.html')" + '\n')
    server_py.write("server.watch('css/*')" + '\n')
    server_py.write("server.watch('js/*')" + '\n')
    server_py.write("server.watch('img/*')" + '\n')
    server_py.write("server.serve(port=8080, host='localhost')" + '\n\n')
    server_py.write("server_data = ('localhost', 8080)" + '\n')
    server_py.write('server = HTTPServer(server_data, CGIHTTPRequestHandler)' + '\n')
    server_py.write('server.serve_forever()' + '\n\n')

# Добавление картинки в папку img
URL = 'https://img2.akspic.ru/image/3937-kosmicheskoe_prostranstvo-atmosfera_zemli-sinij-zvezdy-zvezda-1920x1080.jpg'
r = requests.get(URL)
with open(name + '/img/image.jpg', 'wb') as img:
    img.write(r.content)

print('Шаблон готов!')
