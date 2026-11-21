# Manim Explainer Studio

A modular, scalable **Manim Community Edition** workspace engineered for creating high-contrast, developer-focused animated explainer videos. Each video is self-contained in its own dedicated project directory named directly after its topic.

---

## Workspace Structure

The project follows a modular, content-driven architecture so that new animation projects can be added cleanly without polluting the root namespace.

```
manim-test/
├── videos/                                    # All video projects reside here
│   └── model_context_protocol/                # Video: Model Context Protocol (MCP)
│       ├── model_context_protocol.py          # Main animation scene (ModelContextProtocol / MCPFlow)
│       ├── test_model_context_protocol.py     # Automated verification suite
│       ├── README.md                          # Storyboard, scene timings & script
│       └── media/                             # Dedicated render outputs for this video
│           └── videos/
│               └── model_context_protocol/
│                   ├── 480p15/ModelContextProtocol.mp4
│                   └── 1080p60/ModelContextProtocol.mp4
├── media/                                     # Global / default render output folder
├── venv/                                      # Python virtual environment
├── pytest.ini                                 # Pytest configuration (filters 3rd-party warnings)
├── requirements.txt                           # Pinned dependencies
├── .gitignore                                 # Exclusion rules for caches & partial renders
└── README.md                                  # Repository overview and guide
```

---

## Video Catalog

| Project Folder | Topic / Content | Scene Class | Duration | Formats | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [`videos/model_context_protocol/`](videos/model_context_protocol/) | Model Context Protocol (MCP) Architecture & JSON-RPC flow | `ModelContextProtocol` (alias `MCPFlow`) | ~48.2s | 1080p60, 480p15 | ✅ Completed |

---

## Tech Stack & Prerequisites

- **Python**: 3.12+
- **Animation Framework**: [Manim Community Edition](https://www.manim.community/) `v0.22.1`
- **Typography & Rendering**: Pango `Text()` (zero LaTeX system dependencies)
- **Testing**: [pytest](https://docs.pytest.org/) `v9.2.0`

---

## Quickstart & Commands

### 1. Run Automated Test Suite
Runs tests across all video projects:
```powershell
.\venv\Scripts\pytest
```

To run tests for a specific video project:
```powershell
.\venv\Scripts\pytest videos\model_context_protocol\test_model_context_protocol.py
```

### 2. Render Existing Videos

#### Fast Low-Quality Preview (480p @ 15fps)
```powershell
.\venv\Scripts\manim -ql videos\model_context_protocol\model_context_protocol.py ModelContextProtocol
```

#### Production High-Definition Render (1080p @ 60fps)
```powershell
.\venv\Scripts\manim -qh videos\model_context_protocol\model_context_protocol.py ModelContextProtocol
```

*(Note: `MCPFlow` is also available as an alias for backwards compatibility)*.

---

## Adding a New Video Project

To create a new video, follow this standard pattern to keep projects organized:

1. **Create a dedicated folder** under `videos/` named after your topic:
   ```powershell
   New-Item -ItemType Directory -Path "videos\<your_topic_name>"
   ```
2. **Add your scene script**:
   - Create `videos/<your_topic_name>/<your_topic_name>.py`
   - Define your `Scene` class named after the content (e.g., `class YourTopicName(Scene):`)
3. **Add automated tests**:
   - Create `videos/<your_topic_name>/test_<your_topic_name>.py` to validate scene instantiation, duration, and dependencies.
4. **Add documentation**:
   - Create `videos/<your_topic_name>/README.md` with storyboard notes and rendering instructions.

---

## License

MIT License.
