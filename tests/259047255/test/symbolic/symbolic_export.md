# Symbolic Execution – Export Timetable

## Symbolic variables
List length n = len(entries)
Output path P

## Tree
(n == 0?)
  True  -> write header/empty output -> file exists
  False -> write each entry -> file exists and contains entries

## Path conditions
P1: n == 0 -> file exists
P2: n > 0 -> file exists + content includes entry fields

## Evidence
`tests/259047255/test/blackbox/equivalence_partitioning/test_ep_export.py`
