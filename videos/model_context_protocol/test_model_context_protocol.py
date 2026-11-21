import inspect
from pathlib import Path
import re
import sys
from manim import Scene, config
import pytest

# Ensure video package directory is on sys.path for direct or root test runs
VIDEO_DIR = Path(__file__).resolve().parent
if str(VIDEO_DIR) not in sys.path:
    sys.path.insert(0, str(VIDEO_DIR))

import model_context_protocol
from model_context_protocol import ModelContextProtocol, MCPFlow


def test_scene_class_exists():
    """Verify ModelContextProtocol and backwards-compatible MCPFlow exist and subclass manim.Scene."""
    assert hasattr(model_context_protocol, "ModelContextProtocol")
    assert issubclass(ModelContextProtocol, Scene)
    assert hasattr(model_context_protocol, "MCPFlow")
    assert issubclass(MCPFlow, Scene)
    assert MCPFlow is ModelContextProtocol


def test_no_latex_usage():
    """Verify MathTex and Tex are not used in model_context_protocol.py (LaTeX is not installed)."""
    source = inspect.getsource(model_context_protocol)
    assert not re.search(r"\bMathTex\b", source), "MathTex found in model_context_protocol.py; LaTeX is not installed!"
    assert not re.search(r"\bTex\b", source), "Tex found in model_context_protocol.py; LaTeX is not installed!"


def test_scene_render_low_quality(tmp_path):
    """Verify that ModelContextProtocol renders and duration is within an optimal explainer range (30-90s)."""
    config.quality = "low_quality"
    config.media_dir = str(tmp_path / "media")
    config.verbosity = "WARNING"

    test_scene = ModelContextProtocol()
    test_scene.render()

    total_time = test_scene.renderer.time
    # User confirmed no strict 45s cap; quality and clarity come first (supports 30 to 90 seconds)
    assert 30.0 <= total_time <= 90.0, f"Expected duration between 30 and 90s, got {total_time:.1f}s"
