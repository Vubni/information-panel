from database import Database

with Database() as db:
    db.execute("INSERT INTO achievements (date, title, description, image) VALUES (%s, %s, %s, %s)", (None,
                    "Иманаев Егор, ученик 10Б занял 3 место!",
                    "Ученик занял 3 место в Региональном этапе Чемпионата по профессиональному мастерству 'Профессионалы' в компетенции 'Программные решения для бизнеса'!",
                 open("image_temp/photo_2025-03-09_23-55-21.jpg", 'rb').read()))