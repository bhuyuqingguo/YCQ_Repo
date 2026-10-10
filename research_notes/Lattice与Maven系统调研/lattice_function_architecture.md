# Anduril Lattice: Functional Design and Technical Architecture (as of Oct 2026)

> Method note (方法说明): WebFetch and direct HTTP access to anduril.com, developer.anduril.com, docs.anduril.com, breakingdefense.com, blog.anduril.com and theaviationist.com failed in this environment (DNS / proxy 403). Only GitHub raw content was directly readable. So:
> - The **SDK / API / data-schema** findings below are **primary-source facts**, read directly from Anduril's official public Python SDK repo (`github.com/anduril/lattice-sdk-python`, auto-generated from the Lattice OpenAPI spec). These are the most reliable items in these notes.
> - Program, product and operational findings come from **search-engine snippets** of trade press and Anduril releases. The full articles were not read, so treat the exact wording and dates with some caution.
> - Labels used: **[FACT]** = confirmed by a primary or official document, or by independent reporting of a contract or event. **[CLAIM]** = Anduril marketing or company statement. **[INFERENCE]** = my own analysis. **[3RD-PARTY]** = blog, aggregator or review site of weak reliability.

---

## Q1. Functional modules (entity model, sensor fusion/tracks, COP, tasking & autonomy, kill chain, objects, alerts, geofences, sim)

### Takeaway
Lattice is built around one **entity-centric common operating picture (COP)**. Every track, asset, geo-shape (geofence/zone) and signal of interest is an "Entity" made of optional, typed **components**. Three API families sit on top of the COP: **Entities** (publish/stream/override), **Tasks** (a military-style tasking lifecycle between operators and "taskable agents"), and **Objects** (blob/file store that syncs across the mesh). The public schema directly encodes military concepts: disposition, MIL-STD-style symbology, Link 16-style "strength", track quality 0–15, classification markings, and simulated/exercise flags.

### Cited Findings

**Entity data model (实体数据模型), primary source: official SDK**
- The Entity object "represents a single known object within the Lattice operational environment", and all of its data is held in components. — [lattice-sdk-python types/entity.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/entity.py)
- Top-level Entity fields and components (verbatim names): `entity_id, description, is_live, created_time, expiry_time, no_expiry, status, location, location_uncertainty, kinematics, geo_shape, geo_details, aliases, tracked, correlation, mil_view, ontology, sensors, payloads, power_state, provenance, overrides, indicators, target_priority, signal, transponder_codes, data_classification, task_catalog, media, relationships, visual_details, dimensions, route_details, schedules, health, group_details, supplies, orbit, symbology`. — [entity.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/entity.py)
  - `location` vs `kinematics`: the docs say to populate one or the other, not both. `kinematics` is "preferred for Track Entities". — same source
  - `expiry_time` is required when publishing. It "must be in the future, but less than 30 days from the current time". `is_live` must be true when publishing. — same source
  - `orbit` ("Orbit information for space objects") and `signal` ("signal of interest") show that the model covers the space and EW/SIGINT domains. — same source
- **Ontology templates** (the type of entity, which sets the minimum required components): `TEMPLATE_TRACK, TEMPLATE_SENSOR_POINT_OF_INTEREST, TEMPLATE_ASSET, TEMPLATE_GEO, TEMPLATE_SIGNAL_OF_INTEREST`. Ontology also carries `platform_type` and `specific_type`. — [ontology.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/ontology.py), [ontology_template.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/ontology_template.py)
  - So the five core object classes are track, sensor point of interest, asset (own-force platform), geo (geofence/zone/shape) and signal of interest. In the public model, geofences are entities with `geo_shape`/`geo_details`. — [INFERENCE] from the same files
- **MilView disposition** (identification/affiliation): `UNKNOWN, FRIENDLY, HOSTILE, SUSPICIOUS, ASSUMED_FRIENDLY, NEUTRAL, PENDING`. MilView also has `environment` and `nationality`. — [mil_view_disposition.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/mil_view_disposition.py), [mil_view.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/mil_view.py)
- **Tracked component**: `track_quality_wrapper` ("Quality score, 0-15"), `sensor_hits`, and `number_of_objects` ("Known as Strength in certain contexts (Link16)"). It also has `radar_cross_section`. — [tracked.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/tracked.py)
- **Correlation component** (track fusion / multi-sensor correlation): entities can form an N-to-1 correlation set with one `primary` and several `secondary` members. An explicit `decorrelation` records when "a user in the UI decides that two tracks are not actually the same despite an automatic correlator having correlated them… preventing the correlator from re-correlating them". This confirms there is an **automatic correlator** with human override. — [correlation.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/correlation.py)
- **Indicators**: `simulated, exercise, emergency, c2, egressable` ("the Entity should be egressed to external sources… e.g. if an Entity needs fuzzing") and `starred`. — [indicators.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/indicators.py)
- **Health component**: `connection_status, health_status, components[] (ComponentHealth), update_time, active_alerts`. Alerts are therefore modelled at least partly as entity health alerts. — [health.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/health.py)
- **Data classification** per entity: a `default` classification plus per-field overrides in `fields[]`, which "always precedence over the default". Levels: `UNCLASSIFIED, CONTROLLED_UNCLASSIFIED, CONFIDENTIAL, SECRET, TOP_SECRET`, plus `caveats` (example: "TOPSECRET//NOFORN//FISA" becomes level 5 with caveats [NOFORN, FISA]). — [classification.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/classification.py), [classification_information.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/classification_information.py), [classification_information_level.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/classification_information_level.py)
- **Ownership and override semantics**: entities published through the API are "owned" by the originator, and "other sources, such as the UI, may not edit or delete these entities". Updates are applied only if `provenance.sourceUpdateTime` is newer. Operators can still **override** fields marked overridable (example field path `mil_view.disposition`). Overrides are eventually consistent and last-writer-wins. — [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)
- **Entity event types**: `CREATED, UPDATE, DELETED, PREEXISTING, POST_EXPIRY_OVERRIDE`. — [entity_event_event_type.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/entity_event_event_type.py)
- The COP is explicitly described in the API: StreamEntities "enables clients to maintain a real-time view of the common operational picture (COP)". — [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)

**Tasking (任务分配), primary source: official SDK**
- Task lifecycle statuses: `CREATED, SCHEDULED_IN_MANAGER, SENT, MACHINE_RECEIPT, ACK, WILCO, EXECUTING, WAITING_FOR_UPDATE, DONE_OK, DONE_NOT_OK, REPLACED, CANCEL_REQUESTED, COMPLETE_REQUESTED, VERSION_REJECTED`. "WILCO" is military radio "will comply". — [task_status_status.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/task_status_status.py)
- A Task has `specification` (a `google.protobuf.Any` holding a protobuf task definition), `author` (Principal), `relations` (parent task, assignee), `initial_entities` (e.g. "an entity Objective, an entity Keep In Zone"), `retry_strategy`, `delivery_constraints`, `execution_constraints` and `is_executed_elsewhere`. — [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)
- TaskStatus carries `progress`, `result` and `estimate` (protobuf Any from the "tasks/v*/progress|result|estimates" folders) and `allocation` ("allocated agents of the task"). — [task_status.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/task_status.py)
- Status updates use optimistic concurrency through `status_version`. Terminal states DONE_OK and DONE_NOT_OK are permanent. On cancel, if the task is already with an agent, "the agent is then responsible for deciding whether cancellation is possible", and it can reject with `ERROR_CODE_REJECTED`. — [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)
- Assets advertise what they can do through the entity `task_catalog` component (`task_definitions[]`). — [task_catalog.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/task_catalog.py)
- **Manual control**: `stream_manual_control_frames` streams "joystick movements" for a manual-control task to the executing agent, with epoch and sequence metadata to handle concurrent control sessions and stale frames. — [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)

**Objects store and video, primary source: official SDK**
- Objects API: list/get/upload/delete/metadata by path. Objects can be up to 1 GiB. Objects have `expiry_time`. `all_objects_in_mesh=true` "Lists objects across all environment nodes in a Lattice Mesh", otherwise only the local node is listed. `last_updated_at` "records when an object arrived on the node that holds it". GET supports RFC 9218 priority headers and compression. — [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md); see also [developer.anduril.com Objects overview](https://developer.anduril.com/guides/objects/overview) (search result, page not read)
- Video API (newer): ingress streams over RTSP pull, SRT push or MPEG-TS push. Egress re-publishes over RTSP/SRT. "MPEG-TS ingress is supported only at the edge, in closed networks", and it may be disabled when Lattice runs "in a cloud environment reached over the public internet". — [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)

**Lattice for Mission Autonomy (LMA)**
- [CLAIM] LMA is a "hardware-agnostic, end-to-end software platform" for teams of heterogeneous robotic assets. It shifts "from many operators of one autonomous system to one operator of many". It covers risk and threat modeling, operational analysis, training and exercises, pre-mission planning, C2 and post-mission debrief. — [Anduril blog: Anduril Unveils Lattice for Mission Autonomy (2023)](https://blog.anduril.com/anduril-unveils-lattice-for-mission-autonomy-8e0c5fa0e94b); [Defense One, May 2023](https://defenseone.com/business/2023/05/new-software-aims-allow-fewer-troops-manage-more-drones/385905)
- [FACT/CLAIM] At Army EDGE23 a single soldier did pre-mission planning and controlled multiple UAS. The soldier designated a SAM site "hostile" and authorized an ALTIUS-600M strike, and Lattice then **automatically re-tasked an ALTIUS ISR asset for battle damage assessment**. — [Anduril blog, EDGE23](https://blog.anduril.com/anduril-demonstrates-lattice-for-mission-autonomy-controlling-teams-of-autonomous-assets-at-us-f617c489441)
- [FACT] USSOCOM selected Anduril as its Mission Autonomy Systems Integration Partner. — [Monch](https://monch.com/?p=368148)

**C-UAS kill chain (detect-track-identify-defeat)**
- [FACT] Army selected Lattice as the fire-control and C2 platform for **IBCS-Maneuver (IBCS-M)** counter-UAS (announced 10 Nov 2025). Lattice handles sensor fusion and automated fire control "from detection to defeat". In a 7-day Yuma Proving Ground trial it integrated a previously undisclosed sensor and effector within hours and intercepted 4/4 targets in live fire. Contract value and duration were not disclosed. — [DefenseScoop 2025-11-11](https://defensescoop.com/2025/11/11/army-ibcs-maneuver-anduril-lattice-counter-uas/); [Janes](https://www.janes.com/osint-insights/defence-news/c4isr/us-army-anduril-reach-deal-on-ibcs-maneuver-programme); [ExecutiveBiz](https://www.executivebiz.com/articles/army-anduril-lattice-ibcs-m-program); [Stars and Stripes](https://www.stripes.com/branches/army/2025-11-14/new-software-command-and-control-19763782.html)
- [FACT] At Falcon Peak 25.2 (Eglin AFB, Oct 2025), a Lattice-based kit combined Mobile Sentry for autonomous detection and tracking, Wisp and Pulsar sensors, and Anvil for kinetic defeat. Mobile Sentry detected and tracked a hostile drone, and Anvil defeated it. The kit was delivered to USNORTHCOM. — [Inside Unmanned Systems](https://insideunmannedsystems.com/anduril-demonstrates-and-delivers-counter-uas-capabilities-to-usnorthcom/); [The Defense Post](https://www.thedefensepost.com/2025/10/20/anduril-demos-cuas-falcon-peak/)
- [FACT] USMC PM GBAD: Anvil tracks autonomously but **intercepts only on a human operator's command**, using sensor track data, and is controllable through the Lattice interface. — [Marines.mil PAE](https://www.pae.marines.mil/Media/Article/Article/4484189/pm-gbad-successfully-demonstrates-kinetic-interceptor-capability/)
- [FACT] In 2022 USSOCOM awarded Anduril a counter-UAS contract of up to $1B (Lattice-based C-UAS integration). — [Air Recognition](https://airrecognition.com/index.php/news/defense-aviation-news/2022-news-aviation-aerospace/january/8118-us-special-ops-command-awards-anduril-industries-a-1b-counter-drone-contract.html)

**Fires / NGC2 (division-level C2)**
- [FACT] Army awarded Anduril a $99.6M, 11-month OTA to lead the NGC2 prototype for the 4th Infantry Division. The NGC2 program office was set up in April 2025. — [Tectonic](https://www.tectonicdefense.com/icymi-anduril-wins-99-6m-ngc2-award/); [Raksha Anirveda](https://raksha-anirveda.com/anduril-wins-us-armys-100-million-deal-to-build-next-gen-c2-prototype)
- [FACT] In "Ivy Sting 1", a division-level targeting process ran "entirely on Anduril's Lattice Mesh and Palantir's Target Workbench" from HQ down to the gun line. — [Soldier Systems, 2025-10-02](https://soldiersystems.net/2025/10/02/how-anduril-and-the-army-are-rewriting-fire-missions-with-ngc2/)
- [3RD-PARTY/CLAIM] A later iteration, Ivy Sting 5, reportedly reached more than 50 application scenarios and kept working when satellite and commercial communications failed. — [Militär Aktuell](https://militaeraktuell.at/en/anduril-is-advancing-networked-combat-operations/)

### Inferences
- [INFERENCE] The public schema shows that Lattice's "track management" is built on track entities (kinematics + tracked + correlation) plus an automatic correlator that operators can override. That matches a classic multi-sensor track-fusion design (local tracks correlated into a primary system track). The Lattice AI Core on each device appears to produce local tracks, and the correlator merges them in the COP.
- [INFERENCE] The task lifecycle (SENT → MACHINE_RECEIPT → ACK → WILCO → EXECUTING) copies tactical-datalink and voice C2 acknowledgement semantics. That makes it easier to bridge to Link 16 or JREAP-style tasking and to show human-readable task state.
- [INFERENCE] Kill-chain approval is implemented as tasks. A strike or intercept is a task sent to an effector agent. Disposition changes (e.g. to HOSTILE) are overrides with provenance, which gives an audit trail of who designated what.

### Gaps
- The full contents of developer.anduril.com (alert/geofence-specific APIs, the protobuf task definitions in "tasks/v*" such as VisualId, Investigate, Strike, and the exact list of overridable fields) could not be read. The task specification catalogue (e.g. `anduril.tasks.v2.*`) is not in the Python types.
- No public detail was found on Lattice's simulation or test tools. There is an `indicators.simulated` flag but no source on a simulator product.
- Roadrunner's integration with Lattice was not found in the sources searched.

---

## Q2. Architecture: edge-first/distributed design, Lattice Mesh, deployment, security/classification

### Takeaway
Lattice is deployed as a federation of **nodes** (edge kits, towers, vehicles, cloud or on-prem) joined by **Lattice Mesh**, a peer-to-peer data mesh. The mesh prioritizes live data over backfill and is designed to keep working when links are denied, degraded, intermittent or limited (DDIL). The SDK's Objects API explicitly exposes per-node versus mesh-wide views, which confirms a node-local store that replicates across the mesh. Menace-T/X (built on Klas Voyager hardware) are Anduril's own edge-compute nodes.

### Cited Findings
- [FACT] In Dec 2024 CDAO awarded a 3-year, $100M production OTA to scale an Edge Data Mesh built on Lattice Mesh. The mesh was already "operational across multiple services and combatant commands". — [DefenseScoop 2024-12-03](https://defensescoop.com/2024/12/03/anduril-awarded-100m-deal-cdao-scale-edge-data-mesh-capabilities-ota/); [Anduril news](https://www.anduril.com/news/cdao-awards-anduril-production-agreement-to-deliver-edge-data-mesh); [Breaking Defense](https://breakingdefense.com/2024/12/decentralizing-battle-data-cdao-anduril-open-tactical-mesh-to-third-party-developers)
- [CLAIM] The mesh distributes data across platforms, domains and partners "by prioritising data paths". It is "a decentralized network that already connects thousands of defense systems worldwide — specifically and uniquely built to provide secure, P2P data sharing in degraded environments." — [Anduril on X, Dec 2024](https://x.com/anduriltech/status/1866526178116342016); [Unmanned Airspace](https://www.unmannedairspace.info/counter-uas-systems-and-policies/dod-cdao-awards-production-agreement-to-anduril-to-deliver-edge-data-mesh/)
- [FACT, patent] The Anduril "Lattice Mesh" patent (US 10,506,436 and pub. US 2020/0068404) says "live data is the priority of the system and backfill is operated using the left over bandwidth", and that the network prioritizes real-time data despite variable link performance. It describes secure routing using point-to-point authorizations, and keys held in memory rather than permanent storage on regular nodes. — [USPTO report 10506436](https://uspto.report/patent/grant/10506436); [FreePatentsOnline 20200068404](https://www.freepatentsonline.com/y2020/0068404.html)
- [3RD-PARTY] A blog claims a gossip protocol keeps an asset database on every node and that the network self-heals. This is unverified. — [Phil's Blog](https://philescandon.rbind.io/lattice_os_architecture_guide/)
- [FACT, SDK] Objects can be listed per node or with `all_objects_in_mesh`. `last_updated_at` is the time "a copy" arrived at a node, which confirms store-and-forward replication between nodes. RFC 9218 priority headers let clients set delivery priority. — [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)
- [FACT, SDK] Long-poll sessions end if a client "falls behind more than 3x the total number of entities in the environment". The SSE stream "automatically recovers from temporary disconnections, resuming the stream where it left off", and supports `components_to_include` and a filter `Statement` to save bandwidth. The filter mirrors "the gRPC StreamEntityComponents endpoint". — [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)
- [FACT, SDK] Video API distinguishes edge deployments (closed networks, MPEG-TS allowed) from cloud deployments reached over the public internet. Both edge and cloud environments are therefore supported. — [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)
- [FACT] Menace-T (May 2025) is a 2-case C4 kit that one operator can set up in minutes. It is built on Voyager hardware from Klas (acquired by Anduril), runs Lattice Mesh, can host third-party edge-AI stacks, and is already used on ground vehicles and vessels. Menace-X is the expeditionary, on-the-move version. — [TechCrunch 2025-05-05](https://techcrunch.com/2025/05/05/anduril-is-working-on-the-difficult-ai-related-task-of-real-time-edge-computing/); [Everything RF](https://www.everythingrf.com/news/details/20142-anduril-introduces-compact-field-deployable-c4-system-designed-for-tactical-mission-applications); [Defence Connect](https://www.defenceconnect.com.au/land/16047-andurils-menace-systems-preferred-hardware-partner-for-palantirs-edge-software)
- [FACT] Menace systems are the preferred hardware for Palantir Edge software, paired with Lattice Mesh networking. — [Defence Connect](https://www.defenceconnect.com.au/land/16047-andurils-menace-systems-preferred-hardware-partner-for-palantirs-edge-software)
- [CLAIM] "Each Anduril product houses a Lattice AI Core that performs sensor fusion, target classification and multi-track reconciliation at the edge." — quoted in [Air Recognition 2022](https://airrecognition.com/index.php/news/defense-aviation-news/2022-news-aviation-aerospace/january/8118-us-special-ops-command-awards-anduril-industries-a-1b-counter-drone-contract.html)
- [FACT] Anduril UK demonstrated the edge data mesh for the British Army (Project Asgard), moving data from the frontline to HQ. — [Defence Industry EU](https://defence-industry.eu/anduril-uk-demonstrates-edge-data-mesh-capability-for-british-army-on-project-asgard/)
- [FACT, SDK] Security: OAuth2 client-credentials flow (`oauth.get_token`, short-lived tokens). Field-level classification markings sit on each entity (see Q1). — [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)

### Inferences
- [INFERENCE] The architecture looks like this: each node runs a local Lattice stack (entity store, task manager, object store, video service, local correlator and AI). Lattice Mesh replicates entities and objects peer to peer with priority-aware routing. Clients (UI, SDK apps) connect to their local node. That would explain why APIs are scoped to an "environment" and default to "local objects only".
- [INFERENCE] Field-level classification markings suggest the data model is ready for multi-level and cross-domain filtering when egressing data, together with the `egressable` indicator. No public source describes Lattice's accredited cross-domain solution (CDS) handling.

### Gaps
- No public, detailed protocol description of Lattice Mesh (transport, sync/CRDT model, conflict resolution beyond last-writer-wins overrides). Only the patent and marketing material are available.
- ATO/accreditation levels (IL5/IL6, SIPR/JWICS) and cross-domain solutions for Lattice were not found.
- The exact runtime stack (OS, Kubernetes or not, language) is not publicly documented.

---

## Q3. Lattice SDK / developer platform

### Takeaway
The Lattice SDK was publicly launched on 10 Dec 2024 together with a Partner Program. v1 was gRPC-native. v2 (2025) is OpenAPI/REST with SSE streaming, and Fern-generated client SDKs exist in Python, Go, Java and TypeScript. Its public surface has five API groups: **Entities, Tasks, Objects, OAuth and Video**.

### Cited Findings
- [FACT] Python package `anduril-lattice-sdk`, client `from anduril import Lattice`, authenticating with client_id/client_secret. It has an async client, retries, timeouts, pagination and streaming. — [README](https://github.com/anduril/lattice-sdk-python); the Fern-generated mirror is [fern-api/lattice-sdk-python](https://github.com/fern-api/lattice-sdk-python)
- [FACT] Full method list (v2):
  - Entities: `publish_entity, get_entity, override_entity, remove_entity_override, long_poll_entity_events, stream_entities (SSE)`.
  - Tasks: `create_task, get_task, update_task_status, cancel_task, query_tasks, stream_tasks, listen_as_agent, stream_as_agent, stream_manual_control_frames`.
  - Objects: `list_objects, get_object, upload_object, delete_object, get_object_metadata`.
  - OAuth: `get_token`.
  - Video: `list/create/get/delete` for both ingress and egress streams.
  - Source: [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)
- [FACT] Integration patterns:
  - A **producer** (sensor or C2 adapter) calls PublishEntity with track/asset entities.
  - A **consumer** (UI or analytics) calls StreamEntities, which first sends PREEXISTING events and then CREATE, UPDATE and DELETE. Heartbeats default to 30s.
  - A **taskable agent** (robot or effector) publishes its asset entity with a `task_catalog`, then calls StreamAsAgent or ListenAsAgent with an EntityIdsSelector. It receives ExecuteRequest, CancelRequest and CompleteRequest, and reports progress through UpdateTaskStatus.
  - Source: [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md)
- [FACT] Docs say v1 natively supports gRPC and v2 uses OpenAPI. Anduril recommends upgrading to v2. The v2 SDKs added StreamEntities with examples in Go, Java, Python and TypeScript. A Java SDK page exists. — [developer.anduril.com changelog](https://developer.anduril.com/changelog); [changelog 2025-07-24](https://developer.anduril.com/changelog/2025/7/24); [docs.anduril.com/sdks/java](https://docs.anduril.com/sdks/java); [Watch entities guide](https://developer.anduril.com/guides/entities/watch); [Publish entities](https://docs.anduril.com/entity/publish) (search-result snippets, pages not read)
- [FACT] On 10 Dec 2024 the SDK was released with "data model definitions, API bindings, code samples and reference implementations". The Partner Program launched with 10+ partners: Apex, Forterra, Impulse Space, Numerica, Oracle, Saronic, Scale AI, Spire Global, Striveworks, Textron Systems and Valinor. — [OCBJ](https://www.ocbj.com/defense-2/anduril-industries-enabling-partners-to-operate-on-lattice/); [Breaking Defense](https://breakingdefense.com/2024/12/decentralizing-battle-data-cdao-anduril-open-tactical-mesh-to-third-party-developers)
- [FACT] In CENTCOM's Desert Guardian 1.0, Lattice served as a third-party C2 system. Warfighters used the API and SDK docs to integrate their own systems, some in real time. — [OCBJ](https://www.ocbj.com/defense-2/anduril-industries-enabling-partners-to-operate-on-lattice/)
- [3RD-PARTY] Anduril job postings for "Senior Software Engineer, Lattice SDK" and "Developer Experience Engineer" mention partners "ranging from innovative startups to defense giants and military organizations worldwide". — [General Catalyst jobs](https://jobs.generalcatalyst.com/companies/anduril/jobs/54592249-senior-software-engineer-lattice-sdk)

### Inferences
- [INFERENCE] The v2 REST/SSE surface is clearly generated from the same protobuf definitions as the gRPC v1 API: `google.protobuf.Any` task specs, enum prefixes such as `STATUS_` and `TEMPLATE_`, and the note that the REST filter "mirrors" a gRPC endpoint. Internally, Lattice is very likely protobuf/gRPC-native.

### Gaps
- Could not confirm the sandbox environment details: access model, simulated assets, and whether a free developer sandbox exists. Search results did not mention one directly.
- Pricing and licensing of the SDK were not found.

---

## Q4. Integrated sensors and effectors (Anduril and third-party)

### Takeaway
Publicly confirmed Lattice-controlled or Lattice-fused systems include Sentry towers (fixed, mobile, extended-range), Wisp, Pulsar, Anvil, ALTIUS-600/600M, Ghost-X, the YFQ-44A Fury, partner radars and effectors under IBCS-M, and partner platforms such as Hermeus Quarterhorse. Maritime (Ghost Shark, Dive-LD), Barracuda and Roadrunner links were **not confirmed** in the sources reviewed.

### Cited Findings
- [FACT] Sentry tower: radar plus EO/IR plus RF sensors. It detects and tracks objects and passes data to C2 nodes. — [Defense News 2020](https://www.defensenews.com/digital-show-dailies/ausa/2020/10/16/anduril-adapts-tech-to-detect-cruise-missiles-in-air-force-demo/); [C4ISRNet, Mobile Sentry 2022](https://www.c4isrnet.com/industry/2022/10/10/anduril-debuts-wheeled-version-of-sentry-surveillance-tower); [ExecutiveBiz, Extended Range Sentry 2024](https://executivebiz.com/2024/05/anduril-debuts-latest-autonomous-surveillance-tower-system/)
- [FACT] CBP uses Sentry towers. A CBP official said they track objects and activity, not individuals, and do not do facial recognition. — [FedScoop](https://www.fedscoop.com/anduril-sentry-towers-cbp/)
- [FACT] Falcon Peak C-UAS kit: Mobile Sentry, Wisp, Pulsar and Anvil on Lattice. — [Inside Unmanned Systems](https://insideunmannedsystems.com/anduril-demonstrates-and-delivers-counter-uas-capabilities-to-usnorthcom/)
- [FACT] A proposed Kuwait FMS sale includes several Sentry tower variants tied together by Lattice. — [Defence Matters](https://defencematters.eu/?p=6065)
- [FACT] ALTIUS-600 (ISR) and ALTIUS-600M (strike) are tasked through LMA (EDGE23). — [Anduril blog](https://blog.anduril.com/anduril-demonstrates-lattice-for-mission-autonomy-controlling-teams-of-autonomous-assets-at-us-f617c489441)
- [FACT] YFQ-44A Fury: flew with both Shield AI Hivemind and Anduril LMA on a single flight, switching between autonomy stacks through an early A-GRA implementation. — [The Aviationist 2026-03-03](https://theaviationist.com/2026/03/03/yfq-44a-tests-shivemind-lattice-ais/)
- [FACT/CONFLICTING] The Air Force selected Anduril Lattice mission autonomy software for the next CCA program phase. One source dates related production and autonomy decisions to June 2026. Another describes 6-month autonomy CLINs for Anduril, Shield AI and Collins with a later down-select. The dates and sequence in these sources are inconsistent with each other. — [Defence Industry EU](https://defence-industry.eu/u-s-air-force-selects-anduril-lattice-mission-autonomy-software-for-next-collaborative-combat-aircraft-program-phase/); [Simple Flying](https://simpleflying.com/software-deal-put-anduril-inside-every-cca-air-force-buys/); [TWZ, Fury with F-35s](https://www.twz.com/air/andurils-yfq-44a-fury-cca-has-flown-alongside-f-35s)
- [FACT] Anduril delivered the first CCA to the USAF, and USAF operators now fly Fury themselves. — [Anduril on X](https://x.com/anduriltech/status/2103277104980996308)
- [FACT/CLAIM] Hermeus selected Lattice for Quarterhorse Mk 2. One source calls this the first large-scale integration of Anduril autonomy onto a third-party aircraft. — [andurilnews.com tracker](https://www.andurilnews.com/products/lattice/) [3RD-PARTY aggregator]
- [FACT] IBCS-M: Lattice integrates third-party sensors and effectors. A previously undisclosed sensor and effector were integrated "within hours" at Yuma. — [DefenseScoop](https://defensescoop.com/2025/11/11/army-ibcs-maneuver-anduril-lattice-counter-uas/)
- [CLAIM] Ghost-X C2 runs on Lattice, per Anduril's website as cited in search results. — [Cyberwarzone](https://cyberwarzone.com/2025/11/11/u-s-army-selects-andurils-ai-platform-for-advanced-counter-drone-capabilities/)

### Inferences
- [INFERENCE] The SDK's `sensors`, `payloads`, `signal`, `orbit` and `supplies` components, together with the partners Impulse Space and Spire (space) and Saronic (USV), show the model is meant for all domains. Undersea assets would likely appear as asset entities with `task_catalog` entries.

### Gaps
- No sources were found on how Lattice integrates Ghost Shark, Dive-LD, Barracuda, Roadrunner or Pulsar beyond appearing in kits. These need targeted searches on anduril.com product pages, which were unreachable here.

---

## Q5. AI/ML role and human-machine teaming / engagement approval

### Takeaway
AI runs at the edge (the "Lattice AI Core") for detection, classification and multi-track reconciliation. In every documented use, the decision to engage stays with a human. Operators confirm the track and disposition and authorize the strike. Autonomy then executes and can automatically re-task assets (e.g. for BDA). Public sources do not explain how Lattice meets DoDD 3000.09 requirements.

### Cited Findings
- [CLAIM] Lattice is "an AI backbone that uses computer vision, machine learning and mesh networking to fuse real-time data into a single, autonomous operating picture". Anduril claims the AI recognizes threats more accurately than human operators. No independent test data was found. — [Air Recognition](https://airrecognition.com/index.php/news/defense-aviation-news/2022-news-aviation-aerospace/january/8118-us-special-ops-command-awards-anduril-industries-a-1b-counter-drone-contract.html); [PopSci](https://www.popsci.com/technology/sentry-camera-border-security-texas/)
- [FACT] In the 2020 AFRL/ABMS cruise-missile demo, the operator confirmed that Lattice was tracking the intended target and then issued the engagement command to an effector. — [Defense News 2020](https://www.defensenews.com/digital-show-dailies/ausa/2020/10/16/anduril-adapts-tech-to-detect-cruise-missiles-in-air-force-demo/)
- [FACT] Anvil intercepts only on a human operator's command. — [Marines.mil](https://www.pae.marines.mil/Media/Article/Article/4484189/pm-gbad-successfully-demonstrates-kinetic-interceptor-capability/)
- [FACT] EDGE23: the human designated the target hostile and authorized the strike. Software automatically re-tasked ISR for BDA. — [Anduril blog](https://blog.anduril.com/anduril-demonstrates-lattice-for-mission-autonomy-controlling-teams-of-autonomous-assets-at-us-f617c489441)
- [CLAIM] Defense One (2023): LMA lets robots accomplish more while "still having a human overseeing the missions", and tells the monitor whether pop-up aircraft are hostile. — [Defense One](https://defenseone.com/business/2023/05/new-software-aims-allow-fewer-troops-manage-more-drones/385905)
- [OPINION] Free Press criticizes Lattice as "built to act faster than human judgment" and says Anduril's materials do not explain accountability for autonomous lethal decisions. — [Free Press](https://freepress.org/article/anduril-s-lattice-now-army-s-drone-killing-brain-and-it-s-built-act-faster-human-judgment)
- [FACT, SDK] Human-in-the-loop hooks in the API:
  - Disposition overrides with provenance.
  - User decorrelation that the automatic correlator must respect.
  - Task `author` (Principal) on create, cancel and status changes.
  - Agents may reject a task (`ERROR_CODE_REJECTED`).
  - Manual joystick control tasks.
  - Source: [reference.md](https://github.com/anduril/lattice-sdk-python/blob/HEAD/reference.md); [correlation.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/correlation.py)

### Inferences
- [INFERENCE] The engagement flow appears to be:
  1. Edge AI detects and classifies, then publishes a track entity.
  2. The correlator fuses tracks.
  3. An operator or rule sets the disposition (e.g. HOSTILE), with an override and provenance logged.
  4. The operator creates or approves a strike/intercept task to an effector agent.
  5. The agent goes ACK → WILCO → EXECUTING → DONE.
  6. Autonomy auto-tasks BDA.
  This would be "human-on-the-loop" for movement and sensing, and "human-in-the-loop" for weapons release.

### Gaps
- No public model cards, CV architectures, training data or accuracy metrics were found.
- No public documentation of rules-of-engagement (ROE) configuration or automatic-engage modes (e.g. for C-UAS against Group 1 drones) was found.

---

## Q6. Relation to C2 standards (OMS/UCI, MOSA, A-GRA, TAK, Link 16)

### Takeaway
Only **A-GRA** compliance is clearly documented (Fury and CCA). Link 16 concepts appear in the data model (track "Strength", WILCO-style statuses), and a third-party source lists Link 16 among Menace's communication links. No reliable public source was found for OMS/UCI conformance or a Lattice-ATAK plugin, although Anduril employs ATAK engineers.

### Cited Findings
- [CLAIM/FACT] Anduril says LMA is fully A-GRA compliant. Fury switched between Hivemind and Lattice autonomy in flight through an early A-GRA implementation on both stacks. — [The Aviationist](https://theaviationist.com/2026/03/03/yfq-44a-tests-shivemind-lattice-ais/)
- [FACT, SDK] The Tracked component explicitly references Link 16 "Strength". The entity has `transponder_codes` (IFF/Mode codes) and a `symbology` component "respecting an existing standard". — [tracked.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/tracked.py); [entity.py](https://github.com/anduril/lattice-sdk-python/blob/HEAD/src/anduril/types/entity.py)
- [3RD-PARTY] Menace C4 hardware runs Lattice over multiple communication paths, including Link 16. — [Phil's Blog](https://philescandon.rbind.io/lattice_os_architecture_guide/)
- [FACT] Anduril is hiring "Sr. ATAK Engineer" roles (EW team) to build UIs and APIs for real-time telemetry. This shows ATAK work but not a documented Lattice-TAK bridge. — [Built In job posting](https://builtin.com/job/sr-atak-engineer/7073600)
- [CLAIM] IBCS-M is framed as an open architecture linking sensors, effectors and decision centers, and Lattice is its mobile fire-control layer. — [UAS Magazine](https://uasmagazine.com/articles/anduril-selected-for-us-armys-integrated-battle-command-system-maneuver-program); [Army Recognition](https://www.armyrecognition.com/news/army-news/2025/us-army-picks-anduril-lattice-for-integrated-battle-command-system-maneuver-counter-drone-role)
- [CLAIM] Anduril publicly argues for "interoperability at the edge" and open APIs. — [Anduril: The Contours of War are Changing](https://www.anduril.com/news/the-contours-of-war-are-changing-we-must-prepare-for-interoperability-at-the-edge)

### Inferences
- [INFERENCE] MOSA alignment is mainly through open, published APIs and the SDK, plus A-GRA on aircraft. The `egressable` indicator ("Integrations choose how the egressing happens") points to an adapter or "integration" layer that translates entities to external formats such as CoT/TAK, Link 16/JREAP and IBCS. That is consistent with Lattice ingesting third-party C2 in Desert Guardian.

### Gaps
- No reliable source on OMS/UCI message support in Lattice.
- No confirmed public TAK/CoT bridge product. Link 16 support has only third-party or indirect evidence.
- How Lattice interfaces with the IBCS (Northrop) core for Patriot/LTAMDS was not detailed. Stars and Stripes headlines it as shortening reaction times for Patriot crews, but the article body was not read: [Stripes](https://www.stripes.com/branches/army/2025-11-14/new-software-command-and-control-19763782.html).
