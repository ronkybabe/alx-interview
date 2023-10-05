def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n  # Initialize a list to keep track of visited boxes
    visited[0] = True  # The first box is unlocked initially
    queue = [0]  # Initialize a queue for BFS with the first box

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)  # Check if all boxes have been visited


# Example usage:
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True
