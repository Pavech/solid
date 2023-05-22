class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f' {self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self):
    #     pass
    #
    # def load(self):
    #     pass
    #
    # def load_from_web(self):
    #     pass


j = Journal()
j.add_entry("I play today")
j.add_entry('I ate a bug')
print(f'Journal entries:\n{j}')
