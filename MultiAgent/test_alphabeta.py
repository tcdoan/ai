
import alphabeta
import gamestate as game

# Test the depth limit by checking the number of nodes visited
# -- recall that minimax visits every node in the search tree,
# so if we search depth one on an empty board then minimax should
# visit each of the five open spaces
expected_node_count = 55
rootNode = game.GameState()
alphabeta.alpha_beta_search(rootNode)

print("Expected node count: {}".format(expected_node_count))
print("Your node count: {}".format(game.call_counter))

if game.call_counter == expected_node_count:
    print("That's right! Looks like your alpha-beta pruning is working!")
else:
    print("Uh oh...looks like there may be a problem.")
