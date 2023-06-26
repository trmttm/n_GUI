import unittest


class MyTestCase(unittest.TestCase):
    def test_concepts(self):
        from n_gui.button import Button
        button = Button()

        counter = 0

        def push_button(n: int = 1):
            nonlocal counter
            counter += n

        def mouse_in():
            push_button(2)

        def mouse_out():
            push_button(-2)

        button.push = lambda: push_button()
        button.push()
        self.assertEqual(counter, 1)

        button.mouse_in = mouse_in
        button.mouse_in()
        self.assertEqual(counter, 3)

        button.mouse_out = mouse_out
        button.mouse_out()
        self.assertEqual(counter, 1)


if __name__ == '__main__':
    unittest.main()
