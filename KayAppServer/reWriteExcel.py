import shutil
from zipfile import ZipFile
import os;
def re(filename):
    filename=filename.replace(".xlsx","")
    # Создаем временную папку
    tmp_folder = '/tmp/convert_wrong_excel/'
    os.makedirs(tmp_folder, exist_ok=True)

    # Распаковываем excel как zip в нашу временную папку
    with ZipFile(filename+'.xlsx') as excel_container:
        excel_container.extractall(tmp_folder)

    # Переименовываем файл с неверным названием
    wrong_file_path = os.path.join(tmp_folder, 'xl', 'SharedStrings.xml')
    correct_file_path = os.path.join(tmp_folder, 'xl', 'sharedStrings.xml')
    os.rename(wrong_file_path, correct_file_path) 

    # Запаковываем excel обратно в zip и переименовываем в исходный файл
    shutil.make_archive(filename+'', 'zip', tmp_folder)
    os.rename(filename+'.zip', filename+'.xlsx')