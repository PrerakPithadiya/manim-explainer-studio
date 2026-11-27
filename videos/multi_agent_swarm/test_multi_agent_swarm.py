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

import multi_agent_swarm
from multi_agent_swarm import MultiAgentSwarm, SwarmOrchestration


def test_scene_class_exists():
    """Verify MultiAgentSwarm and alias SwarmOrchestration exist and subclass manim.Scene."""
    assert hasattr(multi_agent_swarm, "MultiAgentSwarm")
    assert issubclass(MultiAgentSwarm, Scene)
    assert hasattr(multi_agent_swarm, "SwarmOrchestration")
    assert issubclass(SwarmOrchestration, Scene)
    assert SwarmOrchestration is MultiAgentSwarm


def test_no_latex_usage():
    """Verify MathTex and Tex are not used in multi_agent_swarm.py (zero LaTeX runtime dependency)."""
    source = inspect.getsource(multi_agent_swarm)
    assert not re.search(r"\bMathTex\b", source), "MathTex found in multi_agent_swarm.py; use Pango Text instead!"
    assert not re.search(r"\bTex\b", source), "Tex found in multi_agent_swarm.py; use Pango Text instead!"


def test_scene_structure_methods_exist():
    """Verify modular scene phases are defined on MultiAgentSwarm."""
    expected_methods = [
        "play_scene_1_bottleneck",
        "play_scene_2_topology",
        "play_scene_3_event_bus_dag",
        "play_scene_4_self_correction",
        "play_scene_5_consensus_outro",
    ]
    for method_name in expected_methods:
        assert hasattr(MultiAgentSwarm, method_name), f"Missing scene phase method: {method_name}"
        assert callable(getattr(MultiAgentSwarm, method_name))


def test_scene_render_low_quality_and_duration(tmp_path):
    """Verify MultiAgentSwarm renders cleanly and meets the >= 120.0s full 2-minute requirement."""
    config.quality = "low_quality"
    config.media_dir = str(tmp_path / "media")
    config.verbosity = "WARNING"

    test_scene = MultiAgentSwarm()
    test_scene.render()

    total_time = test_scene.renderer.time
    assert total_time >= 120.0, f"Expected duration >= 120.0s (2 minutes), got {total_time:.2f}s"
    assert total_time <= 160.0, f"Expected duration <= 160.0s to maintain crisp pacing, got {total_time:.2f}s"
