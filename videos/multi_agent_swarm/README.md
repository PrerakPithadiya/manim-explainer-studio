# Video Project: Autonomous Multi-Agent Swarm Orchestration

A studio-grade, high-contrast animated explainer video breaking down **Autonomous Multi-Agent Swarm Orchestration, Asynchronous Event Loops, and Self-Correction Dynamics** using **Manim Community Edition**.

---

## Content Overview

- **Topic**: Multi-Agent Swarm Orchestration, Pub/Sub Event Bus, DAG Decomposition & Autonomous Self-Correction
- **Format**: `1080p60` (`1920x1080` @ 60fps) and `480p15` (`854x480` @ 15fps) 16:9 Landscape
- **Duration**: `125.60s` (`1080p60`, 2m 05.6s) / `126.60s` (`480p15`, 2m 06.6s) — strictly $\ge 120$ seconds
- **Primary Scene**: `MultiAgentSwarm` (alias `SwarmOrchestration`)
- **Typography**: Pure Pango `Text()` rendering (zero LaTeX system dependency)

---

## Storyboard & Visual Progression

1. **Act 1 — The Monolithic Limit & Paradigm Shift**:
   - Single-thread `128k` context window accumulates 5 consecutive engineering tasks (`18k` to `22k` tokens each).
   - Live Context Saturation Meter climbs from `42%` (Green) $\to$ `79%` (Amber drift) $\to$ `99% FULL` (Crimson overflow), surfacing lost-in-the-middle errors and hallucinated imports.
   - An expanding cyan shockwave fractures the monolith into 5 autonomous sparks, unveiling the title: *"Autonomous Multi-Agent Swarms"*.

2. **Act 2 — Specialized Swarm Topology**:
   - Central `Swarm Orchestrator` coordinates four bounded-context workers:
     - `Architect Agent` (`16k ctx | AST & Repo Map`)
     - `Coder Agent` (`24k ctx | File Edit & Git`)
     - `Reviewer Agent` (`16k ctx | Diff & Linter`)
     - `Runtime Verifier` (`12k ctx | Pytest & Shell`)
   - Sequentially highlights each node's isolated responsibilities and peer-to-peer dashed verification mesh.

3. **Act 3 — Asynchronous Event Bus & DAG Parallel Sharding**:
   - Incoming mission (`"Migrate Auth to OAuth2 + RBAC with 100% Integration Coverage"`) is decomposed by the Architect into an executable 5-node Directed Acyclic Graph (`T1`–`T5`).
   - Once `T1` and `T2` complete, `T3 (OAuth2 Flow)` and `T4 (RBAC Guard)` dispatch concurrently across the `PUB / SUB EVENT BUS` into `Coder-1` and `Coder-2` in parallel before converging on `T5 (Test Suite)`.

4. **Act 4 — Autonomous Self-Correction Feedback Loop**:
   - `Coder Agent` sends `src/auth/jwt_validator.py` to `Runtime Verifier`.
   - Sandbox `pytest` fails (`FAILED test_expired_jwt_rejected — AssertionError: Expected HTTP 401 Unauthorized, got 200 OK`).
   - Failure trace routes to `Reviewer Agent`, which diagnoses `verify_exp=False` and dispatches an AST critique back to `Coder Agent`.
   - Live Git diff patches the vulnerability (`algorithms=["HS256"], leeway=0`), re-runs `pytest`, and achieves `24 passed, 0 failed [EXIT CODE 0]`.

5. **Act 5 — Distributed Consensus, Merge & Telemetry Impact**:
   - All 4 agents commit `APPROVE` votes into a central Quorum Lock (`CONSENSUS LOCKED • QUORUM 4 / 4`).
   - Git branch graph smoothly merges `feat/oauth2` and `feat/rbac` into `main` (`v2.0-auth-rbac [DEPLOYED]`).
   - Production telemetry dashboard highlights `4.8x` Parallel Speedup, `+68%` Context Efficiency, and `0` Human Interventions, concluding with a geometric swarm emblem outro.

---

## Render Commands

Run from the repository root (`F:\manim-test`):

### Fast Low-Quality Preview (480p @ 15fps)
```powershell
.\venv\Scripts\manim -ql --media_dir videos\multi_agent_swarm\media videos\multi_agent_swarm\multi_agent_swarm.py MultiAgentSwarm
```

### High-Definition Production Render (1080p @ 60fps)
```powershell
.\venv\Scripts\manim -qh --media_dir videos\multi_agent_swarm\media videos\multi_agent_swarm\multi_agent_swarm.py MultiAgentSwarm
```

### Memory-Bounded Production Render (Recommended on tighter system commit memory)
```powershell
.\venv\Scripts\python -c "import sys; sys.path.insert(0, 'videos/multi_agent_swarm'); from manim import config; config.quality='high_quality'; config.media_dir='videos/multi_agent_swarm/media'; config.video_dir='{media_dir}/videos/multi_agent_swarm/{quality}'; config.video_encoder_options={'threads':'2'}; config.encoder_queue_size=2; from multi_agent_swarm import MultiAgentSwarm; MultiAgentSwarm().render()"
```

---

## Automated Verification

Run video-specific unit and duration tests:
```powershell
.\venv\Scripts\pytest videos\multi_agent_swarm\test_multi_agent_swarm.py
```
