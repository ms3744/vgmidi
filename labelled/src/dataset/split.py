import math
import random
from collections import OrderedDict

def get_pieces(annotated_mids):
    pieces = {}

    for an in annotated_mids:
        piece_id = an["id"]

        if piece_id not in pieces:
            pieces[piece_id] = []

        pieces[piece_id].append(an)

    return list(pieces.values())

def generate_data_splits(annotated_mids, test_percentage=0.1, remove_duplicates=True):
    test = []

    # Get pieces
    train = get_pieces(annotated_mids, remove_duplicates)

    # Build test set
    test_size = int(test_percentage * len(train))
    print("Train/Text Split:", len(train), test_size)

    for i in range(test_size):
        p = train.pop(random.randint(0, len(train) - 1))
        test.append(p)

    return train, test