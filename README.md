# 👨‍🍳 Chef Gemini — AI Culinary Concierge

![Chef Gemini Demo](./demo.gif)

**Chef Gemini** is an advanced AI culinary concierge built with the **Google Agent Development Kit (ADK)**. It combines deep food science, recipe generation, pantry inventory management, clinical nutrition math, global heritage cuisine expertise, and **200+ specialized domain tools** with rich visual card rendering and long-term user memory.

---

## 🚀 Wired-Up Capabilities & Google Cloud Services

Chef Gemini integrates directly with the following Google Cloud and Vertex AI services:

* **Vertex AI GenAI (`gemini-2.5-flash`)**: Drives the primary agent reasoning loop, tool orchestration, and adaptive culinary responses.
* **Vertex AI Imagen 3 (`imagen-3.0-generate-002`)**: Generates photorealistic dish cards on demand for any recipe or custom dish (`generate_recipe_photo_card`).
* **Vertex AI Memory Bank**: Provides persistent long-term cross-session memory via `PreloadMemoryTool` and memory generation callbacks, remembering dietary restrictions, user preferences, and culinary history across sessions.
* **Google Cloud Storage (GCS)**: Hosts generated recipe photo card assets in a public storage bucket for high-speed delivery to the user interface.
* **Google Maps Places API**: Performs real-time local searches for specialty grocery stores, markets, and butchers near the user (`search_nearby_grocery_stores`).
* **Agent-to-User Interface (A2UI)**: Renders rich, dynamic UI surfaces (cards, structured component lists, image hero banners) using `A2uiSchemaManager` and `a2ui_callback` rather than plain text alone.
* **A2A (Agent-to-Agent) Protocol**: Exposed via standard Agent Runtime endpoints for seamless proxy forwarding and multi-agent collaboration.

---

## 🛠️ 200+ Specialized Culinary Domain Tools

Chef Gemini features **200+ dedicated ADK tools** organized into 10 specialized culinary domains:

1. **Molecular Gastronomy & Flavor Physics** (Tools 101–110): Direct/reverse spherification bath timing, Transglutaminase protein binding, vacuum chamber compression ($<50\,\text{mbar}$), ultrasonic cavitation ($20\,\text{kHz}$), supercritical $\text{CO}_2$ fluid extraction, bromelain/papain protease digestion, cryogenic liquid nitrogen shatter, hydrocolloid syneresis prevention, GC-MS aroma pairing, and centrifugal clarification ($10,000\times g$).
2. **Modernist Bread, Pastry & Polymer Science** (Tools 111–120): Baker's math hydration ($55-90\%$), croissant butter block lamination rheology, Lievito Madre sourdough acid balance (lactic:acetic 3:1), macaronage lava-ribbon flow, Isomalt sugar glass transition ($160^\circ\text{C}$), Gelatin Bloom conversion ($g_2 = g_1 \times \sqrt{B_1 / B_2}$), panada egg hydration absorption, chocolate $\beta_V$ crystal seeding, fat crystallization polymorphs, and ovalbumin foam stabilization.
3. **Artisan Fermentation, Koji & Fungi** (Tools 121–130): *Aspergillus oryzae* koji spore inoculation, thermal enzyme garum proteolysis ($60^\circ\text{C}$), miso salt concentration ($5-14\%$), tsukemono nuka bran bed maintenance, black garlic Maillard chamber ($65^\circ\text{C}$, $85\%\,\text{RH}$), Acetobacter vinegar oxidation, Rhizopus oligosporus tempeh incubation, kombucha SCOBY balancing, lacto-ferment brine math, and wild mushroom foraging safety.
4. **Enology, Spirits & Craft Beverages** (Tools 131–140): Growing Degree Days (GDD) terroir scoring, Champagne *Méthode Traditionnelle* dosage ($24\,\text{g/L} \rightarrow 6\,\text{bar}$), craft cider tannin-acid balance, bourbon oak barrel char extraction, beer hop IBU utilization ($IBU = \frac{g \times \%_\alpha \times U}{V}$), cocktail thermal dilution, absinthe thujone louche effect, vermouth botanical steeping, Henry's Law $\text{CO}_2$ carbonation, and pot still distillation cuts.
5. **Regional Heritage Cuisines** (Tools 141–150): Mexican corn nixtamalization ($\text{Ca(OH)}_2$), Indian tadka fat-soluble spice blooming order, Thai curry paste mortar fiber shear, Ethiopian *ersho* teff sourdough fermentation, semolina bronze die extrusion friction, Spanish paella socarrat bottom flame control, Middle Eastern tahini halva crystallization, Japanese ramen *tare/dashi* umami synergy, Escoffier mother sauce roux reduction, and Georgian khachapuri sulguni stretchability.
6. **Clinical & Performance Nutrition** (Tools 151–160): Ketogenic net carb macro ratios (3:1/4:1), Low-FODMAP fermentable carbohydrate scanning, renal potassium & phosphorus leaching, Glycemic Index/Load response curves, endurance athlete glycogen carb loading ($7-10\,\text{g/kg}$), anti-inflammatory polyphenol density, biogenic amine histamine safety, muscle hypertrophy leucine trigger ($3.0\,\text{g}$), diabetic carb exchange ICR units, and IDDSI texture-modified diet standards.
7. **Butchery, Seafood & Upcycling** (Tools 161–170): Sashimi-grade Ikejime ATP preservation, beef dry-aging calpain/cathepsin tenderization, whole animal nose-to-tail yield, citrus peel *oleo saccharum* cold sugar extraction, Monterey Bay Seafood Watch rating, brewery spent grain upcycled flour milling, cascara coffee cherry tisane brewing, cricket flour protein incorporation, cell-cultivated meat scaffold searing, and food waste methane offset calculator.
8. **Advanced Thermal Transport & Rheology** (Tools 171–180): Fourier's law thermal diffusivity, Stokes' law emulsion creaming velocity, starch gelatinization pasting temperatures, caramelization sucrose pyrolysis curves, Maillard reaction kinetics vs pH, sous-vide thermal pasteurization ($D$/$Z$-values), deep-frying oil TPM degradation, bread staling retrogradation, ice cream freezing point depression, and non-Newtonian yield stress.
9. **Sensory Science & Gastronomic Pairing** (Tools 181–190): Volatile aromatic molecule pairing, monosodium glutamate & disodium inosinate exponential umami multiplier, triangle test sensory difference thresholds, wine & cheese tannin-fat matching, coffee extraction yield TDS brewing charts, tea catechin steep timers, sodium ion bitterness masking, Scoville capsaicin cooling, astringency salivary protein precipitation, and kokumi $\gamma$-glutamyl peptide richness boosters.
10. **Smart Kitchen Automation & Operations** (Tools 191–200): Non-linear recipe batch volume/surface scaling, commercial kitchen prep par levels, food cost & gross contribution margin solver, HACCP critical control point temperature monitoring, Arrhenius accelerated shelf-life modeling, cold chain refrigeration failure evaluation, recipe carbon footprint ($CO_2e$), virtual water footprint scanning, menu engineering matrix (Star, Plowhorse, Puzzle, Dog), and Big-9 allergen cross-contamination auditing.

---

## 📂 Project Structure

```
chef-gemini/
├── app/                       # Core ADK Agent implementation
│   ├── agent.py               # Agent definition, A2UI callbacks, & tool registration
│   ├── tools.py               # 200+ specialized culinary domain tools & Imagen 3 card generator
│   └── a2ui_utils.py          # A2UI schema manager & surface update builder
├── frontend/                  # FastAPI Proxy & Modern Web UI
│   ├── main.py                # FastAPI server communicating via A2A protocol
│   └── static/                # HTML5/CSS3 frontend with A2UI mini-renderer
├── scratch/                   # Unit test suites & validation scripts
│   ├── test_batch_8.py        # Unit tests for Tools 31-100
│   └── test_batch_9.py        # Unit tests for Tools 101-200
├── agents-cli-manifest.yaml   # Manifest for agents-cli deployment & runtime
└── demo.gif                   # Embedded looping demo recording
```

---

## 💻 Local Setup & Execution

### Prerequisites

* Python 3.11+
* `uv` package manager (`pip install uv`)
* `google-agents-cli` (`uv tool install google-agents-cli`)
* Google Cloud SDK with authenticated credentials (`gcloud auth application-default login`)

### Environment Setup

Set your Google Cloud Project and API keys in your environment or `.env` file:

```bash
export GOOGLE_CLOUD_PROJECT="<your-gcp-project-id>"
export GOOGLE_MAPS_API_KEY="<your-google-maps-api-key>"
```

### Running the Agent & Playground Locally

1. Install project dependencies:
   ```bash
   agents-cli install
   ```

2. Run unit tests across all 200+ tools:
   ```bash
   uv run pytest scratch/test_batch_9.py
   ```

3. Launch the ADK local playground:
   ```bash
   agents-cli playground
   ```

### Running the Web UI & FastAPI Proxy

Start the frontend proxy server:

```bash
cd frontend
uv run python main.py
```

The application interface will be available locally on port `8080`.

---

## 🚀 Deployment to Agent Platform

Deploy the agent directly to Vertex AI Agent Runtime:

```bash
agents-cli deploy --project <your-gcp-project-id> --no-confirm-project --update-env-vars GOOGLE_MAPS_API_KEY="<your-key>"
```
