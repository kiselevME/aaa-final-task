import sys
from typing import Callable
import click
from random import randint

PIZZAS = {
    'Margherita': ('🧀', ['tomato sauce', 'mozzarella', 'tomatoes']),
    'Pepperoni': ('🍕', ['tomato sauce', 'mozzarella', 'pepperoni']),
    'Hawaiian': ('🍍', ['tomato sauce', 'mozzarella', 'chicken', 'pineapples'])
    }


def log(arg: str) -> Callable:
    """Декоратор для подсчета времени"""
    def actual_decorator(f: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            time = randint(1, 10)
            result = f(*args, **kwargs)
            click.echo(arg.format(time))
            return result
        return wrapper
    return actual_decorator


class Pizza:
    """Класс с объекта пицца"""
    def __init__(self, name: str, size: str) -> None:
        """Создает объект пицца с выбранным названием и размером

        Args:
            name (str): Название пиццы
            size (str): Размер пиццы
        """
        self.name = name
        self.size = size
        self._valid_pizza_params()
        self.ingredients = self.pizza_ingredients(name)
        self.is_cooked = False

    @log('🍳 Приготовили за {}с!')
    def bake(self) -> None:
        """Готовит пиццу"""
        self.is_cooked = True

    @log('🛵 Доставили за {}с!')
    def delivery(self) -> None:
        """Доставляет пиццу"""
        if not self.is_cooked:
            click.echo('Пицца не приготовлена. Принудительно вызван метод'
                       'bake')
            self.bake()

    @log('🏠 Забрали за {}с!')
    def pickup(self) -> None:
        """Самовывоз"""
        if not self.is_cooked:
            click.echo('Пицца не приготовлена. Принудительно вызван метод'
                       'bake')
            self.bake()

    @staticmethod
    def pizza_ingredients(name: str) -> list:
        """Возвращает состав пиццы

        Args:
            name (str): Название пиццы

        Returns:
            list: Список ингредиентов
        """
        return PIZZAS[name][1]

    def dict(self) -> dict:
        """Возвращает словарь с рецептом

        Returns:
            dict: Словарь с рецептом
        """
        recipe = {'Шаг 0': 'Берем основу для пиццы'}
        for i, item in enumerate(PIZZAS[self.name][1]):
            recipe[f'Шаг {i+1}'] = f'Добавляем {item}'
        recipe[f'Шаг {i+2}'] = 'Запекаем до готовности'
        return recipe

    def _valid_pizza_params(self) -> None:
        """Валидация заданных параметров пиццы"""
        if self.name not in PIZZAS:
            raise KeyError('Пиццы с таким названием в меню не обнаружено.')

        if self.size not in ['L', 'XL']:
            raise KeyError('Пиццы такого размера нет.')

    def __eq__(self, other) -> bool:
        """Сравнение 2-х инстансов Pizza

        Args:
            other (Pizza): Инстанс класса Pizza, с которым сравниваем

        Returns:
            bool: True / False
        """
        return (self.name == other.name) and (self.size == other.size)


def make_order(name: str, size: str, delivery: bool) -> None:
    """Готовит и доставляет пиццу

    Args:
        name (str): Название пиццы
        size (str): Размер пиццы
        delivery (bool): Флаг доставки:
            True -> доставка
            False -> самовывоз
    """
    try:
        pizza = Pizza(name, size)
    except KeyError:
        # mypy ругается на строку ниже, хотя аттрибут существует
        message = sys.exc_info()[1].args[0]
        print(message)
        if message == 'Пиццы с таким названием в меню не обнаружено.':
            name = input('Пожалуйста, введите название пиццы: ')
        elif message == 'Пиццы такого размера нет.':
            size = input('Пожалуйста введите размер (L или XL): ')
        # для корректной работы строки ниже понадобилось вынести make_order
        # в отдельную функцию (отдельно от cli)
        return make_order(name, size, delivery)

    pizza.bake()

    if delivery:
        pizza.delivery()
    else:
        pizza.pickup()


@click.group()
def cli() -> None:
    """Создает группу"""
    pass


@cli.command()
@click.argument('name', nargs=1)
@click.option('--size', default='L')
@click.option('--delivery', default=False, is_flag=True)
def order(name: str, size: str, delivery: bool) -> None:
    """Вызывает make_order

    Args:
        name (str): Название пиццы
        size (str): Размер пиццы
        delivery (bool): Флаг доставки:
            True -> доставка
            False -> самовывоз
    """
    make_order(name, size, delivery)


@cli.command()
def menu() -> None:
    """Выводит меню"""
    for name in PIZZAS:
        ingredients = ', '.join(Pizza.pizza_ingredients(name))
        click.echo(f'- {name} {PIZZAS[name][0]}: {ingredients}')


if __name__ == '__main__':
    cli()
