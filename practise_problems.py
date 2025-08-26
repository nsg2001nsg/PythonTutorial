from collections import Counter


def smallest_path(directions):
    direction_count = Counter(directions)

    east = direction_count['E']
    north = direction_count['N']
    south = direction_count['S']
    west = direction_count['W']

    if north > south:
        north -= south
        south = 0
    else:
        south -= north
        north = 0

    if east > west:
        east -= west
        west = 0
    else:
        west -= east
        east = 0

    if north == south == west == east == 0:
        return 'Sad Alice'

    res = f"{'E' * east}{'N' * north}{'S' * south}{'W' * west}"
    return res


test_cases = [
    'NSWE',         # Expected: "Sad Alice"
    'NNNSS',        # Expected: "N"
    'EEWWWE',       # Expected: "E" (E=3, W=3 → remaining E=0, W=0, total E-W=0? Actually Sad Alice, correct)
    'SSW',          # Expected: "SSW"
    'NNNN',         # Expected: "NNNN"
    'NSEWNSEWNSEW', # Expected: "Sad Alice"
    'NNSS',         # Expected: "Sad Alice"
    'SSEWW'         # Expected: "SSWW"
]

for dire in test_cases:
    print(f"Input: {dire} → Output: {smallest_path(dire)}")