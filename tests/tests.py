import unittest


class MyTestCase(unittest.TestCase):
    def test_concepts(self):
        from n_gui.widgets.button import Button
        button = Button('btn_01')

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

        self.assertEqual(button.name, 'Button_btn_01')

    def test_tree(self):
        from n_gui.widgets.tree import Tree
        tree = Tree()
        tree.select_row(0)
        self.assertEqual(tree.selected_rows, (0,))

        tree.select_rows((1, 3))
        self.assertEqual(tree.selected_rows, (0, 1, 3))


if __name__ == '__main__':
    unittest.main()
