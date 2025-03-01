from abc import abstractmethod


class Group:
    pupils = True
    school_number = 1
    director = 'Marivanna'

    def __init__(self, title, pupil_count, group_leader):
        self.title = title
        self.pupil_count = pupil_count
        self.group_leader = group_leader

    def study(self):
        print('Im studing')

    @abstractmethod
    def move(self):
        pass


class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    building_section = 'Primary building'

    def __init__(self, title, pupil_count, group_leader, specialisation):
        super().__init__(title, pupil_count, group_leader)
        self.specialisation = specialisation

    def move(self):
        print('Runing fast')


class MidleGroup(Group):
    max_age = 15
    min_age = 10


class HighGroup(Group):
    max_age = 18
    min_age = 14

    def move(self):
        print('Walking slowly')


first_a = PrimaryGroup('First A', 20, 'Galina Blanka', specialisation='Biology')
eleven_a = HighGroup('Eleven A', 22, 'GA')
six_a = MidleGroup('Six A', 22, 'DN')

print(first_a.building_section)
first_a.study()
eleven_a.move()
print(six_a.group_leader)
print(first_a.specialisation)
