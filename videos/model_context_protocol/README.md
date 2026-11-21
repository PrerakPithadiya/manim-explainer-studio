# Video Project: Model Context Protocol (MCP) Explainer

A studio-grade, high-contrast animated explainer video breaking down the **Model Context Protocol (MCP)** using **Manim Community Edition**.

---

## Content Overview

- **Topic**: Model Context Protocol (MCP) architecture & workflow
- **Format**: 1080p60 16:9 Landscape (optimized for YouTube, LinkedIn, and mobile dev feeds)
- **Duration**: ~48.2 seconds (relaxed pacing for maximum technical readability)
- **Primary Scene**: `ModelContextProtocol` (alias `MCPFlow`)

---

## Storyboard & Visual Progression

1. **The $M \times N$ Integration Nightmare (0.0s – 7.0s)**:
   - Visualizes 3 AI Clients (`Claude`, `ChatGPT`, `Cursor`) connecting directly to 4 Tools (`GitHub`, `Slack`, `Postgres`, `Files`).
   - 12 tangled, curved Bézier cables highlighting brittle point-to-point glue code.
   - MCP Central Hub appears and emits an expanding shockwave pulse, snapping 12 cables into 7 clean fiber-optic conduits ($M + N$).

2. **The 3 MCP Primitives & Protocol Specification (7.0s – 13.5s)**:
   - Introduces the three core architectural primitives of MCP:
     - `[R] Resources`: Direct context & file reads
     - `[T] Tools`: Executable actions & API invocations
     - `[P] Prompts`: Interactive templates & slash commands

3. **Real-World Developer Scenario: GitHub PR Lookup (13.5s – 39.5s)**:
   - Glassmorphism IDE cards with Mac/Linux window title bar controls and transport indicators (`stdio / SSE`).
   - User Prompt: `"Find my open pull requests on GitHub"` at the AI Client.
   - **Step 1 (Request)**: AI App sends a standardized JSON-RPC packet with multi-layer glowing photon comet:
     `{"method": "tools/call", "params": {"name": "github.list_prs"}}`
     Animated packet navigates to the MCP Server with ripple reception wave and comfortable reading pause.
   - **Step 2 (Execution)**: MCP Server executes the translation to GitHub REST API:
     `GET https://api.github.com/repos/octocat/repo/pulls?state=open`
   - **Step 3 (Response)**: Structured context returns through MCP:
     `{"prs": [{"id": 42, "title": "feat: mcp", "status": "Ready to merge"}]}`
   - AI Client delivers the human-readable answer: `"Found 1 open PR: #42 Ready to merge"`.

4. **Recap & Call-to-Action (39.5s – 48.2s)**:
   - Key takeaway: *"The 'USB-C for AI' Standard: Connect Any Model to Any Tool"*.
   - High-impact end card with glowing CTA button: *"Start Building with MCP Today!"*.

---

## Render Commands

Run from the repository root:

### Fast Low-Quality Preview (480p @ 15fps)
```powershell
.\venv\Scripts\manim -ql --media_dir videos\model_context_protocol\media videos\model_context_protocol\model_context_protocol.py ModelContextProtocol
```

### High-Definition Production Render (1080p @ 60fps)
```powershell
.\venv\Scripts\manim -qh --media_dir videos\model_context_protocol\media videos\model_context_protocol\model_context_protocol.py ModelContextProtocol
```

---

## Automated Verification

Run video-specific unit tests:
```powershell
.\venv\Scripts\pytest videos\model_context_protocol\test_model_context_protocol.py
```
