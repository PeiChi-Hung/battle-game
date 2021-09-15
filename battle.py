"""
Class Battle includes functions which allows users to assign fighter units and conduct battles
"""
__author__ = "Pei-Chi Hung"

from army import Fighter, Soldier, Archer, Cavalry, Army
from stack_adt import ArrayStack
from queue_adt import CircularQueue


class Battle():
    def __conduct_combat(self, army1: Army, army2: Army, formation: int) -> int:
        """
        Conduct combat based on the formation of the two armies passed
        :pre: no precondition
        :post: return either 0, 1, 2
        :complexity: Best and worst are both O(N), where N is the len of the army
        """
        # army cannot be empty
        while len(army1.force) > 0 and len(army2.force) > 0:
            if formation == 0:
                # get the first fighter from the army stack
                fight_u1 = army1.force.pop()
                fight_u2 = army2.force.pop()

                # print(fight_u2)
                # first case: when u1 has better speed - u1 attack u2
                if fight_u1.get_speed() > fight_u2.get_speed():
                    fight_u2.defend(fight_u1.get_attack_damage())
                    # if u2 is alive after attack - u2 attack u1
                    if fight_u2.is_alive():
                        fight_u1.defend(fight_u2.get_attack_damage())
                        # if u1 is alive after attack - both alive both lose 1 life
                        if fight_u1.is_alive():
                            fight_u1.lose_life(1)
                            fight_u2.lose_life(1)
                            # if both are still alive, put pack to stack
                            if fight_u1.is_alive() and fight_u2.is_alive():
                                army1.force.push(fight_u1)
                                army2.force.push(fight_u2)
                            # if only u1 is alive
                            elif fight_u1.is_alive():
                                army1.force.push(fight_u1)
                            # if only u2 is alive
                            elif fight_u2.is_alive():
                                army2.force.push(fight_u2)
                        # if u2 kill u1, u2 gain 1 exp and put back to stack
                        else:
                            fight_u2.gain_experience(1)
                            army2.force.push(fight_u2)
                    # if u1 kill u2, u1 gain 1 exp and put back to stack
                    else:
                        fight_u1.gain_experience(1)
                        army1.force.push(fight_u1)

                # second case: when u2 has better speed - u2 attack u1
                elif fight_u2.get_speed() > fight_u1.get_speed():
                    fight_u1.defend(fight_u2.get_attack_damage())
                    # if u1 is alive after attack - u1 attack u2
                    if fight_u1.is_alive():
                        fight_u2.defend(fight_u1.get_attack_damage())
                        # if u2 is alive after attack - both alive both lose 1 life
                        if fight_u2.is_alive():
                            fight_u1.lose_life(1)
                            fight_u2.lose_life(1)
                            # if both are still alive, put pack to stack
                            if fight_u1.is_alive() and fight_u2.is_alive():
                                army1.force.push(fight_u1)
                                army2.force.push(fight_u2)
                            # if only u1 is alive
                            elif fight_u1.is_alive():
                                army1.force.push(fight_u1)
                            # if only u2 is alive
                            elif fight_u2.is_alive():
                                army2.force.push(fight_u2)
                        # if u1 kill u2, u1 gain 1 exp and put back to stack
                        else:
                            fight_u1.gain_experience(1)
                            army1.force.push(fight_u1)

                    # if u2 kill u1, u2 gain 1 exp and put back to stack
                    else:
                        fight_u2.gain_experience(1)
                        army2.force.push(fight_u2)

                # third case: u1 and u2 have the same speed
                elif fight_u1.get_speed() == fight_u2.get_speed():
                    # attack simultaneously
                    fight_u1.defend(fight_u2.get_attack_damage())
                    fight_u2.defend(fight_u1.get_attack_damage())
                    # if both alive, both lose 1 life
                    if fight_u1.is_alive() and fight_u2.is_alive():
                        fight_u1.lose_life(1)
                        fight_u2.lose_life(1)
                        # if both are still alive, put pack to stack
                        if fight_u1.is_alive() and fight_u2.is_alive():
                            army1.force.push(fight_u1)
                            army2.force.push(fight_u2)
                        # if only u1 is alive
                        elif fight_u1.is_alive():
                            army1.force.push(fight_u1)
                        # if only u2 is alive
                        elif fight_u2.is_alive():
                            army2.force.push(fight_u2)
                    # if only u1 is alive - u1 gain exp and get push back to stack
                    elif fight_u1.is_alive():
                        fight_u1.gain_experience(1)
                        army1.force.push(fight_u1)
                    # if only u2 is alive - u2 gain exp and get push back to stack
                    elif fight_u2.is_alive():
                        fight_u2.gain_experience(1)
                        army2.force.push(fight_u2)

            if formation == 1:
                # get the first fighter from the army queue
                fight_u1 = army1.force.serve()
                fight_u2 = army2.force.serve()

                # print(fight_u2)
                # first case: when u1 has better speed - u1 attack u2
                if fight_u1.get_speed() > fight_u2.get_speed():
                    fight_u2.defend(fight_u1.get_attack_damage())
                    # if u2 is alive after attack - u2 attack u1
                    if fight_u2.is_alive():
                        fight_u1.defend(fight_u2.get_attack_damage())
                        # if u1 is alive after attack - both alive both lose 1 life
                        if fight_u1.is_alive():
                            fight_u1.lose_life(1)
                            fight_u2.lose_life(1)
                            # if both are still alive, put pack to stack
                            if fight_u1.is_alive() and fight_u2.is_alive():
                                army1.force.append(fight_u1)
                                army2.force.append(fight_u2)
                            # if only u1 is alive
                            elif fight_u1.is_alive():
                                army1.force.append(fight_u1)
                            # if only u2 is alive
                            elif fight_u2.is_alive():
                                army2.force.append(fight_u2)
                        # if u2 kill u1, u2 gain 1 exp and put back to stack
                        else:
                            fight_u2.gain_experience(1)
                            army2.force.append(fight_u2)
                    # if u1 kill u2, u1 gain 1 exp and put back to stack
                    else:
                        fight_u1.gain_experience(1)
                        army1.force.append(fight_u1)

                # second case: when u2 has better speed - u2 attack u1
                elif fight_u2.get_speed() > fight_u1.get_speed():
                    fight_u1.defend(fight_u2.get_attack_damage())
                    # if u1 is alive after attack - u1 attack u2
                    if fight_u1.is_alive():
                        fight_u2.defend(fight_u1.get_attack_damage())
                        # if u2 is alive after attack - both alive both lose 1 life
                        if fight_u2.is_alive():
                            fight_u1.lose_life(1)
                            fight_u2.lose_life(1)
                            # if both are still alive, put pack to stack
                            if fight_u1.is_alive() and fight_u2.is_alive():
                                army1.force.append(fight_u1)
                                army2.force.append(fight_u2)
                            # if only u1 is alive
                            elif fight_u1.is_alive():
                                army1.force.append(fight_u1)
                            # if only u2 is alive
                            elif fight_u2.is_alive():
                                army2.force.append(fight_u2)
                        # if u1 kill u2, u1 gain 1 exp and put back to stack
                        else:
                            fight_u1.gain_experience(1)
                            army1.force.append(fight_u1)

                    # if u2 kill u1, u2 gain 1 exp and put back to stack
                    else:
                        fight_u2.gain_experience(1)
                        army2.force.append(fight_u2)

                # third case: u1 and u2 have the same speed
                elif fight_u1.get_speed() == fight_u2.get_speed():
                    # attack simultaneously
                    fight_u1.defend(fight_u2.get_attack_damage())
                    fight_u2.defend(fight_u1.get_attack_damage())
                    # if both alive, both lose 1 life
                    if fight_u1.is_alive() and fight_u2.is_alive():
                        fight_u1.lose_life(1)
                        fight_u2.lose_life(1)
                        # if both are still alive, put pack to stack
                        if fight_u1.is_alive() and fight_u2.is_alive():
                            army1.force.append(fight_u1)
                            army2.force.append(fight_u2)
                        # if only u1 is alive
                        elif fight_u1.is_alive():
                            army1.force.append(fight_u1)
                        # if only u2 is alive
                        elif fight_u2.is_alive():
                            army2.force.append(fight_u2)
                    # if only u1 is alive - u1 gain exp and get push back to stack
                    elif fight_u1.is_alive():
                        fight_u1.gain_experience(1)
                        army1.force.append(fight_u1)
                    # if only u2 is alive - u2 gain exp and get push back to stack
                    elif fight_u2.is_alive():
                        fight_u2.gain_experience(1)
                        army2.force.append(fight_u2)

        if len(army1.force) == 0 and len(army2.force) == 0:
            return 0
        elif len(army1.force) == 0:
            return 2
        elif len(army2.force) == 0:
            return 1

    def gladiatorial_combat(self, player_one: str, player_two: str) -> int:
        """
        Reads and creates an army for each player, set those armies in stack formation and calls method
        __conduct_combat and returns the winner
        :pre: no precondition
        :post: return integer
        :complexity: Best and worst case are both O(N)
        function choose_army has complexity of O(N)
        function __conduct_combat has complexity of O(N)
        O(N) + O(N) = O(N)
        """
        army1 = Army()
        army2 = Army()
        army1.choose_army(player_one, 0)
        army2.choose_army(player_two, 0)
        return self.__conduct_combat(army1, army2, 0)

    def fairer_combat(self, player_one: str, player_two: str) -> int:
        """
        Reads and creates an army for each player, set those armies in queue formation and calls method
        __conduct_combat and returns the winner
        :pre: no precondition
        :post: return integer
        :complexity: Best and worst case are both O(N)
        function choose_army has complexity of O(N)
        function __conduct_combat has complexity of O(N)
        O(N) + O(N) = O(N)
        """
        army1 = Army()
        army2 = Army()
        army1.choose_army(player_one, 1)
        army2.choose_army(player_two, 1)
        return self.__conduct_combat(army1, army2, 1)



