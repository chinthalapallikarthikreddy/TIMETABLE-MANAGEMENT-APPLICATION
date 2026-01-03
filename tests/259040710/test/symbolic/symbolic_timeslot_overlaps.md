# Symbolic Execution – Next Class Selection

## Symbolic variables
Let the entries list contain E1..En with (day_i, start_i, end_i).
Input: current_day = D, current_time = T.

## Decision
Select the entry with:
- day_i == D
- start_i >= T
- minimum start_i among candidates

## Paths
P1: No candidate exists -> return None
P2: One candidate -> return that entry
P3: Multiple candidates -> return earliest start time candidate

## Evidence
Black-box EP tests show P1/P2/P3:
`tests/259040710/test/blackbox/equivalence_partitioning/test_ep_next_class.py`

              (d1 != d2?)
             /          \
         True            False
      return False     (e1 <= s2 OR s1 >= e2?)
                       /                 \
                    True                 False
                 return False          return True
