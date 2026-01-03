import pytest
from tests.test_utils.factories import make_entry
from services.clash_service import ClashService

# Black-box: BVA around overlap boundaries (end==start should be NO overlap)

def test_boundary_end_equals_start_no_overlap():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L001", "R101", "Monday", "10:00", "11:00")  # boundary
    errors = ClashService.validate_no_clashes(existing, new)
    assert errors == []
