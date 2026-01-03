# Symbolic Execution – Clash Validation

## Goal
Detect clashes when inserting a new timetable entry N against existing entry E.

## Symbolic variables
dE, dN: day  
sE, eE: start/end time of E  
sN, eN: start/end time of N  
lE, lN: lecturer ids  
rE, rN: room ids  
Precondition: sE<eE and sN<eN

## Overlap predicate
Overlap = (dE == dN) AND (eE > sN) AND (sE < eN)

## Symbolic execution tree
Overlap?
  False -> No clash
  True  -> (lE == lN?) and (rE == rN?)
            (F,F) -> No clash
            (T,F) -> Lecturer clash
            (F,T) -> Room clash
            (T,T) -> Lecturer + Room clash

## Path conditions
P1: NOT Overlap -> no errors  
P2: Overlap AND lE!=lN AND rE!=rN -> no errors  
P3: Overlap AND lE==lN AND rE!=rN -> lecturer error  
P4: Overlap AND lE!=lN AND rE==rN -> room error  
P5: Overlap AND lE==lN AND rE==rN -> both errors  

## Derived test evidence
`tests/249058832/test/whitebox/path_coverage/test_path_clash_combinations.py`
