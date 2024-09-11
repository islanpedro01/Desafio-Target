class Dog:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sit(self):
        print(self.nome.title() + " is now sitting.")

    def run(self):
        print(self.nome.title() + " is now running.")


    if __name__ == '__main__':
        my_dog = Dog('willie', 6)
        print("My dog's name is " + my_dog.nome.title() + ".")
        print("My dog is " + str(my_dog.idade) + " years old.")
        my_dog.sit()
        my_dog.run()