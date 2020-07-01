"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""

import time
import turtle


class TrafficLight:

    def __init__(self):
        self.__color = 'grey'

    def running(self):
        """makes traffic light switch the lights indefinitely visually represented via turtle module"""

        # draw background
        main_screen = turtle.Screen()
        main_screen.title('Traffic light')
        main_screen.bgcolor('black')

        # draw main traffic light box
        pen = turtle.Turtle()
        pen.color(self.__color)
        pen.width(4)
        pen.hideturtle()
        pen.penup()
        pen.goto(-30, 60)
        pen.pendown()
        pen.fd(60)
        pen.rt(90)
        pen.fd(120)
        pen.rt(90)
        pen.fd(60)
        pen.rt(90)
        pen.fd(120)

        # starting positions of traffic light
        red_light_switch = turtle.Turtle()
        yellow_light_switch = turtle.Turtle()
        green_light_switch = turtle.Turtle()

        red_light_switch.shape("circle")
        red_light_switch.color(self.__color)
        red_light_switch.penup()
        red_light_switch.goto(0, 40)
        yellow_light_switch.shape("circle")
        yellow_light_switch.color(self.__color)
        yellow_light_switch.penup()
        yellow_light_switch.goto(0, 0)
        green_light_switch.shape("circle")
        green_light_switch.color(self.__color)
        green_light_switch.penup()
        green_light_switch.goto(0, -40)

        # make traffic light change colors indefinitely in a certain order with a certain delay
        while True:
            self.__color = 'red'
            red_light_switch.color(self.__color)
            time.sleep(7)

            self.__color = 'grey'
            red_light_switch.color(self.__color)
            self.__color = 'yellow'
            yellow_light_switch.color(self.__color)
            time.sleep(2)

            self.__color = 'grey'
            yellow_light_switch.color(self.__color)
            self.__color = 'green'
            green_light_switch.color(self.__color)
            time.sleep(7)
            self.__color = 'grey'
            green_light_switch.color(self.__color)

        main_screen.mainloop()


traffic_light = TrafficLight()
traffic_light.running()
