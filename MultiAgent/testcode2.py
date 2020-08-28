import minimax
import gamestate as game

# Test the depth limit by checking the number of nodes visited
# -- recall that minimax visits every node in the search tree,
# so if we search depth one on an empty board then minimax should
# visit each of the five open spaces
depth_limit = 1
expected_node_count = 5
rootNode = game.GameState()
_ = minimax.minimax_decision(rootNode, depth_limit)

print("Expected node count: {}".format(expected_node_count))
print("Your node count: {}".format(game.call_counter))

if game.call_counter == expected_node_count:
    print("That's right! Looks like your depth limit is working!")
else:
    print("Uh oh...looks like there may be a problem.")
