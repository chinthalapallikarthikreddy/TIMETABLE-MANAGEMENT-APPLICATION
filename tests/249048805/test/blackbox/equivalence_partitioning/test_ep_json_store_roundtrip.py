import os
from storage.data_context import DataContext
from storage.json_store import JsonStore
from tests.test_utils.factories import make_course, make_lecturer

# Black-box: EP for persistence (save/load)

def test_json_store_save_load_roundtrip(tmp_path):
    store_path = os.path.join(tmp_path, "store.json")

    ctx = DataContext()
    ctx.courses["C001"] = make_course("C001")
    ctx.lecturers["L001"] = make_lecturer("L001")

    store = JsonStore(store_path)
    store.save(ctx)

    loaded = store.load()
    assert "C001" in loaded.courses
    assert "L001" in loaded.lecturers
