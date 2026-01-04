# Symbolic Execution – Timeslot.overlaps(other)

## Function under test
`Timeslot.overlaps(other)`

## Symbolic variables
d1=self.day, d2=other.day
s1=self.start_time, e1=self.end_time
s2=other.start_time, e2=other.end_time
Assume valid time ranges: s1<e1 and s2<e2

## Symbolic execution tree
(d1 != d2?)
  True  -> return False
  False -> (e1 <= s2 OR s1 >= e2?)
            True  -> return False
            False -> return True

## Path conditions
P1: d1 != d2 -> False
P2: d1==d2 AND (e1<=s2 OR s1>=e2) -> False
P3: d1==d2 AND (e1>s2 AND s1<e2) -> True

## Derived tests
P1: Monday vs Tuesday -> False
P2: [09:00–10:00] vs [10:00–11:00] -> False
P3: [09:00–10:00] vs [09:30–10:30] -> True

## Evidence
`tests/259048805/test/whitebox/path_coverage/test_path_timeslot_overlaps.py`
