# Particle-model recovery and specification check


## 2026-10-03: live recovery and source verification

The stored question and mark-scheme PDFs were each only 2 bytes (CRLF), and GitHub displayed Invalid PDF for the question file. The source JSON was intact. Rebuilt the existing 26-group selection from its exact 16 PMT-hosted AQA PDFs, preserving original wording, diagrams and mark schemes as raster crops. No original questions added.

Output: particle-model-questions.pdf (54 pages), particle-model-markscheme.pdf (36 pages), questions-restored.json. There are 26 groups and 182 selected marks. Question pages are longer than the old reported 28 because original answer space and figures are preserved; no claim of reproducing the old page layout. Two front pages describe scope and give a route/index.

### Verified specification mapping

- 4.3.1.1 Density and RP5: 2018 Q10.1, 2019 Q09.3, 2020 Q03.1-2, 2021 Q04, 2022 Q02, 2024 Q07, 2025 Q01.2-3. Includes regular-object calculation and irregular-solid displacement work.
- 4.3.1.2 / 4.3.2.1 State changes/internal energy: 2019 Q11, 2021 Q11, 2023 Q03.4-5; also latent-heat/gas crossovers.
- 4.3.2.2 Specific heat capacity: the eight existing SHC groups, plus 2024 Q08.3 crossover.
- 4.3.2.3 Specific latent heat and heating graphs: 2022 Q08, 2024 Q10.4-5, 2025 Q08; also 2019 Q08.4 and 2021 Q11.
- 4.3.3.1 Gas motion/temperature/pressure: 2020 Q10, 2023 Q09 and other gas groups.
- 4.3.3.2 Physics-only pressure-volume: 2018 Q07.4, 2020 Q10.2, 2021 Q09.3-4, 2024 Q08.1.
- 4.3.3.3 Physics-only, Higher-only work on a gas: explicitly verified in 2018 Q07.5 and MS p18 (work done on enclosed air increases temperature).

This is a restored selection, not an exhaustive spec assessment or proof every relevant subquestion in the papers was inventoried. Not separately isolated: drawing all three particle arrangements; every named change of state; physical reversibility and mass conservation; a full liquid-density method. The front page flags those revision gaps. No 2026 release sweep was completed.

### QA and revisions

All 16 source PDFs were downloaded, opened and parsed. Every source page/row selected by the manifest was located. Full-question MS tables retained; mixed-question crops restricted to selected parts. Source totals can refer to omitted parts; headers explicitly instruct marking only selected parts. 2020 Q07.2 requires Figure 10 on the previous page: included the graph but removed Q07.1, keeping the 5-mark selected scope. Removed empty extra-space area from 2025 Q02 continuation.

Visually inspected contact sheets covering all 52 question screenshot pages and all 34 mark-scheme screenshot pages. Also inspected the final front pages and full-size final pages showing the 2020 kettle graph, the cropped 2025 continuation and the 2023 six-mark level descriptors. Text and diagrams readable, no clipped screenshot boundaries found. Final footer page numbers include the two front pages.

Automated QA: 950 concrete structural/source/range checks, zero failures. These are mechanical checks, not 950 independent expert content reviews. The check results are retained separately.

### Filing and privacy

No repository content or visibility changed in this recovery run. Repository filing is handed back to the parent; no upload completion is claimed. The restored PDF pair, JSON and research notes are ready to file, with the existing audience preserved. Original user scope was private school revision with claimed copy permission; that permission was not independently checked.

# Sources checked 3 October 2026

- AQA particle-model specification: https://www.aqa.org.uk/subjects/physics/gcse/physics-8463/specification/subject-content/particle-model-of-matter
- AQA assessment overview: https://www.aqa.org.uk/subjects/physics/gcse/physics-8463/specification/specification-at-a-glance
- AQA practical handbook: https://filestore.aqa.org.uk/resources/physics/AQA-8463-PRACTICALS-HB.PDF
- AQA specification PDF: https://media.aqa.org.uk/resources/physics/specifications/AQA-8463-SP-2016.PDF
- AQA June 2022 examiner report: https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-84631H-WRE-JUN22.PDF
- PMT Paper 1 collection: https://www.physicsandmathstutor.com/past-papers/gcse-physics/aqa-paper-1/

## Downloaded and parsed primary exam PDFs, PMT mirror

- 2018-QP.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/QP/June%202018%20QP.pdf
- 2018-MS.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/MS/June%202018%20MS.pdf
- 2019-QP.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/QP/June%202019%20QP.pdf
- 2019-MS.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/MS/June%202019%20MS.pdf
- 2020-QP.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/QP/June%202020%20QP.PDF
- 2020-MS.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/MS/June%202020%20MS.PDF
- 2021-QP.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/QP/June%202021%20QP.PDF
- 2021-MS.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/MS/June%202021%20MS.PDF
- 2022-QP.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/QP/June%202022%20QP.PDF
- 2022-MS.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/MS/June%202022%20MS.PDF
- 2024-QP.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/QP/June%202024%20QP.pdf
- 2024-MS.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/MS/June%202024%20MS.pdf
- 2025-QP.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/QP/June%202025%20QP.pdf
- 2025-MS.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/MS/June%202025%20MS.pdf
- 2023-QP.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/QP/June%202023%20QP.pdf
- 2023-MS.pdf: https://pmt.physicsandmathstutor.com/download/Physics/GCSE/Past-Papers/AQA/Paper-1H/MS/June%202023%20MS.pdf
