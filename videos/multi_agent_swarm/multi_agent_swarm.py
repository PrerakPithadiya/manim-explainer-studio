"""
Autonomous Multi-Agent Swarm Orchestration & Event Loop
High-contrast, expert-level animated explainer engineered with Manim Community Edition.

Production Design Highlights:
1. Studio Cybernetic Dark Aesthetic (#070A12 Obsidian canvas with neon state accents).
2. Persistent HUD Chapter Timeline across all 5 acts for documentary-grade clarity.
3. Pure Pango Text typography (zero LaTeX system dependencies).
4. Five full-length acts totaling ~130 seconds (>= 120s requirement):
   - Act 1: Monolithic LLM Context Bottleneck & Paradigm Fracture
   - Act 2: Decentralized Swarm Topology & Bounded-Context Roles
   - Act 3: Asynchronous Pub/Sub Event Bus & DAG Parallel Sharding
   - Act 4: Tool Invocation, Runtime Failure & Autonomous Self-Correction Loop
   - Act 5: Distributed Consensus Quorum, Branch Merge & Telemetry Impact
"""

import numpy as np
from manim import *


class Palette:
    """Centralized visual tokens for consistent dark-mode studio styling."""

    BG_DARK = "#070A12"
    GRID_LINE = "#111827"
    SURFACE = "#0F172A"
    SURFACE_ALT = "#111827"
    CODE_BG = "#030712"
    BORDER = "#1E293B"
    BORDER_LIGHT = "#334155"

    CYAN = "#38BDF8"       # Orchestrator, Event Bus, Primary Highlight
    PURPLE = "#BC8CFF"     # Architect Agent & DAG Planning
    GREEN = "#3FB950"      # Coder Agent & Passing Tests
    TEAL = "#2DD4BF"       # Runtime Verifier & Sandbox
    AMBER = "#F0883E"      # Reviewer Agent & Warnings
    RED = "#F85149"        # Context Overflow & Test Failures
    GOLD = "#FBBF24"       # Consensus Quorum Lock

    TEXT_PRIMARY = "#F0F6FC"
    TEXT_SECONDARY = "#CBD5E1"
    TEXT_MUTED = "#8B949E"


class MultiAgentSwarm(Scene):
    """Studio-grade animated explainer illustrating Multi-Agent Swarm Orchestration."""

    def construct(self):
        self.camera.background_color = Palette.BG_DARK

        # Persistent studio grid & bottom chapter HUD
        self.hud_grid = self._build_background_grid()
        self.chapter_items, self.chapter_bar = self._build_chapter_bar()

        self.play(
            FadeIn(self.hud_grid),
            FadeIn(self.chapter_bar, shift=UP * 0.15),
            run_time=0.8,
        )

        # Execute the 5 structured documentary scenes
        self.play_scene_1_bottleneck()
        self.play_scene_2_topology()
        self.play_scene_3_event_bus_dag()
        self.play_scene_4_self_correction()
        self.play_scene_5_consensus_outro()

    # =========================================================================
    # REUSABLE UI BUILDERS & HUD HELPERS
    # =========================================================================

    def _build_background_grid(self):
        """Subtle blueprint grid lines and corner framing marks."""
        lines = VGroup()
        for x in range(-7, 8):
            lines.add(
                Line(
                    [x, -4.0, 0],
                    [x, 4.0, 0],
                    color=Palette.GRID_LINE,
                    stroke_width=0.7,
                    stroke_opacity=0.55,
                )
            )
        for y in range(-4, 5):
            lines.add(
                Line(
                    [-7.2, y, 0],
                    [7.2, y, 0],
                    color=Palette.GRID_LINE,
                    stroke_width=0.7,
                    stroke_opacity=0.55,
                )
            )
        return lines

    def _build_chapter_bar(self):
        """Bottom documentary progress strip showing the 5 chapters."""
        labels = [
            "01 BOTTLENECK",
            "02 TOPOLOGY",
            "03 EVENT BUS & DAG",
            "04 SELF-CORRECTION",
            "05 CONSENSUS",
        ]
        items = []
        group = VGroup()
        for label in labels:
            bg = RoundedRectangle(
                width=2.32,
                height=0.34,
                corner_radius=0.08,
                stroke_color=Palette.BORDER,
                stroke_width=1.1,
                fill_color=Palette.SURFACE,
                fill_opacity=0.9,
            )
            txt = Text(
                label,
                font_size=9,
                weight=BOLD,
                color=Palette.TEXT_MUTED,
            ).move_to(bg.get_center())
            pill = VGroup(bg, txt)
            items.append({"pill": pill, "bg": bg, "txt": txt})
            group.add(pill)

        group.arrange(RIGHT, buff=0.16).move_to([0, -3.68, 0])
        return items, group

    def _activate_chapter(self, active_idx, accent=Palette.CYAN):
        """Return animations highlighting the active chapter and marking prior ones done."""
        anims = []
        for idx, item in enumerate(self.chapter_items):
            if idx < active_idx:
                anims.append(item["bg"].animate.set_stroke(color=Palette.GREEN, width=1.4))
                anims.append(item["bg"].animate.set_fill(color="#081C15", opacity=0.9))
                anims.append(item["txt"].animate.set_color(Palette.GREEN))
            elif idx == active_idx:
                anims.append(item["bg"].animate.set_stroke(color=accent, width=2.2))
                anims.append(item["bg"].animate.set_fill(color="#0A192F", opacity=0.98))
                anims.append(item["txt"].animate.set_color(Palette.TEXT_PRIMARY))
            else:
                anims.append(item["bg"].animate.set_stroke(color=Palette.BORDER, width=1.1))
                anims.append(item["bg"].animate.set_fill(color=Palette.SURFACE, opacity=0.9))
                anims.append(item["txt"].animate.set_color(Palette.TEXT_MUTED))
        return anims

    def _make_scene_header(self, tag, title, subtitle, accent=Palette.CYAN):
        """Consistent top header block leaving y=[-3.25, +2.50] open for scene action."""
        t_tag = Text(tag, font_size=10, weight=BOLD, color=accent)
        t_title = Text(title, font_size=22, weight=BOLD, color=Palette.TEXT_PRIMARY)
        t_sub = Text(subtitle, font_size=12, color=Palette.TEXT_MUTED)
        header = VGroup(t_tag, t_title, t_sub).arrange(DOWN, buff=0.09)
        header.move_to([0, 3.22, 0])
        return header

    def _make_window_dots(self):
        """Mac/Linux IDE window controls."""
        return VGroup(
            Dot(radius=0.042, color="#EF4444"),
            Dot(radius=0.042, color="#F59E0B"),
            Dot(radius=0.042, color="#10B981"),
        ).arrange(RIGHT, buff=0.075)

    def _make_status_pill(self, text, color, width=1.22, height=0.26):
        """Compact uppercase status badge."""
        bg = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=1.3,
            fill_color=color,
            fill_opacity=0.16,
        )
        lbl = Text(text.upper(), font_size=8.5, weight=BOLD, color=color).move_to(bg.get_center())
        return VGroup(bg, lbl)

    def _make_agent_card(
        self,
        title,
        role_tag,
        meta,
        status_text,
        accent,
        pos=ORIGIN,
        width=3.25,
        height=1.42,
    ):
        """Construct a rich cybernetic agent card with replaceable status pill."""
        box = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.16,
            stroke_color=accent,
            stroke_width=2.0,
            fill_color=Palette.SURFACE,
            fill_opacity=0.96,
        ).move_to(pos)

        dots = self._make_window_dots().move_to(box.get_top() + DOWN * 0.19 + LEFT * (width * 0.34))
        badge = Text(role_tag.upper(), font_size=8.5, weight=BOLD, color=accent).move_to(
            box.get_top() + DOWN * 0.19 + RIGHT * (width * 0.23)
        )

        divider = Line(
            box.get_left() + RIGHT * 0.15 + UP * (height * 0.22),
            box.get_right() + LEFT * 0.15 + UP * (height * 0.22),
            color=Palette.BORDER,
            stroke_width=1.0,
        )

        t_title = Text(title, font_size=15, weight=BOLD, color=Palette.TEXT_PRIMARY).move_to(
            box.get_center() + UP * 0.04
        )
        t_meta = Text(meta, font_size=10, color=Palette.TEXT_MUTED).move_to(
            box.get_center() + DOWN * 0.24
        )
        status_pill = self._make_status_pill(status_text, accent, width=1.18, height=0.24).move_to(
            box.get_bottom() + UP * 0.21
        )

        # Position title cleanly slightly above center and meta below
        t_title.move_to(box.get_center() + UP * 0.12)
        t_meta.move_to(box.get_center() + DOWN * 0.16)
        status_pill.move_to(box.get_bottom() + UP * 0.20)

        group = VGroup(box, dots, badge, divider, t_title, t_meta, status_pill)
        return {
            "group": group,
            "box": box,
            "title": t_title,
            "meta": t_meta,
            "status_pill": status_pill,
            "accent": accent,
        }

    def _update_agent_status(self, card_dict, new_text, new_color, border_width=2.8):
        """Animate updating an agent's status pill and border color cleanly without glyph morphing."""
        old_pill = card_dict["status_pill"]
        new_pill = self._make_status_pill(new_text, new_color, width=1.22, height=0.24).move_to(
            old_pill.get_center()
        )
        card_dict["status_pill"] = new_pill
        return [
            FadeOut(old_pill, scale=0.88),
            FadeIn(new_pill, scale=1.05),
            card_dict["box"].animate.set_stroke(color=new_color, width=border_width),
        ]

    def _clear_stage(self, run_time=0.8, extra_anims=None):
        """Fade out all non-HUD scene mobjects so zero orphaned pills or shapes leak across scenes."""
        to_remove = [m for m in self.mobjects if m not in (self.hud_grid, self.chapter_bar)]
        anims = [FadeOut(m, shift=DOWN * 0.15) for m in to_remove]
        if extra_anims:
            anims.extend(extra_anims)
        if anims:
            self.play(*anims, run_time=run_time)

    def _make_photon_packet(self, color=Palette.CYAN, scale=1.0):
        """Multi-layered glowing photon pulse."""
        outer = Dot(radius=0.23 * scale, color=color).set_opacity(0.28)
        inner = Dot(radius=0.14 * scale, color=color).set_opacity(0.68)
        core = Dot(radius=0.075 * scale, color="#FFFFFF")
        return VGroup(outer, inner, core)

    def _make_ide_window(self, title, width=6.4, height=4.4, pos=ORIGIN, border_color=Palette.BORDER_LIGHT):
        """Glassmorphism IDE/Terminal container."""
        outer = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.16,
            stroke_color=border_color,
            stroke_width=2.0,
            fill_color=Palette.CODE_BG,
            fill_opacity=0.97,
        ).move_to(pos)

        header_bg = RoundedRectangle(
            width=width - 0.06,
            height=0.42,
            corner_radius=0.12,
            stroke_width=0,
            fill_color=Palette.SURFACE,
            fill_opacity=0.95,
        ).move_to(outer.get_top() + DOWN * 0.23)

        dots = self._make_window_dots().move_to(header_bg.get_left() + RIGHT * 0.45)
        lbl = Text(title, font_size=10, weight=BOLD, color=Palette.TEXT_SECONDARY).move_to(
            header_bg.get_center()
        )
        divider = Line(
            outer.get_left() + UP * (height / 2 - 0.46),
            outer.get_right() + UP * (height / 2 - 0.46),
            color=Palette.BORDER,
            stroke_width=1.2,
        )
        group = VGroup(outer, header_bg, dots, lbl, divider)
        return {"group": group, "outer": outer, "header": header_bg}

    # =========================================================================
    # SCENE 1: THE MONOLITHIC BOTTLENECK & THE SWARM SHIFT (~23s)
    # =========================================================================

    def play_scene_1_bottleneck(self):
        header = self._make_scene_header(
            "01 / THE MONOLITHIC LIMIT",
            "Why Single-Thread LLMs Fail at Scale",
            "Long horizons saturate context windows and compound reasoning errors",
            accent=Palette.RED,
        )
        self.play(
            *self._activate_chapter(0, accent=Palette.RED),
            FadeIn(header, shift=DOWN * 0.15),
            run_time=0.9,
        )

        # Left Panel: Monolithic LLM Card
        mono_win = self._make_ide_window(
            "monolithic-llm-thread  (128k Context)",
            width=5.4,
            height=4.35,
            pos=[-3.25, -0.05, 0],
            border_color=Palette.BORDER_LIGHT,
        )

        # Right Top: Context Saturation Meter
        meter_card = RoundedRectangle(
            width=5.8,
            height=1.75,
            corner_radius=0.16,
            stroke_color=Palette.BORDER_LIGHT,
            stroke_width=1.8,
            fill_color=Palette.SURFACE,
            fill_opacity=0.96,
        ).move_to([3.1, 1.25, 0])

        meter_lbl = Text("CONTEXT SATURATION METER", font_size=10, weight=BOLD, color=Palette.TEXT_SECONDARY).move_to(
            meter_card.get_top() + DOWN * 0.30 + LEFT * 1.35
        )
        meter_pct = Text("0%", font_size=14, weight=BOLD, color=Palette.GREEN).move_to(
            meter_card.get_top() + DOWN * 0.30 + RIGHT * 2.15
        )
        bar_bg = RoundedRectangle(
            width=5.1,
            height=0.38,
            corner_radius=0.08,
            stroke_color=Palette.BORDER_LIGHT,
            stroke_width=1.2,
            fill_color=Palette.CODE_BG,
            fill_opacity=1.0,
        ).move_to(meter_card.get_center() + DOWN * 0.05)

        bar_fill = RoundedRectangle(
            width=0.12,
            height=0.32,
            corner_radius=0.06,
            stroke_width=0,
            fill_color=Palette.GREEN,
            fill_opacity=0.92,
        ).align_to(bar_bg, LEFT).shift(RIGHT * 0.04).set_y(bar_bg.get_y())

        meter_status = Text("State: Optimal Reasoning Window", font_size=10, color=Palette.TEXT_MUTED).move_to(
            meter_card.get_bottom() + UP * 0.28
        )
        meter_group = VGroup(meter_card, meter_lbl, meter_pct, bar_bg, bar_fill, meter_status)

        # Right Bottom: Reasoning Integrity Panel
        log_card = RoundedRectangle(
            width=5.8,
            height=2.3,
            corner_radius=0.16,
            stroke_color=Palette.BORDER_LIGHT,
            stroke_width=1.8,
            fill_color=Palette.SURFACE,
            fill_opacity=0.96,
        ).move_to([3.1, -1.05, 0])
        log_title = Text("EXECUTION TELEMETRY", font_size=10, weight=BOLD, color=Palette.TEXT_SECONDARY).move_to(
            log_card.get_top() + DOWN * 0.28 + LEFT * 1.65
        )
        log_line1 = Text("[OK] Token attention sharp across early files", font_size=10.5, color=Palette.GREEN)
        log_line2 = Text("[WARN] Schema constraints pushed out of active focus", font_size=10.5, color=Palette.AMBER)
        log_line3 = Text("[FAIL] Hallucinated OAuth import • Zero runtime checks", font_size=10.5, color=Palette.RED)
        log_lines = VGroup(log_line1, log_line2, log_line3).arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to(
            log_card.get_center() + DOWN * 0.14 + LEFT * 0.1
        )
        log_group_frame = VGroup(log_card, log_title)

        self.play(
            FadeIn(mono_win["group"], shift=RIGHT * 0.2),
            FadeIn(meter_group, shift=LEFT * 0.2),
            FadeIn(log_group_frame, shift=LEFT * 0.2),
            run_time=1.0,
        )

        # Stack of task blocks piling inside the monolithic window
        task_specs = [
            ("01. Repository AST & Dependencies (18k tokens)", Palette.CYAN),
            ("02. Database Schema & Migrations (29k tokens)", Palette.CYAN),
            ("03. OAuth2 Provider & Key Rotation (34k tokens)", Palette.AMBER),
            ("04. RBAC Policy Matrix & Routes (28k tokens)", Palette.AMBER),
            ("05. Edge-Case Integration Suite (22k tokens)", Palette.RED),
        ]
        stacked_blocks = VGroup()
        anchor_y = mono_win["outer"].get_top()[1] - 0.85

        for idx, (label, clr) in enumerate(task_specs):
            blk_bg = RoundedRectangle(
                width=4.85,
                height=0.52,
                corner_radius=0.09,
                stroke_color=clr,
                stroke_width=1.4,
                fill_color=Palette.SURFACE,
                fill_opacity=0.95,
            )
            blk_txt = Text(label, font_size=10, weight=BOLD, color=Palette.TEXT_PRIMARY).move_to(blk_bg.get_center())
            blk = VGroup(blk_bg, blk_txt).move_to([mono_win["outer"].get_x(), anchor_y - idx * 0.64, 0])
            stacked_blocks.add(blk)

        # Stage 1: Tasks 1 & 2 (42% Healthy)
        new_fill_42 = RoundedRectangle(
            width=2.1, height=0.32, corner_radius=0.06, stroke_width=0, fill_color=Palette.GREEN, fill_opacity=0.92
        ).align_to(bar_bg, LEFT).shift(RIGHT * 0.04).set_y(bar_bg.get_y())
        pct_42 = Text("42%", font_size=14, weight=BOLD, color=Palette.GREEN).move_to(meter_pct.get_center())

        self.play(
            FadeIn(stacked_blocks[0], shift=DOWN * 0.15),
            FadeIn(stacked_blocks[1], shift=DOWN * 0.15),
            Transform(bar_fill, new_fill_42),
            FadeOut(meter_pct, scale=0.85),
            FadeIn(pct_42, scale=1.05),
            FadeIn(log_line1, shift=RIGHT * 0.15),
            run_time=1.8,
        )
        meter_pct = pct_42
        self.wait(1.1)

        # Stage 2: Tasks 3 & 4 (79% Amber Warning)
        new_fill_79 = RoundedRectangle(
            width=3.95, height=0.32, corner_radius=0.06, stroke_width=0, fill_color=Palette.AMBER, fill_opacity=0.95
        ).align_to(bar_bg, LEFT).shift(RIGHT * 0.04).set_y(bar_bg.get_y())
        pct_79 = Text("79%", font_size=14, weight=BOLD, color=Palette.AMBER).move_to(meter_pct.get_center())
        status_warn = Text("State: Lost-in-the-Middle Degradation", font_size=10, weight=BOLD, color=Palette.AMBER).move_to(
            meter_status.get_center()
        )

        self.play(
            FadeIn(stacked_blocks[2], shift=DOWN * 0.15),
            FadeIn(stacked_blocks[3], shift=DOWN * 0.15),
            Transform(bar_fill, new_fill_79),
            FadeOut(meter_pct, scale=0.85),
            FadeIn(pct_79, scale=1.05),
            FadeOut(meter_status, shift=UP * 0.05),
            FadeIn(status_warn, shift=UP * 0.05),
            mono_win["outer"].animate.set_stroke(color=Palette.AMBER, width=2.4),
            FadeIn(log_line2, shift=RIGHT * 0.15),
            run_time=2.1,
        )
        meter_pct = pct_79
        meter_status = status_warn
        self.wait(1.4)

        # Stage 3: Task 5 Overflow (99% Crimson Failure)
        new_fill_99 = RoundedRectangle(
            width=5.02, height=0.32, corner_radius=0.06, stroke_width=0, fill_color=Palette.RED, fill_opacity=0.98
        ).align_to(bar_bg, LEFT).shift(RIGHT * 0.04).set_y(bar_bg.get_y())
        pct_99 = Text("99% FULL", font_size=13, weight=BOLD, color=Palette.RED).move_to(meter_pct.get_center() + LEFT * 0.22)
        status_fail = Text("CRITICAL: Context Saturation & Compounding Drift", font_size=10, weight=BOLD, color=Palette.RED).move_to(
            meter_status.get_center()
        )

        self.play(
            FadeIn(stacked_blocks[4], shift=DOWN * 0.15),
            Transform(bar_fill, new_fill_99),
            FadeOut(meter_pct, scale=0.85),
            FadeIn(pct_99, scale=1.05),
            FadeOut(meter_status, shift=UP * 0.05),
            FadeIn(status_fail, shift=UP * 0.05),
            mono_win["outer"].animate.set_stroke(color=Palette.RED, width=3.5),
            meter_card.animate.set_stroke(color=Palette.RED, width=2.8),
            log_card.animate.set_stroke(color=Palette.RED, width=2.8),
            FadeIn(log_line3, shift=RIGHT * 0.15),
            run_time=1.9,
        )
        meter_pct = pct_99
        meter_status = status_fail
        self.wait(3.2)

        # Stage 4: Paradigm Fracture Shockwave -> Hero Reveal
        monolith_all = VGroup(
            mono_win["group"],
            stacked_blocks,
            meter_card,
            meter_lbl,
            meter_pct,
            bar_bg,
            bar_fill,
            meter_status,
            log_card,
            log_title,
            log_lines,
        )
        shockwave = Circle(radius=0.25, color=Palette.CYAN, stroke_width=4.5).move_to(ORIGIN)
        sparks = VGroup(
            *[
                self._make_photon_packet(c, scale=1.2).move_to(ORIGIN)
                for c in [Palette.CYAN, Palette.PURPLE, Palette.GREEN, Palette.AMBER, Palette.TEAL]
            ]
        )
        spark_targets = [
            [-4.6, 1.8, 0],
            [4.6, 1.8, 0],
            [-4.6, -1.8, 0],
            [4.6, -1.8, 0],
            [0, 2.2, 0],
        ]

        self.play(
            FadeOut(monolith_all, scale=0.85),
            FadeOut(header, shift=UP * 0.2),
            shockwave.animate.scale(26).set_opacity(0),
            *[sparks[i].animate.move_to(spark_targets[i]) for i in range(5)],
            run_time=1.6,
        )

        hero_badge = Text("THE PARADIGM SHIFT", font_size=12, weight=BOLD, color=Palette.CYAN).shift(UP * 1.45)
        hero_title = Text(
            "Autonomous Multi-Agent Swarms",
            font_size=38,
            weight=BOLD,
            color=Palette.TEXT_PRIMARY,
        ).next_to(hero_badge, DOWN, buff=0.22)
        hero_line = Line(LEFT * 4.2, RIGHT * 4.2, color=Palette.CYAN, stroke_width=2.5).next_to(
            hero_title, DOWN, buff=0.24
        )
        hero_sub = Text(
            "Bounded Contexts   •   Event-Driven Bus   •   Self-Healing Verification",
            font_size=14,
            weight=BOLD,
            color=Palette.TEXT_SECONDARY,
        ).next_to(hero_line, DOWN, buff=0.28)

        hero_group = VGroup(hero_badge, hero_title, hero_line, hero_sub)

        self.play(
            FadeIn(hero_badge, shift=UP * 0.15),
            FadeIn(hero_title, shift=UP * 0.15),
            GrowFromCenter(hero_line),
            run_time=1.2,
        )
        self.play(FadeIn(hero_sub, shift=UP * 0.12), run_time=0.9)
        self.wait(3.2)

        self._clear_stage(run_time=0.8)

    # =========================================================================
    # SCENE 2: SWARM TOPOLOGY & SPECIALIZED ROLES (~26s)
    # =========================================================================

    def play_scene_2_topology(self):
        header = self._make_scene_header(
            "02 / SPECIALIZED SWARM TOPOLOGY",
            "Replacing Monoliths with Bounded-Context Workers",
            "Each agent operates with dedicated system prompts and strict tool boundaries",
            accent=Palette.CYAN,
        )
        self.play(
            *self._activate_chapter(1, accent=Palette.CYAN),
            FadeIn(header, shift=DOWN * 0.15),
            run_time=0.9,
        )

        # Central Orchestrator
        orch_card = self._make_agent_card(
            "Swarm Orchestrator",
            "Coordinator",
            "Task Routing & State Sync",
            "ACTIVE",
            Palette.CYAN,
            pos=[0, 0.15, 0],
            width=3.35,
            height=1.45,
        )
        orch_ring = RoundedRectangle(
            width=3.58,
            height=1.68,
            corner_radius=0.22,
            color=Palette.CYAN,
            stroke_width=1.4,
            stroke_opacity=0.38,
        ).move_to(orch_card["box"].get_center())

        self.play(
            FadeIn(orch_card["group"], scale=0.85),
            Create(orch_ring),
            run_time=1.2,
        )

        # 4 Cardinal Specialized Workers
        architect = self._make_agent_card(
            "Architect Agent",
            "Planner",
            "Ctx: 16k | AST & Repo Map",
            "IDLE",
            Palette.PURPLE,
            pos=[-4.35, 1.48, 0],
            width=3.25,
            height=1.40,
        )
        coder = self._make_agent_card(
            "Coder Agent",
            "Builder",
            "Ctx: 24k | File Edit & Git",
            "IDLE",
            Palette.GREEN,
            pos=[4.35, 1.48, 0],
            width=3.25,
            height=1.40,
        )
        reviewer = self._make_agent_card(
            "Reviewer Agent",
            "Auditor",
            "Ctx: 16k | Diff & Linter",
            "IDLE",
            Palette.AMBER,
            pos=[-4.35, -1.18, 0],
            width=3.25,
            height=1.40,
        )
        verifier = self._make_agent_card(
            "Runtime Verifier",
            "Sandbox",
            "Ctx: 12k | Pytest & Shell",
            "IDLE",
            Palette.TEAL,
            pos=[4.35, -1.18, 0],
            width=3.25,
            height=1.40,
        )

        # Primary Orchestrator <-> Worker Links
        link_arch = Line(orch_card["box"].get_left() + UP * 0.25, architect["box"].get_right() + DOWN * 0.15, color=Palette.PURPLE, stroke_width=2.2)
        link_code = Line(orch_card["box"].get_right() + UP * 0.25, coder["box"].get_left() + DOWN * 0.15, color=Palette.GREEN, stroke_width=2.2)
        link_rev = Line(orch_card["box"].get_left() + DOWN * 0.25, reviewer["box"].get_right() + UP * 0.15, color=Palette.AMBER, stroke_width=2.2)
        link_ver = Line(orch_card["box"].get_right() + DOWN * 0.25, verifier["box"].get_left() + UP * 0.15, color=Palette.TEAL, stroke_width=2.2)

        self.play(
            FadeIn(architect["group"], shift=LEFT * 0.3),
            FadeIn(coder["group"], shift=RIGHT * 0.3),
            Create(link_arch),
            Create(link_code),
            run_time=1.4,
        )
        self.play(
            FadeIn(reviewer["group"], shift=LEFT * 0.3),
            FadeIn(verifier["group"], shift=RIGHT * 0.3),
            Create(link_rev),
            Create(link_ver),
            run_time=1.4,
        )

        # Peer-to-peer verification dashed lines
        peer_top = DashedLine(
            architect["box"].get_right(), coder["box"].get_left(), color=Palette.BORDER_LIGHT, stroke_width=1.6
        )
        peer_right = DashedLine(
            coder["box"].get_bottom(), verifier["box"].get_top(), color=Palette.BORDER_LIGHT, stroke_width=1.6
        )
        peer_bottom = DashedLine(
            verifier["box"].get_left(), reviewer["box"].get_right(), color=Palette.BORDER_LIGHT, stroke_width=1.6
        )
        peer_left = DashedLine(
            reviewer["box"].get_top(), architect["box"].get_bottom(), color=Palette.BORDER_LIGHT, stroke_width=1.6
        )
        peer_mesh = VGroup(peer_top, peer_right, peer_bottom, peer_left)
        self.play(Create(peer_mesh), run_time=1.2)
        self.wait(1.0)

        # Bottom Callout Pill for Role Spotlights
        callout_box = RoundedRectangle(
            width=11.4,
            height=0.68,
            corner_radius=0.14,
            stroke_color=Palette.BORDER_LIGHT,
            stroke_width=1.8,
            fill_color=Palette.SURFACE,
            fill_opacity=0.97,
        ).move_to([0, -2.68, 0])
        callout_txt = Text(
            "Swarm Principle: Narrow context per worker eliminates cross-concern interference",
            font_size=12.5,
            weight=BOLD,
            color=Palette.TEXT_PRIMARY,
        ).move_to(callout_box.get_center())
        self.play(FadeIn(callout_box, shift=UP * 0.1), FadeIn(callout_txt), run_time=0.8)
        self.wait(1.2)

        spotlights = [
            (
                architect,
                Palette.PURPLE,
                "PLANNING",
                "1. Architect Agent: Reads repo structure & splits goals into executable DAG shards",
            ),
            (
                coder,
                Palette.GREEN,
                "READY",
                "2. Coder Agent: Generates clean patches inside focused 24k context without noise",
            ),
            (
                reviewer,
                Palette.AMBER,
                "AUDITING",
                "3. Reviewer Agent: Evaluates diffs & security invariants independently of author bias",
            ),
            (
                verifier,
                Palette.TEAL,
                "ARMED",
                "4. Runtime Verifier: Executes tests & linters inside isolated sandbox containers",
            ),
        ]

        for card_obj, clr, state_lbl, caption in spotlights:
            new_cap = Text(caption, font_size=12, weight=BOLD, color=clr).move_to(callout_box.get_center())
            pulse = self._make_photon_packet(clr, scale=0.9).move_to(orch_card["box"].get_center())
            self.play(
                *self._update_agent_status(card_obj, state_lbl, clr, border_width=3.2),
                callout_box.animate.set_stroke(color=clr, width=2.2),
                FadeOut(callout_txt, shift=UP * 0.08),
                FadeIn(new_cap, shift=UP * 0.08),
                pulse.animate.move_to(card_obj["box"].get_center()),
                run_time=1.3,
            )
            callout_txt = new_cap
            self.play(FadeOut(pulse, scale=1.8), run_time=0.4)
            self.wait(2.5)

            # Dim border slightly back before next card
            self.play(card_obj["box"].animate.set_stroke(color=clr, width=2.0), run_time=0.35)

        self.wait(1.8)
        self._clear_stage(run_time=0.8)

    # =========================================================================
    # SCENE 3: ASYNCHRONOUS EVENT BUS & DAG DECOMPOSITION (~27s)
    # =========================================================================

    def play_scene_3_event_bus_dag(self):
        header = self._make_scene_header(
            "03 / ASYNCHRONOUS EVENT BUS & DAG",
            "Task Decomposition & Non-Blocking Parallel Execution",
            "Architect shards the mission into a Directed Acyclic Graph streamed over a shared bus",
            accent=Palette.PURPLE,
        )
        self.play(
            *self._activate_chapter(2, accent=Palette.PURPLE),
            FadeIn(header, shift=DOWN * 0.15),
            run_time=0.9,
        )

        # Top-Left: Mission Prompt Box
        mission_box = RoundedRectangle(
            width=4.5,
            height=1.75,
            corner_radius=0.14,
            stroke_color=Palette.CYAN,
            stroke_width=2.0,
            fill_color=Palette.SURFACE,
            fill_opacity=0.96,
        ).move_to([-4.0, 1.48, 0])
        m_tag = Text("INCOMING MISSION", font_size=9.5, weight=BOLD, color=Palette.CYAN).move_to(
            mission_box.get_top() + DOWN * 0.25
        )
        m_txt1 = Text('"Migrate Auth to OAuth2 + RBAC', font_size=11.5, weight=BOLD, color=Palette.TEXT_PRIMARY).next_to(
            m_tag, DOWN, buff=0.18
        )
        m_txt2 = Text('with 100% Integration Coverage"', font_size=11.5, weight=BOLD, color=Palette.TEXT_PRIMARY).next_to(
            m_txt1, DOWN, buff=0.09
        )
        m_meta = Text("Scope: 14 Files   •   Priority: P0", font_size=9.5, color=Palette.TEXT_MUTED).next_to(
            m_txt2, DOWN, buff=0.18
        )
        mission_group = VGroup(mission_box, m_tag, m_txt1, m_txt2, m_meta)

        # Top-Right: Executable DAG Container
        dag_panel = RoundedRectangle(
            width=7.45,
            height=2.45,
            corner_radius=0.16,
            stroke_color=Palette.BORDER_LIGHT,
            stroke_width=1.8,
            fill_color=Palette.CODE_BG,
            fill_opacity=0.96,
        ).move_to([2.45, 1.15, 0])
        dag_lbl = Text("EXECUTABLE DIRECTED ACYCLIC GRAPH (DAG)", font_size=9.5, weight=BOLD, color=Palette.PURPLE).move_to(
            dag_panel.get_top() + DOWN * 0.22
        )

        def make_dag_node(code, desc, pos, clr=Palette.BORDER_LIGHT):
            n_box = RoundedRectangle(
                width=1.55,
                height=0.58,
                corner_radius=0.10,
                stroke_color=clr,
                stroke_width=1.8,
                fill_color=Palette.SURFACE,
                fill_opacity=0.98,
            ).move_to(pos)
            n_code = Text(code, font_size=9.5, weight=BOLD, color=clr).move_to(n_box.get_center() + UP * 0.11)
            n_desc = Text(desc, font_size=8.5, color=Palette.TEXT_SECONDARY).move_to(n_box.get_center() + DOWN * 0.11)
            return {"group": VGroup(n_box, n_code, n_desc), "box": n_box, "code": n_code}

        t1 = make_dag_node("T1", "Schema RFC", [-0.35, 1.05, 0], Palette.PURPLE)
        t2 = make_dag_node("T2", "DB Migration", [1.55, 1.05, 0], Palette.PURPLE)
        t3 = make_dag_node("T3", "OAuth2 Flow", [3.45, 1.52, 0], Palette.CYAN)
        t4 = make_dag_node("T4", "RBAC Guard", [3.45, 0.58, 0], Palette.CYAN)
        t5 = make_dag_node("T5", "Test Suite", [5.32, 1.05, 0], Palette.TEAL)

        e12 = Arrow(t1["box"].get_right(), t2["box"].get_left(), buff=0.06, color=Palette.TEXT_MUTED, stroke_width=2.0, max_tip_length_to_length_ratio=0.22)
        e23 = Arrow(t2["box"].get_right(), t3["box"].get_left(), buff=0.06, color=Palette.CYAN, stroke_width=2.0, max_tip_length_to_length_ratio=0.22)
        e24 = Arrow(t2["box"].get_right(), t4["box"].get_left(), buff=0.06, color=Palette.CYAN, stroke_width=2.0, max_tip_length_to_length_ratio=0.22)
        e35 = Arrow(t3["box"].get_right(), t5["box"].get_left(), buff=0.06, color=Palette.TEXT_MUTED, stroke_width=2.0, max_tip_length_to_length_ratio=0.22)
        e45 = Arrow(t4["box"].get_right(), t5["box"].get_left(), buff=0.06, color=Palette.TEXT_MUTED, stroke_width=2.0, max_tip_length_to_length_ratio=0.22)

        dag_nodes = [t1, t2, t3, t4, t5]
        dag_edges = VGroup(e12, e23, e24, e35, e45)

        # Middle: Shared Pub/Sub Event Bus
        bus_bar = RoundedRectangle(
            width=12.1,
            height=0.48,
            corner_radius=0.12,
            stroke_color=Palette.CYAN,
            stroke_width=2.4,
            fill_color="#0A192F",
            fill_opacity=0.98,
        ).move_to([0, -0.62, 0])
        bus_txt = Text(
            "PUB / SUB EVENT BUS   •   SHARED BLACKBOARD STATE   •   NON-BLOCKING DISPATCH",
            font_size=10,
            weight=BOLD,
            color=Palette.CYAN,
        ).move_to(bus_bar.get_center())
        bus_group = VGroup(bus_bar, bus_txt)

        # Bottom: 4 Active Worker Pods
        pod_arch = self._make_agent_card(
            "Architect", "Planner", "DAG Generator", "PLANNING", Palette.PURPLE, pos=[-4.55, -2.18, 0], width=2.8, height=1.35
        )
        pod_c1 = self._make_agent_card(
            "Coder-1", "Shard A", "OAuth2 Handlers", "IDLE", Palette.GREEN, pos=[-1.52, -2.18, 0], width=2.8, height=1.35
        )
        pod_c2 = self._make_agent_card(
            "Coder-2", "Shard B", "RBAC Middleware", "IDLE", Palette.GREEN, pos=[1.52, -2.18, 0], width=2.8, height=1.35
        )
        pod_ver = self._make_agent_card(
            "Verifier", "Runner", "Integration Gate", "WAITING", Palette.TEAL, pos=[4.55, -2.18, 0], width=2.8, height=1.35
        )
        pods = [pod_arch, pod_c1, pod_c2, pod_ver]

        # Vertical bus taps linking Bus <-> Pods
        taps = VGroup(
            *[
                Line(
                    [p["box"].get_x(), bus_bar.get_bottom()[1], 0],
                    p["box"].get_top(),
                    color=Palette.BORDER_LIGHT,
                    stroke_width=2.0,
                )
                for p in pods
            ]
        )

        # Step 1: Mission + Architect + DAG Panel
        self.play(
            FadeIn(mission_group, shift=RIGHT * 0.2),
            FadeIn(dag_panel, shift=LEFT * 0.2),
            FadeIn(dag_lbl),
            run_time=1.1,
        )
        self.play(
            FadeIn(bus_group, shift=UP * 0.15),
            *[FadeIn(p["group"], shift=UP * 0.15) for p in pods],
            Create(taps),
            run_time=1.3,
        )

        # Architect sends mission breakdown into DAG
        arch_pkt = self._make_photon_packet(Palette.PURPLE).move_to(mission_box.get_right())
        self.play(arch_pkt.animate.move_to(t1["box"].get_left()), run_time=0.9)
        self.play(FadeOut(arch_pkt), FadeIn(t1["group"], scale=0.8), run_time=0.5)
        self.play(GrowArrow(e12), FadeIn(t2["group"], scale=0.8), run_time=0.7)
        self.play(
            GrowArrow(e23),
            GrowArrow(e24),
            FadeIn(t3["group"], scale=0.8),
            FadeIn(t4["group"], scale=0.8),
            run_time=0.9,
        )
        self.play(GrowArrow(e35), GrowArrow(e45), FadeIn(t5["group"], scale=0.8), run_time=0.8)
        self.wait(1.2)

        # T1 & T2 complete quickly
        for node in (t1, t2):
            self.play(
                node["box"].animate.set_stroke(color=Palette.GREEN, width=2.5),
                node["code"].animate.set_color(Palette.GREEN),
                run_time=0.55,
            )
        self.play(*self._update_agent_status(pod_arch, "DONE", Palette.GREEN, border_width=2.2), run_time=0.7)

        # Parallel Dispatch on the Event Bus: T3 -> Coder-1 AND T4 -> Coder-2 simultaneously!
        pkt_a = self._make_photon_packet(Palette.CYAN).move_to(t3["box"].get_bottom())
        pkt_b = self._make_photon_packet(Palette.CYAN).move_to(t4["box"].get_bottom())

        path_a = VMobject().set_points_as_corners([
            t3["box"].get_bottom(),
            [t3["box"].get_x(), bus_bar.get_y(), 0],
            [pod_c1["box"].get_x(), bus_bar.get_y(), 0],
            pod_c1["box"].get_top(),
        ])
        path_b = VMobject().set_points_as_corners([
            t4["box"].get_bottom(),
            [t4["box"].get_x(), bus_bar.get_y(), 0],
            [pod_c2["box"].get_x(), bus_bar.get_y(), 0],
            pod_c2["box"].get_top(),
        ])

        dispatch_banner = Text(
            "EVENT DISPATCHED:  T3 (OAuth2)  ||  T4 (RBAC)  EXECUTING IN PARALLEL",
            font_size=10,
            weight=BOLD,
            color=Palette.GOLD,
        ).move_to(bus_bar.get_center())

        self.play(
            FadeOut(bus_txt, shift=UP * 0.06),
            FadeIn(dispatch_banner, shift=UP * 0.06),
            MoveAlongPath(pkt_a, path_a),
            MoveAlongPath(pkt_b, path_b),
            run_time=2.6,
        )
        bus_txt = dispatch_banner

        # Both Coders transition to WORKING concurrently
        r_a = Circle(radius=0.35, color=Palette.GREEN, stroke_width=3.0).move_to(pod_c1["box"].get_center())
        r_b = Circle(radius=0.35, color=Palette.GREEN, stroke_width=3.0).move_to(pod_c2["box"].get_center())
        self.play(
            FadeOut(pkt_a),
            FadeOut(pkt_b),
            r_a.animate.scale(2.8).set_opacity(0),
            r_b.animate.scale(2.8).set_opacity(0),
            *self._update_agent_status(pod_c1, "WORKING", Palette.GREEN, border_width=3.0),
            *self._update_agent_status(pod_c2, "WORKING", Palette.GREEN, border_width=3.0),
            taps[1].animate.set_color(Palette.GREEN),
            taps[2].animate.set_color(Palette.GREEN),
            run_time=1.0,
        )
        self.wait(2.8)

        # Completion events publish back up to Blackboard -> T3, T4 green -> T5 unlocks!
        ret_a = self._make_photon_packet(Palette.GREEN).move_to(pod_c1["box"].get_top())
        ret_b = self._make_photon_packet(Palette.GREEN).move_to(pod_c2["box"].get_top())
        path_ret_a = VMobject().set_points_as_corners([
            pod_c1["box"].get_top(),
            [pod_c1["box"].get_x(), bus_bar.get_y(), 0],
            [pod_ver["box"].get_x(), bus_bar.get_y(), 0],
            pod_ver["box"].get_top(),
        ])
        path_ret_b = VMobject().set_points_as_corners([
            pod_c2["box"].get_top(),
            [pod_c2["box"].get_x(), bus_bar.get_y(), 0],
            [pod_ver["box"].get_x(), bus_bar.get_y(), 0],
            pod_ver["box"].get_top(),
        ])

        sync_banner = Text(
            "SHARDS MERGED ON BLACKBOARD  ->  TRIGGERING T5 INTEGRATION VERIFICATION",
            font_size=10,
            weight=BOLD,
            color=Palette.TEAL,
        ).move_to(bus_bar.get_center())

        self.play(
            FadeOut(bus_txt, shift=UP * 0.06),
            FadeIn(sync_banner, shift=UP * 0.06),
            t3["box"].animate.set_stroke(color=Palette.GREEN, width=2.5),
            t3["code"].animate.set_color(Palette.GREEN),
            t4["box"].animate.set_stroke(color=Palette.GREEN, width=2.5),
            t4["code"].animate.set_color(Palette.GREEN),
            *self._update_agent_status(pod_c1, "COMMITTED", Palette.GREEN, border_width=2.2),
            *self._update_agent_status(pod_c2, "COMMITTED", Palette.GREEN, border_width=2.2),
            MoveAlongPath(ret_a, path_ret_a),
            MoveAlongPath(ret_b, path_ret_b),
            run_time=2.5,
        )
        bus_txt = sync_banner

        self.play(
            FadeOut(ret_a),
            FadeOut(ret_b),
            t5["box"].animate.set_stroke(color=Palette.TEAL, width=3.0),
            *self._update_agent_status(pod_ver, "TESTING", Palette.TEAL, border_width=3.0),
            taps[3].animate.set_color(Palette.TEAL),
            run_time=1.0,
        )
        self.wait(2.8)

        self._clear_stage(run_time=0.8)

    # =========================================================================
    # SCENE 4: RUNTIME FAILURE & AUTONOMOUS SELF-CORRECTION LOOP (~34s)
    # =========================================================================

    def play_scene_4_self_correction(self):
        header = self._make_scene_header(
            "04 / AUTONOMOUS SELF-CORRECTION LOOP",
            "Real Tool Execution: Fail, Diagnose, Patch & Verify",
            "Runtime test failures trigger zero-human automated critique cycles",
            accent=Palette.TEAL,
        )
        self.play(
            *self._activate_chapter(3, accent=Palette.TEAL),
            FadeIn(header, shift=DOWN * 0.15),
            run_time=0.9,
        )

        # Left Column: Cyclic Agent Triad
        coder = self._make_agent_card(
            "Coder Agent", "Author", "auth_jwt.py", "PATCHING", Palette.GREEN, pos=[-3.55, 1.48, 0], width=3.0, height=1.36
        )
        verifier = self._make_agent_card(
            "Runtime Verifier", "Pytest", "Sandbox Runner", "STANDBY", Palette.TEAL, pos=[-1.95, -1.28, 0], width=2.85, height=1.36
        )
        reviewer = self._make_agent_card(
            "Reviewer Agent", "Critic", "AST Security", "STANDBY", Palette.AMBER, pos=[-5.15, -1.28, 0], width=2.85, height=1.36
        )

        arc_c_to_v = CurvedArrow(
            coder["box"].get_right() + DOWN * 0.2,
            verifier["box"].get_top() + RIGHT * 0.35,
            angle=-0.45,
            color=Palette.GREEN,
            stroke_width=2.4,
            tip_length=0.18,
        )
        arc_v_to_r = CurvedArrow(
            verifier["box"].get_left(),
            reviewer["box"].get_right(),
            angle=-0.25,
            color=Palette.BORDER_LIGHT,
            stroke_width=2.4,
            tip_length=0.18,
        )
        arc_r_to_c = CurvedArrow(
            reviewer["box"].get_top() + LEFT * 0.35,
            coder["box"].get_left() + DOWN * 0.2,
            angle=-0.45,
            color=Palette.BORDER_LIGHT,
            stroke_width=2.4,
            tip_length=0.18,
        )

        lbl_cv = Text("1. Run Tests", font_size=9.5, weight=BOLD, color=Palette.GREEN).move_to([-1.08, 0.35, 0])
        lbl_vr = Text("2. Trace", font_size=9.5, weight=BOLD, color=Palette.TEXT_MUTED).move_to([-3.55, -2.28, 0])
        lbl_rc = Text("3. Critique", font_size=9.5, weight=BOLD, color=Palette.TEXT_MUTED).move_to([-5.95, 0.35, 0])

        # Right Column: Sandbox IDE & Terminal Window
        ide = self._make_ide_window(
            "sandbox-container  —  auth_jwt.py  |  pytest",
            width=6.6,
            height=4.55,
            pos=[3.15, -0.05, 0],
            border_color=Palette.BORDER_LIGHT,
        )

        # Upper pane inside IDE: Code/Diff Preview
        code_box = RoundedRectangle(
            width=6.15,
            height=1.55,
            corner_radius=0.10,
            stroke_color=Palette.BORDER,
            stroke_width=1.2,
            fill_color="#090F1A",
            fill_opacity=0.98,
        ).move_to([3.15, 0.92, 0])

        code_file_tag = Text("FILE: src/auth/jwt_validator.py", font_size=9.5, weight=BOLD, color=Palette.CYAN).move_to(
            code_box.get_top() + DOWN * 0.22 + LEFT * 1.65
        )
        code_v1 = VGroup(
            Text("def verify_token(token: str) -> dict:", font_size=10, color=Palette.TEXT_SECONDARY),
            Text('  return jwt.decode(token, KEY, options={"verify_exp": False})', font_size=9.5, color=Palette.AMBER),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(code_box.get_center() + DOWN * 0.14)

        # Lower pane inside IDE: Terminal Output
        term_box = RoundedRectangle(
            width=6.15,
            height=2.15,
            corner_radius=0.10,
            stroke_color=Palette.BORDER,
            stroke_width=1.2,
            fill_color="#020408",
            fill_opacity=0.99,
        ).move_to([3.15, -1.08, 0])

        term_cmd_1 = Text("$ pytest tests/test_oauth_rbac.py -v", font_size=10, weight=BOLD, color=Palette.CYAN)
        term_res_1a = Text("PASSED  tests/test_oauth_rbac.py::test_rbac_admin_role", font_size=9.5, color=Palette.GREEN)
        term_res_1b = Text("FAILED  tests/test_oauth_rbac.py::test_expired_jwt_rejected", font_size=9.5, weight=BOLD, color=Palette.RED)
        term_res_1c = Text("AssertionError: Expected HTTP 401 Unauthorized, got 200 OK", font_size=9.2, color=Palette.RED)
        term_fail_block = VGroup(term_cmd_1, term_res_1a, term_res_1b, term_res_1c).arrange(
            DOWN, aligned_edge=LEFT, buff=0.16
        ).move_to(term_box.get_center())

        self.play(
            FadeIn(coder["group"]),
            FadeIn(verifier["group"]),
            FadeIn(reviewer["group"]),
            Create(arc_c_to_v),
            Create(arc_v_to_r),
            Create(arc_r_to_c),
            FadeIn(lbl_cv),
            FadeIn(lbl_vr),
            FadeIn(lbl_rc),
            FadeIn(ide["group"]),
            FadeIn(code_box),
            FadeIn(code_file_tag),
            FadeIn(code_v1),
            FadeIn(term_box),
            run_time=1.6,
        )

        # --- Iteration 1: Coder sends patch -> Verifier runs -> FAILS! ---
        pkt_run1 = self._make_photon_packet(Palette.GREEN).move_to(coder["box"].get_right())
        self.play(
            MoveAlongPath(pkt_run1, arc_c_to_v),
            run_time=1.3,
        )
        self.play(
            FadeOut(pkt_run1),
            *self._update_agent_status(verifier, "RUNNING", Palette.TEAL, border_width=3.0),
            FadeIn(term_cmd_1, shift=RIGHT * 0.1),
            run_time=0.8,
        )
        self.play(FadeIn(term_res_1a, shift=RIGHT * 0.1), run_time=0.6)

        fail_shock = Circle(radius=0.35, color=Palette.RED, stroke_width=3.8).move_to(verifier["box"].get_center())
        self.play(
            FadeIn(term_res_1b, shift=RIGHT * 0.1),
            FadeIn(term_res_1c, shift=RIGHT * 0.1),
            *self._update_agent_status(verifier, "FAILED", Palette.RED, border_width=3.4),
            ide["outer"].animate.set_stroke(color=Palette.RED, width=3.0),
            term_box.animate.set_stroke(color=Palette.RED, width=2.0),
            fail_shock.animate.scale(3.0).set_opacity(0),
            run_time=1.2,
        )
        self.wait(3.2)  # Allow viewer to clearly read AssertionError!

        # --- Phase 2: Failure Trace -> Reviewer Diagnosis -> Critique to Coder ---
        pkt_err = self._make_photon_packet(Palette.RED).move_to(verifier["box"].get_left())
        self.play(
            arc_v_to_r.animate.set_color(Palette.RED),
            lbl_vr.animate.set_color(Palette.RED),
            MoveAlongPath(pkt_err, arc_v_to_r),
            run_time=1.4,
        )
        diag_note = Text(
            "DIAGNOSIS: verify_exp=False disables timestamp expiry validation!",
            font_size=9.5,
            weight=BOLD,
            color=Palette.AMBER,
        ).move_to(code_box.get_bottom() + UP * 0.22)

        self.play(
            FadeOut(pkt_err),
            *self._update_agent_status(reviewer, "DIAGNOSING", Palette.AMBER, border_width=3.2),
            FadeIn(diag_note, shift=UP * 0.1),
            run_time=1.1,
        )
        self.wait(2.5)

        pkt_critique = self._make_photon_packet(Palette.AMBER).move_to(reviewer["box"].get_top())
        self.play(
            arc_r_to_c.animate.set_color(Palette.AMBER),
            lbl_rc.animate.set_color(Palette.AMBER),
            MoveAlongPath(pkt_critique, arc_r_to_c),
            run_time=1.4,
        )
        self.play(
            FadeOut(pkt_critique),
            *self._update_agent_status(coder, "FIXING", Palette.AMBER, border_width=3.2),
            run_time=0.8,
        )

        # --- Phase 3: Live Git Diff Patch & Re-Verification ---
        code_diff = VGroup(
            Text('- return jwt.decode(token, KEY, options={"verify_exp": False})', font_size=9.2, color=Palette.RED),
            Text('+ return jwt.decode(token, KEY, algorithms=["HS256"], leeway=0)', font_size=9.2, weight=BOLD, color=Palette.GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(code_box.get_center() + DOWN * 0.04)

        self.play(
            FadeOut(code_v1),
            FadeOut(diag_note),
            FadeIn(code_diff, shift=UP * 0.1),
            code_box.animate.set_stroke(color=Palette.GREEN, width=1.8),
            run_time=1.2,
        )
        self.wait(2.8)  # Clear time to read the exact code patch diff!

        # Re-run Tests -> Green Exit 0!
        pkt_run2 = self._make_photon_packet(Palette.GREEN).move_to(coder["box"].get_right())
        self.play(
            *self._update_agent_status(coder, "PATCHED", Palette.GREEN, border_width=2.6),
            MoveAlongPath(pkt_run2, arc_c_to_v),
            FadeOut(term_fail_block),
            run_time=1.3,
        )

        term_cmd_2 = Text("$ pytest tests/test_oauth_rbac.py -v", font_size=10, weight=BOLD, color=Palette.CYAN)
        term_res_2a = Text("PASSED  tests/test_oauth_rbac.py::test_rbac_admin_role", font_size=9.5, color=Palette.GREEN)
        term_res_2b = Text("PASSED  tests/test_oauth_rbac.py::test_expired_jwt_rejected", font_size=9.5, weight=BOLD, color=Palette.GREEN)
        term_res_2c = Text(">> 24 passed, 0 failed in 0.42s  [EXIT CODE 0]", font_size=10, weight=BOLD, color=Palette.GREEN)
        term_pass_block = VGroup(term_cmd_2, term_res_2a, term_res_2b, term_res_2c).arrange(
            DOWN, aligned_edge=LEFT, buff=0.16
        ).move_to(term_box.get_center())

        pass_shock = Circle(radius=0.35, color=Palette.GREEN, stroke_width=4.0).move_to(verifier["box"].get_center())
        self.play(
            FadeOut(pkt_run2),
            FadeIn(term_cmd_2),
            FadeIn(term_res_2a),
            FadeIn(term_res_2b),
            run_time=1.0,
        )
        self.play(
            FadeIn(term_res_2c, shift=UP * 0.08),
            pass_shock.animate.scale(3.4).set_opacity(0),
            *self._update_agent_status(verifier, "VERIFIED", Palette.GREEN, border_width=3.2),
            *self._update_agent_status(reviewer, "APPROVED", Palette.GREEN, border_width=2.6),
            ide["outer"].animate.set_stroke(color=Palette.GREEN, width=3.0),
            term_box.animate.set_stroke(color=Palette.GREEN, width=2.2),
            arc_v_to_r.animate.set_color(Palette.GREEN),
            arc_r_to_c.animate.set_color(Palette.GREEN),
            run_time=1.3,
        )
        self.wait(3.8)

        self._clear_stage(run_time=0.8)

    # =========================================================================
    # SCENE 5: DISTRIBUTED CONSENSUS, MERGE & TELEMETRY OUTRO (~26s)
    # =========================================================================

    def play_scene_5_consensus_outro(self):
        header = self._make_scene_header(
            "05 / CONSENSUS & PRODUCTION SYNTHESIS",
            "Quorum Approval, Branch Merge & Telemetry",
            "Verified code converges safely into production without human bottlenecks",
            accent=Palette.GOLD,
        )
        self.play(
            *self._activate_chapter(4, accent=Palette.GOLD),
            FadeIn(header, shift=DOWN * 0.15),
            run_time=0.9,
        )

        # Row 1: 4 Agent Consensus Cards
        agents_meta = [
            ("Architect", "Spec Match", Palette.PURPLE, -4.65),
            ("Coder", "Clean Diff", Palette.GREEN, -1.55),
            ("Reviewer", "Zero Vulns", Palette.AMBER, 1.55),
            ("Verifier", "24/24 Pass", Palette.TEAL, 4.65),
        ]
        consensus_cards = []
        for name, detail, clr, x_pos in agents_meta:
            c = self._make_agent_card(
                name, "QUORUM", detail, "APPROVE", clr, pos=[x_pos, 1.85, 0], width=2.75, height=1.15
            )
            consensus_cards.append(c)

        # Central Quorum Seal
        seal_box = RoundedRectangle(
            width=4.6,
            height=0.56,
            corner_radius=0.14,
            stroke_color=Palette.GOLD,
            stroke_width=2.6,
            fill_color="#1A1506",
            fill_opacity=0.98,
        ).move_to([0, 0.64, 0])
        seal_txt = Text("CONSENSUS LOCKED  •  QUORUM 4 / 4", font_size=11.5, weight=BOLD, color=Palette.GOLD).move_to(
            seal_box.get_center()
        )
        seal_group = VGroup(seal_box, seal_txt)

        vote_lines = VGroup(
            *[
                Line(c["box"].get_bottom(), seal_box.get_top(), color=Palette.GOLD, stroke_width=1.8)
                for c in consensus_cards
            ]
        )

        self.play(
            *[FadeIn(c["group"], shift=DOWN * 0.15) for c in consensus_cards],
            run_time=1.0,
        )

        pkts = [self._make_photon_packet(Palette.GOLD, scale=0.85).move_to(c["box"].get_bottom()) for c in consensus_cards]
        self.play(
            Create(vote_lines),
            *[pkts[i].animate.move_to(seal_box.get_top()) for i in range(4)],
            run_time=1.4,
        )
        seal_pulse = Circle(radius=0.35, color=Palette.GOLD, stroke_width=3.8).move_to(seal_box.get_center())
        self.play(
            *[FadeOut(p) for p in pkts],
            FadeIn(seal_group, scale=0.85),
            seal_pulse.animate.scale(3.5).set_opacity(0),
            *[c["box"].animate.set_stroke(color=Palette.GOLD, width=2.4) for c in consensus_cards],
            run_time=1.0,
        )

        # Row 2: Git Branch Merge Visualizer (cleanly separated from seal_box & text)
        main_line = Line([-4.6, -0.62, 0], [2.6, -0.62, 0], color=Palette.CYAN, stroke_width=3.2)
        branch_a = CubicBezier(
            [-3.8, -0.62, 0], [-2.8, -0.10, 0], [0.2, -0.10, 0], [1.2, -0.62, 0],
            color=Palette.GREEN, stroke_width=2.6
        )
        branch_b = CubicBezier(
            [-2.6, -0.62, 0], [-1.5, -1.12, 0], [1.0, -1.12, 0], [2.1, -0.62, 0],
            color=Palette.PURPLE, stroke_width=2.6
        )
        node_start = Dot([-4.6, -0.62, 0], radius=0.11, color=Palette.CYAN)
        node_merge = Dot([2.6, -0.62, 0], radius=0.15, color=Palette.GREEN)
        lbl_main = Text("main", font_size=10.5, weight=BOLD, color=Palette.CYAN).next_to(node_start, LEFT, buff=0.18)
        lbl_feat_a = Text("feat/oauth2", font_size=9.5, weight=BOLD, color=Palette.GREEN).move_to([-1.3, 0.04, 0])
        lbl_feat_b = Text("feat/rbac", font_size=9.5, weight=BOLD, color=Palette.PURPLE).move_to([-0.25, -1.24, 0])
        lbl_ship = Text("v2.0-auth-rbac [DEPLOYED]", font_size=10.5, weight=BOLD, color=Palette.GREEN).next_to(
            node_merge, RIGHT, buff=0.18
        )

        git_group = VGroup(main_line, branch_a, branch_b, node_start, node_merge, lbl_main, lbl_feat_a, lbl_feat_b, lbl_ship)
        self.play(
            Create(main_line),
            FadeIn(node_start),
            FadeIn(lbl_main),
            Create(branch_a),
            Create(branch_b),
            FadeIn(lbl_feat_a),
            FadeIn(lbl_feat_b),
            run_time=1.8,
        )
        self.play(
            FadeIn(node_merge, scale=1.4),
            FadeIn(lbl_ship, shift=RIGHT * 0.15),
            run_time=1.0,
        )

        # Row 3: Telemetry Impact Dashboard (3 Stat Cards)
        def make_stat_card(val, title, sub, clr, x_pos):
            sb = RoundedRectangle(
                width=3.6,
                height=1.22,
                corner_radius=0.15,
                stroke_color=clr,
                stroke_width=2.0,
                fill_color=Palette.SURFACE,
                fill_opacity=0.97,
            ).move_to([x_pos, -2.28, 0])
            t_val = Text(val, font_size=26, weight=BOLD, color=clr).move_to(sb.get_center() + UP * 0.24)
            t_tit = Text(title, font_size=11.5, weight=BOLD, color=Palette.TEXT_PRIMARY).move_to(sb.get_center() + DOWN * 0.15)
            t_sub = Text(sub, font_size=9.5, color=Palette.TEXT_MUTED).move_to(sb.get_center() + DOWN * 0.40)
            return VGroup(sb, t_val, t_tit, t_sub)

        stat1 = make_stat_card("4.8x", "Parallel Execution Speedup", "Concurrent DAG Sharding", Palette.CYAN, -4.15)
        stat2 = make_stat_card("+68%", "Context Token Efficiency", "Bounded Worker Windows", Palette.PURPLE, 0.0)
        stat3 = make_stat_card("0", "Human Interventions", "Self-Correcting Tool Loop", Palette.GREEN, 4.15)

        self.play(
            FadeIn(stat1, shift=UP * 0.2),
            FadeIn(stat2, shift=UP * 0.2),
            FadeIn(stat3, shift=UP * 0.2),
            run_time=1.3,
        )
        self.wait(4.0)

        # Clear Scene 5 Workspace for Final Cinematic Outro
        self._clear_stage(
            run_time=0.9,
            extra_anims=self._activate_chapter(5, accent=Palette.GREEN),
        )

        # Cinematic Outro Emblem & Closing CTA
        emblem_ring = Circle(radius=0.72, color=Palette.CYAN, stroke_width=2.6).move_to([0, 1.55, 0])
        emblem_nodes = VGroup(
            Dot([0, 2.27, 0], radius=0.11, color=Palette.PURPLE),
            Dot([0.72, 1.55, 0], radius=0.11, color=Palette.GREEN),
            Dot([0, 0.83, 0], radius=0.11, color=Palette.TEAL),
            Dot([-0.72, 1.55, 0], radius=0.11, color=Palette.AMBER),
            Dot([0, 1.55, 0], radius=0.14, color=Palette.CYAN),
        )
        emblem_cross = VGroup(
            Line([-0.72, 1.55, 0], [0.72, 1.55, 0], color=Palette.CYAN, stroke_width=1.4, stroke_opacity=0.6),
            Line([0, 0.83, 0], [0, 2.27, 0], color=Palette.CYAN, stroke_width=1.4, stroke_opacity=0.6),
        )
        emblem = VGroup(emblem_ring, emblem_cross, emblem_nodes)

        outro_title = Text(
            "Autonomous Multi-Agent Swarms",
            font_size=40,
            weight=BOLD,
            color=Palette.TEXT_PRIMARY,
        ).move_to([0, -0.05, 0])

        outro_sub = Text(
            "Decompose   •   Coordinate   •   Self-Correct   •   Ship",
            font_size=17,
            weight=BOLD,
            color=Palette.CYAN,
        ).next_to(outro_title, DOWN, buff=0.28)

        outro_pill = RoundedRectangle(
            width=7.8,
            height=0.72,
            corner_radius=0.16,
            stroke_color=Palette.CYAN,
            stroke_width=1.8,
            fill_color=Palette.SURFACE,
            fill_opacity=0.95,
        ).next_to(outro_sub, DOWN, buff=0.45)
        outro_cta = Text(
            "Built for Deterministic, Production-Grade AI Engineering",
            font_size=14,
            weight=BOLD,
            color=Palette.TEXT_SECONDARY,
        ).move_to(outro_pill.get_center())

        self.play(
            Create(emblem_ring),
            Create(emblem_cross),
            FadeIn(emblem_nodes, scale=0.6),
            run_time=1.3,
        )
        self.play(
            FadeIn(outro_title, shift=UP * 0.15),
            FadeIn(outro_sub, shift=UP * 0.12),
            run_time=1.2,
        )
        self.play(FadeIn(outro_pill, shift=UP * 0.1), FadeIn(outro_cta), run_time=0.9)
        self.wait(4.5)


# Backwards-compatible alias
SwarmOrchestration = MultiAgentSwarm
