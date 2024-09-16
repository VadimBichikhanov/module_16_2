from fastapi import FastAPI, Path
from typing import Annotated
# Создаем объект FastAPI
app = FastAPI()

# Маршрут к главной странице
@app.get("/")
async def read_main_page():
    return {"message": "Главная страница"}

# Маршрут к странице администратора
@app.get("/user/admin")
async def read_admin_page():
    return {"message": "Вы вошли как администратор"}

# Маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}")
async def read_user_page( 
    user_id: Annotated[int, Path(description='Enter User ID', ge=1, le=100)]) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут к страницам пользователей с передачей данных в адресной строке
@app.get("/user/{username}/{age}")
async def read_user_info(
    username: Annotated[str, Path(description='Enter username', min_length=5, max_length=20)],
    age: Annotated[int, Path(description='Enter age', ge=18, le=120)]) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}