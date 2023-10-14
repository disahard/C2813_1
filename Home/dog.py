class dog:
    def __init__(self, name:str, age:float, breed:str, gender:str):
        self.Name:str = name
        self.Age = age
        self.Breed = breed
        self.Gender = gender
    def __bool__(self):
        return self.Name != None and\
                self.Age != None and\
                self.Breed != None and\
                self.Gender != None
    def __len__(self):
        return len(self.Name)
    def __str__(self):
        return (f"Name - {self.Name}\n"
                f"Age - {self.Age}\n"
                f"Breed - {self.Breed}\n"
                f"Gender - {self.Gender}")
