class Snowflake:
    def __init__(self, change_size: int, change_shape: str):
        self.change_size = change_size
        self.change_shape = change_shape
    def info(self):
        return f"Size: {self.change_size}\nShape: {self.change_shape}"
    def edit_change_size(self, new_size):
        print(f"Новый диаметр снежинки: {new_size}")
        self.change_size = new_size
    def edit_change_shape(self, new_shape):
        print(f"Новая форма снежинки: {new_shape}")
        self.change_shape = new_shape

snow_flake = Snowflake(20, 'round')

print(snow_flake.info())
print("Menu")
while True:
    command = input(""" 
1 - показать информацию о снежинке
2 - изменить диаметр
3 - изменить форму 
4 - выход
""")
    if command == "1":
        print(snow_flake.info())
    elif command == "2":
        new_size = int(input("Введите диаметр снежинки: "))
        snow_flake.edit_change_size(new_size)
    elif command == "3":
        new_shape = str(input("Введите форму снежинки: "))
        snow_flake.edit_change_shape(new_shape)
    elif command == "4":
        print("До новых встреч!")
        break

