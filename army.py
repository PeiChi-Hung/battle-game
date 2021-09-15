"""
Create abstract class 'Fighter' and class 'Soldier', 'Archer', 'Cavalry' which are the child class of Fighter.
"""
__author__ = "Pei-Chi Hung"

from abc import ABC, abstractmethod
from stack_adt import ArrayStack
from queue_adt import CircularQueue

class Fighter(ABC):
    """
    The class 'Fighter' includes function that indicates whether a fighter is alive, how many lives has a fighter lost,
    how much experience has a fighter gain and its experience status. The abstract methods are passed to its child
    classes as they have different lives, experience and cost.
    """

    def __init__(self, life: int, experience: int) -> None:
        """
        Initial the attributes of the class
        :pre: life and experience must be larger or equal to 0
        :post: no postcondition
        :raise Assertion: if either of life or experience is less than 0
        :complexity: Best and worst are both O(1)
        """
        # check life or experience is less than 0
        assert life >= 0, "life cannot be less than 0"
        assert experience >= 0, "experience cannot be less than 0"
        self.life = life
        self.experience = experience

    def is_alive(self) -> bool:
        """
        Check whether a fighter is still alive
        :pre: no precondition
        :post: return True or False
        :complexity: Best and worst case are both O(1)
        """
        if self.life > 0:
            return True
        return False

    def lose_life(self, lost_life: int) -> None:
        """
        Decrease the life of the unit by the amount indicated by lost life
        :raise assertion: if lost_life is larger than 0
        :pre: lost life must be larger or equal to 0
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        assert lost_life >= 0, "lost life cannot be smaller than 0"
        self.life = self.life - lost_life

    def get_life(self) -> int:
        """
        Return the fighter's life
        :pre: no precondition
        :post: return life of the fighter as integer
        :complexity: Best and worst case are both O(1)
        """
        return self.life

    def gain_experience(self, gained_experience: int) -> None:
        """
        Increase the experience of the unit by the amount indicated by gained experience
        :pre: gain_experience must be larger or equal to 0
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        assert gained_experience >= 0, "gained experience cannot be less than 0"
        self.experience = self.experience + gained_experience

    def get_experience(self) -> int:
        """
        Return the fighter's experience
        :pre: no precondition
        :post: return the experience of the fighter as integer
        :complexity: Best case and worst case are both O(1)
        """
        return self.experience

    @abstractmethod
    def get_speed(self) -> int:
        """
        Abstract method - Return the speed of the unit
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        pass

    @abstractmethod
    def get_cost(self) -> int:
        """
        Abstract method - Return the cost of the unit
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        pass

    @abstractmethod
    def get_attack_damage(self) -> int:
        """
        Abstract method - Return the amount of damage performed by the unit when it attacks
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        pass

    @abstractmethod
    def defend(self, damage: int) -> None:
        """
        Abstract method - Evaluate the life lost after defence expression and changes life accordingly
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        pass

    @abstractmethod
    def get_unit_type(self) -> str:
        """
        Abstract method - Return the unit's type
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Abstract method - Return a string indicating the type of unit, its current life and experience
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        pass


class Soldier(Fighter):
    """
    The class Soldier is the child class of 'Fighter'. It contains function which return spend, cost, attack_damage,
    defend, unit type and string
    """
    COST = 1

    def __init__(self) -> None:
        """
        Initial the life and experience of the class t0 3 and 0
        :pre: life and experience must be larger or equal to 0
        :post: no postcondition
        :complexity: Best and worst are both O(1)
        """
        Fighter.__init__(self, 3, 0)

    def get_speed(self) -> int:
        """
        Return the speed of the unit
        :pre: no precondition
        :post: return speed of Soldier unit as integer
        :complexity: Best and worst case are both O(1)
        """
        return 1 - self.get_experience()

    def get_cost(self) -> int:
        """
        Return the cost of the unit
        :pre: no precondition
        :post: return cost of the unit as integer
        :complexity: Best and worst case are both O(1)
        """
        return self.COST

    def get_attack_damage(self) -> int:
        """
        Return the amount of damage performed by the unit when it attacks
        :pre: no precondition
        :post: return attack damage as integer
        :complexity: Best and worst case are both O(1)
        """
        return self.get_experience() + 1

    def defend(self, damage: int) -> None:
        """
        Evaluate the life lost after defence expression and changes life accordingly
        :pre: damage must be greater or equal to 0
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        assert damage >= 0, "damage has to be greater or equal to 0"
        if damage > self.get_experience():
            self.life -= 1

    def get_unit_type(self) -> str:
        """
        Return the unit's type
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        return "Soldier"

    def __str__(self):
        """
        Return a string indicating the type of unit, its current life and experience
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        return "Soldier's life = " + str(self.life) + " and experience = " + str(self.get_experience())


class Archer(Fighter):
    """
    The class Archer is the child class of 'Fighter'. It contains function which return spend, cost, attack_damage,
    defend, unit type and string
    """
    SPEED = 3
    COST = 2

    def __init__(self):
        """
        Initial the life and experience of the class to 3 and 0
        :pre: life and experience must be larger or equal to 0
        :post: no postcondition
        :complexity: Best and worst are both O(1)
        """
        Fighter.__init__(self, 3, 0)

    def get_speed(self) -> int:
        """
        Return the speed of the unit
        :pre: no precondition
        :post: return speed of Archer unit
        :complexity: Best and worst case are both O(1)
        """
        return self.SPEED

    def get_cost(self) -> int:
        """
        Return the cost of the unit
        :pre: no precondition
        :post: return cost of the unit as integer
        :complexity: Best and worst case are both O(1)
        """
        return self.COST

    def get_attack_damage(self) -> int:
        """
        Return the amount of damage performed by the unit when it attacks
        :pre: no precondition
        :post: return attack damage as integer
        :complexity: Best and worst case are both O(1)
        """
        return 2 * self.get_experience() + 1

    def defend(self, damage: int) -> None:
        """
        Evaluate the life lost after defence expression and changes life accordingly
        :pre: damage must be greater or equal to 0
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        assert damage >= 0, "damage has to be greater or equal to 0"
        self.life -= 1

    def get_unit_type(self) -> str:
        """
        Return the unit's type
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        return "Archer"

    def __str__(self):
        """
        Return a string indicating the type of unit, its current life and experience
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        return "Archer's life = " + str(self.life) + " and experience = " + str(self.get_experience())


class Cavalry(Fighter):
    """
    The class Archer is the child class of 'Fighter'. It contains function which return spend, cost, attack_damage,
    defend, unit type and string
    """
    COST = 3

    def __init__(self):
        """
        Initial the life and experience of the class to 4 and 0
        :pre: life and experience must be larger or equal to 0
        :post: no postcondition
        :complexity: Best and worst are both O(1)
        """
        Fighter.__init__(self, 4, 0)

    def get_speed(self) -> int:
        """
        Return the speed of the unit
        :pre: no precondition
        :post: return speed of Cavalry unit as integer
        :complexity: Best and worst case are both O(1)
        """
        return 2 + self.get_experience()

    def get_cost(self) -> int:
        """
        Return the cost of the unit
        :pre: no precondition
        :post: return cost of the unit as integer
        :complexity: Best and worst case are both O(1)
        """
        return self.COST

    def get_attack_damage(self) -> int:
        """
        Return the amount of damage performed by the unit when it attacks
        :pre: no precondition
        :post: return attack damage as integer
        :complexity: Best and worst case are both O(1)
        """
        return self.get_experience() + 1

    def defend(self, damage: int) -> None:
        """
        Evaluate the life lost after defence expression and changes life accordingly
        :pre: damage must be greater or equal to 0
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        assert damage >= 0, "damage has to be greater or equal to 0"
        if damage > (self.get_experience() / 2):
            self.life -= 1

    def get_unit_type(self) -> str:
        """
        Return the unit's type
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        return "Cavalry"

    def __str__(self):
        """
        Return a string indicating the type of unit, its current life and experience
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and worst case are both O(1)
        """
        return "Cavalry's life = " + str(self.life) + " and experience = " + str(self.get_experience())


class Army():
    """
    The class Army ask for user input and use valid inputs to create an army
    """

    def __init__(self) -> None:
        """
        Initialise name and force
        """
        self.name = None
        self.force = None

    def __correct_army_given(self, soldiers: int, archers: int, cavalry: int) -> bool:
        """
        Check whether the total costs of fighter units are less or equal to the budget
        :pre: no precondition
        :post: return boolean
        :complexity: Best and worst case are O(1)
        """
        s_cost = soldiers*1
        a_cost = archers*2
        c_cost = cavalry*3

        ttl_cost = s_cost + a_cost + c_cost
        if ttl_cost <= 30:
            return True
        return False

    def __assign_army(self, name: str, sold: int, arch: int, cav: int, formation: int) -> None:
        """
        Assign fighter units in different form based on formation. If formation is 0, fighter units will be in
        stack form. If formation is 1, fighter units will be in queue form. The order of army will be soldiers, archers
        and cavalries respectively.
        :pre: no precondition
        :post: no postcondition
        :complexity: Best = worst = O(N) , where N is the number of total fighters.
        """
        self.name = name
        ttl_fighter = sold + arch + cav
        if formation == 0:
            self.force = ArrayStack(ttl_fighter)
            while cav > 0:
                self.force.push(Cavalry())
                cav -= 1
            while arch > 0:
                self.force.push(Archer())
                arch -= 1
            while sold > 0:
                self.force.push(Soldier())
                sold -= 1

        if formation == 1:
            self.force = CircularQueue(ttl_fighter)
            while sold > 0:
                self.force.append(Soldier())
                sold -= 1
            while arch > 0:
                self.force.append(Archer())
                arch -= 1
            while cav > 0:
                self.force.append(Cavalry())
                cav -= 1

    def choose_army(self, name: str, formation: int) -> None:
        """
        Ask for input repeatedly until valid inputs are given
        :pre: inputs have to be integers
        :post: no postcondition
        :complexity: Best and worst case are both O(N) because of function __assign_army, N is the number of total
        fighters
        """
        while True:
            army_input = input("Player " + name + " choose your army as S A C \n" +
                               "where S is the number of soldiers \n" +
                               "      A is the number of archers \n" +
                               "      C is the number of cavalry \n")

            army_input = army_input.split()

            # if length of the input is less than 3, ask for inputs again
            if len(army_input) != 3:
                continue

            # check if inputs are integer
            elif not army_input[0].isdigit() or not army_input[1].isdigit() or not army_input[2].isdigit():
                continue

            elif int(army_input[0]) + int(army_input[1]) + int(army_input[2]) == 0:
                continue

            elif not self.__correct_army_given(int(army_input[0]), int(army_input[1]), int(army_input[2])):
                continue

            # all conditions were met, stop asking for inputs
            break
        self.__assign_army(name, int(army_input[0]), int(army_input[1]), int(army_input[2]), formation)

    def __str__(self):
        """
        Print the status of army
        :pre: no precondition
        :post: no postcondition
        :complexity: Best and Worst are both O(1)
        """
        return str(self.force)






