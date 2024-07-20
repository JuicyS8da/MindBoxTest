# MindBoxTest

Практические задания для компании MindBox

Задание 2:

Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:

    Юнит-тесты
    Легкость добавления других фигур
    Вычисление площади фигуры без знания типа фигуры в compile-time
    Проверку на то, является ли треугольник прямоугольным

Задание 3:

В PySpark приложении датафреймами(pyspark.sql.DataFrame) заданы продукты, категории и их связи. Каждому продукту может соответствовать несколько категорий или ни одной. А каждой категории может соответствовать несколько продуктов или ни одного. Напишите метод на PySpark, который в одном датафрейме вернет все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий.

# Гайд на установку:

If you haven't installed python yet, here is an instruction on how to set up everything correctly:
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server

How to create a virtual python environment:

    Pick a folder for a project
    Use

python -m venv venv for Windows or

python3 -m venv venv for Linux.

    Enter your vitrual environment source test/bin/activate for Linux or

test/Scripts/activate.bat In Windows CMD

test/Scripts/Activate.ps1 In Windows Powershell

How to clone project to your virtual environment:
1. ```git clone https://github.com/JuicyS8da/MindBoxTest```
2. ```pip install PySpark```
3. ```python MindBoxTest.py```

To run tests use: ```python -m unittest tests/objects_test.py```
