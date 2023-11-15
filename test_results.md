`python -m pytest -v test.py`
=================================================================================================== test session starts ====================================================================================================
platform darwin -- Python 3.11.5, pytest-7.4.3, pluggy-1.3.0 -- /opt/homebrew/Caskroom/miniconda/base/envs/base_env/bin/python
cachedir: .pytest_cache
rootdir: /Users/max/aaa-final-task
plugins: cov-4.1.0
collected 11 items                                                                                                                                                                                                         

test.py::test_pizza_order[input0-\U0001f373 \u041f\u0440\u0438\u0433\u043e\u0442\u043e\u0432\u0438\u043b\u0438 \u0437\u0430 \u0441!\n\U0001f3e0 \u0417\u0430\u0431\u0440\u0430\u043b\u0438 \u0437\u0430 \u0441!\n] PASSED [  9%]
test.py::test_pizza_order[input1-\U0001f373 \u041f\u0440\u0438\u0433\u043e\u0442\u043e\u0432\u0438\u043b\u0438 \u0437\u0430 \u0441!\n\U0001f6f5 \u0414\u043e\u0441\u0442\u0430\u0432\u0438\u043b\u0438 \u0437\u0430 \u0441!\n] PASSED [ 18%]
test.py::test_pizza_order[input2-\U0001f373 \u041f\u0440\u0438\u0433\u043e\u0442\u043e\u0432\u0438\u043b\u0438 \u0437\u0430 \u0441!\n\U0001f6f5 \u0414\u043e\u0441\u0442\u0430\u0432\u0438\u043b\u0438 \u0437\u0430 \u0441!\n] PASSED [ 27%]
test.py::test_pizza_order[input3-\U0001f373 \u041f\u0440\u0438\u0433\u043e\u0442\u043e\u0432\u0438\u043b\u0438 \u0437\u0430 \u0441!\n\U0001f6f5 \u0414\u043e\u0441\u0442\u0430\u0432\u0438\u043b\u0438 \u0437\u0430 \u0441!\n] PASSED [ 36%]
test.py::test_pizza_order[input4-\U0001f373 \u041f\u0440\u0438\u0433\u043e\u0442\u043e\u0432\u0438\u043b\u0438 \u0437\u0430 \u0441!\n\U0001f3e0 \u0417\u0430\u0431\u0440\u0430\u043b\u0438 \u0437\u0430 \u0441!\n] PASSED [ 45%]
test.py::test_pizza_order[input5-\U0001f373 \u041f\u0440\u0438\u0433\u043e\u0442\u043e\u0432\u0438\u043b\u0438 \u0437\u0430 \u0441!\n\U0001f3e0 \u0417\u0430\u0431\u0440\u0430\u043b\u0438 \u0437\u0430 \u0441!\n] PASSED [ 54%]
test.py::test_pizza_menu[- Margherita \U0001f9c0: tomato sauce, mozzarella, tomatoes\n- Pepperoni \U0001f355: tomato sauce, mozzarella, pepperoni\n- Hawaiian \U0001f34d: tomato sauce, mozzarella, chicken, pineapples\n] PASSED [ 63%]
test.py::test_pizza_equal[input0-True] PASSED                                                                                                                                                                        [ 72%]
test.py::test_pizza_equal[input1-False] PASSED                                                                                                                                                                       [ 81%]
test.py::test_pizza_equal[input2-False] PASSED                                                                                                                                                                       [ 90%]
test.py::test_pizza_dict[input0-expected_result0] PASSED                                                                                                                                                             [100%]

==================================================================================================== 11 passed in 0.02s ====================================================================================================