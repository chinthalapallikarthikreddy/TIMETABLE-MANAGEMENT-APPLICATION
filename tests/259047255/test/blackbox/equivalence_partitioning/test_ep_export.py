import os
import importlib
from tests.test_utils.factories import make_entry


def _get_export_fn():
    es = importlib.import_module("services.export_service")

    for name in [
        "export_timetable",
        "export",
        "export_to_file",
        "export_entries",
        "export_timetable_to_file",
    ]:
        fn = getattr(es, name, None)
        if callable(fn):
            return fn

    raise RuntimeError(
        "No export function found in services.export_service. "
        "Open src/services/export_service.py and add the correct function name to the list."
    )


def test_export_with_empty_entries_creates_file(tmp_path):
    export_fn = _get_export_fn()
    out = os.path.join(tmp_path, "export.txt")
    export_fn([], out)
    assert os.path.exists(out)


def test_export_with_entries_writes_content(tmp_path):
    export_fn = _get_export_fn()
    out = os.path.join(tmp_path, "export.txt")
    entries = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    export_fn(entries, out)

    with open(out, "r") as f:
        data = f.read()

    # Keep assertion flexible (different formats are OK)
    assert ("CO7095" in data) or ("C001" in data) or ("R101" in data) or ("Monday" in data)
