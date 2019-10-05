# Exercises


class Library:
    def __init__(self, book, shelf):
        self.shelf = shelf
        self.book = book


library1 = Library(300, 45)


class science_section(Library):
    def __init__(self, name, book, shelf):
        super().__init__(book, shelf)
        self.name = name

    def print_content(self):
        print(
            "Sience Section Name:", self.name,
            "\nSience Section Books:", self.book,
            "\nSience Section Shelfs:", self.shelf
        )


ss1 = science_section("Physics books", 300, 45)
ss1.print_content()

ss1.book = 20
ss1.shelf = 4
ss1.print_content()
