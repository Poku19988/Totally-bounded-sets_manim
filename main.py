from manim import *
import numpy as np

class Compact(Scene):
    def construct(self):
        ArabTexTemplate = TexTemplate(
            tex_compiler="xelatex",   
            output_format='.xdv',            
            preamble = r'''
\usepackage{polyglossia}\setotherlanguage{arabic}\newfontfamily\arabicfont[Script=Arabic]{B Nazanin}
            '''
        )
        # Title animation
        arabicText = Tex(
            r"به نام خدا",
            tex_template=ArabTexTemplate,
            tex_environment="Arabic"
        ).shift(UP*3)
        self.play(FadeIn(arabicText))
        self.wait(2)
        title = Text("Total boundedness", font_size=36)
        self.play(Write(title))
        self.wait(1.5)
        self.play(FadeOut(title))
        self.play(FadeOut(arabicText))
        self.wait(2)
        # Create and animate circle A (moving up as in original)
        circle_A = Circle(radius=2, color=BLUE, fill_opacity=0.3, stroke_width=4)
        circle_A.move_to(ORIGIN)
        self.play(Create(circle_A), run_time=1.5)
        
        # Move circle up (keeping your original animation)
        self.play(circle_A.animate.shift(UP*1.3), run_time=1.5)
        
        # Label the set
        A_label = Text("A", font_size=36).next_to(circle_A, DOWN, buff=0.7)
        self.play(Write(A_label))
        self.wait(1)
        
        # Create covering sets with proper stroke widths
        covering_sets = VGroup()
        
        # 1. Large covering set (thinner stroke)
        large_cover = Circle(radius=2.3, color=RED, fill_opacity=0.2, stroke_width=2)
        large_cover.move_to(circle_A.get_center() + RIGHT*0.3 + UP*0.2)
        
        # 2. Top cover (annulus with thin stroke)
        top_cover = Circle(radius=5.3, color=GREEN, fill_opacity=0.2, stroke_width=2)
        top_cover.move_to(circle_A.get_center() + UP*1.7)
        
        # 3. Bottom cover (annulus)
        bottom_cover = Circle(radius=2.3, color=YELLOW, fill_opacity=0.2, stroke_width=2)
        bottom_cover.move_to(circle_A.get_center() + DOWN*1.5)
        
        # 4. Left sector (thinner stroke)
        left_cover = Circle(radius=3.3, color=PURPLE, fill_opacity=0.2, stroke_width=2)
        left_cover.move_to(circle_A.get_center() + LEFT*1.4)
        
        # 5. Right sector
        right_cover = Circle(radius=1.3, color=ORANGE, fill_opacity=0.2, stroke_width=2)
        right_cover.move_to(circle_A.get_center() + RIGHT*1.4)
        
        # 6. Center cover
        center_cover = Circle(radius=1.7, color=TEAL, fill_opacity=0.2, stroke_width=2)
        center_cover.move_to(circle_A.get_center())
        
        covering_sets.add(large_cover, top_cover, bottom_cover, 
                         left_cover, right_cover, center_cover)
        
        # Animate covers appearing
        self.wait(2)
        self.play(LaggedStart(
            *[FadeIn(cover) for cover in covering_sets],
            lag_ratio=0.15,
            run_time=2.5
        ))
        
        # Show coverage text
        cover_text = Text("Open Cover of A", font_size=32).to_edge(DOWN)
        self.play(Write(cover_text))
        self.wait(1.5)
        
        # Demonstrate finite subcover
        subcover = VGroup(large_cover, top_cover, bottom_cover)
        
        # Fade out non-essential covers
        self.play(
            *[FadeOut(cover) for cover in covering_sets if cover not in subcover],
            FadeOut(cover_text),
            run_time=1.5
        )
        
        # Show finite subcover text
        subcover_text = Text("Finite Subcover (still covers A)", font_size=32).to_edge(DOWN)
        self.play(Write(subcover_text))
        
        # Highlight the remaining covers
        self.play(
            subcover[0].animate.set_stroke(width=3),
            subcover[1].animate.set_stroke(width=3),
            subcover[2].animate.set_stroke(width=3),
            run_time=1
        )
        
        self.wait(3)

        self.play(*[FadeOut(obj) for obj in self.mobjects])
        tex = Tex(r"A set is Compact when \\ any of its open covers has a finite subcover")
        self.play(Write(tex))
        self.wait(2)
        #introduce what is heine borel for for 4 seconds
        self.play(FadeOut(tex),run_time = 1)
        text = Tex(r"Theorem 1: ")
        self.play(FadeIn(text))
        self.wait(3)
        self.play(text.animate.to_corner(UL))
        heine_borel =MathTex(
            r"\text{Heine-Borel Theorem: }",
            r"\text{A subset } S \subset \mathbb{R}^n \text{ is compact}\\",
            r"\text{ if and only if}\\",
            r"\text{ it is closed and bounded.}"
        )
        box = SurroundingRectangle(heine_borel, color=BLUE, buff=MED_LARGE_BUFF)
        self.play(FadeIn(box))
        self.play(Write(heine_borel),run_time=5)
        self.wait(3)

        #what about sets other than R^n??\
        tex = Tex(r"What about sets other than \[R^n\]?")
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.play(Write(tex))

        #take an example where heine borel fails
        self.wait(1)
        tex = MathTex(r"(\mathbb{N},discrete)")
            
        self.play(Write(tex))
        self.play(tex.animate.to_corner(UL))
        self.wait(2)
        #showing its closed and bounded
        text = Tex(r"closed:")
        checkmark = Tex(r"\checkmark", color=GREEN)
        checkmark2 = Tex(r"\checkmark",color=GREEN)
        text3 =  Tex(r"bounded:")
        text.next_to(tex,DOWN)
        text3.next_to(text,DOWN)
        self.play(Write(text))
        
        self.wait(3)
        checkmark.next_to(text,RIGHT,buff=0.8)
        self.play(Write(checkmark),checkmark.animate.next_to(text,RIGHT)) #closed checkmark
        self.wait(1)
        self.play(Write(text3))
        self.wait(3)
        checkmark2.next_to(text3,RIGHT,buff=0.8)
        self.play(Write(checkmark2),checkmark2.animate.next_to(text3,RIGHT)) #bounded checkmark                                                     #bounded checkmark
        tex2 = MathTex(r"C_{n} = \{i | i < n\}")
        self.play(Write(tex2))
        proof = VGroup(
            MathTex(r"\text{Let } \mathcal{C} = \{\{n\} \mid n \in \mathbb{N}\}"),
            MathTex(r"\text{1. } \mathcal{C}\text{ is an open cover (discrete topology)}"),
            MathTex(r"\text{2. Any finite subcover } \{C_1, \ldots, C_k\}"),
            MathTex(r"\text{3. Let } N = \max\{n \mid \{n\} \in \{C_1, \ldots, C_k\}\}"),
            MathTex(r"\text{4. Then } \{N+1\} \notin \text{subcover}"),
            MathTex(r"\text{5. Thus no finite subcover exists}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.9)
        
        self.play(tex2.animate.shift(UP*1.5))
        self.wait(0.5)
        # Animate proof
        for i, step in enumerate(proof):
            if(i==0):
                step.next_to(tex2,DOWN)
                last_step = step
            else :
                step.next_to(last_step,DOWN)
                last_step=step
            self.play(FadeIn(step, shift=0.2*RIGHT), run_time=1 if i==0 else 0.7)
            if i == 4:  # Emphasize contradiction
                self.play(step.animate.set_color(RED))

        #now say how heine borel was unable to show compactness
        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        tex = Tex(r"How we can modify Heine-borel ?")
        self.play(FadeIn(tex))
        #definition of total boundedness
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        tex = MathTex(r"\text{Take set A again, now imagine if we }\\ \text{tried to do the same thing we did in the start} \\ \text{but now with equal size balls } (\varepsilon balls) \text{ instead of random sets}")
        self.wait(2)
        tex2 = MathTex(r"\text{This is called an } \varepsilon \text{ net for set A.}\\ \text{ If this set was finite as well, then we could say } \\ \text{ A is totally bounded.}")
        tex2.next_to(tex,DOWN)
        self.play(Write(tex),runt_time=5)
        self.wait(1)
        self.play(Write(tex2),run_time= 5)
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        #schematic
        circle_A = Circle(radius=2, color=BLUE, fill_opacity=0.3, stroke_width=4)
        circle_A.move_to(ORIGIN)
        self.play(Create(circle_A), run_time=1.5)
        
        # Move circle up (keeping your original animation)
        self.play(circle_A.animate.shift(UP*1.3), run_time=1.5)
        
        # Label the set
        A_label = Text("A", font_size=36).next_to(circle_A, DOWN, buff=0.7)
        self.play(Write(A_label))
        self.wait(1)
        # Create covering sets with proper stroke widths
        covering_sets = VGroup()
        
        # 1. Large covering set (thinner stroke)
        large_cover = Circle(radius=2.3, color=RED, fill_opacity=0.2, stroke_width=2)
        large_cover.move_to(circle_A.get_center() + RIGHT*0.3 + UP*0.2)
        
        # 2. Top cover (annulus with thin stroke)
        top_cover = Circle(radius=2.3, color=GREEN, fill_opacity=0.2, stroke_width=2)
        top_cover.move_to(circle_A.get_center() + UP*1.7)
        
       
        
        # 4. Left sector (thinner stroke)
        left_cover = Circle(radius=2.3, color=PURPLE, fill_opacity=0.2, stroke_width=2)
        left_cover.move_to(circle_A.get_center() + LEFT*1.4)
        
        # 5. Right sector
        right_cover = Circle(radius=2.3, color=ORANGE, fill_opacity=0.2, stroke_width=2)
        right_cover.move_to(circle_A.get_center() + RIGHT*1.4)
        
        # 6. Center cover
        center_cover = Circle(radius=2.7, color=TEAL, fill_opacity=0.2, stroke_width=2)
        center_cover.move_to(circle_A.get_center())
        
        covering_sets.add(large_cover, top_cover, bottom_cover, 
                         left_cover, right_cover, center_cover)
        
        # Animate covers appearing
        self.wait(2)
        covering_sets.remove(bottom_cover)
        self.play(LaggedStart(
            *[FadeIn(cover) for cover in covering_sets],
            lag_ratio=0.15,
            run_time=2.5
        ))
        self.play(
            LaggedStart(
                Wiggle(large_cover),
                Wiggle(top_cover),
                Wiggle(left_cover),
                lag_ratio=0.2,
                run_time=7
            )
        )
        e_label = Tex(r"\[\epsilon = 2.3\]", font_size=40).next_to(A_label, DOWN, buff=0.7)
        self.play(FadeIn(e_label ),run_time=2)
        self.wait(2)
        tbounded = Tex(r"is therefore totally bounded")
        self.play(A_label.animate.shift(LEFT*2))
        tbounded.next_to(A_label)
        self.play(Write(tbounded),run_time = 2)
        self.wait(3)
        
        #general_heine_borel theorem
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        text = Tex(r"Theorem 2: ")
        self.play(FadeIn(text))
        self.wait(3)
        self.play(text.animate.to_corner(UL))
        general_heine_borel = VGroup(
            Tex(r"General Heine-Borel Theorem:"),
            Tex(r"A subset of a complete metric space is compact"),
            Tex(r"if and only if"),
            Tex(r"it is closed and totally bounded."),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(FadeIn(general_heine_borel),run_time=4)
        self.wait(3)

        #Proof
        self.play(general_heine_borel.animate.scale(0.5))
        self.play(general_heine_borel.animate.next_to(text, RIGHT))
        proof = Tex(r"Proof:").next_to(text,DR)
        proof.shift(DOWN*1.5)
        self.play(Write(proof))
        prooff = VGroup(
                MathTex(r"=> \text{Let } A \text{ be compact , therofore its complete}"),
                MathTex(r"\text{let } \epsilon \text{ be given , then take }"),
                MathTex(r"{M_{\epsilon}x : x \in  A} "),
                MathTex(r" \text{to be an open cover of } A "),
                MathTex(r"A \text{ is compact therefore there exists a finite subcover}"),
                MathTex(r"\text{this implies total boundedness.}"),
            ).scale(0.9)
        for i, step in enumerate(prooff):
            if(i==0):
                step.next_to(general_heine_borel,DOWN).next_to(proof)
                last_step = step
            else :
                self.wait(1)
                step.next_to(last_step,DOWN)
                last_step=step
            self.play(FadeIn(step, shift=0.2*RIGHT), run_time=1 if i==0 else 0.7)
        self.wait(3)
        #proof <= (skipped for now)
        #corollary
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        text = Tex(r"Corollary 1: ")
        self.play(FadeIn(text))
        self.wait(3)
        self.play(text.animate.to_corner(UL))
        general_heine_borel = VGroup(
            Tex(r"A metric space is compact if and only if"),
            Tex(r"it is complete and totally bounded."),
           
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(general_heine_borel),run_time=4)
        self.wait(3)
        #proof
        self.play(general_heine_borel.animate.scale(0.5))
        self.play(general_heine_borel.animate.next_to(text, RIGHT))
        proof = Tex(r"Proof:").next_to(text,DR)
        proof.shift(DOWN*1.5)
        self.play(Write(proof))
        prooff = VGroup(
                MathTex(r"\text{Every compact metric space } M \text{ is complete}"),
                MathTex(r"\text{As observed compactness implies total boundedness }"),
                MathTex(r" \text{conversely assume } M \text{ is totally bounded and complete} "),
                MathTex(r"\text{every metric space is closed in itself}"),
                MathTex(r"\text{by general heine-borel theorem M is compact}"),
            ).scale(0.9)

        for i, step in enumerate(prooff):
            if(i==0):
                step.next_to(general_heine_borel,DOWN).next_to(proof)
                last_step = step
                self.wait(1)
            else :
                self.wait(1)
                step.next_to(last_step,DOWN)
                last_step=step
            self.play(FadeIn(step, shift=0.2*RIGHT), run_time=1 if i==0 else 0.7) 
        ArabTexTemplate = TexTemplate(
            tex_compiler="xelatex",   
            output_format='.xdv',            
            preamble = r'''
\usepackage{polyglossia}\setotherlanguage{arabic}\newfontfamily\arabicfont[Script=Arabic]{B Nazanin}
            '''
        )
        UrduTexTemplate = TexTemplate(
            tex_compiler="xelatex",   
            output_format='.xdv',            
            preamble = r'''
\usepackage{polyglossia}\setotherlanguage{arabic}\newfontfamily\arabicfont[Script=Arabic]{B Nazanin}
            '''
        )
       
#Examples(from najafi's book)---------
        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        text = Tex(r"Examples ")
        self.play(FadeIn(text))
        self.wait(3)
        self.play(text.animate.to_corner(UL))
        #take set of real numbers how can we find a 1-net ? for each x(number change animation) we need to find a y which d(x,y) = |x-y| <1

        number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            color=WHITE,
            include_numbers=True,
        )
        self.add(number_line)

        # ValueTracker for x
        x_tracker = ValueTracker(2.3)

        # Dot for x (red)
        x_dot = always_redraw(lambda: Dot(
            number_line.n2p(x_tracker.get_value()),
            color=RED
        ))

        # Dot for y = nearest integer to x (blue)
        y_dot = always_redraw(lambda: Dot(
            number_line.n2p(round(x_tracker.get_value())),
            color=BLUE
        ))

        # Brace showing distance between x and y
        distance_brace = always_redraw(lambda: BraceBetweenPoints(
            x_dot.get_center(),
            y_dot.get_center(),
            direction=DOWN
        ))

        # Label for d(x,y)
        d_label = always_redraw(lambda: MathTex("d(x,y)")
            .next_to(distance_brace, DOWN)
        )

        # Label for |x-y|
        abs_label = always_redraw(lambda: MathTex(
            f"|x - y| = |{x_tracker.get_value():.2f} - {round(x_tracker.get_value())}|"
        ).next_to(d_label, DOWN))

        # Add all updaters
        self.add(x_dot, y_dot, distance_brace, d_label, abs_label)

        # Animate x moving across the line
        for new_x in [2.3, -1.7, 4.8, 0.1]:
            self.play(
                x_tracker.animate.set_value(new_x),
                run_time=2,
                rate_func=there_and_back
            )
            # Pause to emphasize each position
            self.wait(1)
        self.wait(1)
        tex3 = MathTex(r"=|x-[x]|",color = GREEN).next_to(abs_label,RIGHT)
        self.play(FadeIn(tex3))
        # Example 2: [a,b ] is totally bounded
        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        title = MathTex(r"[a,b]").to_edge(UP)
        self.play(FadeIn(title))
        self.wait(2)
        #to see why lets draw it on euclidean line
        number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            color=WHITE,
            include_numbers=False,
        )
        number_line.shift(DOWN * 1.5)
        self.play(Create(number_line),runtime = 2)

        # Labels for a and b
        a = -4
        b = 4
        dic = {a: "a", b: "b"}
        labels = number_line.add_labels(dic)
        self.wait(3)
        # try to cover it
        epsilon = 0.5
        n_balls = int(np.ceil((b - a) / epsilon))
        ball_centers = [-3,-2,1,3]
        balls = VGroup()
        for center in ball_centers:
            dot = Dot(point=number_line.n2p(center), color=YELLOW)
            ball = Circle(radius=0.5 * number_line.get_unit_size(), color=BLUE, fill_opacity=0.2)
            ball.move_to(dot)
            balls.add(ball)
            self.play(FadeIn(ball), FadeIn(dot), run_time=0.5)
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in balls])
        self.play(FadeOut(title))
        text1 = MathTex(r"a_i = a + i \cdot [\frac{b - a}{\varepsilon}]").to_edge(UP)
        text2 = MathTex(r"\text{say } \varepsilon = 0.5 ").next_to(text1,DOWN)
        self.play(Write(text1),duration = 3)
        self.wait(2)
        self.play(FadeIn(text2))
        self.wait(1)
        # Generate centers of the epsilon-balls
        ball_centers = [a + i * epsilon for i in range(n_balls + 1)]
        self.wait(2)
        # Draw the ε-balls on the number line as translucent circles
        balls = VGroup()
        for center in ball_centers:
            dot = Dot(point=number_line.n2p(center), color=YELLOW)
            ball = Circle(radius=0.5 * number_line.get_unit_size(), color=BLUE, fill_opacity=0.2)
            ball.move_to(dot)
            balls.add(ball)
            self.play(FadeIn(ball), FadeIn(dot), run_time=0.5)

        self.wait()

        # Annotate how many balls are used, it can be shown there is always finitely many of these balls
        ball_count = MathTex(r"\text{Number of balls: }", str(len(ball_centers)))
        ball_count.next_to(number_line, DOWN, buff=1.5)
        self.play(Write(ball_count))

        self.wait(2)

        #Ending
        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        text = Tex("By Amirhusein Jazayeri ")
        text2 = Tex("Dr. Najafi's Real analysis course" ).next_to(text,DOWN)
        self.play(FadeIn(text))
        self.play(FadeIn(text2))
        self.wait(2)
        """#example 2
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        arabicText = Tex(
            r"عابدات",
            tex_template=ArabTexTemplate,
            tex_environment="Arabic"
        ).shift(UP)
        self.play(Write(arabicText))"""
    
