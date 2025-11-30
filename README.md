# Totally-bounded-sets_manim
A Python project that explains what totall bounded sets are and provides some examples

---

# Compactness & Total Boundedness — Manim Animation

A Manim scene (Python) that visualizes the notions of **compactness**, **total boundedness**, and the **Heine–Borel** theorems.
The animation contains bilingual title slides (Persian/Arabic using XeLaTeX), geometric schematics (open covers and finite subcovers), formal statements of theorems, short proofs / counterexamples (e.g. ℕ with discrete topology), and concrete examples (ε-nets, `[a,b]`).

**Author:** Amirhosein Jazayeri
**Based on:** material from Dr. Najafi’s Real Analysis course
<video width="640" controls>
  <source src="gif.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
---

## Demo / What it shows

* Persian/Arabic title slide (XeLaTeX + polyglossia)
* Schematic of a set `A` with an open cover and a finite subcover (visual intuition for compactness)
* Statement of the Heine–Borel theorem (ℝⁿ: compact ⇔ closed + bounded)
* Counterexample: `ℕ` with discrete topology (closed + bounded but not compact)
* Definition and visualization of **total boundedness** (ε-nets)
* General Heine–Borel theorem for complete metric spaces (compact ⇔ closed + totally bounded)
* Short proofs/sketches and worked examples:

  * Construction of a 1-net on ℝ (nearest integers)
  * `[a,b]` is totally bounded (finite ε-balls)
* Closing/credit slide

---

## Requirements

* **Python 3.8+**
* **Manim Community** (the `manim` pip package) — Manim Community Edition (CE)
* **NumPy**
* A working **LaTeX** installation with `xelatex` (TeX Live or MiKTeX). Required for Persian/Arabic typesetting.
* LaTeX package **polyglossia**
* An Arabic font accessible to XeLaTeX (e.g. **B Nazanin**, **Amiri**, or another Arabic/Persian font). If the font used in the code is not installed, replace with a font available on your system or install the font.

Example `requirements.txt` (minimal):

```
manim
numpy
```

> Note: Manim has additional system dependencies (ffmpeg, cairo, fonts). See Manim Community docs if you need help installing the runtime environment.

---

## Files

* `compact_scene.py` (or whatever you name your script) — the main Manim scene (class `Compact`).
* Any additional assets (fonts, images) — optional.

> If your repo uses a different filename, update the examples below accordingly.

---

## How to render

From the repository root, run Manim with the scene class name.

Low-quality, preview (fast):

```bash
manim -pql compact_scene.py Compact
```

High-quality render:

```bash
manim -pqh compact_scene.py Compact
```

* `-p` : open the result after rendering
* `-q l` / `-q h` : quality presets (low / high). Replace `l`/`h` with other quality flags as needed.

If you prefer to render a specific time window or export as GIF, use Manim CLI options; e.g.:

```bash
manim -pql compact_scene.py Compact -s   # -s for short/static (snapshot)
manim -pql compact_scene.py Compact -o output_name  # specify output file name
```

---

## LaTeX (Persian/Arabic) notes

The scene uses a `TexTemplate` with `xelatex` and `polyglossia`. To avoid errors:

1. Install a TeX distribution that includes `xelatex` and `polyglossia` (TeX Live recommended).
2. Install an Arabic/Persian font referenced in the script (e.g. **B Nazanin**). If you don't have that font, either:

   * install it, or
   * change the font name in the `TexTemplate` preamble to one you have (e.g., `Amiri`).

Example preamble used in the script:

```tex
\usepackage{polyglossia}
\setotherlanguage{arabic}
\newfontfamily\arabicfont[Script=Arabic]{B Nazanin}
```

If you have LaTeX errors, run a simple `xelatex` compile on a minimal TeX file to verify your TeX installation and font availability before running Manim.

---

## Tips & Troubleshooting

* **Missing `xelatex` / polyglossia errors:** install/enable XeLaTeX and polyglossia in your TeX distribution.
* **Font not found:** change the font name in the `TexTemplate` to one installed in your OS, or install the requested font.
* **Manim errors about ffmpeg/cairo:** install platform-specific dependencies (ffmpeg, libcairo). On Ubuntu/Debian: `sudo apt install ffmpeg libcairo2-dev` (or follow Manim docs).
* **Long render times:** use `-pql` (preview low quality) during development and `-pqh` for final export.
* **Windows users:** ensure `PATH` contains your TeX and ffmpeg executable directories.

---

## Project structure (suggested)

```
.
├── compact_scene.py        # Manim script (class Compact)
├── requirements.txt
├── README.md
└── assets/                 # optional: fonts, images, sound
```

---

## License

Add a license of your choice (e.g., MIT). If you want, include `LICENSE` file.

---

## Credits

* Animation & code: **Amirhosein Jazayeri**
* Course material inspiration: **Dr. Najafi** (Real Analysis)
* Manim Community for core animation utilities

---

