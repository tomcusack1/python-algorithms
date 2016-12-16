from .Graph import Graph


def knight_graph(board_size):
    graph = Graph()
    for row in range(board_size):
        for column in range(board_size):
            node_id = position_to_node_id(row, column, board_size)
            new_positions = generate_legal_moves(row, column, board_size)
            for edge in new_positions:
                id = position_to_node_id(edge[0], edge[1], board_size)
                graph.add_edge(node_id, id)
    return graph


def position_to_node_id(row, column, board_size):
    return (row * board_size) + column


def generate_legal_moves(x, y, board_size):
    new_moves = []
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                    (1, -2), (1, 2), (2, -1), (2, 2)]
    for i in move_offsets:
        new_x = x + i[0]
        new_y = y + i[1]
        if legal_coordinate(new_x, board_size) and legal_coordinate(new_y, board_size):
            new_moves.append((new_x, new_y))
    return new_moves


def legal_coordinate(x, board_size):
    if x >= 0 and x < board_size:
        return True
    else:
        return False


def knight_tour(n, path, u, limit):
    u.set_colour('gray')
    path.append(u)
    if n < limit:
        neighbour_list = list(u.get_connections())
        i = 0
        done = False
        while i < len(neighbour_list) and not done:
            if neighbour_list[i].get_colour() == 'white':
                done = knight_tour(n+1, path, neighbour_list[i], limit)
            i += 1

        if not done:
            path.pop()
            u.set_colour('white')
    else:
        done = True
    return done
