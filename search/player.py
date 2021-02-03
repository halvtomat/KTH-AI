#!/usr/bin/env python3
import random
import math

from fishing_game_core.game_tree import Node
from fishing_game_core.player_utils import PlayerController
from fishing_game_core.shared import ACTION_TO_STR


class PlayerControllerHuman(PlayerController):
    def player_loop(self):
        """
        Function that generates the loop of the game. In each iteration
        the human plays through the keyboard and send
        this to the game through the sender. Then it receives an
        update of the game through receiver, with this it computes the
        next movement.
        :return:
        """

        while True:
            # send message to game that you are ready
            msg = self.receiver()
            if msg["game_over"]:
                return


class PlayerControllerMinimax(PlayerController):

    def __init__(self):
        super(PlayerControllerMinimax, self).__init__()

    def player_loop(self):
        """
        Main loop for the minimax next move search.
        :return:
        """

        # Generate game tree object
        first_msg = self.receiver()
        # Initialize your minimax model
        model = self.initialize_model(initial_data=first_msg)

        while True:
            msg = self.receiver()

            # Create the root node of the game tree
            node = Node(message=msg, player=0)

            # Possible next moves: "stay", "left", "right", "up", "down"
            best_move = self.search_best_next_move(
                model=model, initial_tree_node=node)

            # Execute next action
            self.sender({"action": best_move, "search_time": None})

    def initialize_model(self, initial_data):
        
        """
        Initialize your minimax model 
        :param initial_data: Game data for initializing minimax model
        :type initial_data: dict
        :return: Minimax model
        :rtype: object

        Sample initial data:
        { 'fish0': {'score': 11, 'type': 3}, 
          'fish1': {'score': 2, 'type': 1}, 
          ...
          'fish5': {'score': -10, 'type': 4},
          'game_over': False }

        Please note that the number of fishes and their types is not fixed between test cases.
        """
        # EDIT THIS METHOD TO RETURN A MINIMAX MODEL ###
        return None

    def search_best_next_move(self, model, initial_tree_node):
        """
        Use your minimax model to find best possible next move for player 0 (green boat)
        :param model: Minimax model
        :type model: object
        :param initial_tree_node: Initial game tree node 
        :type initial_tree_node: game_tree.Node 
            (see the Node class in game_tree.py for more information!)
        :return: either "stay", "left", "right", "up" or "down"
        :rtype: str
        """

        # EDIT THIS METHOD TO RETURN BEST NEXT POSSIBLE MODE FROM MINIMAX MODEL ###
        
        # NOTE: Don't forget to initialize the children of the current node 
        #       with its compute_and_get_children() method!
        node = initial_tree_node
        children = node.compute_and_get_children()
        moves = []
        for child in children:
            moves.append(self.minimax(node=child, player=0, depth=3))

        best_move = moves.index(max(moves))
        return ACTION_TO_STR[best_move]

    def state_utility(self, node, player):
        score_p0, score_p1 = node.state.get_player_scores()
        utility = score_p0 - score_p1
        if player == 1:
            return -utility
        utility -= self.closest_fish_distance(node)
        return utility

    def minimax(self, node, player, depth):

        # if no fishes --> terminal state
        if not list(node.state.get_fish_positions().keys()) == [] or depth == 0:
            return self.state_utility(node=node, player=0)
        
        else:
            if player == 0:
                bestpossible = -math.inf
                for child in node.compute_and_get_children():
                    v = self.minimax(node=child, player=1, depth=depth-1)
                    bestpossible = max(bestpossible, v)
                return bestpossible
            
            else:
                bestpossible = math.inf
                for child in node.compute_and_get_children():
                    v = self.minimax(node=child, player=0, depth=depth-1)
                    bestpossible = min(bestpossible, v)
                return bestpossible

    def closest_fish_distance(self, node):
        dist = []
        hooks = node.state.get_hook_positions()
        for fish in list(node.state.get_fish_positions().values()):
            dist.append(self.fish_hook_distance(hooks[0], fish))
        return min(dist)

    def fish_hook_distance(self, hook, fish):
        return math.sqrt(math.pow(hook[0] - fish[0], 2) + math.pow(hook[1] - fish[1], 2))