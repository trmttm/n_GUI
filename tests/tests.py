import unittest


class MyTestCase(unittest.TestCase):
    def test_concepts(self):
        from n_gui.button import Button
        button = Button()

        counter = 0

        def upon_push_button(n: int = 1):
            nonlocal counter
            counter += n

        def upon_mouse_in():
            upon_push_button(2)

        def upon_mouse_out():
            upon_push_button(-2)

        button.push = lambda: upon_push_button()
        button.push()
        self.assertEqual(counter, 1)

        button.mouse_in = upon_mouse_in
        button.mouse_in()
        self.assertEqual(counter, 3)

        button.mouse_out = upon_mouse_out
        button.mouse_out()
        self.assertEqual(counter, 1)


if __name__ == '__main__':
    unittest.main()
