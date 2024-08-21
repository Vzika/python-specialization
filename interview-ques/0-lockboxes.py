def canUnlockAll(boxes: list) -> bool:
    for box in boxes:
        for num in box:
            if not isinstance(num, int) or num < 0:
                return False  # Return False if invalid key found
    
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is always unlocked
    keys = list(boxes[0])  # Start with the keys from the first box

    for key in keys:
        if key < len(boxes) and not unlocked[key]:
            unlocked[key] = True  # Unlock the box
            for new_key in boxes[key]:
                if new_key not in keys:
                    keys.append(new_key)  # Add new keys only if they are not already in the list

    return all(unlocked)  # Return True if all boxes are unlocked

boxes = [[3, 5, 2], [5], [0, 1], []]

print(canUnlockAll(boxes))  # Should return True or False

