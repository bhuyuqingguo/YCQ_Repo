# Lattice vs. Maven Smart System: relationship, integrations, and place in the US/allied C2 modernization landscape (as of 2026-10-10)

> Method note (for the report writer): Direct page fetching (WebFetch/curl) was blocked by the sandbox proxy in this session (DNS/403 errors on breakingdefense.com, defence-blog.com). All findings below come from search-engine result summaries of the cited URLs, not full-text reads. The URLs are real search hits. Treat exact quotes and figures as "per search summary" and spot-check high-stakes numbers before publication. Every fact carries the date of the event and/or the article.

## Q1. Anduril–Palantir partnership (Dec 2024) and the reported "consortium" with OpenAI/SpaceX/Scale/Saronic: members, goals, joint bids

### Takeaway
Two separate December 2024 items get conflated. (1) **Confirmed:** On 2024-12-06 Anduril and Palantir announced a bilateral partnership/"consortium." Lattice + Menace collect and transport edge data, and Palantir AIP prepares it for AI training across classification levels up to SCI/SAP. Coverage also said Lattice/Menace would be combined with Maven Smart System. (2) **Reported only:** On 2024-12-22 the FT/Reuters said Palantir and Anduril were in *talks* with SpaceX, OpenAI, Scale AI and Saronic (L3Harris was not named) about a joint-bidding group to challenge the primes. No finalized membership list was found. Since then the pair has jointly appeared on NGC2 (2025–26) and reportedly Golden Dome C2 software (2026).

### Cited Findings
- 2024-12-06: Anduril and Palantir announced a partnership to "accelerate AI capabilities for national security." It names two obstacles to military AI adoption: data readiness, and the processing/compute needed to deploy AI at scale. — [BusinessWire press release](https://www.businesswire.com/news/home/20241206684306/en/Anduril-and-Palantir-to-Accelerate-AI-Capabilities-for-National-Security); [DefenseScoop 2024-12-06](https://defensescoop.com/2024/12/06/palantir-anduril-consortium-ai-new-alliance-merge-capabilities/)
- Mechanism (2024-12-06): Battlefield data from sensors, vehicles, robots and weapons is collected by **Anduril Lattice** and the **Menace** family of deployable compute/comms. It is pulled into a secure Palantir platform (**AIP**) that prepares it for AI training, including data at the highest classification levels (SCI/SAP). — [BNN Bloomberg 2024-12-06](https://bnnbloomberg.ca/business/technology/2024/12/06/defense-startups-palantir-anduril-to-save-data-from-battlefield-to-train-ai-models); [Intelligence Community News](https://intelligencecommunitynews.com/anduril-and-palantir-announce-partnership/)
- Coverage said executives planned to combine Lattice and Menace with Palantir AIP **and Maven Smart System**, framed as "edge to enterprise." — [DefenseScoop 2024-12-06](https://defensescoop.com/2024/12/06/palantir-anduril-consortium-ai-new-alliance-merge-capabilities/); [Inside Defense](https://insidedefense.com/daily-news/palantir-and-anduril-join-forces-defense-ai)
- The partners said they expected to "expand the partnership to other industry partners." — [Intelligence Community News](https://intelligencecommunitynews.com/anduril-and-palantir-announce-partnership/)
- 2024-12-22 (FT via TechCrunch/Reuters): Palantir and Anduril were **in talks** with **SpaceX, OpenAI, Saronic, Scale AI** to form a consortium to jointly bid for Pentagon work and challenge primes (Lockheed, RTX, Boeing). Members could be announced as early as January 2025. All companies declined or did not immediately comment. — [TechCrunch 2024-12-22](https://techcrunch.com/2024/12/22/palantir-and-anduril-reportedly-building-a-tech-consortium-to-bid-on-defense-contracts/); [Boursorama/Reuters (FR)](https://www.boursorama.com/bourse/actualites-amp/palantir-et-anduril-s-associent-a-des-groupes-technologiques-pour-repondre-aux-appels-d-offres-du-pentagone-selon-le-ft-1f1a0ea036e3bbd4f47127886b49bc5d); [Maginative](https://www.maginative.com/article/palantir-and-anduril-lead-silicon-valley-consortium-to-bid-for-pentagon-contracts/)
- Joint work since then:
  - NGC2 team (2025-07), with Palantir as an Anduril sub (see Q2).
  - NGC2 common data layer as "Lattice + Foundry" (2026-06; see Q2).
  - Golden Dome C2 software (reported 2026-03-24; see Q3).
  - Anduril and OpenAI also have a separate counter-drone partnership (not verified in this session).
  - Sources: [Defense News 2025-07-21](https://www.defensenews.com/land/2025/07/21/anduril-wins-100m-deal-to-build-us-armys-next-gen-c2-ecosystem/); [US News/Reuters 2026-03-24](https://www.usnews.com/news/top-news/articles/2026-03-24/anduril-palantir-developing-golden-dome-missile-shields-software-source-says)

### Inferences
- The "consortium" is better described as a durable Anduril–Palantir teaming pattern than a formal multi-company bidding entity. No evidence was found that OpenAI, SpaceX, Scale or Saronic ever formally joined a named consortium.
- The 2024 design already shows the division of labor that later shows up in NGC2. Anduril owns edge collection and transport (Lattice/Menace). Palantir owns enterprise data preparation, ontology and decision apps (AIP/Foundry/Maven).

### Gaps
- No primary confirmation of a finalized multi-company consortium roster or charter (searched; none found as of 2026-10).
- L3Harris is **not** named in any consortium reporting found. The brief's "L3Harris?" appears to be incorrect.
- No documented formal Lattice↔Maven Smart System API integration announcement was found, beyond the 2024 statement of intent and NGC2 use.

## Q2. Army NGC2: Anduril-led team, how Lattice and Palantir components fit, awards, Ivy Sting results

### Takeaway
NGC2 is the most concrete documented Lattice–Palantir integration. Anduril (prime) won a $99.6M OTA on 2025-07-18 for a 4th ID division prototype. The team was Palantir, Microsoft, Striveworks, Govini, Instant Connect Enterprise and Research Innovations Inc. At Ivy Sting 1 (Sept 2025), **Lattice Mesh** on rugged edge kits was the data backbone, and **Palantir's Target Workbench** managed target tracking and allocation. A Lockheed-led team prototyped a rival data layer for 25th ID ($26M OTA). In June 2026 the Army chose Anduril to lead the NGC2 **common data layer baseline**: an edge-to-cloud data mesh of **Lattice + Palantir Foundry**, with Raft supplying registries/federation. On 2026-10-05/06 Anduril won a 5-year contract worth up to $1.8B ($162.8M base) to field NGC2 starting with I Corps.

### Cited Findings
- **2025-07-18:** The Army (PEO C3N) awarded Anduril a **$99.6M OTA** to prototype NGC2 for the **4th Infantry Division**, with an 11-month timeline. Team: Palantir, Microsoft, Striveworks, Govini, Instant Connect Enterprise, Research Innovations Inc. — [Defense News 2025-07-21](https://www.defensenews.com/land/2025/07/21/anduril-wins-100m-deal-to-build-us-armys-next-gen-c2-ecosystem/); [DefenseScoop 2025-07-21](https://defensescoop.com/2025/07/21/anduril-army-next-generation-command-and-control-award/); [Soldier Systems 2025-07-18](https://soldiersystems.net/2025/07/18/anduril-awarded-99-6m-for-u-s-army-next-generation-command-and-control-prototype/)
- The prototype was described as an integrated hardware/software C2 suite on a common data layer, with compute nodes on multiple mechanized vehicle types. The Army planned further competitions for 25th ID and III Corps. — [Soldier Systems](https://soldiersystems.net/2025/07/18/anduril-awarded-99-6m-for-u-s-army-next-generation-command-and-control-prototype/); [Inside Defense](https://insidedefense.com/node/224724)
- Development runs in incremental "sprints" to scale to division level (2025-08-26). — [DefenseScoop 2025-08-26](https://defensescoop.com/2025/08/26/army-next-gen-c2-sprints-scale-division-level/)
- **Ivy Sting 1 (Sept 2025, live fire):**
  - 4th ID ran a division-level targeting process on **Anduril Lattice Mesh** (running on rugged "Voyager" edge compute kits) and **Palantir Target Workbench (TWB)**. TWB managed, tracked and allocated resources for each target.
  - A beta artillery data tool (AXS) on Lattice Mesh was used in a howitzer strike. Crews were digitally ready in **under 30 seconds**, versus AFATDS crews who often had to troubleshoot connections first.
  - The readiness comparison is an Army/company claim reported by trade press.
  - Sources: [Breaking Defense 2025-10](https://breakingdefense.com/2025/10/in-ngc2-first-army-uses-beta-artillery-data-tool-in-howitzer-strike-at-ivy-sting-1/); [defence-industry.eu](https://defence-industry.eu/anduril-and-u-s-army-showcase-next-gen-command-and-control-with-ngc2-in-live-fire-ivy-sting-1/); [Army.mil](https://www.army.mil/article/288651/its_about_lethal_formations_ivy_division_launches_army_prototype_for_next_gen_command_and_control)
- **Ivy Sting 2 (Oct 2025):** Expanded scope to airspace management/deconfliction before fires, plus headquarters C2. — [Defense One 2025-10](https://www.defenseone.com/technology/2025/10/army-test-next-gen-c2-prototype-second-time-july-contract-award/408895/); [Federal News Network 2025-10](https://federalnewsnetwork.com/federal-insights/2025/10/armys-4th-infantry-division-kicks-off-ivy-sting-exercises-to-scale-ngc2-prototype/)
- Scaling architecture to a full division — [Breaking Defense 2025-10](https://breakingdefense.com/2025/10/heres-how-the-army-is-scaling-its-next-gen-c2-platform-to-an-entire-division/) (full text not retrieved)
- **Security memo (dated 2025-09-05; reported by Reuters ~2025-10-03):**
  - Army CTO Gabriele Chiulli wrote that the prototype must be treated as "**very high risk**" given the likelihood of "persistent undetectable access" by adversaries. He also wrote: "We cannot control who sees what, we cannot see what users are doing, and we cannot verify that the software itself is secure."
  - The memo reportedly found one app with 25 high-severity vulnerabilities and three others with 200+ flaws awaiting review.
  - Anduril called it an "outdated snapshot." Palantir said "No vulnerabilities were found in the Palantir platform." Army CIO Leonel Garciga said the memo was part of triage, and the Army said the critical deficiencies were mitigated.
  - Sources: [Reuters via TradingView](https://de.tradingview.com/news/reuters.com,2025:newsml_L2N3VK0G9:0-anduril-and-palantir-battlefield-communication-system-very-high-risk-us-army-memo-says); [Breaking Defense 2025-10](https://breakingdefense.com/2025/10/army-says-its-mitigated-critical-cybersecurity-deficiencies-in-early-ngc2-prototype/); [Yahoo/Reuters](https://www.yahoo.com/news/articles/anduril-palantir-battlefield-communication-system-115526922.html)
- **Lockheed / 25th ID:**
  - Lockheed-led team won a **$26M, 16-month OTA** (2025) to provide an integrated data layer for 25th ID.
  - First Army test of Lockheed's data layer prototype: Jan 2026.
  - "Lightning Surge 2" sensor-to-shooter demo: around 2026-03. A third iteration (airspace thread) was planned for April 2026.
  - Sources: [Army.mil](https://www.army.mil/article/288233/army_announces_additional_competitive_award_for_next_generation_command_and_control_ngc2_prototyping_efforts); [Tectonic](https://www.tectonicdefense.com/lockheed-wins-26m-ota-for-ngc2/); [Breaking Defense 2026-01](https://breakingdefense.com/2026/01/army-tests-next-gen-c2-data-layer-for-the-first-time/); [Defense Post 2026-03-03](https://thedefensepost.com/2026/03/03/lockheed-ngc2-lightning-surge-2/)
- Special Forces joined NGC2 prototype experiments (May 2026). — [Breaking Defense 2026-05](https://breakingdefense.com/2026/05/going-to-change-everything-special-forces-joins-armys-next-gen-c2-prototype-experiments/)
- **2026-06-22: Army picks Anduril to lead the NGC2 common data layer baseline.** No dollar value was disclosed; it falls under Anduril's Army enterprise agreement.
  - The data mesh is "**Anduril's Lattice and Palantir's Foundry**" (edge-to-cloud).
  - **Raft** provides registries, data transformation tools and federation.
  - Lockheed remains lead for 25th ID's full-stack implementation, built on the "C2 Fix" network baseline. Officials call the efforts complementary.
  - Sources: [Breaking Defense 2026-06](https://breakingdefense.com/2026/06/army-picks-anduril-to-lead-next-gen-c2-common-data-layer-baseline/); [DefenseScoop 2026-06-22](https://defensescoop.com/2026/06/22/army-taps-anduril-lead-ngc2-common-data-layer-baseline/); [Inside Defense](https://insidedefense.com/insider/army-anduril-work-out-common-data-layer-baseline-ngc2)
- **Ivy Mass (spring 2026):** Anduril says NGC2 connected **2,500+ soldier end-user devices**. This is a company claim. — [MeriTalk](https://www.meritalk.com/articles/army-awards-anduril-up-to-1-8b-to-scale-ngc2-across-i-corps/)
- **2026-10-05 (Anduril) / 2026-10-06 (Army/DefenseScoop):** Five-year contract, **ceiling up to $1.8B**, **base $162.8M**, to expand and field the NGC2 common data layer, starting with **I Corps**.
  - The Army aims to extend NGC2 to all 11 divisions.
  - In the Oct 2026 release, Anduril describes Lattice as the "distributed data layer" connecting apps, sensors and AI models.
  - One trade outlet says Lockheed will help implement Anduril's baseline.
  - Sources: [DefenseScoop 2026-10-06](https://defensescoop.com/2026/10/06/army-awards-anduril-1-8b-contract-expand-ngc2/); [Anduril release](https://www.anduril.com/news/anduril-continues-to-scale-next-generation-command-and-control-across-the-army); [ASDNews 2026-10-05](https://www.asdnews.com/news/defense/2026/10/05/anduril-continues-scale-nextgen-command-control-across-army); [defence-industry.eu](https://defence-industry.eu/anduril-wins-u-s-army-contract-worth-up-to-1-8-billion-for-new-battlefield-command-network/)

### Inferences
- In NGC2, Lattice works as the **tactical edge mesh / data transport and entity layer**, and Palantir works as the **enterprise data platform (Foundry) plus targeting and decision apps (Target Workbench)**. This supports the "Lattice = edge, Palantir = fusion/targeting workflow" framing. In NGC2, though, Palantir also sits *at the division echelon*, not only at the operational/strategic level.
- The NGC2 selection process ended with the Anduril baseline (with Palantir) as the Army-wide standard, and Lockheed in an implementing role. That is a strong lock-in point for the Lattice–Foundry pairing.
- The $1.8B NGC2 contract and the $20B Anduril Army enterprise agreement (Q4) are different vehicles. Sources do not clarify exactly how they relate. The June 2026 baseline award was reported as falling under the EA.

### Gaps
- Exact Palantir products in the final baseline beyond Foundry and Target Workbench (for example, whether Maven Smart System itself is in NGC2) are not documented. One aggregator claim was not verified.
- No published quantitative results for Ivy Sting 3+ or Project Convergence Capstone 6 were found.
- Palantir's subcontract value within NGC2 has not been disclosed.

## Q3. Golden Dome, CJADC2 MVC, GIDE, DAF Battle Network/ABMS, NATO: roles of each

### Takeaway
**Maven Smart System is the de facto joint/COCOM C2 and targeting backbone.** It underpinned the CJADC2 minimum viable capability (certified Dec 2023, announced Feb 2024), built through GIDE. It was ordered to become a program of record under CDAO by the end of FY2026, and is being considered for a CJADC2 program office. NATO also bought MSS NATO (March 2025). **Lattice's joint-level role is smaller and more experimental.** It has been demonstrated in ABMS exercises and is the data backbone in DIU's Thunderforge (2025). Both companies are reportedly building the Golden Dome C2 "glue layer" (March 2026, anonymous-source reporting).

### Cited Findings
- **CJADC2 MVC:**
  - Then-DepSecDef Hicks ordered CDAO to deliver an MVC through GIDE by end-2023. It was certified Dec 2023 and announced 2024-02.
  - Focus: information sharing among the 11 COCOMs, with apps including the Joint Fires Network and a "global integration" tool.
  - Sources: [DefenseScoop 2023-12-15](https://defensescoop.com/2023/12/15/dod-jadc2-minimum-viable-product-gide/); [DefenseScoop 2024-02-26](https://defensescoop.com/2024/02/26/dod-cdao-ai-cjadc2-minimum-viable-capability/); [Nextgov 2024-02](https://www.nextgov.com/defense/2024/02/minimum-viable-cjadc2-real-and-ready-dod-official-says/394371/)
- Maven Smart System was described as the de facto backbone of the CJADC2 effort. Its open architecture lets third-party apps plug in, and the Open DAGIR initiative (2024) brings other vendors' apps onto that data layer. Breaking Defense in 2024 called the MVC "minimal." — [Breaking Defense 2024-05](https://breakingdefense.com/2024/05/open-dagir-dod-plans-july-industry-day-experiments-for-new-cjadc2-command-apps/); [Breaking Defense 2024-07 GIDE](https://breakingdefense.com/2024/07/gide-goes-wide-defense-ai-chief-seeks-host-of-industry-players-for-global-battle-network/); [Breaking Defense 2024-12](https://breakingdefense.com/2024/12/killer-apps-5-stories-highlight-quiet-progress-on-military-ai-and-cjadc2/)
- **Maven program status:**
  - 2026-03-09: DepSecDef Feinberg memo sets MSS as a **program of record by end of FY2026**.
  - Oversight moves from NGA to a new **CDAO MSS Program Office** within 30 days.
  - All MSS contracts move to the **Army Enterprise Agreement** vehicle.
  - The CTO (Emil Michael) is to evaluate placing MSS under a potential **CJADC2 Program Office**.
  - The directive calls AI-enabled decision-making "the cornerstone" for CJADC2.
  - Sources: [DefenseScoop 2026-04-03](https://defensescoop.com/2026/04/03/palantir-maven-feinberg-directive/); [DefenseScoop 2026-04-15](https://defensescoop.com/2026/04/15/palantir-maven-smart-system-pentagon-program-transition-feinberg/); [CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do); [GlobalSecurity](https://www.globalsecurity.org/intell/systems/maven.htm)
  - Note: one outlier site dates the memo 2026-03-21; DefenseScoop says 03-09.
- A new MSS program director was appointed 2026-08-05 "in fresh push for C2 integration." — [DefenseScoop 2026-08-05](https://defensescoop.com/2026/08/05/pentagon-appoints-new-maven-smart-system-program-director/)
- **Golden Dome (2026-03-24, Reuters citing a source; WSJ):**
  - Anduril and Palantir are developing the missile shield's software, as part of an industry consortium building a C2 platform that fuses disparate sensor data and lets commanders control weapons. The platform was targeted for testing in summer 2026.
  - Other firms named: Aalyria, Scale AI, Swoop Technologies.
  - Gen. Michael Guetlein called C2 "our secret sauce," a "glue layer" across radars, sensors and batteries.
  - Anduril was also among firms awarded small Golden Dome prototype contracts in Nov 2025.
  - Cost estimates vary: $175B (White House), $185B (widely reported), $831B (CBO), $3.6T (AEI).
  - Sources: [US News/Reuters 2026-03-24](https://www.usnews.com/news/top-news/articles/2026-03-24/anduril-palantir-developing-golden-dome-missile-shields-software-source-says); [GovConWire](https://www.govconwire.com/articles/anduril-palantir-golden-dome-software-wash100)
- **DAF ABMS / Battle Network:**
  - SAIC received a $112M contract as the ABMS cloud-based C2 (CBC2) software integrator.
  - Lattice was demonstrated in an ABMS exercise linking F-16s, NASAMS, MQ-9s and Army howitzers. The source's date was not established (likely the 2020–21 ABMS on-ramps).
  - Sources: [RAF Mildenhall/af.mil](https://www.mildenhall.af.mil/News/Article-Display/Article/3262645/abms-moves-forward-on-cloud-based-c2/); [Lodi411 (secondary)](https://lodi411.com/lodi-eye/anduril-and-palantir-ai-enabled-transformation-of-us-defense)
- **Thunderforge (2025-03-05):**
  - DIU picked Scale AI to lead AI-assisted operational/campaign planning for INDOPACOM and EUCOM.
  - It combines **Anduril Lattice** (data-sharing) with LLMs from Microsoft and Scale, using agentic workflows "always under human oversight."
  - Sources: [DefenseScoop 2025-03-05](https://defensescoop.com/2025/03/05/diu-thunderforge-scale-ai-combatant-commands-indopacom-eucom/); [DIU](https://www.diu.mil/latest/dius-thunderforge-project-to-integrate-commercial-ai-powered-decision-making); [Scale blog](https://scale.com/blog/thunderforge-ai-for-american-defense)
- **NATO:** NATO acquired **MSS NATO** (via NCIA, for Allied Command Operations) in a procurement concluded March 2025, reported as taking about 6 months. Value was not disclosed. These are secondary sources. — [Wikipedia: Project Maven](https://en.wikipedia.org/wiki/Project_Maven); [Escudo Digital](https://www.escudodigital.com/en/defense/europe/foreign-software-europes-war-how-maven-and-palantir-are-already-making-decisions-for-europe.html)

### Inferences
- Layering as of 2026:
  - **Maven** = joint/COCOM and coalition (NATO) C2 and targeting enterprise system. It is now a CDAO program of record and the likely core of a CJADC2 program office.
  - **Lattice** = tactical/division edge mesh (Army NGC2), autonomy/C2 for Anduril and third-party effectors, and the data layer in planning experiments (Thunderforge).
  - Golden Dome is the first reported joint-level program where the two are co-developing the core C2 layer.
- The DAF picture is less clear. The search found no current (2025–26) DAF Battle Network/DAF Battle Network PEO award to either company.

### Gaps
- No primary source on specific DAF Battle Network (PEO C3BM) awards to Anduril or Palantir in 2025–26.
- Golden Dome: no contract values or confirmed summer-2026 test results were found.
- NATO MSS: no contract value or user count. No primary NATO NCIA release was retrieved.
- Lattice's role in GIDE iterations has not been documented.

## Q4. Side-by-side comparison (origin, owner, kill-chain layer, data model, deployment, AI, autonomy, business model, scale)

### Takeaway
Maven Smart System is a government-owned *program* (Project Maven, 2017; now CDAO) whose primary software is Palantir's commercial platform. It is enterprise, intelligence-to-targeting and COCOM-scale, with over 100k users as of Sept 2026. Lattice is Anduril's own product (company founded 2017): an edge mesh, entity and autonomy OS built to drive sensors and effectors. Both are now sold through massive Army enterprise agreements: Palantir up to $10B (2025-07-31) and Anduril up to $20B (early 2026).

### Cited Findings
- **Maven scale and use:**
  - Users: about 20,000+ in 2025 (per NGA Director Whitworth), ~50,000 in Jan 2026, and **100,000+** by Sept 2026 after "Operation Epic Fury" (Iran).
  - CDAO's Cameron Stanley said Maven supported strikes on **13,000 targets over 38 days**.
  - Sources: [DefenseScoop 2026-09-22](https://defensescoop.com/2026/09/22/maven-smart-system-ai-james-mazol-cameron-stanley-defensetalks/); [Defense Post 2026-09-25](https://thedefensepost.com/2026/09/25/pentagon-maven-ai-expansion/); [DefenseScoop 2025-05-23](https://defensescoop.com/2025/05/23/dod-palantir-maven-smart-system-contract-increase/)
- **Maven contract values:**
  - $480M IDIQ (May 2024).
  - Ceiling raised by $795M to about **$1.3B through 2029** (2025-05-23), citing "growing demand" from COCOMs.
  - FY2027 budget request of **>$1.5B** to expand MSS access.
  - Sources: [DefenseScoop 2025-05-23](https://defensescoop.com/2025/05/23/dod-palantir-maven-smart-system-contract-increase/); [Inside Defense](https://insidedefense.com/insider/pentagon-surges-palantir-maven-smart-system-contract-spending-more-1b); [DefenseScoop 2026-04-15](https://defensescoop.com/2026/04/15/palantir-maven-smart-system-pentagon-program-transition-feinberg/)
- **Palantir Army EA:** 2025-07-31, consolidates 75 contracts. 10-year term, **ceiling up to $10B**. The ceiling is not an obligation. — [DefenseScoop 2025-07-31](https://defensescoop.com/2025/07/31/army-palantir-software-enterprise-agreement-10-billion/); [Washington Technology 2025-08](https://www.washingtontechnology.com/contracts/2025/08/palantir-signs-10b-enterprise-agreement-army/407153/); [Army.mil](https://www.army.mil/article/287506/u_s_army_awards_enterprise_service_agreement_to_enhance_military_readiness_and_drive_operational_efficiency)
- **Anduril Army EA:** About March 2026. 10-year (5-year base + 5-year option), **ceiling up to $20B**. Covers software plus hardware and services, with Lattice at its core. — [GovConWire](https://www.govconwire.com/articles/anduril-20b-army-enterprise-it-contract-award); [Overt Defense 2026-03-24](https://www.overtdefense.com/2026/03/24/u-s-army-awards-anduril-20-billion-ai-battlefield-tech-contract/)
- **Lattice role:**
  - Lattice + Menace = edge data capture and deployable compute (2024-12-06). — [BNN Bloomberg](https://bnnbloomberg.ca/business/technology/2024/12/06/defense-startups-palantir-anduril-to-save-data-from-battlefield-to-train-ai-models)
  - Lattice = NGC2 "distributed data layer" (2026-10). — [ASDNews](https://www.asdnews.com/news/defense/2026/10/05/anduril-continues-scale-nextgen-command-control-across-army)
  - Lattice Mesh ran on Voyager edge kits in Ivy Sting (2025-09). — [Breaking Defense](https://breakingdefense.com/2025/10/in-ngc2-first-army-uses-beta-artillery-data-tool-in-howitzer-strike-at-ivy-sting-1/)
- **Autonomy:** Lattice is Anduril's common autonomy layer across its own systems (for example, the Fury CCA). Shield AI Hivemind was selected (Feb 2026) for USAF CCA flight demos on Anduril's Fury airframe, which suggests government interest in autonomy-stack interchangeability. These are secondary sources. — [robotics.press](https://www.robotics.press/news/shield-ai-hivemind-cca-fury-airframe/); [tech-insider (FR)](https://tech-insider.org/fr/shield-ai-serie-g-12-milliards-defense-autonome-ia-militaire-2026/)

Comparison table (built from the findings above; cells with no citation above are marked as unverified background):

| Dimension | Maven Smart System (Palantir) | Lattice (Anduril) |
|---|---|---|
| Origin | Project Maven / AWCFT 2017 (DoD). Palantir MSS as primary platform. NGA took about 80% of lines in 2023. CDAO PoR ordered in 2026 ([GlobalSecurity](https://www.globalsecurity.org/intell/systems/maven.htm)) | Anduril proprietary OS (company founded 2017; background, unverified this session) |
| Owner / customer | DoD program (CDAO MSS PO), COCOMs, services, NATO ACO | Anduril product. Army (NGC2, EA), DIU Thunderforge, USAF CCA ecosystem |
| Kill-chain layer | Find/fix/target/assess at COCOM to division level. Target nomination, workflows, COP | Sense/track/transport at the edge. Sensor-to-shooter, tasking of autonomous assets |
| Data model | Palantir Foundry **ontology** (objects/links/actions; vendor documentation, not fetched) | Lattice **entities** (tracked objects with components such as location, mil_view, provenance, ontology; per Lattice SDK schema, not fetched) |
| Deployment | Enterprise/cloud across 3 security domains (per Whitworth 2025) | Edge mesh on rugged kits/vehicles (Voyager, Menace); DDIL |
| AI role | CV detection, target recommendation, LLM/agentic assist (Minab case shows recommendation role) | Sensor fusion, track correlation, autonomy behaviors; data for AI training |
| Business model | IDIQ ($1.3B ceiling) + Army EA ($10B); FY27 >$1.5B request | Army EA ($20B ceiling, HW+SW+services); NGC2 $1.8B ceiling |
| Users / scale | 100k+ users (Sep 2026) | 2,500+ devices in Ivy Mass (company claim); fielding to I Corps, plan for 11 divisions |

### Inferences
- The brief's framing ("Maven = operational/strategic intelligence fusion and targeting; Lattice = tactical-edge sensor-to-shooter/autonomy") is **broadly supported, with a caveat**. In NGC2, Palantir tools (Foundry, Target Workbench) also run at division level. In Thunderforge and Golden Dome, Lattice plays at theater and joint levels. The cleaner split is *enterprise data/decision platform* (Palantir) vs. *edge mesh/effector control* (Anduril).
- Commercially, both firms have moved from program contracts to enterprise licensing agreements with ceilings far above current obligations. That raises lock-in and competition questions (Q5).

### Gaps
- No authoritative primary comparison of the Lattice entity model vs. the Palantir ontology. Documented interoperability between the two (for example, entity↔object mapping in NGC2) was not found in public sources.
- Revenue attributable to Lattice vs. Maven is not publicly broken out.

## Q5. Critiques and competitors

### Takeaway
The most serious documented critiques are:
- **NGC2 cybersecurity**: the Army CTO's "very high risk" memo of 2025-09-05.
- **AI targeting harms**: a Pentagon review reportedly found overreliance on Maven contributed to the 2026-02-28 Minab, Iran school strike. 120+ House Democrats wrote to Secretary Hegseth on 2026-03-12.
- **Concentration/lock-in**: enterprise agreements worth $10B and $20B, and Army-wide standardization on one data layer.

Competitors include Lockheed (25th ID NGC2), Scale AI (Thunderforge lead, which uses Lattice), Shield AI Hivemind (autonomy), SAIC (ABMS CBC2), and Raft (now a partner).

### Cited Findings
- **Minab strike (2026-02-28):**
  - Pentagon investigators (unpublished review, per Bloomberg) concluded overreliance on MSS contributed. The school site was in outdated records as an IRGC facility, and Maven returned it as a recommended day-one target.
  - CENTCOM civilian-harm staff had been cut from 10 to 1.
  - Palantir says it "is not responsible for the underlying data." It has since added re-review of underlying intelligence for disqualifying factors.
  - Casualty counts vary (123+ children; 150–170+ total).
  - Sources: [Bloomberg 2026](https://www.bloomberg.com/graphics/2026-iran-school-attack/); [Gizmodo](https://gizmodo.com/pentagon-investigators-say-overreliance-on-palantir-ai-tech-contributed-to-u-s-strike-that-killed-123-iranian-children-2000814477); [Responsible Statecraft](https://responsiblestatecraft.org/ai-palantir-weapons/)
- **Congressional oversight:** On 2026-03-12, 120+ House Democrats wrote to Hegseth on AI/Maven's role in Minab. The Pentagon cited the ongoing investigation. — [Gizmodo](https://gizmodo.com/pentagon-investigators-say-overreliance-on-palantir-ai-tech-contributed-to-u-s-strike-that-killed-123-iranian-children-2000814477); [AOL "Lawmakers send stern warning to Palantir"](https://www.aol.com/finance/lawmakers-send-stern-warning-palantir-223700109.html) (content not verified)
- **NGC2 cyber:** "Very high risk" memo, 2025-09-05 (see Q2). — [Breaking Defense](https://breakingdefense.com/2025/10/army-says-its-mitigated-critical-cybersecurity-deficiencies-in-early-ngc2-prototype/)
- **Lock-in framing:** The Army itself names avoiding vendor lock and leaving room for sensors and upgrades as critical considerations for the common data layer (2026-06). — [Breaking Defense 2026-06](https://breakingdefense.com/2026/06/army-picks-anduril-to-lead-next-gen-c2-common-data-layer-baseline/)
- **Allied sovereignty critique:** European commentary argues MSS NATO means foreign (US) software is shaping European decisions. — [Escudo Digital](https://www.escudodigital.com/en/defense/europe/foreign-software-europes-war-how-maven-and-palantir-are-already-making-decisions-for-europe.html)
- **Activist critique:** "Silicon Valley's plan to conquer the world with AI weapons." — [Project Censored](https://www.projectcensored.org/silicon-valley-military-ai-weapons/)
- **Competitors:**
  - Lockheed-led NGC2 team, 25th ID ($26M OTA). — [Tectonic](https://www.tectonicdefense.com/lockheed-wins-26m-ota-for-ngc2/)
  - Scale AI Thunderforge. — [DefenseScoop](https://defensescoop.com/2025/03/05/diu-thunderforge-scale-ai-combatant-commands-indopacom-eucom/)
  - Shield AI Hivemind. — [robotics.press](https://www.robotics.press/news/shield-ai-hivemind-cca-fury-airframe/)
  - SAIC ABMS CBC2. — [af.mil](https://www.mildenhall.af.mil/News/Article-Display/Article/3262645/abms-moves-forward-on-cloud-based-c2/)
  - Golden Dome co-participants Aalyria, Scale AI, Swoop. — [US News/Reuters](https://www.usnews.com/news/top-news/articles/2026-03-24/anduril-palantir-developing-golden-dome-missile-shields-software-source-says)

### Inferences
- The Minab case is the most concrete public example of the "automation bias" critique of AI targeting. It involves Maven (enterprise targeting), not Lattice.
- Critiques of Lattice center on cybersecurity, autonomy and lock-in. No equivalent documented harm incident was found.
- Raft moved from a competitor-type data-layer vendor to an NGC2 partner (2026-06). Lockheed moved from rival prototype lead to implementer (2026-10, single trade source). Together these suggest the Army is consolidating around the Anduril/Palantir baseline.

### Gaps
- No GAO report, NDAA provision, or congressional hearing specifically on NGC2 or Maven data rights/lock-in was found in this session.
- No 2025–26 analytical reports from CSIS/CNAS/RAND/War on the Rocks comparing Lattice and Maven were found. Only the CSIS explainer "What Is Maven Smart System" was located ([CSIS](https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do)).
- Chinese/Russian counterparts were not covered in this session's searches.
- Reports of an Anthropic Claude dependency inside Maven (hinted at by a low-quality aggregator) are unverified and were excluded.
- The L3Harris and Silvus (mesh radios) roles relative to Lattice were not researched.
