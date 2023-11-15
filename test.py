import cli
import pytest
from click.testing import CliRunner
import re


@pytest.mark.parametrize(
        'input, expected_result',
        [
            (['Margherita'],
             '🍳 Приготовили за с!\n'
             '🏠 Забрали за с!\n'),
            (['Margherita', '--delivery'],
             '🍳 Приготовили за с!\n'
             '🛵 Доставили за с!\n'),
            (['Margherita', '--delivery', '--size=L'],
             '🍳 Приготовили за с!\n'
             '🛵 Доставили за с!\n'),
            (['Margherita', '--delivery', '--size=XL'],
             '🍳 Приготовили за с!\n'
             '🛵 Доставили за с!\n'),
            (['Pepperoni', '--size=XL'],
             '🍳 Приготовили за с!\n'
             '🏠 Забрали за с!\n'),
            (['Hawaiian', '--size=L'],
             '🍳 Приготовили за с!\n'
             '🏠 Забрали за с!\n')
        ]
)
def test_pizza_order(input, expected_result):
    runner = CliRunner()
    result = runner.invoke(cli.order, input).output

    assert re.sub(r'\d+', '', result) == re.sub(r'\d+', '', expected_result)


@pytest.mark.parametrize(
        'expected_result',
        [
            ('- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n'
             '- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n'
             '- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n')
        ]
)
def test_pizza_menu(expected_result):
    runner = CliRunner()
    result = runner.invoke(cli.menu).output

    assert result == expected_result


@pytest.mark.parametrize(
        'input, expected_result',
        [
            ([('Margherita', 'L'), ('Margherita', 'L')],
             True),
            ([('Margherita', 'L'), ('Margherita', 'XL')],
             False),
            ([('Margherita', 'XL'), ('Hawaiian', 'XL')],
             False)
        ]
)
def test_pizza_equal(input, expected_result):
    pizza1 = cli.Pizza(input[0][0], input[0][1])
    pizza2 = cli.Pizza(input[1][0], input[1][1])

    if expected_result:
        assert pizza1 == pizza2
    else:
        assert not (pizza1 == pizza2)


@pytest.mark.parametrize(
        'input, expected_result',
        [
            (['Margherita', 'L'],
             {'Шаг 0': 'Берем основу для пиццы',
              'Шаг 1': 'Добавляем tomato sauce',
              'Шаг 2': 'Добавляем mozzarella',
              'Шаг 3': 'Добавляем tomatoes',
              'Шаг 4': 'Запекаем до готовности'})
        ]
)
def test_pizza_dict(input, expected_result):
    pizza = cli.Pizza(input[0], input[1])
    result = pizza.dict()

    assert result == expected_result
