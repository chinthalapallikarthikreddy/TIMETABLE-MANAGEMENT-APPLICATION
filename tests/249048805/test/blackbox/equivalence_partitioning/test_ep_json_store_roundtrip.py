import os
import importlib

from storage.data_context import DataContext
from storage.json_store import JsonStore
from tests.test_utils.factories import make_course, make_lecturer


def _get_model_factory():
    """
    Your JsonStore.load requires (ctx, model_factory).
    This helper tries common locations/names and returns an instance.
    If your project uses a different class name, update the candidates list.
    """
    candidates = [
        ("models.model_factory", "ModelFactory"),
        ("storage.model_factory", "ModelFactory"),
        ("services.model_factory", "ModelFactory"),
        ("models.factory", "ModelFactory"),
    ]
    for module_name, cls_name in candidates:
        try:
            mod = importlib.import_module(module_name)
            return getattr(mod, cls_name)()
        except Exception:
            continue

    raise RuntimeError(
        "ModelFactory not found. Search in src for 'ModelFactory' and add its module path to candidates."
    )


def test_json_store_save_load_roundtrip(tmp_path):
    store_path = os.path.join(tmp_path, "store.json")

    ctx = DataContext()
    ctx.courses["C001"] = make_course("C001")
    ctx.lecturers["L001"] = make_lecturer("L001")

    store = JsonStore(store_path)
    store.save(ctx)

    loaded_ctx = DataContext()
    model_factory = _get_model_factory()

    # Your signature: load(ctx, model_factory)
    store.load(loaded_ctx, model_factory)

    assert "C001" in loaded_ctx.courses
    assert "L001" in loaded_ctx.lecturers
