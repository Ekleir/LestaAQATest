import pytest
from engine2d import *


def test_circle_positive():
    circle_test = Circle(1, 2, 3)
    assert circle_test.x == 1
    assert circle_test.y == 2
    assert circle_test.radius == 3
    assert circle_test.color == 'black'


def test_circle_negative():
    with pytest.raises(AttributeError) as error1:
        circle_test = Circle(0, 0, 0)
    with pytest.raises(AttributeError) as error2:
        circle_test = Circle(0, 0, -1)
    assert str(error1.value) == "Radius can't be empty"
    assert str(error2.value) == "Radius can't be negative!"


def test_triangle():
    triangle_test = Triangle(1, 1, 2, 2, 3, 3)
    assert triangle_test.point1 == (1, 1)
    assert triangle_test.point2 == (2, 2)
    assert triangle_test.point3 == (3, 3)
    assert triangle_test.color == 'black'


def test_triangle_negative():
    with pytest.raises(ValueError) as error:
        triangle_test = Triangle(1, 1, 1, 1, 3, 3)
    assert str(error.value) == 'Points should not be equal!'


def test_rectangle():
    rectangle_test = Rectangle(1, 1, 2, 3)
    assert rectangle_test.start_point == (1, 1)
    assert rectangle_test.width == 2
    assert rectangle_test.height == 3
    assert rectangle_test.color == 'black'


@pytest.mark.parametrize('x1, y1, x2, x3, error_text', [(1, 1, 0, 3, "Width can't be empty"),
                                                        (1, 1, 'a', 1, "Width must be int!"),
                                                        (1, 1, -1, 1, "Width can't be negative!"),
                                                        (1, 1, 1, 0, "Height can't be empty"),
                                                        (1, 1, 1, 'a', "Height must be int!"),
                                                        (1, 1, 1, -1, "Height can't be negative!")
                                                        ])
def test_rectangle_negative(x1, y1, x2, x3, error_text):
    with pytest.raises(AttributeError, match=error_text):
        Rectangle(x1, y1, x2, x3)


def test_circle_draw(capsys):
    circle_test = Circle(1, 2, 3)
    circle_test.draw()
    out, err = capsys.readouterr()
    assert circle_test.color == 'black'
    assert out == 'Drawing Circle: (1, 2) with radius 3\n'


def test_triangle_draw(capsys):
    triangle_test = Triangle(1, 1, 2, 2, 3, 3)
    triangle_test.draw()
    out, err = capsys.readouterr()
    assert triangle_test.color == 'black'
    assert out == 'Drawing Triangle: ((1, 1), (2, 2), (3, 3)\n'


def test_rectangle_draw(capsys):
    rectangle_test = Rectangle(1, 1, 2, 3)
    rectangle_test.draw()
    out, err = capsys.readouterr()
    assert rectangle_test.color == 'black'
    assert out == 'Drawing Rectangle: ((1, 1) with width 2, height 3\n'


def test_engine2d():
    engine_test = Engine2D()
    assert engine_test.color == 'black'
    assert engine_test.canvas == []


def test_add_figures():
    rectangle_test1 = Rectangle(1, 1, 2, 3)
    triangle_test1 = Triangle(1, 1, 2, 2, 3, 3)
    circle_test1 = Circle(1, 2, 3)
    rectangle_test2 = Rectangle(10, 10, 20, 30)
    triangle_test2 = Triangle(10, 10, 20, 20, 30, 30)
    circle_test2 = Circle(10, 20, 30)
    engine_test = Engine2D()
    engine_test.add_figures(rectangle_test1, triangle_test1, circle_test1)
    assert engine_test.canvas == [rectangle_test1, triangle_test1, circle_test1]
    engine_test.add_figures(rectangle_test2, triangle_test2, circle_test2)
    assert engine_test.canvas == [rectangle_test1, triangle_test1, circle_test1, rectangle_test2, triangle_test2,
                                  circle_test2]
    assert len(engine_test.canvas) == 6


def test_color():
    engine_test = Engine2D()
    assert engine_test.color == 'black'
    engine_test.set_color('yellow')
    assert engine_test.color == 'yellow'
    engine_test.set_color('white')
    assert engine_test.color == 'white'


def test_add_figures_color():
    engine_test = Engine2D()
    rectangle_test1 = Rectangle(1, 1, 2, 3)
    triangle_test1 = Triangle(1, 1, 2, 2, 3, 3)
    circle_test1 = Circle(1, 2, 3)
    engine_test.add_figures(rectangle_test1, triangle_test1, circle_test1)
    engine_test.set_color('white')
    assert rectangle_test1.color == 'black'
    assert triangle_test1.color == 'black'
    assert circle_test1.color == 'black'
    rectangle_test2 = Rectangle(10, 10, 20, 30)
    triangle_test2 = Triangle(10, 10, 20, 20, 30, 30)
    circle_test2 = Circle(10, 20, 30)
    assert rectangle_test2.color == 'black'
    assert triangle_test2.color == 'black'
    assert circle_test2.color == 'black'
    engine_test.add_figures(rectangle_test2, triangle_test2, circle_test2)
    assert rectangle_test2.color == 'white'
    assert triangle_test2.color == 'white'
    assert circle_test2.color == 'white'
    assert engine_test.canvas[0].color == 'black'
    assert engine_test.canvas[1].color == 'black'
    assert engine_test.canvas[2].color == 'black'
    assert engine_test.canvas[3].color == 'white'
    assert engine_test.canvas[4].color == 'white'
    assert engine_test.canvas[5].color == 'white'


def test_add_figures_draw_default(capsys):
    engine_test = Engine2D()
    rectangle_test1 = Rectangle(1, 1, 2, 3)
    triangle_test1 = Triangle(1, 1, 2, 2, 3, 3)
    circle_test1 = Circle(1, 2, 3)
    engine_test.add_figures(rectangle_test1, triangle_test1, circle_test1)
    engine_test.draw()
    out, err = capsys.readouterr()
    assert out == 'Drawing Rectangle: ((1, 1) with width 2, height 3\n' \
                  'Drawing Triangle: ((1, 1), (2, 2), (3, 3)\n' \
                  'Drawing Circle: (1, 2) with radius 3\n'
    assert engine_test.canvas == []


def test_add_figures_draw_color_change(capsys):
    engine_test = Engine2D()
    rectangle_test1 = Rectangle(1, 1, 2, 3)
    engine_test.add_figures(rectangle_test1)
    engine_test.set_color('green')
    triangle_test_green = Triangle(1, 1, 2, 2, 3, 3)
    circle_test1_green = Circle(1, 2, 3)
    engine_test.add_figures(triangle_test_green, circle_test1_green)
    engine_test.draw()
    out, err = capsys.readouterr()
    assert out == 'Drawing Rectangle: ((1, 1) with width 2, height 3\n' \
                  'Drawing Triangle: ((1, 1), (2, 2), (3, 3), color - green\n' \
                  'Drawing Circle: (1, 2) with radius 3, color - green\n'
    assert engine_test.canvas == []


def test_add_figures_draw_color_change_multiple(capsys):
    engine_test = Engine2D()
    rectangle_test1 = Rectangle(1, 1, 2, 3)
    engine_test.add_figures(rectangle_test1)
    engine_test.set_color('green')
    triangle_test_green = Triangle(1, 1, 2, 2, 3, 3)
    circle_test1_green = Circle(1, 2, 3)
    engine_test.add_figures(triangle_test_green, circle_test1_green)
    engine_test.set_color('white')
    rectangle_test_white = Rectangle(10, 10, 20, 30)
    engine_test.add_figures(rectangle_test_white)
    engine_test.draw()
    out, err = capsys.readouterr()
    assert out == 'Drawing Rectangle: ((1, 1) with width 2, height 3\n' \
                  'Drawing Triangle: ((1, 1), (2, 2), (3, 3), color - green\n' \
                  'Drawing Circle: (1, 2) with radius 3, color - green\n' \
                  'Drawing Rectangle: ((10, 10) with width 20, height 30, color - white\n'
    assert engine_test.canvas == []
