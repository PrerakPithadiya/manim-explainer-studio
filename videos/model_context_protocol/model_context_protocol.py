"""
Model Context Protocol (MCP) - World-Class Developer Explainer Video
Engineered with Manim Community Edition.

Master Edition Enhancements:
1. Cinematic Studio Dark Aesthetic with Obsidian Void (#070A12) & Neon Highlights.
2. Glassmorphism IDE-style Cards with Mac/Linux Window Header Controls.
3. Curved Tangled Cables Hook with Dynamic Shockwave Transformation.
4. Explains the 3 Core MCP Primitives: Resources, Tools, and Prompts.
5. Highlights Transports: stdio (Local) & SSE (Remote HTTP).
6. Multi-Layer Glowing Photon Comets with Particle Trailing Trails.
7. Authentic JSON-RPC Payloads & Real-world GitHub PR Lookup Workflow.
8. Generous pacing and visual breathing room so developers can comfortably read payloads.
9. High-Impact Call-to-Action End Card with Visual Depth.
"""

import numpy as np
from manim import *


class ModelContextProtocol(Scene):
    """World-class animated explainer illustrating Model Context Protocol architecture & execution."""

    def construct(self):
        # =============================================================
        # 0. GLOBAL CINEMATIC PALETTE & CONFIGURATION
        # =============================================================
        self.camera.background_color = "#070A12"  # Ultra-deep obsidian tech background

        # Neon Accents & Cyber Tones
        ACCENT_CYAN = "#38BDF8"       # Primary protocol & MCP cyan
        ACCENT_PURPLE = "#A855F7"     # AI Intelligence & Client purple
        CHAOS_RED = "#F43F5E"         # Tangled spaghetti warning crimson
        SUCCESS_GREEN = "#10B981"     # Verified execution & live data green
        CODE_AMBER = "#F59E0B"        # Method & JSON property accent
        
        # Typography & Glassmorphism Surfaces
        TEXT_PRIMARY = "#FFFFFF"      # Pure brilliant white
        TEXT_SECONDARY = "#E2E8F0"    # Crisp light slate
        TEXT_MUTED = "#94A3B8"        # Soft muted slate
        SURFACE_CARD = "#0F172A"      # Translucent dark slate surface
        CARD_BORDER = "#1E293B"       # Subtle border slate
        CODE_BG = "#030712"           # Terminal dark obsidian fill

        # Helper: Terminal window title bar dots (Mac/Linux IDE aesthetic)
        def make_window_dots():
            return VGroup(
                Dot(radius=0.045, color="#EF4444"),
                Dot(radius=0.045, color="#F59E0B"),
                Dot(radius=0.045, color="#10B981"),
            ).arrange(RIGHT, buff=0.08)

        # Helper: Multi-layer photon packet with glowing comet tail
        def create_photon_packet(color=ACCENT_CYAN):
            core = Dot(radius=0.09, color="#FFFFFF")
            inner_halo = Dot(radius=0.16, color=color).set_opacity(0.7)
            outer_glow = Dot(radius=0.26, color=color).set_opacity(0.3)
            # Trailing tail particles
            tail1 = Dot(radius=0.065, color=color).set_opacity(0.45).shift(LEFT * 0.14)
            tail2 = Dot(radius=0.045, color=color).set_opacity(0.22).shift(LEFT * 0.25)
            return VGroup(outer_glow, inner_halo, tail1, tail2, core)

        # =============================================================
        # 1. ACT I: THE "BEFORE VS AFTER" HOOK (M x N CHAOS -> M + N) (~7.0s)
        # =============================================================
        hook_badge = Text(
            "THE DEVELOPER INTEGRATION NIGHTMARE",
            font_size=12,
            weight=BOLD,
            color=CHAOS_RED,
        ).shift(UP * 2.85)

        hook_title = Text(
            "Before MCP: The M x N Problem",
            font_size=25,
            weight=BOLD,
            color=TEXT_PRIMARY,
        ).next_to(hook_badge, DOWN, buff=0.14)

        hook_subtitle = Text(
            "Every AI client requires brittle, custom glue code for every tool",
            font_size=14,
            color=TEXT_MUTED,
        ).next_to(hook_title, DOWN, buff=0.12)

        hook_headers = VGroup(hook_badge, hook_title, hook_subtitle)

        # AI Clients (Left Side)
        ai_data = [("Claude", 1.05), ("ChatGPT", 0.0), ("Cursor", -1.05)]
        ai_nodes = VGroup()
        for name, y in ai_data:
            box = RoundedRectangle(
                width=1.9,
                height=0.62,
                corner_radius=0.14,
                stroke_color=ACCENT_PURPLE,
                stroke_width=1.8,
                fill_color=SURFACE_CARD,
                fill_opacity=0.95,
            ).move_to([-4.5, y, 0])
            dots = make_window_dots().move_to(box.get_top() + DOWN * 0.12 + LEFT * 0.5)
            lbl = Text(name, font_size=13, weight=BOLD, color=TEXT_PRIMARY).move_to(box.get_center() + DOWN * 0.04)
            ai_nodes.add(VGroup(box, dots, lbl))

        # Tools & Services (Right Side)
        tool_data = [("GitHub", 1.2), ("Slack", 0.4), ("Postgres", -0.4), ("Files", -1.2)]
        tool_nodes = VGroup()
        for name, y in tool_data:
            box = RoundedRectangle(
                width=1.9,
                height=0.55,
                corner_radius=0.14,
                stroke_color=CARD_BORDER,
                stroke_width=1.8,
                fill_color=SURFACE_CARD,
                fill_opacity=0.95,
            ).move_to([4.5, y, 0])
            lbl = Text(name, font_size=12, weight=BOLD, color=TEXT_SECONDARY).move_to(box.get_center())
            tool_nodes.add(VGroup(box, lbl))

        # 12 Tangled, Curved Spaghetti Cables
        spaghetti_cables = VGroup()
        for i, ai in enumerate(ai_nodes):
            for j, t in enumerate(tool_nodes):
                y_delta = (j - 1.5) * 0.35 - (i - 1.0) * 0.25
                mid1 = np.array([-1.5, ai.get_y() + y_delta, 0])
                mid2 = np.array([1.5, t.get_y() - y_delta, 0])
                cable = CubicBezier(
                    ai.get_right(),
                    mid1,
                    mid2,
                    t.get_left(),
                    color=CHAOS_RED,
                    stroke_width=1.5,
                    stroke_opacity=0.6,
                )
                spaghetti_cables.add(cable)

        # Entrance: The Chaos Appears
        self.play(FadeIn(hook_headers, shift=DOWN * 0.15), run_time=0.6)
        self.play(
            FadeIn(ai_nodes, shift=RIGHT * 0.25),
            FadeIn(tool_nodes, shift=LEFT * 0.25),
            Create(spaghetti_cables),
            run_time=1.3,
        )
        self.wait(1.2)  # Ample time to appreciate the chaotic tangle

        # --- The MCP Solution Shockwave ---
        mcp_hub_box = RoundedRectangle(
            width=2.5,
            height=1.4,
            corner_radius=0.2,
            stroke_color=ACCENT_CYAN,
            stroke_width=3.2,
            fill_color="#091224",
            fill_opacity=0.98,
        ).move_to(ORIGIN)

        mcp_hub_badge = Text("UNIVERSAL STANDARD", font_size=8, weight=BOLD, color=ACCENT_CYAN).move_to(
            mcp_hub_box.get_top() + DOWN * 0.22
        )
        mcp_hub_lbl = Text("MCP Hub", font_size=19, weight=BOLD, color=TEXT_PRIMARY).next_to(
            mcp_hub_badge, DOWN, buff=0.1
        )
        mcp_hub_sub = Text("Open Protocol", font_size=11, color=TEXT_MUTED).next_to(
            mcp_hub_lbl, DOWN, buff=0.08
        )
        mcp_hub_group = VGroup(mcp_hub_box, mcp_hub_badge, mcp_hub_lbl, mcp_hub_sub)

        # Clean fiber-optic conduits to MCP Hub
        hub_clean_conduits = VGroup(
            *[Line(ai.get_right(), mcp_hub_box.get_left(), color=ACCENT_CYAN, stroke_width=2.6) for ai in ai_nodes],
            *[Line(mcp_hub_box.get_right(), t.get_left(), color=ACCENT_CYAN, stroke_width=2.6) for t in tool_nodes],
        )

        solution_title = Text(
            "With MCP: Clean M + N Simplicity!",
            font_size=25,
            weight=BOLD,
            color=ACCENT_CYAN,
        ).move_to(hook_title.get_center())

        solution_subtitle = Text(
            "Every AI connects to every tool through one open, universal protocol",
            font_size=14,
            color=TEXT_SECONDARY,
        ).move_to(hook_subtitle.get_center())

        shockwave = Circle(radius=0.3, color=ACCENT_CYAN, stroke_width=4.0).move_to(ORIGIN)

        self.play(
            FadeIn(mcp_hub_group, scale=0.7),
            shockwave.animate.scale(14).set_opacity(0),
            ReplacementTransform(spaghetti_cables, hub_clean_conduits),
            Transform(hook_title, solution_title),
            Transform(hook_subtitle, solution_subtitle),
            run_time=1.3,
        )
        self.wait(1.5)  # Let viewer absorb the clean resolution

        hook_all = VGroup(
            hook_headers,
            ai_nodes,
            tool_nodes,
            mcp_hub_group,
            hub_clean_conduits,
            solution_title,
            solution_subtitle,
            shockwave,
        )
        self.play(FadeOut(hook_all, shift=DOWN * 0.2), run_time=0.7)

        # =============================================================
        # 2. ACT II: TITLE CARD & THE 3 MCP PRIMITIVES (~6.5s)
        # =============================================================
        title_tag = Text(
            "PROTOCOL SPECIFICATION",
            font_size=13,
            weight=BOLD,
            color=ACCENT_CYAN,
        ).shift(UP * 2.1)

        title_h1 = Text(
            "How MCP Works",
            font_size=46,
            weight=BOLD,
            color=TEXT_PRIMARY,
        ).next_to(title_tag, DOWN, buff=0.22)

        title_glow_line = Line(
            LEFT * 3.8, RIGHT * 3.8,
            color=ACCENT_CYAN,
            stroke_width=2.5,
        ).next_to(title_h1, DOWN, buff=0.2)

        # The 3 Core Primitives of MCP
        def make_primitive_badge(icon, name, role, color):
            bg = RoundedRectangle(
                width=3.4,
                height=0.9,
                corner_radius=0.14,
                stroke_color=color,
                stroke_width=1.6,
                fill_color=SURFACE_CARD,
                fill_opacity=0.95,
            )
            t_icon = Text(icon, font_size=16, color=color).move_to(bg.get_left() + RIGHT * 0.45)
            t_name = Text(name, font_size=14, weight=BOLD, color=TEXT_PRIMARY).next_to(t_icon, RIGHT, buff=0.25).shift(UP * 0.12)
            t_role = Text(role, font_size=10, color=TEXT_MUTED).next_to(t_name, DOWN, buff=0.08, aligned_edge=LEFT)
            return VGroup(bg, t_icon, t_name, t_role)

        badge_res = make_primitive_badge("[R]", "Resources", "Direct Context & Files", ACCENT_CYAN)
        badge_tools = make_primitive_badge("[T]", "Tools", "Executable Actions & APIs", SUCCESS_GREEN)
        badge_prompts = make_primitive_badge("[P]", "Prompts", "Interactive Templates", ACCENT_PURPLE)

        primitives_group = VGroup(badge_res, badge_tools, badge_prompts).arrange(RIGHT, buff=0.35).next_to(title_glow_line, DOWN, buff=0.55)

        self.play(
            FadeIn(title_tag, shift=UP * 0.15),
            FadeIn(title_h1, shift=UP * 0.15),
            GrowFromCenter(title_glow_line),
            run_time=0.8,
        )
        self.play(
            FadeIn(badge_res, shift=UP * 0.15),
            FadeIn(badge_tools, shift=UP * 0.15),
            FadeIn(badge_prompts, shift=UP * 0.15),
            run_time=0.9,
        )
        self.wait(2.2)  # Ample time to register the 3 pillars of MCP

        title_all = VGroup(title_tag, title_h1, title_glow_line, primitives_group)
        self.play(FadeOut(title_all, shift=DOWN * 0.2), run_time=0.7)

        # =============================================================
        # 3. ACT III: THE 3-TIER ARCHITECTURE & CONCRETE SCENARIO (~5.5s)
        # =============================================================
        header_text = Text(
            "Model Context Protocol in Action",
            font_size=23,
            weight=BOLD,
            color=ACCENT_CYAN,
        ).to_edge(UP, buff=0.55)

        def make_tech_card(title, role, meta, pos, border_color=CARD_BORDER, badge_color=ACCENT_CYAN):
            card = RoundedRectangle(
                width=3.25,
                height=2.3,
                corner_radius=0.18,
                stroke_color=border_color,
                stroke_width=2.2,
                fill_color=SURFACE_CARD,
                fill_opacity=0.96,
            ).move_to(pos)

            dots = make_window_dots().move_to(card.get_top() + DOWN * 0.22 + LEFT * 0.95)
            badge = Text(role.upper(), font_size=9, weight=BOLD, color=badge_color).move_to(
                card.get_top() + DOWN * 0.22 + RIGHT * 0.45
            )

            t_title = Text(title, font_size=19, weight=BOLD, color=TEXT_PRIMARY).move_to(
                card.get_center() + UP * 0.2
            )
            t_meta = Text(meta, font_size=12, color=TEXT_MUTED).move_to(
                card.get_center() + DOWN * 0.35
            )

            return card, VGroup(card, dots, badge, t_title, t_meta)

        # 1. Left Node: AI Client (Host App)
        card_client, client_group = make_tech_card(
            "AI Client",
            "Host App",
            "Claude, Cursor, IDE",
            LEFT * 4.4 + UP * 0.45,
            border_color=ACCENT_PURPLE,
            badge_color=ACCENT_PURPLE,
        )

        # 2. Middle Node: MCP Server (Universal Bridge)
        card_server, server_group = make_tech_card(
            "MCP Server",
            "Protocol Bridge",
            "stdio / SSE Transport",
            ORIGIN + UP * 0.45,
            border_color=ACCENT_CYAN,
            badge_color=ACCENT_CYAN,
        )

        # 3. Right Node: GitHub Tool (Resource)
        card_tools, tools_group = make_tech_card(
            "GitHub Tool",
            "Target Resource",
            "PRs, Issues, Repos",
            RIGHT * 4.4 + UP * 0.45,
            border_color=CARD_BORDER,
            badge_color=SUCCESS_GREEN,
        )

        # Conduits: Forward Request Flow (Left -> Right)
        req_conduit_1 = Arrow(
            start=[-2.75, 0.9, 0],
            end=[-1.65, 0.9, 0],
            buff=0,
            color=ACCENT_CYAN,
            stroke_width=3.5,
            max_tip_length_to_length_ratio=0.28,
        )
        req_conduit_2 = Arrow(
            start=[1.65, 0.9, 0],
            end=[2.75, 0.9, 0],
            buff=0,
            color=ACCENT_CYAN,
            stroke_width=3.5,
            max_tip_length_to_length_ratio=0.28,
        )

        # Conduits: Reverse Response Flow (Right -> Left)
        res_conduit_1 = Arrow(
            start=[2.75, 0.0, 0],
            end=[1.65, 0.0, 0],
            buff=0,
            color=TEXT_MUTED,
            stroke_width=3.5,
            max_tip_length_to_length_ratio=0.28,
        )
        res_conduit_2 = Arrow(
            start=[-1.65, 0.0, 0],
            end=[-2.75, 0.0, 0],
            buff=0,
            color=TEXT_MUTED,
            stroke_width=3.5,
            max_tip_length_to_length_ratio=0.28,
        )

        lbl_req1 = Text("1. tools/call", font_size=11, weight=BOLD, color=ACCENT_CYAN).next_to(req_conduit_1, UP, buff=0.1)
        lbl_req2 = Text("2. REST API", font_size=11, weight=BOLD, color=ACCENT_CYAN).next_to(req_conduit_2, UP, buff=0.1)
        lbl_res1 = Text("3. Raw Data", font_size=11, color=TEXT_MUTED).next_to(res_conduit_1, DOWN, buff=0.1)
        lbl_res2 = Text("4. Context", font_size=11, color=TEXT_MUTED).next_to(res_conduit_2, DOWN, buff=0.1)
        conduit_labels = VGroup(lbl_req1, lbl_req2, lbl_res1, lbl_res2)

        # Concrete Scenario: User Prompt Bubble
        user_prompt_bubble = RoundedRectangle(
            width=3.5,
            height=0.68,
            corner_radius=0.14,
            stroke_color=ACCENT_PURPLE,
            stroke_width=1.6,
            fill_color="#110E24",
            fill_opacity=0.98,
        ).next_to(card_client, UP, buff=0.25)
        user_prompt_txt = Text(
            'User: "Find my open PRs on GitHub"',
            font_size=12,
            weight=BOLD,
            color=TEXT_PRIMARY,
        ).move_to(user_prompt_bubble.get_center())
        user_prompt_group = VGroup(user_prompt_bubble, user_prompt_txt)

        self.play(FadeIn(header_text, shift=DOWN * 0.15), run_time=0.6)
        self.play(
            FadeIn(client_group, shift=RIGHT * 0.25),
            FadeIn(server_group, shift=UP * 0.25),
            FadeIn(tools_group, shift=LEFT * 0.25),
            run_time=0.9,
        )
        self.play(
            GrowArrow(req_conduit_1),
            GrowArrow(req_conduit_2),
            GrowArrow(res_conduit_1),
            GrowArrow(res_conduit_2),
            FadeIn(conduit_labels),
            run_time=0.9,
        )
        self.play(FadeIn(user_prompt_group, shift=DOWN * 0.1), run_time=0.6)
        self.wait(1.2)

        # =============================================================
        # 4. STEP CONTAINER: IDE CONSOLE PAYLOAD VIEWER
        # =============================================================
        console_container = RoundedRectangle(
            width=11.2,
            height=1.55,
            corner_radius=0.16,
            stroke_color=CARD_BORDER,
            stroke_width=1.8,
            fill_color=SURFACE_CARD,
            fill_opacity=0.98,
        ).move_to([0, -2.48, 0])

        def make_step_console(step_num, title, method_tag, payload_text, tag_color=ACCENT_CYAN, code_color=ACCENT_CYAN):
            badge = Text(f"STEP {step_num}", font_size=11, weight=BOLD, color=tag_color)
            headline = Text(title, font_size=15, weight=BOLD, color=TEXT_PRIMARY)
            top_bar = VGroup(badge, headline).arrange(RIGHT, buff=0.22)

            code_box = RoundedRectangle(
                width=10.4,
                height=0.48,
                corner_radius=0.1,
                fill_color=CODE_BG,
                fill_opacity=0.95,
                stroke_color="#1E293B",
                stroke_width=1.2,
            )
            p_tag = Text(method_tag, font_size=11, weight=BOLD, color=CODE_AMBER)
            p_val = Text(payload_text, font_size=12, weight=BOLD, color=code_color)
            payload_row = VGroup(p_tag, p_val).arrange(RIGHT, buff=0.2).move_to(code_box.get_center())
            terminal_strip = VGroup(code_box, payload_row)

            step_widget = VGroup(top_bar, terminal_strip).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
            step_widget.move_to(console_container.get_center())
            return step_widget

        step1_console = make_step_console(
            "1",
            "AI Client sends standard JSON-RPC tool request to MCP Server",
            "JSON-RPC REQUEST:",
            '{"method": "tools/call", "params": {"name": "github.list_prs"}}',
            tag_color=ACCENT_CYAN,
            code_color=ACCENT_CYAN,
        )

        step2_console = make_step_console(
            "2",
            "MCP Server translates standard call to GitHub REST API",
            "HTTP REST CALL:",
            'GET https://api.github.com/repos/octocat/repo/pulls?state=open',
            tag_color=ACCENT_CYAN,
            code_color=ACCENT_CYAN,
        )

        step3_console = make_step_console(
            "3",
            "Structured response returns through MCP as clean LLM context",
            "STRUCTURED CONTEXT:",
            '{"prs": [{"id": 42, "title": "feat: mcp", "status": "Ready to merge"}]}',
            tag_color=SUCCESS_GREEN,
            code_color=SUCCESS_GREEN,
        )

        # =============================================================
        # 5. STEP 1: CLIENT -> MCP SERVER (JSON-RPC DISPATCH) (~6.0s)
        # =============================================================
        req_pill = RoundedRectangle(
            width=3.4,
            height=0.42,
            corner_radius=0.1,
            stroke_color=ACCENT_CYAN,
            stroke_width=1.5,
            fill_color="#0A1628",
            fill_opacity=0.95,
        )
        req_pill_txt = Text(
            'tools/call: "github.list_prs"',
            font_size=11,
            weight=BOLD,
            color=ACCENT_CYAN,
        ).move_to(req_pill.get_center())
        req_pill_group = VGroup(req_pill, req_pill_txt).next_to(req_conduit_1, UP, buff=0.25)

        self.play(
            FadeIn(console_container),
            FadeIn(step1_console, shift=UP * 0.1),
            FadeIn(req_pill_group, shift=DOWN * 0.1),
            card_client.animate.set_stroke(color=ACCENT_PURPLE, width=4.0),
            run_time=0.8,
        )

        packet1 = create_photon_packet(ACCENT_CYAN)
        self.play(
            MoveAlongPath(packet1, req_conduit_1),
            req_pill_group.animate.shift(RIGHT * 1.1),
            run_time=1.8,
        )

        # Server impact ripple
        server_ripple = Circle(radius=0.4, color=ACCENT_CYAN, stroke_width=3.5).move_to(card_server.get_center())
        self.play(
            card_client.animate.set_stroke(color=CARD_BORDER, width=2.2),
            card_server.animate.set_stroke(color=ACCENT_CYAN, width=4.0),
            FadeOut(packet1),
            FadeOut(req_pill_group),
            server_ripple.animate.scale(3.2).set_opacity(0),
            run_time=0.8,
        )
        self.wait(1.8)  # Full breathing room to read the JSON-RPC payload

        # =============================================================
        # 6. STEP 2: MCP SERVER -> GITHUB EXECUTION (~5.5s)
        # =============================================================
        self.play(
            FadeOut(step1_console, shift=UP * 0.1),
            FadeIn(step2_console, shift=UP * 0.1),
            run_time=0.6,
        )

        exec_pill = RoundedRectangle(
            width=3.2,
            height=0.42,
            corner_radius=0.1,
            stroke_color=ACCENT_CYAN,
            stroke_width=1.5,
            fill_color="#0A1628",
            fill_opacity=0.95,
        )
        exec_pill_txt = Text(
            'GET /pulls?state=open',
            font_size=11,
            weight=BOLD,
            color=ACCENT_CYAN,
        ).move_to(exec_pill.get_center())
        exec_pill_group = VGroup(exec_pill, exec_pill_txt).next_to(req_conduit_2, UP, buff=0.25)

        self.play(FadeIn(exec_pill_group, shift=DOWN * 0.1), run_time=0.4)

        packet2 = create_photon_packet(ACCENT_CYAN)
        self.play(
            MoveAlongPath(packet2, req_conduit_2),
            exec_pill_group.animate.shift(RIGHT * 1.1),
            run_time=1.8,
        )

        tool_ripple = Circle(radius=0.4, color=SUCCESS_GREEN, stroke_width=3.5).move_to(card_tools.get_center())
        self.play(
            card_server.animate.set_stroke(color=CARD_BORDER, width=2.2),
            card_tools.animate.set_stroke(color=SUCCESS_GREEN, width=4.0),
            FadeOut(packet2),
            FadeOut(exec_pill_group),
            tool_ripple.animate.scale(3.2).set_opacity(0),
            run_time=0.8,
        )
        self.wait(1.6)  # Breathing room for API execution step

        # =============================================================
        # 7. STEP 3: DATA RETURNS AS CLEAN CONTEXT (~7.8s)
        # =============================================================
        self.play(
            FadeOut(step2_console, shift=UP * 0.1),
            FadeIn(step3_console, shift=UP * 0.1),
            run_time=0.6,
        )

        data_pill = RoundedRectangle(
            width=3.4,
            height=0.42,
            corner_radius=0.1,
            stroke_color=SUCCESS_GREEN,
            stroke_width=1.5,
            fill_color="#061A14",
            fill_opacity=0.95,
        )
        data_pill_txt = Text(
            '"PR #42: Ready to merge"',
            font_size=11,
            weight=BOLD,
            color=SUCCESS_GREEN,
        ).move_to(data_pill.get_center())
        data_pill_group = VGroup(data_pill, data_pill_txt).next_to(res_conduit_1, DOWN, buff=0.25)

        self.play(FadeIn(data_pill_group, shift=UP * 0.1), run_time=0.5)

        # Return journey part 1: Tool -> MCP Server
        return_pkt1 = create_photon_packet(SUCCESS_GREEN)
        self.play(
            MoveAlongPath(return_pkt1, res_conduit_1),
            data_pill_group.animate.shift(LEFT * 1.1),
            run_time=1.8,
        )

        # Server standardizes context
        server_return_ripple = Circle(radius=0.4, color=ACCENT_CYAN, stroke_width=3.5).move_to(card_server.get_center())
        self.play(
            card_tools.animate.set_stroke(color=CARD_BORDER, width=2.2),
            card_server.animate.set_stroke(color=ACCENT_CYAN, width=4.0),
            FadeOut(return_pkt1),
            server_return_ripple.animate.scale(3.2).set_opacity(0),
            run_time=0.8,
        )

        # Return journey part 2: MCP Server -> AI Client
        return_pkt2 = create_photon_packet(SUCCESS_GREEN)
        self.play(
            MoveAlongPath(return_pkt2, res_conduit_2),
            data_pill_group.animate.shift(LEFT * 2.8),
            run_time=1.8,
        )

        # AI Client receives context and delivers synthesis
        ai_resp_bubble = RoundedRectangle(
            width=4.2,
            height=0.68,
            corner_radius=0.14,
            stroke_color=SUCCESS_GREEN,
            stroke_width=1.6,
            fill_color="#061C14",
            fill_opacity=0.98,
        ).next_to(card_client, DOWN, buff=0.25)
        ai_resp_txt = Text(
            'AI: "Found 1 open PR: #42 Ready to merge"',
            font_size=11,
            weight=BOLD,
            color=SUCCESS_GREEN,
        ).move_to(ai_resp_bubble.get_center())
        ai_resp_group = VGroup(ai_resp_bubble, ai_resp_txt)

        client_ripple = Circle(radius=0.4, color=SUCCESS_GREEN, stroke_width=3.5).move_to(card_client.get_center())
        self.play(
            card_server.animate.set_stroke(color=CARD_BORDER, width=2.2),
            card_client.animate.set_stroke(color=SUCCESS_GREEN, width=4.0),
            FadeOut(return_pkt2),
            FadeOut(data_pill_group),
            FadeIn(ai_resp_group, shift=UP * 0.1),
            client_ripple.animate.scale(3.2).set_opacity(0),
            run_time=0.9,
        )
        self.wait(2.2)  # Generous time to read the successful AI synthesis

        # =============================================================
        # 8. ACT IV: THE USB-C METAPHOR & VALUE TAKEAWAY (~3.2s)
        # =============================================================
        recap_banner = Text(
            'The "USB-C for AI" Standard: Connect Any Model to Any Tool',
            font_size=18,
            weight=BOLD,
            color=ACCENT_CYAN,
        ).move_to(console_container.get_center())

        self.play(
            FadeOut(step3_console),
            FadeIn(recap_banner, shift=UP * 0.1),
            card_client.animate.set_stroke(color=ACCENT_CYAN, width=2.8),
            card_server.animate.set_stroke(color=ACCENT_CYAN, width=3.8),
            card_tools.animate.set_stroke(color=ACCENT_CYAN, width=2.8),
            run_time=0.8,
        )
        self.wait(2.4)

        # =============================================================
        # 9. ACT V: HIGH-IMPACT END CARD & CALL TO ACTION (~5.5s)
        # =============================================================
        diagram_elements = VGroup(
            header_text,
            client_group,
            server_group,
            tools_group,
            req_conduit_1,
            req_conduit_2,
            res_conduit_1,
            res_conduit_2,
            conduit_labels,
            user_prompt_group,
            ai_resp_group,
            console_container,
            recap_banner,
        )
        self.play(FadeOut(diagram_elements, shift=DOWN * 0.15), run_time=0.7)

        # Outro Badge
        end_badge = Text(
            "THE OPEN STANDARD FOR AGENTIC AI",
            font_size=13,
            weight=BOLD,
            color=ACCENT_CYAN,
        ).shift(UP * 1.85)

        end_title = Text(
            "Model Context Protocol",
            font_size=46,
            weight=BOLD,
            color=TEXT_PRIMARY,
        ).next_to(end_badge, DOWN, buff=0.25)

        end_tagline = Text(
            "Build Once. Connect Anywhere. Infinite AI Extensibility.",
            font_size=18,
            color=TEXT_SECONDARY,
        ).next_to(end_title, DOWN, buff=0.3)

        # Modern Interactive CTA Button with Double Neon Glow
        cta_border = RoundedRectangle(
            width=7.6,
            height=0.95,
            corner_radius=0.18,
            fill_color=ACCENT_CYAN,
            fill_opacity=1.0,
            stroke_width=0,
        )
        cta_text = Text(
            "Start Building with MCP Today!",
            font_size=20,
            weight=BOLD,
            color="#070A12",
        ).move_to(cta_border.get_center())
        cta_button = VGroup(cta_border, cta_text).next_to(end_tagline, DOWN, buff=0.5)

        sub_cta = Text(
            "Like & Save this video for your AI Engineering stack",
            font_size=13,
            color=TEXT_MUTED,
        ).next_to(cta_button, DOWN, buff=0.35)

        self.play(
            FadeIn(end_badge, shift=UP * 0.18),
            FadeIn(end_title, shift=UP * 0.18),
            run_time=0.8,
        )
        self.play(
            FadeIn(end_tagline, shift=UP * 0.12),
            FadeIn(cta_button, shift=UP * 0.18),
            FadeIn(sub_cta, shift=UP * 0.12),
            run_time=0.8,
        )
        self.wait(3.5)


# Alias for backwards compatibility
MCPFlow = ModelContextProtocol
