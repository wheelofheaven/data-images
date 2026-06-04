# Timeline Moodscape Production Board

This board tracks the replacement English timeline moodscapes created after the
successful Age of Sagittarius pilot. The goal is a consistent visual spine for
the long timeline chapters: wide, quiet landscape illustrations that match each
age's palette, sit between major arguments, and do not compete with the prose.

## Style Contract

- Aspect and framing: wide landscape moodscapes, suitable for full-width article
  figures.
- Detail level: low to medium detail, atmospheric rather than explanatory.
- Treatment: cinematic matte-painting / concept-art mood, not photorealistic
  documentation, not diagram, not infographic.
- Contents: no visible text, no symbols, no logos, no UI overlays, no captions
  inside the image.
- Human presence: distant or implied only unless the chapter requires otherwise.
- Technology: plausible, restrained, distant, and integrated into the landscape.
- Palette: anchor to the chapter `extra.color`, with at least two supporting
  colors so the page does not become monochrome.
- Caption style: `Ill. N - ...`, matching the Sagittarius pilot.
- Asset naming: `age-of-{sign}-{scene}.png` in `raw/`, published as
  `images/timeline/age-of-{sign}-{scene}.avif|webp`.
- Prompt taxonomy: `stylized-concept`.

## Rollout Budget

| Chapter | Palette Anchor | Target Images | Status |
| --- | --- | ---: | --- |
| Age of Capricorn | mauve | 4 | Integrated |
| Age of Sagittarius | blue | 4 | Done |
| Age of Scorpio | red | 4 | Integrated |
| Age of Libra | green | 4 | Integrated |
| Age of Virgo | brown | 5 | Integrated |
| Age of Leo | yellow | 5 | Integrated |
| Age of Cancer | teal | 5 | Integrated |
| Age of Gemini | blue | 6 | Integrated |
| Age of Taurus | orange | 5 | Integrated |
| Age of Aries | pink | 5 | Integrated |
| Age of Pisces | turquoise | 5 | Integrated |
| Age of Aquarius | cyan | 5 | Integrated |

Total target for the twelve age chapters: 57 images. Sagittarius accounts for 4
completed images, leaving 53 new images after the pilot.

Framing chapters add 12 supporting images outside the zodiac-age sequence,
bringing full `/timeline/` coverage to 69 images.

Optional second pass: `preamble.md`, `in-the-beginning.md`, and
`the-wheel-keeps-turning.md`, 2-3 images each.

## Completed Pilot: Sagittarius

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-sagittarius-firmament` | after "The Firmament" atmospheric work | Ill. 1 - The firmament: a cleared band between the waters above and the waters below. | Done |
| `age-of-sagittarius-continent-raising` | after continent-raising setup | Ill. 2 - Continent-raising: the first dry land emerging from the global ocean. | Done |
| `age-of-sagittarius-survey` | before the scoping discussion | Ill. 3 - The planetary survey: seabed mapping and atmospheric modeling before the work began. | Done |
| `age-of-sagittarius-first-sunlight` | near the chapter close | Ill. 4 - First sunlight over the prepared world at the threshold of Scorpio. | Done |

## Batch 1: Capricorn

Palette: mauve, violet-gray, deep blue, cold silver.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-capricorn-threshold` | after Section I introduction | Ill. 1 - The threshold: a dark water-covered Earth before the work begins. | Integrated |
| `age-of-capricorn-homeworld` | after "The World That Sent Them" | Ill. 2 - The home world: a mature scientific civilization before its outward turn. | Integrated |
| `age-of-capricorn-voyage` | after "The Journey" | Ill. 3 - The voyage: the long transit from one inhabited world to another. | Integrated |
| `age-of-capricorn-survey` | after "The Survey" | Ill. 4 - The survey: orbital instruments measuring a mist-shrouded candidate world. | Integrated |

### Capricorn Prompts

`age-of-capricorn-threshold`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: a wide, quiet landscape of primordial Earth at the beginning of the Age of Capricorn, almost entirely covered by dark water and thick mist, with only a faint suggestion of orbital presence above. Scene/backdrop: global ocean under heavy cloud, no continents, no life, no cities. Subject: the threshold before any visible creation work begins. Palette: mauve, violet-gray, deep blue, cold silver. Composition: low horizon, broad empty water, cloud ceiling, a tiny distant survey light in the upper sky. Style: low-detail cinematic matte painting, atmospheric, restrained, no text, no logos, no diagrams, no sharp sci-fi spectacle.

`age-of-capricorn-homeworld`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: a distant view of the Elohim home world as a mature scientific civilization, seen as landscape rather than city detail. Scene/backdrop: luminous coastal research complexes beneath a large pale sun, far mountains or sea, subtle aircraft trails. Subject: the civilization that developed synthetic biology and interstellar travel before the Earth project. Palette: mauve, pearl violet, warm silver, deep blue shadows. Composition: broad landscape with architecture embedded into terrain, no readable text, no close people. Style: elegant low-detail concept art, calm, old, scientifically advanced, no fantasy ornament, no logos.

`age-of-capricorn-voyage`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the interstellar voyage from the home world toward Earth, shown as a quiet deep-space passage rather than an action scene. Scene/backdrop: small expedition vessels crossing a dark star field with a mauve nebular haze, a distant pale destination star ahead. Subject: the two-month journey that carries the project away from the home world. Palette: mauve, black-blue, silver, muted violet. Composition: very wide, vessels small against space, strong sense of distance and patience. Style: atmospheric matte painting, low-detail, no weapons, no explosions, no readable markings.

`age-of-capricorn-survey`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: orbital and atmospheric survey craft measuring a water-covered, mist-shrouded Earth before the first surface work. Scene/backdrop: high atmospheric view over global ocean, cloud layers, faint instrument beams or survey arcs. Subject: planetary selection, habitability measurement, and site modeling. Palette: mauve, blue-gray, cold white, deep ocean blue. Composition: curvature of the planet visible, tiny platforms and craft, subtle gridded light only as atmosphere, not as UI. Style: restrained cinematic concept art, no text, no diagram labels, no crowded spacecraft.

## Batch 1: Scorpio

Palette: red, ember, dark green, black soil, humid gold.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-scorpio-first-cell` | after "The First Biology" | Ill. 1 - The first cell: life assembled from chemistry in the new laboratories. | Integrated |
| `age-of-scorpio-teams` | after "The Teams and the Factions" | Ill. 2 - The distributed teams: separate laboratories working across the young supercontinent. | Integrated |
| `age-of-scorpio-artists` | after "The Artists" | Ill. 3 - The artists: beauty entering the biological program alongside function. | Integrated |
| `age-of-scorpio-green-world` | after "What the Age Produces" | Ill. 4 - The green world: the first biosphere spreading across the prepared land. | Integrated |

### Scorpio Prompts

`age-of-scorpio-first-cell`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: a quiet laboratory landscape at the beginning of biological creation, where the first plant cells are being assembled from chemistry. Scene/backdrop: partially open research structure beside dark water and new soil, warm red interior light, shallow bioreactors glowing softly. Subject: the first viable photosynthetic life emerging from inorganic chemistry. Palette: red, ember, black soil, dark green, humid gold. Composition: wide view, lab small within landscape, no close scientists, no screens with text. Style: atmospheric concept art, low-detail, reverent, no microscopic diagram, no labels.

`age-of-scorpio-teams`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: distributed biological research teams across the new supercontinent, represented by distant laboratory domes and green test plots under a red dawn. Scene/backdrop: broad young landmass with multiple small research stations separated by distance, early vegetation patches, wet ground. Subject: parallel factional teams comparing and developing plant varieties. Palette: red sky, dark green shoots, black earth, muted copper. Composition: sweeping aerial or hilltop view, multiple tiny stations, no crowded figures, no city. Style: low-detail cinematic matte painting, calm, organized, no text or symbols.

`age-of-scorpio-artists`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the moment artistic design enters the plant-creation program, shown as a serene bio-design garden rather than a literal studio. Scene/backdrop: experimental botanical terraces near a research pavilion, unfamiliar but plausible plant forms, warm red evening light. Subject: beauty and variation added to biological function. Palette: red, rose shadow, dark botanical green, soft gold. Composition: wide terrace landscape, no close faces, plants as silhouettes and masses rather than detailed specimens. Style: poetic concept art, low-detail, no fantasy flowers, no text, no diagrams.

`age-of-scorpio-green-world`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the end of Scorpio, with the prepared supercontinent now covered by abundant early vegetation and a living soil beneath it. Scene/backdrop: wide valley or coastal plain on a young continent, spreading green biomass, red-gold sky, no animals. Subject: a self-sustaining plant biosphere reshaping the atmosphere. Palette: deep green, red-gold light, black soil, misted blue distance. Composition: broad layered landscape with vegetation in sweeping bands, no people, no structures except perhaps one tiny distant station. Style: atmospheric matte painting, beautiful but restrained, no jungle clutter, no text.

## Batch 1: Libra

Palette: green, jade, night blue, white star light, soft gold.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-libra-calibrated-sky` | after Section I introduction | Ill. 1 - The calibrated sky: the luminaries becoming instruments of the project. | Integrated |
| `age-of-libra-observatories` | after "The Observation Infrastructure" | Ill. 2 - The observatories: a distributed network measuring days, years, and stars. | Integrated |
| `age-of-libra-biology-time` | after circadian/seasonal calibration discussion | Ill. 3 - Biological time: the growing biosphere tuned to solar and lunar rhythm. | Integrated |
| `age-of-libra-sky-ground` | near "What Libra Is" | Ill. 4 - Sky and ground: astronomical rhythm balanced against living earth. | Integrated |

### Libra Prompts

`age-of-libra-calibrated-sky`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: a green-tinged night landscape where the sun, moon, and stars are understood as instruments for time rather than as gods. Scene/backdrop: young vegetated plain beneath a precise, clear sky with moon and bright stars; faint observatory light at the horizon. Subject: the sky becoming useful for signs, seasons, days, and years. Palette: jade green, night blue, white star light, soft gold. Composition: wide horizon, sky dominant, land quiet and dark, no literal zodiac diagram. Style: restrained cinematic concept art, low-detail, no text, no constellational labels.

`age-of-libra-observatories`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: a distributed network of observatories on the young supercontinent, placed at different elevations and latitudes. Scene/backdrop: ridge, coastal plain, and distant highland stations under clear green-blue twilight. Subject: long-duration astronomical infrastructure for calibration and navigation. Palette: green, blue-black, white instrument light, muted stone. Composition: wide landscape with several tiny observatory structures connected by faint light traces; no UI overlays, no readable markings. Style: low-detail matte painting, scientific, quiet, no fantasy towers.

`age-of-libra-biology-time`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the biological program being tuned to planetary time, shown as experimental vegetation growing under controlled light beside an open sky. Scene/backdrop: research terraces with plants at different growth stages, a moonlit sky, subtle tidal or seasonal markers in the landscape. Subject: circadian, seasonal, and lunar calibration entering organism design. Palette: jade, dark green, moon white, warm gold, deep blue. Composition: broad terrace landscape, lab mostly distant, no close people, no diagrams. Style: atmospheric concept art, low-detail, no text, no literal clocks.

`age-of-libra-sky-ground`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the end of Libra, with sky and ground balanced: mature green groundcover below, precise celestial order above. Scene/backdrop: expansive living plain with observatory silhouettes, clear sky with moon and stars, first hint of seasonal variation. Subject: astronomy and biosphere brought into operational balance. Palette: rich green, night blue, white star light, soft gold. Composition: symmetrical but natural, low horizon, sky and ground equally weighted. Style: quiet cinematic matte painting, no text, no scales symbol, no diagram.

## Batch 2: Virgo

Palette: brown, umber, wet green, ocean blue, amber light, bone white.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-virgo-moving-world` | after Section I introduction | Ill. 1 - The moving world: the first visible animals entering sea, sky, and land. | Integrated |
| `age-of-virgo-oceanic-labs` | after "The Oceanic Laboratories" | Ill. 2 - The oceanic laboratories: aquatic life seeded through the one ocean. | Integrated |
| `age-of-virgo-birds` | after "The Air" | Ill. 3 - The birds: aesthetic excess taking flight across the firmament. | Integrated |
| `age-of-virgo-dragons` | after "The Dragons" | Ill. 4 - The dragons: formidable forms released by particular teams. | Integrated |
| `age-of-virgo-garden-of-forms` | near "What Virgo Is" | Ill. 5 - The garden of forms: a moving biosphere balanced across water, air, and land. | Integrated |

### Virgo Prompts

`age-of-virgo-moving-world`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the opening of the Age of Virgo, when the quiet plant world becomes visibly animate for the first time. Scene/backdrop: a broad young supercontinent coastline with dark soil, low forests, shallow water, and open sky. Subject: first macro-animals entering the visible world, suggested by small fish breaking the water, distant bird silhouettes, and faint reptilian movement far inland. Palette: brown, umber, wet green, ocean blue, amber light, bone white. Composition: very wide landscape, low to medium detail, no close animals, no spectacle, movement implied through spacing and silhouettes. Style: restrained cinematic matte painting, atmospheric, no text, no symbols, no diagrams.

`age-of-virgo-oceanic-labs`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: distributed aquatic laboratories seeding the first visible marine food web into the one ocean. Scene/backdrop: calm brown-green coastline and blue ocean with a few floating or partly submerged research platforms, faint underwater glow, early kelp beds, and small schools of fish in the shallows. Subject: plankton, small fish, and larger fish being introduced in a staged ecological program. Palette: umber coast, dark teal water, muted green, amber lab light, pale foam. Composition: wide coastal view, labs small and integrated into the seascape, no close scientists, no UI overlays, no text. Style: low-detail concept art, quiet engineering mood, ecological rather than industrial.

`age-of-virgo-birds`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the first birds filling the air, with beauty and display entering animal design through artist pressure. Scene/backdrop: warm brown cliffs and wet green forest edge beneath a clear amber sky, distant release terraces or aviary structures integrated into the terrain. Subject: colorful birds in flight and courtship motion, seen mostly as silhouettes and soft color marks rather than detailed specimens. Palette: brown, amber, wet green, cream, muted red and blue accents. Composition: sky-dominant wide landscape with many tiny bird forms, no close faces, no decorative pattern overload. Style: atmospheric matte painting, poetic but restrained, no fantasy creatures, no text.

`age-of-virgo-dragons`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the creation of the great tanninim, dragons or dinosaurs, shown as a troubling but majestic landscape rather than a monster scene. Scene/backdrop: vast umber plain with low vegetation, humid haze, distant laboratory outposts, and enormous reptilian silhouettes moving far away. Subject: formidable dinosaur-like forms released by particular factional teams, implying scale and political risk without violence. Palette: dark brown, red umber, bone white haze, black-green vegetation, muted gold. Composition: low horizon, animals distant and partly obscured by dust or mist, one tiny outpost for scale, no close teeth, no chase, no gore. Style: cinematic concept art, low-detail, serious, no Jurassic action-poster composition, no text.

`age-of-virgo-garden-of-forms`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the end of Virgo, with a fully moving biosphere balanced across water, air, and land. Scene/backdrop: panoramic coastline where ocean, wet forest, open plain, and sky meet in one continuous ecological landscape. Subject: abundant animal life as quiet distributed presence: fish in water, birds in air, distant reptilian forms on land, all integrated into a designed ecosystem. Palette: rich brown, wet green, ocean blue, amber sun, pale bone highlights. Composition: very wide layered landscape, no single dominant creature, movement everywhere but calm, a sense of ecological balance. Style: restrained matte painting, low to medium detail, no text, no diagram, no crowded wildlife documentary look.

## Batch 3: Leo

Palette: yellow, gold, dry green, warm stone, deep shadow, pale sky.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-leo-land-animals` | after "The Land Animals" | Ill. 1 - The land animals: herbivores and carnivores completing the terrestrial web. | Integrated |
| `age-of-leo-human-threshold` | after "From Primate to Human" | Ill. 2 - The human threshold: the primate template brought to the mirror. | Integrated |
| `age-of-leo-seven-teams` | after "The Factional Teams and the Seven Races" | Ill. 3 - The seven teams: one template shaped through seven provincial traditions. | Integrated |
| `age-of-leo-eden` | after "The Most Talented Team" | Ill. 4 - Eden: the most accomplished garden of the age. | Integrated |
| `age-of-leo-sphinx` | after "The Sphinx: A Monument of the Age" | Ill. 5 - The Sphinx: the lion age remembered in stone and sky. | Integrated |

### Leo Prompts

`age-of-leo-land-animals`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the early Age of Leo, when land animals complete the terrestrial food web after the world of Virgo. Scene/backdrop: golden supercontinent plain with dry green vegetation, scattered trees, distant water, and warm low sunlight. Subject: herbivore herds in the middle distance and a few carnivore silhouettes far away, all calm and ecologically balanced rather than predatory. Palette: yellow, gold, dry green, warm stone, deep shadow, pale sky. Composition: very wide 2:1 landscape, animals distributed quietly across the plain, no close animal portrait, no violence. Style: restrained cinematic matte painting, low to medium detail, no text, no symbols, no diagram.

`age-of-leo-human-threshold`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the threshold from advanced primate template to human design, shown as a quiet research landscape rather than a literal laboratory diagram. Scene/backdrop: warm golden highland research terrace with distant translucent work chambers, trees, and pale sky. Subject: a small group of indistinct human-like silhouettes seen from far away near a reflective pool or polished stone surface, suggesting the mirror idea without showing faces or specific races. Palette: gold, ochre, warm stone, dry green, soft white light. Composition: wide landscape with the figures tiny and anonymous, the environment dominant, no close bodies, no nudity, no medical scene. Style: atmospheric concept art, serious, humane, no text, no diagrams, no UI overlays.

`age-of-leo-seven-teams`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: seven factional creator teams working in parallel across the supercontinent, without depicting racial hierarchy or close human differences. Scene/backdrop: wide aerial view of a golden continental landscape divided by rivers, ridges, forests, and plains, with seven small research sites glowing faintly in different regions. Subject: one shared human-design template expressed through seven provincial scientific traditions, represented by the seven sites rather than close people. Palette: yellow gold, dry green, slate shadow, pale blue sky, subtle varied accent lights. Composition: very wide map-like landscape but not a literal map, seven sites visible as tiny lights, no symbols, no text, no flags. Style: restrained matte painting, low-detail, contemplative, no infographic.

`age-of-leo-eden`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the Garden of Eden as the most accomplished biological garden of Leo, created by the talented team in the region later remembered as Israel. Scene/backdrop: fragrant golden garden valley with water channels, flowering trees, lush plants, warm stone terraces, and distant research architecture integrated into the landscape. Subject: paradise as a designed living environment, with beauty, order, and intelligence implied; no close Adam and Eve scene. Palette: yellow gold, honey, fresh green, warm limestone, soft blue shadow. Composition: wide landscape, garden paths and water lead the eye inward, one or two tiny distant human silhouettes only for scale. Style: poetic cinematic concept art, low to medium detail, no fantasy palace, no religious iconography, no text.

`age-of-leo-sphinx`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the Sphinx as a monument of the Age of Leo, facing the equinoctial sunrise and the constellation Leo in the deep past. Scene/backdrop: early wet North African plateau before full desertification, golden dawn, distant humid green along the horizon, a newly carved lion-bodied monument facing east. Subject: the Sphinx as stone memory of the lion age and the human creation, with sky alignment implied atmospherically rather than diagrammed. Palette: gold, pale limestone, yellow dawn, muted green, blue-gray pre-dawn shadow. Composition: very wide landscape, monument mid-distance and dignified, sun low on horizon, no pyramids dominating, no modern ruins, no labels, no constellation lines. Style: restrained historical-concept matte painting, serious, no text, no tourist postcard.

## Batch 4: Cancer

Palette: teal, blue-green, wet stone, muted gold, copper light, storm gray, deep shadow.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-cancer-awakening` | after "The Awakening" | Ill. 1 - The awakening: forbidden knowledge crossing from makers to made. | Integrated |
| `age-of-cancer-expulsion` | after "The Expulsion and the Settlement" | Ill. 2 - The expulsion: the garden sealed and the exiles left on Earth. | Integrated |
| `age-of-cancer-long-generations` | after "The Tree of Life and the Long Generations" | Ill. 3 - The long generations: patriarchs and cities growing under borrowed longevity. | Integrated |
| `age-of-cancer-watchers` | after "The Sons of Elohim and the Daughters of Men" | Ill. 4 - The Watchers: descended teachers among the human settlements. | Integrated |
| `age-of-cancer-preflood-world` | after "The Broader World" | Ill. 5 - The pre-flood world: a networked civilization approaching the threshold. | Integrated |

### Cancer Prompts

`age-of-cancer-awakening`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the Age of Cancer awakening, when forbidden knowledge passes from the disclosing creators to the first humans. Scene/backdrop: teal twilight garden-laboratory at the edge of water channels and dense trees, with distant translucent research architecture half-hidden among foliage. Subject: a small group of indistinct human figures in the middle distance facing a calm luminous teaching presence or opened archive of light; the knowledge transfer is atmospheric, not literal. Palette: teal, blue-green, wet stone, muted gold, soft copper light, deep shadow. Composition: very wide 2:1 landscape, figures tiny and anonymous, environment dominant, no close faces, no nudity, no serpent animal, no religious iconography. Style: restrained cinematic matte painting, low to medium detail, serious and humane, no text, no diagram.

`age-of-cancer-expulsion`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the Eden expulsion and political settlement at the start of Cancer, with the garden sealed and the dissident creators left on Earth. Scene/backdrop: wet teal dawn outside a walled garden valley, with a sealed luminous gate, mist, trees, and distant water. Subject: two or three tiny human silhouettes walking away from the garden while several distant exiled creator figures remain outside the perimeter; guardian lights at the gate imply armed sentries without showing combat. Palette: teal, blue-green, storm gray, wet stone, muted gold, copper highlights. Composition: very wide landscape, gate off-center, exiles and humans small, strong sense of separation and consequence, no angels, no wings, no demons, no flaming sword close-up. Style: sober historical-concept matte painting, low to medium detail, no text, no symbol.

`age-of-cancer-long-generations`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the long generations after Eden, with patriarchal leaders and early city life developing under limited tree-of-life longevity. Scene/backdrop: early pre-flood settlement on a teal river plain, stone terraces, cultivated fields, workshops, small herds, and water channels under a low luminous sky. Subject: one distant elder-leader figure on a terrace overlooking younger generations building, farming, and trading below; longevity suggested by continuity and scale, not by medical imagery. Palette: teal water, blue-green vegetation, wet limestone, muted gold lamps, copper dusk. Composition: wide landscape with settlement layers receding into distance, people tiny and generalized, no portraits, no biblical costume drama. Style: restrained matte painting, low to medium detail, no text, no diagram.

`age-of-cancer-watchers`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the Watchers and Nephilim period, showing descended teachers among human settlements without literalizing sexual relationships or racial claims. Scene/backdrop: teal nightfall over a growing pre-flood city, with workshops, observatory terraces, and water-lit streets. Subject: tall but distant teacher figures among human groups, demonstrating metallurgy, astronomy, and writing through glowing tools and sky observation; hybrid legacy implied by scale and civic presence, not by close bodies. Palette: dark teal, blue-green, copper firelight, muted gold, stone gray, deep shadow. Composition: very wide cityscape, figures small and respectful, no intimacy, no violence, no giant monster imagery, no wings, no halos, no demons. Style: serious cinematic concept art, low to medium detail, no text, no symbols.

`age-of-cancer-preflood-world`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the end of Cancer, when the networked pre-flood world has advanced far enough to alarm the home world. Scene/backdrop: panoramic teal supercontinent with connected cities, river routes, coastal lights, distant monumental sites, and storm clouds gathering beyond the horizon. Subject: a civilization at substantial sophistication and political danger, with tiny trade routes, watch fires, and faint orbital or high-sky observation lights implying distant scrutiny. Palette: teal, blue-green, storm gray, wet stone, muted gold city light, cold white sky glints. Composition: very wide 2:1 landscape, elevated viewpoint, no literal map labels, no destruction yet, no flood wave, no modern skyscrapers. Style: restrained epic matte painting, low to medium detail, ominous but quiet, no text, no diagram.

## Batch 5: Gemini

Palette: deep blue, storm blue, cold white, slate, sea green, silver, dark cloud.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-gemini-flood-decision` | after "The Decision" | Ill. 1 - The decision: the home world turns from warning to intervention. | Integrated |
| `age-of-gemini-ark-preparation` | after "The Counter-Preparation: Building the Ark" | Ill. 2 - The ark prepared: preservation work under a darkening sky. | Integrated |
| `age-of-gemini-orbital-ark` | after "The Genetic Cargo" | Ill. 3 - The orbital refuge: life held above the catastrophe. | Integrated |
| `age-of-gemini-cataclysm` | after "The Catastrophe" | Ill. 4 - The cataclysm: the waters and the continents remade. | Integrated |
| `age-of-gemini-covenant` | after "The Recovery and the Covenant" | Ill. 5 - The covenant: the remnant returns to a changed world. | Integrated |
| `age-of-gemini-war-in-heaven` | after "The War in Heaven" | Ill. 6 - The war in heaven: the last conflict over humanity's future. | Integrated |

### Gemini Prompts

`age-of-gemini-flood-decision`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the opening decision of the Age of Gemini, when the home-world Council turns from warning to catastrophic intervention against the pre-flood civilization. Scene/backdrop: vast high council landscape on a distant advanced world, with cold blue architecture embedded in cliffs above an ocean or cloud plain, tiny decision-makers implied only by lights and silhouettes. Subject: a grieving political decision becoming operational, with distant starward communication beams aimed toward Earth but no readable screens. Palette: deep blue, storm blue, cold white, slate, silver, dark cloud. Composition: very wide 2:1 landscape, architecture and sky dominant, no close faces, no throne room, no religious iconography, no text. Style: restrained cinematic matte painting, low to medium detail, solemn, no spectacle, no diagrams.

`age-of-gemini-ark-preparation`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: Noah's ark prepared as an orbital preservation vessel, built by human and exiled-creator partners under a darkening pre-flood sky. Scene/backdrop: broad blue-gray construction basin on the supercontinent, water channels, scaffolding, preservation facilities, and a sealed vessel integrated into the landscape rather than shaped like a wooden boat. Subject: preservation work under deadline pressure, with tiny anonymous workers, sample convoys, and soft laboratory light. Palette: storm blue, sea green, slate, cold white, muted silver, dark cloud. Composition: very wide landscape, vessel mid-distance, workers small, no close Noah portrait, no animals marching two by two, no text. Style: atmospheric concept art, serious, technical but quiet, no UI overlays, no diagram.

`age-of-gemini-orbital-ark`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the ark as an orbital refuge carrying human survivors and genetic cargo above the flood catastrophe. Scene/backdrop: high orbit over Earth, with the curved planet below partly obscured by storm systems, impact haze, and cold blue atmospheric glow. Subject: a large quiet preservation vessel and a few smaller support craft suspended above the catastrophe, implying life held safe without showing interiors. Palette: deep blue space, storm blue atmosphere, cold white light, slate shadow, silver hull, faint sea green. Composition: very wide 2:1, ark small to medium against the planet, no explosions dominating, no visible suffering, no labels or markings. Style: restrained cinematic space moodscape, low to medium detail, solemn, no text, no diagram.

`age-of-gemini-cataclysm`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the flood cataclysm and shattering of the supercontinent, shown from a distant elevated viewpoint as planetary transformation rather than disaster spectacle. Scene/backdrop: vast blue-black ocean and fractured landmass under storm towers, radiant impact glow far on the horizon, sheets of rain, broken coastlines, and new seas opening through the land. Subject: waters from below and above, continental fragments beginning to separate, the old world being remade. Palette: storm blue, black slate, cold white foam, sea green water, silver lightning, dark cloud. Composition: very wide landscape, no bodies, no cities in close destruction, no gore, no tsunami action-poster framing, no text. Style: atmospheric matte painting, epic but restrained, low to medium detail, geological scale.

`age-of-gemini-covenant`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the post-flood recovery and covenant, with the remnant returning to a reshaped Earth and the bow laid down in the clouds. Scene/backdrop: newly exposed wet highland above receding waters, broken coastlines in the distance, young vegetation returning, cold blue sky clearing after long storms. Subject: tiny human and creator silhouettes gathered near a simple altar or landing site, with a pale rainbow arc in cloud as atmospheric sign rather than religious symbol. Palette: blue, sea green, wet slate, cold white, muted silver, soft gold sunrise. Composition: wide landscape, figures tiny and anonymous, horizon clearing, no close Noah scene, no animals in parade, no divine hand, no text. Style: restrained historical-concept moodscape, quiet recovery, low to medium detail.

`age-of-gemini-war-in-heaven`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the war in heaven after Babel, shown as a distant conflict between advanced factions over Earth and humanity's future, without angelic or demonic imagery. Scene/backdrop: night sky above a dark post-flood mountain and sea landscape, with distant orbital lights, atmospheric contrails, and faint energy flashes high above the clouds. Subject: a conflict moving from political rupture into open war, with the Earthbound alliance below and the home-world Council above implied through position and motion. Palette: deep blue, black slate, cold white, silver, storm violet, faint sea green. Composition: very wide 2:1 landscape, sky dominant, conflict distant, no angels, no demons, no wings, no close combat, no explosions filling the frame, no text. Style: sober cinematic matte painting, low-detail, mythic but technological, no symbols or diagrams.

## Batch 6: Taurus

Palette: burnt orange, copper dawn, lapis blue, warm limestone, desert rose, olive green, black basalt, salt white.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-taurus-pardon` | after "The Pardon and the Long Quiet" | Ill. 1 - The pardon: the exiles return to plead humanity's case. | Integrated |
| `age-of-taurus-bull-civilizations` | after "The Rise of the Post-Flood Civilizations" | Ill. 2 - The Taurean world: post-flood civilizations rising under the sign of the bull. | Integrated |
| `age-of-taurus-cities-plain` | after "The Humans Alone, the Cities of the Plain" | Ill. 3 - The Cities of the Plain: inheritance gathering into a dangerous project. | Integrated |
| `age-of-taurus-dead-sea-strike` | after "The Two Scouts, the Strike, and the Dead Sea" | Ill. 4 - The strike: the fertile plain overturned into salt and silence. | Integrated |
| `age-of-taurus-abraham-test` | after "Abraham at the Edge" | Ill. 5 - The test: Abraham's lineage verified for the recovery program. | Integrated |

### Taurus Prompts

`age-of-taurus-pardon`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the pardon at the beginning of the Age of Taurus, with the exiled creators returning to the home world to plead humanity's case. Scene/backdrop: an advanced home-world civic landscape at copper dawn, broad terraces, ocean or cloud plain below, and distant assemblies watching a small delegation arrive. Subject: return from exile and public advocacy for Earth, with Earth suggested as a small blue point or holographic globe in the distance but no readable display. Palette: burnt orange, copper dawn, lapis blue, warm limestone, silver, soft cloud white. Composition: very wide 2:1 landscape, figures tiny and anonymous, architecture embedded in landscape, no throne room, no close faces, no religious iconography, no text. Style: restrained cinematic matte painting, low to medium detail, political and quiet rather than triumphant.

`age-of-taurus-bull-civilizations`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the post-flood civilizations of Taurus rising across river valleys and trade routes under the cultural sign of the bull. Scene/backdrop: wide elevated view joining several early Bronze Age landscapes in one continuous panorama: river city terraces, distant pyramid-like monuments, fields, herds, boats, and trade caravans. Subject: civilizational recovery and bull-age symbolism, with bull forms present only as distant herds, carved horn shapes, or small ritual silhouettes, not as a giant symbol. Palette: burnt orange sky, olive green fields, lapis blue water, warm limestone, desert rose, black basalt shadows. Composition: very wide 2:1, multiple centers connected by routes, people tiny, no literal map labels, no flags, no readable marks. Style: atmospheric historical-concept matte painting, low to medium detail, no infographic, no modern city.

`age-of-taurus-cities-plain`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the Cities of the Plain during the long quiet, prosperous but politically dangerous, where fragments of inherited knowledge gather into a vengeance project. Scene/backdrop: fertile orange-green plain near a broad water basin, walled cities, orchards, canals, workshops, and hidden elevated facilities under a copper evening sky. Subject: urban prosperity and concealed technical ambition before the strike, with tiny anonymous figures and faint guarded lights but no visible violence. Palette: copper orange, olive green, lapis water, warm stone, black basalt, salt-white haze. Composition: wide landscape, cities mid-distance, basin and mountains framing the scene, no close crowd, no biblical costume drama, no text. Style: restrained matte painting, ominous but quiet, low to medium detail.

`age-of-taurus-dead-sea-strike`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the Sodom and Gomorrah strike and the Dead Sea basin as aftermath, shown at great distance as landscape transformation rather than spectacle. Scene/backdrop: high overlook of a fertile plain being overturned into a salt basin, with a distant vertical flash fading on the horizon, mineral haze, broken water channels, and white salt spreading across orange terrain. Subject: a targeted preventive strike leaving the physical scar later remembered as the Dead Sea. Palette: dark orange, salt white, black basalt, sulfur yellow, lapis shadow, smoky gray. Composition: very wide 2:1, no bodies, no close city destruction, no firestorm poster composition, no divine hand, no angels, no text. Style: sober cinematic matte painting, low to medium detail, geological and tragic.

`age-of-taurus-abraham-test`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: Abraham's loyalty test at the edge of Taurus, shown as a distant mountain scene of assessment and interruption, not as violence. Scene/backdrop: warm orange dawn over a bare highland ridge, a simple stone altar, low shrubs, and a vast empty sky with a faint descending light far above. Subject: two tiny anonymous figures at the altar and a ram-like animal shape caught in a thicket nearby, suggesting the test and its peaceful stop without showing a knife, harm, or close faces. Palette: copper dawn, warm limestone, desert rose, olive scrub, lapis blue shadow, soft white light. Composition: very wide landscape, figures small, silence and tension carried by space, no gore, no child close-up, no religious iconography, no text. Style: restrained historical-concept moodscape, low detail, solemn and humane.

## Batch 7: Aries

Palette: rose pink, desert rose, copper light, warm limestone, indigo night, linen white, black basalt, muted gold.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-aries-burning-bush` | after "The Burning Bush and the Mission Briefing" | Ill. 1 - The mission briefing: the direct-contact operation begins in the wilderness. | Integrated |
| `age-of-aries-wilderness-column` | after "The Plagues, the Departure, and the Wilderness" | Ill. 2 - The departure: a guided people sustained between empire and land. | Integrated |
| `age-of-aries-sinai-law` | after "Sinai and the Law" | Ill. 3 - Sinai: law descends as public order. | Integrated |
| `age-of-aries-ark-conquest` | after "The Tabernacle, the Ark, and the Conquest" | Ill. 4 - The Ark: alliance hardware moving with the camp and the campaign. | Integrated |
| `age-of-aries-axial-preparation` | after "The End of Aries and the Preparation for Pisces" | Ill. 5 - The Axial preparation: many civilizations readied for Pisces. | Integrated |

### Aries Prompts

`age-of-aries-burning-bush`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the burning bush encounter as a mission briefing at the beginning of Aries, with Moses tiny in a desert wilderness and a restrained landing craft illuminating thorn bushes without consuming them. Scene/backdrop: rose-pink Sinai dusk, dry scrub, warm limestone ridges, a small flock far away, and a compact luminous vessel partly veiled by dust and plasma glow. Subject: direct contact resuming with the Eden lineage through Moses, shown as operational encounter rather than religious icon. Palette: rose pink, desert rose, copper light, warm limestone, indigo shadow, linen white. Composition: very wide 2:1 landscape, Moses and animals tiny, craft small and integrated into the terrain, no close faces, no angels, no wings, no halos, no readable symbols. Style: restrained cinematic matte painting, low to medium detail, quiet and uncanny, no text, no diagram.

`age-of-aries-wilderness-column`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the Exodus departure and wilderness support, shown as a long displaced people moving through desert under a pillar-like guidance phenomenon. Scene/backdrop: wide rose-copper desert plain between Egypt and Sinai, distant water or reed sea behind, encampment traces, dawn haze, and an upright cloud-by-day / fire-by-night column at the horizon. Subject: navigation, protection, synthetic food, water, and field support for a dependent population in transit. Palette: dusty pink, copper dawn, warm sand, linen white cloud, indigo distance, muted gold sparks. Composition: very wide landscape, human column tiny and anonymous, no battle, no drowning bodies, no close Pharaoh scene, no literal miracle spectacle, no text. Style: low-detail historical-concept moodscape, atmospheric, sober, technologically ambiguous.

`age-of-aries-sinai-law`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: Mount Sinai as a formal alliance audience where law is given, with a mountain under smoke, light, and controlled distance protocols. Scene/backdrop: rose and indigo mountain valley, Israelite camp far below, summit wrapped in copper-white cloud and furnace-like light, atmospheric shock and dust around a descending craft silhouette. Subject: public awe, security perimeter, and the legal framework entering the culture. Palette: rose pink, black basalt, copper-white light, warm limestone, deep indigo, muted gold. Composition: very wide 2:1 landscape, mountain dominant, camp tiny, no close Moses, no readable tablets or letters, no divine hand, no angels, no halos, no text. Style: restrained cinematic matte painting, serious and monumental but low-detail.

`age-of-aries-ark-conquest`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the Tabernacle, Ark of the Covenant, and early conquest as mobile alliance hardware moving with Israel, shown from a respectful distance. Scene/backdrop: rose-gold desert camp with a compact tabernacle enclosure, distant walled city and river crossing beyond, priests and carriers reduced to tiny silhouettes, faint electromagnetic glow contained inside the sanctuary area. Subject: a dangerous communications and power artifact central to the camp and campaign, with conquest implied through landscape logistics rather than violence. Palette: desert rose, muted gold, warm linen, copper, black basalt shadow, indigo sky. Composition: wide landscape, tabernacle mid-distance, no close artifact detail, no readable symbols, no violence, no collapsing bodies, no religious iconography, no text. Style: atmospheric historical-concept matte painting, low to medium detail, quiet hardware presence.

`age-of-aries-axial-preparation`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the late Aries preparation for Pisces, when prophetic traditions and philosophical civilizations across Eurasia are cultivated in parallel. Scene/backdrop: panoramic rose-indigo twilight joining multiple distant cultural landscapes in one continuous horizon: Jerusalem hills, Persian highlands, Greek coastal city, Indian river plain, Chinese mountain observatory, all suggested by silhouettes rather than detailed monuments. Subject: indirect cultivation after the discovery, many lineages being readied for a pluriform prophetic strategy. Palette: rose pink, indigo night, copper city lights, muted turquoise accents, warm limestone, linen white stars. Composition: very wide 2:1 elevated panorama, no literal map, no borders, no flags, no readable writing, no giant symbols, people tiny or absent. Style: restrained epic matte painting, low to medium detail, contemplative, no infographic, no text.

## Batch 8: Pisces

Palette: turquoise, sea green, pearl white, warm gold, Levant sand, deep indigo, soft coral.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-pisces-annunciation` | after "The Preparation and the Conception" | Ill. 1 - The conception: the Piscean intervention enters a human household. | Integrated |
| `age-of-pisces-galilee-mission` | after "The Scientific Miracles and the Cosmic-Competition Teaching" | Ill. 2 - The mission: fishers and parables carry the hidden teaching. | Integrated |
| `age-of-pisces-doubled-signature` | after "The Commission and the Fish-and-Virgin Signature" | Ill. 3 - The doubled signature: fish and virgin preserve the age's memory. | Integrated |
| `age-of-pisces-islamic-intervention` | after "Islam and the Question of Its Origin" | Ill. 4 - The Islamic intervention: the message takes a second Piscean route. | Integrated |
| `age-of-pisces-scientific-threshold` | after "The Signs of the End" | Ill. 5 - The threshold: science brings Pisces to the edge of Aquarius. | Integrated |

### Pisces Prompts

`age-of-pisces-annunciation`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the Piscean conception operation in Nazareth, shown as a quiet human household under restrained alliance presence rather than a religious annunciation icon. Scene/backdrop: turquoise-blue Galilean night, limestone village terraces, small courtyard, olive trees, distant hills, a compact pearl-white light or craft high above casting a soft beam into one humble house. Subject: the final direct intervention entering a human household through Mary and Joseph's managed social world. Palette: turquoise, pearl white, warm gold window light, Levant sand, deep indigo, soft coral shadow. Composition: very wide 2:1 landscape, people tiny or implied inside the lit house, no close Mary, no pregnancy scene, no angel wings, no halos, no divine hand, no readable text, no crosses. Style: restrained cinematic matte painting, low to medium detail, tender but operational.

`age-of-pisces-galilee-mission`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: Jesus's Galilean mission as a landscape of fishermen, teaching, scientific miracles, and the hidden cosmic-competition parable. Scene/backdrop: turquoise dawn over the Sea of Galilee, small fishing boats, shore fields, scattered listeners, and a faint luminous disturbance on the water far from shore. Subject: fishers becoming messengers and parables carrying the deeper teaching about created worlds. Palette: turquoise water, sea green fields, pearl mist, warm gold sunrise, indigo shadows, soft coral sky. Composition: very wide 2:1 landscape, figures tiny and anonymous, lake and fields sharing the frame, no close Jesus portrait, no halos, no cross, no literal fish symbol, no readable text, no spectacle. Style: quiet historical-concept moodscape, atmospheric and humane.

`age-of-pisces-doubled-signature`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the fish-and-virgin doubled signature of Pisces, shown as cultural memory distributed through landscape rather than as a church icon. Scene/backdrop: turquoise coastal monastery garden at twilight, shallow water with small fish glints, a distant white-veiled woman silhouette crossing a terrace, fishermen's nets drying near stone steps, stars just appearing above the sea. Subject: Pisces and Virgo encoded together in the age's Christian memory without literal zodiac diagrams. Palette: turquoise, pearl white, sea green, muted gold lamps, indigo sky, soft coral stone. Composition: very wide 2:1 landscape, woman and fishermen tiny, no Madonna icon, no halo, no crescent, no church cross, no readable symbols, no text. Style: restrained poetic matte painting, low to medium detail, symbolic but not illustrative.

`age-of-pisces-islamic-intervention`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the Islamic intervention as a second Piscean route for the message, with the Petra/Levantine question kept atmospheric rather than diagrammatic. Scene/backdrop: turquoise night over a sandstone canyon city and desert trade routes, early prayer courtyard silhouettes, caravan lights, distant observatory-like high place, and stars reflected in water channels. Subject: a new prophetic transmission emerging from the Jewish-Christian-Arabic cultural matrix and spreading across routes. Palette: turquoise night, sea-green shadow, rose sandstone, pearl star light, warm gold lamps, deep indigo. Composition: very wide 2:1 landscape, no close Muhammad depiction, no faces, no readable Arabic, no crescent emblem, no flags, no map arrows, no text. Style: sober historical-concept moodscape, low to medium detail, reverent but non-iconic.

`age-of-pisces-scientific-threshold`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the end of Pisces, when medieval religious worlds give way to humanity's own scientific maturity and the Aquarian threshold appears. Scene/backdrop: wide turquoise-to-indigo panorama blending observatory domes, manuscript rooms, early laboratories, telescope silhouettes, Dead Sea cave openings, a distant city of 1940s lights, and a pale rocket-like trail near the horizon. Subject: independent scientific development reaching the threshold marked by 1946, Israel's restoration, and renewed contact. Palette: turquoise, cyan-white instrument light, warm gold, deep indigo, stone gray, soft coral dawn. Composition: very wide 2:1 landscape, no mushroom cloud, no national flags, no UN logo, no readable papers, no equations, no text, no crowded modern skyline. Style: restrained epic matte painting, contemplative transition from old age to new.

## Batch 9: Aquarius

Palette: cyan, electric blue, clear white, silver, deep indigo, water blue, black earth, warm gold.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `age-of-aquarius-nuclear-threshold` | after "1946: The First Year of the New Era" | Ill. 1 - The threshold: humanity reaches powers once reserved for its makers. | Integrated |
| `age-of-aquarius-rael-contact` | after "1973: The Contact" | Ill. 2 - The contact: the Aquarian disclosure begins at Puy-de-Lassolas. | Integrated |
| `age-of-aquarius-world-government-seed` | after "The New Commandments" | Ill. 3 - The seed of world government: one planet beginning to imagine one polity. | Integrated |
| `age-of-aquarius-embassy` | after "The Embassy and the Third Temple" | Ill. 4 - The embassy: a place prepared for the return of the creators. | Integrated |
| `age-of-aquarius-two-futures` | after "The Two Futures and the Golden Age" | Ill. 5 - The two futures: golden age or self-destruction at the threshold. | Integrated |

### Aquarius Prompts

`age-of-aquarius-nuclear-threshold`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the 1945-1946 Aquarian threshold, when humanity acquires atomic power and the age opens. Scene/backdrop: very wide cyan-indigo night desert plain with distant test towers, a restrained white-blue horizon flash far away, observatory silhouettes, early computing rooms suggested by small window grids, and a faint water-bearer stream of light crossing the sky. Subject: civilizational maturity and danger at the crossing from Pisces into Aquarius, shown as threshold rather than catastrophe. Palette: cyan, electric blue, clear white, silver, deep indigo, black earth, faint warm gold. Composition: very wide 2:1 landscape, flash small and distant, no mushroom cloud, no bodies, no city destruction, no flags, no readable documents, no equations, no text. Style: restrained cinematic matte painting, low to medium detail, sober, luminous, not an action scene.

`age-of-aquarius-world-government-seed`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the seed of world government in the Aquarian age, from the United Nations and global institutions toward a single planetary coordination. Scene/backdrop: wide cyan dawn over a circular international assembly landscape beside water, many small delegations approaching through bridges and river-like paths, Earth suggested as a pale reflected globe in a pool or sky but no actual logo. Subject: nations beginning to flow toward one coordinating center, the political water imagery of Aquarius. Palette: cyan, water blue, clear white, silver architecture, deep indigo shadows, warm gold interior lights, muted green land. Composition: very wide 2:1 landscape, people tiny and anonymous, no UN emblem, no national flags, no readable placards, no map labels, no text. Style: quiet civic matte painting, optimistic but restrained, low to medium detail.

`age-of-aquarius-rael-contact`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the December 1973 contact at Puy-de-Lassolas, when the Aquarian disclosure begins in an extinct volcanic crater in France. Scene/backdrop: cold cyan winter morning in the Auvergne, dark volcanic crater bowl, frost on grass and basalt, low mist, and a small silent metallic craft descended into the crater. Subject: a single ordinary human figure at great distance receiving contact from a small humanoid emissary, with the encounter quiet and operational rather than sensational. Palette: cyan mist, silver craft light, deep indigo volcanic shadow, black basalt, clear white frost, faint warm gold horizon. Composition: very wide 2:1 landscape, figures tiny, no close portrait of Rael, no readable symbols, no UFO poster drama, no beams hitting faces, no text. Style: restrained historical-concept matte painting, uncanny and quiet, low to medium detail.

`age-of-aquarius-embassy`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the embassy for the Elohim as the Aquarian Third Temple, a diplomatic and scientific center prepared for open return. Scene/backdrop: wide cyan-white coastal or desert-edge site at dawn, a low futuristic embassy complex within a discreet circular boundary, water channels flowing outward, landing platform, gardens, and distant pilgrimage roads approaching from several directions. Subject: a prepared place where the water of understanding flows from the threshold into the world. Palette: cyan, clear white, silver, water blue, warm gold windows, pale stone, deep indigo shade, muted green gardens. Composition: very wide 2:1 landscape, architecture integrated into terrain, no giant religious monument, no flags, no logos, no readable signage, no crowd closeups, no text. Style: restrained architectural moodscape, clean and contemplative, low to medium detail.

`age-of-aquarius-two-futures`

> Use case: stylized-concept. Asset type: timeline chapter moodscape. Primary request: the two possible Aquarian futures: self-destruction or Golden Age, held in one threshold landscape. Scene/backdrop: a single wide horizon split subtly by light, with one side showing dark indigo industrial clouds, warning lights, and distant ruined infrastructure, and the other side showing cyan-gold gardens, clean laboratories, quiet cities, water channels, and a pale path toward stars. Subject: humanity standing at the threshold between catastrophic failure and mature participation in the creation cycle. Palette: cyan, clear white, warm gold, water blue, silver, deep indigo, black earth, muted green. Composition: very wide 2:1 landscape, contrast integrated naturally, no gore, no mushroom cloud, no superhero apocalypse, no utopian skyline spectacle, no readable text. Style: restrained symbolic matte painting, contemplative, low to medium detail.

## Framing Chapter Addendum

These chapters sit outside the twelve zodiac ages but are part of the rendered
`/timeline/` reading sequence.

### Preamble

Palette: silver, charcoal, moon white, parchment gold, muted cyan, deep blue, soft amber.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `preamble-recurring-shape` | after "A Shape That Recurs" | Ill. 1 - The recurring shape: many traditions remember a council above the world. | Integrated |
| `preamble-cross-cultural-pattern` | after "The Pattern Across Traditions" | Ill. 2 - The pattern across traditions: fragments from many cultures converge on one question. | Integrated |
| `preamble-chaos-polarity` | after "Crichton, Chaos, and the Polarity" | Ill. 3 - The polarity: the maker's confidence answered by the cautionary voice. | Integrated |
| `preamble-open-door` | after "The Door" | Ill. 4 - The door: the corpus begins as an interpretive threshold. | Integrated |

#### Preamble Prompts

`preamble-recurring-shape`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: the recurring shape behind the corpus: a prior intelligence, a deliberating council above the world, and life on Earth as the outcome of contested decisions. Scene/backdrop: very wide silver-blue night landscape with Earth below as a dark ocean-and-cloud world, high above it a distant luminous council terrace or orbital chamber implied by silhouettes and lights. Subject: memory of a decision above the world recurring across traditions. Palette: silver, moon white, charcoal, muted cyan, deep blue, soft amber. Composition: very wide 2:1 landscape, figures tiny and anonymous, no throne room, no angels, no halos, no readable symbols, no text. Style: restrained cinematic matte painting, low to medium detail, contemplative and unresolved.

`preamble-cross-cultural-pattern`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: cross-cultural creation traditions preserving fragments of one structural pattern. Scene/backdrop: wide moonlit archive-landscape where stone tablets, scroll shelves, cave paintings, oceanic carvings, desert stelae, and mountain ritual sites appear as small illuminated fragments across one continuous horizon. Subject: many traditions disagreeing in detail but sharing an underlying shape. Palette: silver, parchment gold, muted cyan, charcoal stone, deep blue night, soft amber lamps. Composition: very wide 2:1 landscape, no readable writing, no literal map, no flags, no giant religious symbols, people tiny or absent. Style: restrained poetic matte painting, low to medium detail, scholarly but atmospheric.

`preamble-chaos-polarity`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: the Jurassic Park / chaos-theory polarity as a secular mirror of the ancient creator argument. Scene/backdrop: wide silver-charcoal research island or remote laboratory compound at stormy dusk, bio-containment structures, jungle edge, abstract fractal storm patterns in clouds, and two distant human silhouettes facing the facility from opposite sides of a path. Subject: the maker's confidence and the cautionary voice before complex life escapes control. Palette: silver, charcoal, electric rain blue, muted green, soft amber lab light, moon white. Composition: very wide 2:1 landscape, no dinosaurs in close view, no movie references, no gore, no readable monitors, no equations, no text. Style: restrained cinematic concept art, low to medium detail, tense but not action-oriented.

`preamble-open-door`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: the corpus as an open door into the twelve-age sequence. Scene/backdrop: wide silver dawn interior-exterior threshold, a simple monumental doorway standing open onto a distant cosmic landscape where the zodiacal wheel is suggested by faint lights along a horizon path. Subject: invitation to attention rather than belief, with the reader implied at the threshold. Palette: silver, moon white, soft amber, muted cyan, deep blue, charcoal shadow. Composition: very wide 2:1 landscape, no readable inscriptions, no religious iconography, no literal text, no oversized symbols, no person close-up. Style: restrained symbolic matte painting, quiet and spacious, low to medium detail.

### In the Beginning

Palette: yellow gold, black basalt, deep blue, silver, pale green, amber laboratory light, star white.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `in-the-beginning-home-civilization` | after "The Civilization Before" | Ill. 1 - The home civilization: a mature world reaches the threshold of creation. | Integrated |
| `in-the-beginning-synthesis-work` | after "The Synthesis Work" | Ill. 2 - The synthesis work: life assembled in laboratories before the crisis. | Integrated |
| `in-the-beginning-council-vote` | after "The Vote" | Ill. 3 - The vote: the home world closes the work, but the question remains alive. | Integrated |
| `in-the-beginning-arrival` | after "The Arrival" | Ill. 4 - The arrival: the relocation expedition reaches the barren Earth. | Integrated |

#### In the Beginning Prompts

`in-the-beginning-home-civilization`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: the Elohim home civilization before the Earth project, technologically mature and politically organized around a council of long-lived leaders. Scene/backdrop: very wide golden-blue alien home world at dusk, advanced civic terraces embedded in mountains and water, orbital paths faint in the sky, a distant council complex glowing above a city. Subject: a civilization much like ours at a higher stage, reaching the threshold of creation. Palette: yellow gold, deep blue, silver, black basalt, star white, pale green gardens, amber lights. Composition: very wide 2:1 landscape, people tiny, no close faces, no throne room, no readable signage, no text. Style: restrained epic matte painting, low to medium detail, civic and calm.

`in-the-beginning-synthesis-work`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: the synthesis work on the home planet, where laboratories begin assembling living organisms from non-living materials. Scene/backdrop: wide golden-silver research valley with transparent laboratories, soft bioluminescent tanks, sterile courtyards, and distant institutional buildings under a deep blue sky. Subject: cellular and organismic synthesis becoming ordinary within a mature scientific culture. Palette: amber lab light, silver glass, yellow gold, pale green bioluminescence, deep blue, black basalt shadow. Composition: very wide 2:1 landscape, no close creatures, no horror imagery, no readable screens, no equations, no text. Style: restrained scientific moodscape, low to medium detail, beautiful but uneasy.

`in-the-beginning-council-vote`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: the Council vote to halt the synthesis work after the breach, with laboratories closing and a political decision becoming irreversible. Scene/backdrop: wide golden-black civic terrace at night overlooking darkened laboratory districts, small council silhouettes in a luminous chamber, sealed research domes below, and transport lights beginning to move toward the horizon. Subject: the conservative vote wins at home while the defeated scientists retain the unresolved question. Palette: yellow gold, black basalt, deep blue, silver, amber windows, cold white. Composition: very wide 2:1 landscape, no violence, no monsters, no close courtroom, no readable documents, no text. Style: restrained political matte painting, solemn and quiet.

`in-the-beginning-arrival`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: the relocation expedition arriving at a barren early Earth to begin the Capricorn-age surveys. Scene/backdrop: wide golden dawn over lifeless Earth coast or volcanic plain, dark oceans, empty rock, low atmosphere haze, several small survey craft descending, and temporary lights marking future base sites across the land. Subject: seven creation teams arriving at a raw-material world before life begins. Palette: yellow gold dawn, black basalt, deep blue ocean, silver craft light, pale green atmospheric haze, star white. Composition: very wide 2:1 landscape, craft small, no modern city, no existing plants or animals, no flags, no readable markings, no text. Style: restrained cinematic space-historical moodscape, low to medium detail.

### The Wheel Keeps Turning

Palette: lavender, deep indigo, silver, clear white, cyan, warm gold, black, muted green.

| Slug | Placement | Caption | Status |
| --- | --- | --- | --- |
| `wheel-keeps-turning-infinity` | after "Infinity" | Ill. 1 - Infinity: worlds within worlds, without first or last scale. | Integrated |
| `wheel-keeps-turning-lens-synthesis` | after "The Asymmetric Synthesis" | Ill. 2 - The lens: traditions gathered into one asymmetric synthesis. | Integrated |
| `wheel-keeps-turning-four-levels` | after "The Four Levels" | Ill. 3 - The four levels: self, humanity, creators, and the Infinite held together. | Integrated |
| `wheel-keeps-turning-future-cycle` | after "The Wheel Keeps Turning" | Ill. 4 - The next turn: humanity prepares to join the cycle of creators. | Integrated |

#### The Wheel Keeps Turning Prompts

`wheel-keeps-turning-infinity`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: fractal cosmology and infinity, worlds within worlds and scales without top or bottom. Scene/backdrop: very wide lavender-indigo cosmic landscape where a human hand silhouette, a spiral galaxy, an atom-like structure, and tiny planetary systems echo each other recursively in mist and starlight. Subject: infinite self-similar scale, not a scientific diagram. Palette: lavender, deep indigo, silver, clear white, cyan highlights, black space, faint warm gold. Composition: very wide 2:1 landscape, no equations, no labels, no readable text, no literal infographic, no oversized religious symbol. Style: restrained cosmic matte painting, low to medium detail, contemplative and immense.

`wheel-keeps-turning-lens-synthesis`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: the Raelian lens and asymmetric synthesis of traditions after the twelve-age sweep. Scene/backdrop: wide lavender-silver observatory archive where Hebrew scrolls, Persian firelight, Greek columns, Indian river lamps, desert manuscripts, and modern scientific instruments are arranged as distant illuminated stations around a subtle circular path. Subject: many traditions gathered into an ordered but non-flat synthesis. Palette: lavender, silver, deep indigo, warm gold lamps, muted green, clear white instrument light. Composition: very wide 2:1 landscape, no readable writing, no flags, no giant symbols, no close religious icons, no text. Style: restrained scholarly-cosmic matte painting, low to medium detail.

`wheel-keeps-turning-four-levels`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: the four levels of meaning: the individual self, human society, the Elohim creators, and the Infinite. Scene/backdrop: wide lavender twilight landscape built as four nested horizons: a lone small figure near water, a distant city of humanity, a higher luminous creator terrace above the clouds, and a vast starfield beyond. Subject: four scales held together without one canceling the others. Palette: lavender, deep indigo, silver, clear white, cyan water, warm gold city lights, black sky. Composition: very wide 2:1 landscape, nested but natural, no diagram rings, no labels, no readable text, no close portrait. Style: restrained symbolic matte painting, contemplative, low to medium detail.

`wheel-keeps-turning-future-cycle`

> Use case: stylized-concept. Asset type: timeline framing chapter moodscape. Primary request: the wheel continuing beyond Aquarius, with humanity preparing to create life on other worlds. Scene/backdrop: wide lavender-gold future horizon with Earth behind, interstellar craft departing, a distant young planet with oceans below, and faint precessional arcs in the sky suggesting the next Great Year. Subject: humanity taking its place in the creator-created cycle, forward into the next turn. Palette: lavender, warm gold, deep indigo, silver craft light, cyan atmosphere, muted green distant world, star white. Composition: very wide 2:1 landscape, no flags, no logos, no readable markings, no triumphalist poster style, no text. Style: restrained hopeful matte painting, low to medium detail, open-ended.

## Pipeline Checklist

For each accepted image:

1. Save selected PNG to `data-images/raw/{slug}.png`.
2. Add a manifest entry with `category: "timeline"`, `quality: 85`, and
   `grain_intensity: 0.05`.
3. Run `python scripts/process_images.py --config manifest.yaml --verbose`.
4. Copy the generated `.avif`, `.webp`, `_thumb.avif`, and `_thumb.webp` files
   to `assets.wheelofheaven.world/images/timeline/`.
5. Insert a `{{ figure(...) }}` shortcode in the canonical English timeline
   chapter with `src`, `alt`, and `caption`.
6. Update the `www.wheelofheaven.world/content` submodule checkout and the
   website superproject pointer.
7. Run `zola build` from `www.wheelofheaven.world`.
