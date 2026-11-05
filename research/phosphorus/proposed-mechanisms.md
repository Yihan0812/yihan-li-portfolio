# Notebook-derived mechanism inventory and reconstruction limits

## Rules

These are notebook hypotheses, not established elementary mechanisms or validated computed structures. The new figures preserve notebook labels by prefixing the source page, e.g. `p4-a`; labels from separate pages are not assumed to identify the same intermediate. The previous I1/N1/A2/B2/A3/B3 network is retained only as a **previously generated conceptual model** in supplementary files.

The notebook has no consistent phosphorus atom numbering. Local vertex indices in the structure audit are editorial bookkeeping only. A global P1–P4 mapping is deliberately not imposed through crowded/reprojected drawings. Selected P–P edges can be highlighted within a readable precursor, while exact atom transfer is flagged where uncertain.

## Activation alternatives

- **K-S (pp. 1–2, 8–9):** K[N(SiMe3)2] + PhSSPh → PhS–N(SiMe3)2 + K+PhS−, proposed. The N–S species is notebook-reported/GC–MS-assigned but not independently established.
- **E-S (p. 6):** Et3N + PhSSPh → [Et3N–SPh]+ + PhS−, candidate formal ion pair.
- **K-P / “route 1” (pp. 1–2):** amide-anion attack at a thiolated P–P compound → P–N product + phosphorus anion. This is the route associated with the unverified energy sketch.
- **E-P (p. 6):** direct Et3N cleavage/adduct hypothesis at (PhS)2P–P(SPh)2.
- **Direct base–P4 (p. 7):** Et3N or OH− attack; precise adduct connectivity is not recoverable. No unique adduct structure is invented.
- **OH-S (p. 7):** OH− + disulfide → proposed PhS–OH + thiolate.

## P4 framework network

| Notebook relation | Readable precursor/product | Bond-change reading | What remains unresolved |
|---|---|---|---|
| pp. 2–4 initial transfer | Tetrahedral P4 → proposed P4–SPh cation | New P–S bond; electrophilic sulfur transfer from PhS–N(SiMe3)2; HMDS anion departure proposed | Existence and geometry; crossed-out N–S-retaining alternative is ambiguous |
| p. 4 boxed endpoint | Sulfur-functionalised P4 + thiolate → two-SPh opened P4 | One P–P cleavage and another P–S formation | Exact historical atom mapping not recorded |
| p. 4 `(1)` → `a` | Opened P4 → triangle-plus-pendant P4, four SPh | Further S transfer/capture and one fewer P–P edge at topology level | Several intermediate charge drawings crowded; not silently normalised |
| p. 4 `(2)` → `b` | Opened P4 → four-membered P4 ring, four SPh | Different site/cleavage possibility | Ring is reprojected; no reliable global atom map |
| p. 4 `a` → circled `(1)` | P(SPh)3 + thiolated P3 ring | Candidate P1 release from P4 framework | Intermediate ion-pair sequence not experimentally established |
| p. 4 `a` → circled `(2)` / `(3)` | Additional open/branched P4 sketches | Further alternative bond rearrangement/cleavage | Some internal edges and charges ambiguous; shown as unresolved branches, not new structures |
| p. 5 `b` → circled `(2)` | More open, multiply thiolated P4 motif | Ring-opening candidate | Clear open-chain representative is an interpreted motif, not a unique recovered atom map |
| pp. 3–5 later-stage motifs | Thiolated P3 ring ↔ more open P3 structures | Alternative sulfur-transfer/thiolate-mediated openings | Crossed-out arrows and alternative charges preserved in notes |
| pp. 5–6 P2/P1 possibilities | Thiolated P3/P2 candidates → P(SPh)3 | Fragmentation toward smaller P units | No isolated P3/P2 intermediate is established |

## Chemical drawing policy

The figures draw only readable, formally consistent motif endpoints. Ion-pair species are shown with charges/counterions where recoverable. Curved-arrow details that are crowded, crossed out or electronically ambiguous are not reconstructed by guesswork. Missing detail is signposted at the corresponding branch. A neutral tricoordinate P drawing can satisfy formal valence without being a real minimum; neither fact is conflated with experimental detection.

The later-stage figure uses candidate motif relationships supported across pp. 3–6, not a claim that all of those steps form one complete, uniquely ordered cycle. It explicitly leaves unresolvable open/branched alternatives unassigned.

## Machine-readable network

`mechanism-network.json` records each readable precursor/product relation, notebook reference, bond-change interpretation and uncertainty. It includes the unresolved circled (2)/(3) branches rather than replacing them with extra structures. `notebook-connectivity.json` and the CML files contain local motif connectivity only.
