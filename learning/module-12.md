# Module 12: The Layout Enforcer (`verify_layout.py`)

## 1. Tool Definition
**What is it?** 
The primary directive of this entire repository is **The 1-Page Law**: Every single lesson must fit perfectly onto one physical A4 page. 
But how does an AI know if a string of HTML will overflow a physical page? 
`Jules-workspace/verify_layout.py` solves this. It performs a headless simulation of the PDF rendering engine, calculates the exact millimeter geometry of every `<div>` tag on the page, and mathematically proves whether the content is too long (Overflow) or too short (Underflow).

## 2. I/O Mapping
*   **Inputs:** 
    *   A single HTML file (e.g., `pages/05.0_n15_mansubat.html`).
*   **Processes:**
    *   Calls the `lint_pages.py` script to ensure the HTML follows the atomic design system.
    *   Renders the HTML in memory using `WeasyPrint`.
    *   Crawls the Document Object Model (DOM), calculating the exact Y-axis coordinate of the absolute lowest HTML element on the page.
    *   Compares that coordinate against the physical height of an A4 piece of paper (297 mm).
*   **Outputs:**
    *   A strict JSON object declaring `PASS`, `OVERFLOW`, or `UNDERFLOW`, including exact millimeter metrics of the blank space left on the page.

---

## 3. The Deep Dive: Codebase Analysis

Below is an exhaustive, 100% codebase breakdown of the geometry layout verifier.

### Block A: Constants & Math Settings
To calculate physical paper layouts, the script defines hard mathematical constants.

```python
# From Jules-workspace/verify_layout.py

42: # ── Constants ─────────────────────────────────────────────────────────────────
43: 
44: #: WeasyPrint renders at 96 DPI
45: PX_TO_MM: float = 25.4 / 96.0
46: 
47: #: A4 page height
48: PAGE_HEIGHT_MM: float = 297.0
49: 
50: #: Bottom margin in CSS is 9 mm
51: PRINTABLE_BOTTOM_MM: float = PAGE_HEIGHT_MM - 9.0
52: 
53: #: If blank space exceeds this % of page height, it's UNDERFLOW
54: UNDERFLOW_THRESHOLD_PCT: float = 10.0
55: 
56: #: CSS classes to skip during geometry analysis (non-content layers)
57: SKIP_CLASSES: frozenset[str] = frozenset(
58:     {"global-background-layer", "global-watermark-layer", "watermark-text", "force-new-page"}
59: )
60: 
61: #: HTML tags to skip
62: SKIP_TAGS: frozenset[str] = frozenset({"html", "body"})
63: 
64: #: WeasyPrint box types to skip
65: SKIP_BOX_TYPES: frozenset[str] = frozenset({"MarginBox", "PageBox"})
```
#### Line-by-Line Commentary
*   **Line 45:** `PX_TO_MM = 25.4 / 96.0`
    *   WeasyPrint calculates everything in standard web pixels (96 Dots Per Inch). To convert pixels to millimeters, we must use this exact mathematical ratio.
*   **Lines 48-51:** Standard A4 paper is exactly 297 mm tall. Because our CSS has a 9 mm footer (for page numbers), the absolute bottom limit of the page is `288.0 mm`. 
*   **Line 54:** `UNDERFLOW_THRESHOLD_PCT = 10.0`
    *   If the page is more than 10% empty space, it fails the check and the AI is ordered to write more content.
*   **Lines 57-65:** The script will measure the coordinates of DOM elements. However, things like the background image or the watermark text stretch all the way to the bottom of the page. If we didn't skip them, the script would always think the page was 100% full!

### Block B: Data Models
The script enforces strict typings to ensure it communicates properly with the JSON automation systems.

```python
# From Jules-workspace/verify_layout.py

70: LayoutStatus = Literal["PASS", "FAIL", "OVERFLOW", "UNDERFLOW", "UNKNOWN"]
71: LayoutRecommendation = Literal[
72:     "NONE", "GO_TO_NEXT_PAGE", "SPLIT_PAGE_OR_CONDENSE", "FIT_ANOTHER_SECTION"
73: ]
74: 
75: 
76: @dataclass
77: class ElementInfo:
78:     tag: str
79:     id: str
80:     css_class: str
81:     bottom_mm: float
82: 
83: 
84: @dataclass
85: class LayoutResult:
86:     status: LayoutStatus = "UNKNOWN"
87:     remaining_height_mm: float = 0.0
88:     blank_space_percentage: float = 0.0
89:     recommendation: LayoutRecommendation = "NONE"
90:     details: str = ""
91:     split_recommendation: ElementInfo | None = None
92: 
93:     def to_dict(self) -> dict:  # type: ignore[type-arg]
94:         d = asdict(self)
95:         return d
96: 
97:     def print(self) -> None:
98:         print(json.dumps(self.to_dict(), indent=2, ensure_ascii=False))
```
#### Line-by-Line Commentary
*   **Lines 70-73:** `Literal` types restrict the output. The automation pipeline expects exactly these words; if a typo occurred here, the entire pipeline would crash.
*   **Lines 76-81:** `ElementInfo` tracks the exact HTML element that is currently at the bottom of the page. This is brilliant: if a page overflows, the script can tell the AI exactly which `<div>` tag pushed it over the edge!
*   **Lines 84-98:** `LayoutResult` aggregates all the data. The `print` method automatically dumps the dataclass as a formatted JSON string, allowing Node.js or bash scripts to parse the results.

### Block C: Geometry Analysis & AST Traversal
This is the core physics engine of the script. It calculates where elements physically render on the paper.

```python
# From Jules-workspace/verify_layout.py

132: def _find_content_bottom(page: object) -> tuple[float, ElementInfo | None]:  # type: ignore[type-arg]
133:     """Walk all boxes on the page to find the lowest content boundary."""
134:     max_y: float = 0.0
135:     last_element: ElementInfo | None = None
136: 
137:     page_box = getattr(page, "_page_box", None)
138:     if page_box is None:
139:         return max_y, last_element
140: 
141:     for box in page_box.descendants():
142:         if type(box).__name__ in SKIP_BOX_TYPES:
143:             continue
144: 
145:         element = getattr(box, "element", None)
146:         if element is None:
147:             continue
148: 
149:         # Skip non-content layers and root containers
150:         el_classes: list[str] = element.get("class", "").split() if element.get("class") else []
151:         if any(c in SKIP_CLASSES for c in el_classes):
152:             continue
153:         if element.tag in SKIP_TAGS:
154:             continue
155: 
156:         bottom: float = getattr(box, "position_y", 0) + getattr(box, "height", 0)
157:         if bottom > max_y:
158:             max_y = bottom
159:             last_element = ElementInfo(
160:                 tag=element.tag,
161:                 id=element.get("id", ""),
162:                 css_class=element.get("class", ""),
163:                 bottom_mm=round(bottom * PX_TO_MM, 2),
164:             )
165: 
166:     return max_y, last_element
```
#### Line-by-Line Commentary
*   **Line 132:** The function takes a rendered `WeasyPrint` page object.
*   **Line 141:** `for box in page_box.descendants():`
    *   It recursively loops through every single node in the rendered DOM tree.
*   **Lines 142-154:** It aggressively filters out the structural/background elements defined in Block A to ensure it only tracks *actual* text content (like I'rab tables and headers).
*   **Line 156:** `bottom: float = getattr(box, "position_y", 0) + getattr(box, "height", 0)`
    *   *The Physics Math*: To find the absolute bottom edge of an element, you take its starting Y-coordinate and add its height!
*   **Lines 157-164:** If this element is lower than the previous `max_y`, it becomes the new "lowest element". It records the HTML tag, the CSS class, and converts the pixels into millimeters (`* PX_TO_MM`).

### Block D: The Core Verifier & Linter Integration
Before measuring geometry, the script verifies the HTML isn't broken.

```python
# From Jules-workspace/verify_layout.py

172: def verify_layout(filepath: Path, *, skip_lint: bool = False) -> LayoutResult:
173:     """Verify that a page renders to exactly one A4 page."""
174:     result = LayoutResult()
...
181:     # ── Linter Check ──────────────────────────────────────────────────────
182:     if not skip_lint and _LINT_AVAILABLE:
183:         lint_result = lint_pages.lint_file(filepath)
184:         # Support both old tuple API and new LintResult API
...
194:             # New LintResult dataclass
195:             if not lint_result.passed:
196:                 result.status = "FAIL"
197:                 result.details = "Linter errors: " + "; ".join(
198:                     i.message for i in lint_result.errors[:5]
199:                 )
200:                 return result
201: 
202:     # ── Read file ──────────────────────────────────────────────────────────
203:     try:
204:         content = filepath.read_text(encoding="utf-8")
205:     except OSError as exc:
206:         result.status = "FAIL"
207:         result.details = f"Error reading file: {exc}"
208:         return result
209: 
210:     # ── Render ────────────────────────────────────────────────────────────
211:     try:
212:         from weasyprint import HTML
213:     except (ImportError, OSError) as exc:
214:         result.status = "FAIL"
215:         result.details = f"WeasyPrint unavailable: {exc}"
216:         return result
217: 
218:     body_inner = _extract_body(content)
219:     html_content = _build_verification_html(body_inner)
220: 
221:     try:
222:         doc = HTML(string=html_content, base_url=".").render()
223:     except Exception as exc:
224:         result.status = "FAIL"
225:         result.details = f"Rendering error: {exc}"
226:         return result
```
#### Line-by-Line Commentary
*   **Lines 181-200:** It calls `lint_pages.py`. If the AI used a forbidden HTML tag (like `<section>`), the script stops immediately and returns a `FAIL`. There is no point checking the geometry of a page if the code is invalid.
*   **Lines 203-216:** Standard I/O and library import safety checks.
*   **Lines 218-219:** It strips the `<head>` of the target file and wraps it in a sterile `_build_verification_html` wrapper. This ensures the geometry is calculated without unpredictable CSS interference from other global stylesheets.
*   **Lines 221-226:** It triggers the headless `WeasyPrint` render. If the HTML is massively malformed (e.g., an unclosed `<table>` tag), WeasyPrint will crash, which is caught here.

### Block E: The Overflow Decision Engine
Once the render finishes, it's time to make the final ruling.

```python
# From Jules-workspace/verify_layout.py

228:     page_count = len(doc.pages)
...
234:     # ── Geometry Analysis ─────────────────────────────────────────────────
235:     max_y_px, last_element = _find_content_bottom(doc.pages[0])
236:     max_y_mm = max_y_px * PX_TO_MM
237:     remaining_mm = PRINTABLE_BOTTOM_MM - max_y_mm
238:     blank_pct = (remaining_mm / PAGE_HEIGHT_MM) * 100.0
239: 
240:     result.remaining_height_mm = round(remaining_mm, 2)
241:     result.blank_space_percentage = round(blank_pct, 1)
242: 
243:     # ── Rule 1: Overflow ──────────────────────────────────────────────────
244:     if page_count > 1:
245:         result.status = "OVERFLOW"
246:         result.details = (
247:             f"Page count is {page_count} (expected 1). Content overflows. "
248:             "Split into multiple files or condense content."
249:         )
250:         result.recommendation = "SPLIT_PAGE_OR_CONDENSE"
251:         result.split_recommendation = last_element
252:         return result
253: 
254:     # ── Rule 2: Underflow ─────────────────────────────────────────────────
255:     if blank_pct >= UNDERFLOW_THRESHOLD_PCT:
256:         result.status = "UNDERFLOW"
257:         result.recommendation = "FIT_ANOTHER_SECTION"
258:         result.details = (
259:             f"Page is {blank_pct:.1f}% empty ({remaining_mm:.1f} mm blank). "
260:             "Add more content or pull from adjacent pages."
261:         )
262:     else:
263:         result.status = "PASS"
264:         result.recommendation = "GO_TO_NEXT_PAGE"
265:         result.details = f"Layout valid. Blank space: {blank_pct:.1f}%."
266: 
267:     return result
```
#### Line-by-Line Commentary
*   **Lines 235-238:** It runs the physics engine (Block C) to get the lowest Y-coordinate. It subtracts that from the total paper height (`PRINTABLE_BOTTOM_MM - max_y_mm`) to figure out exactly how many millimeters of blank space are left at the bottom of the page. It converts this to a percentage.
*   **Lines 243-252:** `if page_count > 1:`
    *   *The Overflow Catch*: If WeasyPrint generated 2 pages instead of 1, the AI wrote too much text. The status is set to `OVERFLOW`, and it importantly passes the `last_element` data back to the AI so the AI knows exactly *where* to cut the text!
*   **Lines 254-261:** `if blank_pct >= UNDERFLOW_THRESHOLD_PCT:`
    *   *The Underflow Catch*: If the page is more than 10% blank, the status is set to `UNDERFLOW`. The AI is told to generate more content to fill the gap.
*   **Lines 262-265:** `else: result.status = "PASS"`
    *   If it didn't overflow, and it's not underfilled, it is a perfect page!

### Block F: The CLI
```python
# From Jules-workspace/verify_layout.py

273: def parse_args() -> argparse.Namespace:
274:     parser = argparse.ArgumentParser(
275:         prog="verify_layout.py",
276:         description="Verify the One-Page Law for an HTML page.",
277:         formatter_class=argparse.RawDescriptionHelpFormatter,
278:     )
279:     parser.add_argument(
280:         "filepath",
281:         type=Path,
282:         metavar="FILE",
283:         help="HTML page file to verify",
284:     )
285:     parser.add_argument(
286:         "--skip-lint",
287:         action="store_true",
288:         help="Skip the linter compliance check before layout verification",
289:     )
290:     return parser.parse_args()
291: 
292: 
293: def main() -> None:
294:     args = parse_args()
295:     result = verify_layout(args.filepath, skip_lint=args.skip_lint)
296:     result.print()
297: 
298:     # Exit 1 only on hard failures (file not found, render error)
299:     if result.status == "FAIL":
300:         sys.exit(1)
301:     sys.exit(0)
```
#### Line-by-Line Commentary
*   **Lines 273-290:** The `argparse` configuration allows execution from the terminal. The `--skip-lint` flag is provided as an emergency override in case the linter is giving false positives.
*   **Line 296:** `result.print()`
    *   Outputs the JSON summary to the console so other tools can pipe the output (e.g., `stdout`).
*   **Lines 298-301:** Crucially, it only exits with an error code (`sys.exit(1)`) if the tool *crashed* (e.g., `FAIL`). If the layout simply over/underflowed, it exits with `0` because the tool itself executed successfully!

### Review
You have successfully dissected `verify_layout.py` in its absolute entirety. You now understand physical millimeter conversion, DOM geometry analysis, and automated WeasyPrint layout enforcement!
