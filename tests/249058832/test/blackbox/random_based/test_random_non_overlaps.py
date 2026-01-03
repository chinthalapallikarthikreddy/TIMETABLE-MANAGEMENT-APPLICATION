import random
from tests.test_utils.factories import make_entry
from services.clash_service import ClashService

# Black-box: Random-based testing (random non-overlapping slots should yield no clash)

def test_random_non_overlapping_should_not_clash():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]

    non_overlaps = [("10:00", "11:00"), ("11:00", "12:00"), ("13:00", "14:00")]
    for _ in range(20):
        start, end = random.choice(non_overlaps)
        new = make_entry("C002", "L001", "R101", "Monday", start, end)
        errors = ClashService.validate_no_clashes(existing, new)
        assert errors == []
