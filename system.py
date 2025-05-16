import pandas as pd
from datetime import datetime, timedelta
from database import Database

months = {
    'январь': 1, 'января': 1,
    'февраль': 2, 'февраля': 2,
    'март': 3, 'марта': 3,
    'апрель': 4, 'апреля': 4,
    'май': 5, 'мая': 5,
    'июнь': 6, 'июня': 6,
    'июль': 7, 'июля': 7,
    'август': 8, 'августа': 8,
    'сентябрь': 9, 'сентября': 9,
    'октябрь': 10, 'октября': 10,
    'ноябрь': 11, 'ноября': 11,
    'декабрь': 12, 'декабря': 12
}
    
def delete_nan(data : list):
    new_data = []
    for item in data:
        item = str(item)
        if item != None and item != "nan":
            new_data.append(item)
    return new_data
    

def sort_key(class_name):
    # Разделяем строку на числовую и буквенную части
    number = int(''.join(filter(str.isdigit, class_name)))  # Извлекаем число
    letter = ''.join(filter(str.isalpha, class_name)).upper()  # Извлекаем букву и приводим к нижнему регистру
    return (number, letter)

def contains_digits(s):
    return any(char.isdigit() for char in s)    


class Schedule():
    def __init__(self):
        self.classes = []
        self.lessons = {}
        self.final_lessons = {}
        self.substitutions = {}
        self.times_days = {}
        
        self.today = datetime.today()
        
        self.url_lessons = "https://docs.google.com/spreadsheets/d/1NsYsa8QUu1tki0Wloc1wyhRrpSLhkI5L/export?format=xlsm"
        
        self.url_substitutions = "https://docs.google.com/spreadsheets/d/1BWGgHETchbg1_GHCPBX_AF_w_WWg-keO/export?format=xlsm"
        pass
    
    def load_substitutions(self):
        df_substitutions = pd.ExcelFile(self.url_substitutions)
        filtered_dates = []
        for item in df_substitutions.sheet_names:
            date = self.parse_date(item)
            if date and date > self.today and date < self.today + timedelta(60):
                filtered_dates.append(item)
        data_found = ["№", "класс", "фио отсутствующего", "предмет", "фио заменяющего", "кабинет", "примечание"]
        for filtered_date in filtered_dates:
            df = pd.read_excel(self.url_substitutions, sheet_name=filtered_date)
            for item in df.iloc[0]:
                for founded in data_found:
                    if founded in str(item):
                        data = delete_nan(df.iloc[:, data_found.index(founded)])[1:]
                        print(data)
                        return
    
    def load_lessons(self):
        df_lessons = pd.ExcelFile(self.url_lessons)
        filtered_dates = [df_lessons.sheet_names[0]]
        for item in df_lessons.sheet_names:
            date = self.parse_date(item)
            if date and date > self.today and date < self.today + timedelta(60):
                filtered_dates.append(item)
        df = pd.read_excel(self.url_lessons, sheet_name=filtered_dates[0])
        data = delete_nan(df.iloc[:, 1])
        indx = 0
        temp = None
        for item in data:
            if "время" in item.lower():
                indx += 1
                self.times_days[indx] = []
                continue
            if not temp:
                temp = datetime.strptime(item, "%H:%M:%S").time()
                continue
            self.times_days[indx].append([temp, datetime.strptime(item, "%H:%M:%S").time()])
            temp = None
        indx1 = 0
        with Database() as db:
            for item in df.iloc[1]:
                indx1 += 1
                if item != "10Б":
                    continue
                if type(item) != str:
                    continue
                self.lessons[item] = {}
                self.classes.append(item)
                data = list(df.iloc[:, indx1])[3:]
                indx = 1
                i = 0
                save_i = 0
                while True:
                    indx_lesson = 0
                    self.lessons[item][indx] = []
                    while True:
                        if (i - save_i) % 2 == 0:
                            indx_lesson += 1
                        if i >= len(data)-1:
                            break
                        office = str(data[i])
                        title = str(data[i + 1])
                        if office == "Каб/Предмет":
                            i += 1
                            save_i = i
                            break
                        if title == "Каб/Предмет":
                            i += 2
                            save_i = i
                            break
                        if title == "nan" or not title:
                            i += 2
                            continue
                        i += 2
                        if "физку" in title.lower():
                            office = "Спортивный зал"
                        # db.execute("INSERT INTO schedule (class_name, day, lesson_number, lesson_name, offices) VALUES (%s, %s, %s, %s, %s)", (item, indx, indx_lesson, title, office))
                        
                        self.lessons[item][indx].append({title : office})
                    if i >= len(data)-1:
                        break
                    indx += 1
        self.classes = sorted(self.classes, key=sort_key)
        # Добавить обработку спец дней
                
    
    def parse_date(self, string):
        try:
            # Разделяем строку на слова
            parts = string.split() 
            # Ищем число и месяц
            for i, part in enumerate(parts):
                if part.isdigit():  # Если часть является числом
                    day = int(part)
                    month_name = parts[i + 1].lower()  # Берем следующее слово как название месяца
                    if month_name in months:  # Если месяц найден в словаре
                        month = months[month_name]
                        # Создаем объект datetime (год берем текущий)
                        return datetime(self.today.year, month, day)
            return None
        except (IndexError, ValueError):
            return None
    
schedule = Schedule()
schedule.load_lessons()
print(schedule.classes)
print(schedule.lessons)
# with Database() as db:
#     for day, items in schedule.times_days.items():
#         indx = 0
#         for item in items:
#             indx += 1
#             lesson_start = item[0]
#             lesson_stop = item[1]
#             db.execute("INSERT INTO call_schedule (day_number, lesson_number, lesson_start, lesson_stop) VALUES (%s, %s, %s, %s)", (day, indx, lesson_start, lesson_stop))