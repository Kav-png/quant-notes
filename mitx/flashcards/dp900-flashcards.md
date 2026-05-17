---
tags: [azure, dp900, flashcards]
exam: DP-900
format: obsidian-sr
---

# DP-900 Flashcards

> Format: `Q::A` (Obsidian Spaced Repetition plugin)

---

## Domain 1 — Core Data Concepts

What are the three types of data by structure?::Structured (fixed schema, relational tables), Semi-structured (JSON/XML, flexible schema), Unstructured (no schema: images, video, audio)

What is the difference between OLTP and OLAP?::OLTP = high-volume short transactions, row-store, normalised schema. OLAP = complex analytical queries, column-store, denormalised (star/snowflake schema).

What file format is preferred for analytical queries in Azure Data Lake?::Parquet — columnar, compressed, fast for analytics.

What is "schema-on-read" vs "schema-on-write"?::Schema-on-read = apply schema at query time (unstructured/semi-structured). Schema-on-write = enforce schema at insert time (relational databases).

What is the role of a Data Engineer vs Data Analyst?::Data Engineer builds pipelines (ETL/ELT), moves/transforms data. Data Analyst queries data and creates reports/dashboards.
<!--SR:!2026-04-26,1,230-->

What are the three Avro / Parquet / ORC file formats best suited for?::Avro = row-based binary, streaming/Kafka. Parquet = columnar, analytics (preferred in Azure). ORC = columnar, Hive/Hadoop.

What is a fact table in a star schema?::Central table containing measurable numeric events (sales, revenue, quantity). Surrounded by dimension tables.

What is the Lambda architecture?::Big data pattern with three layers: batch layer (historical), speed layer (real-time streaming), serving layer (merged results).

Name two Azure services for batch processing and two for streaming::Batch: Azure Data Factory, Synapse Pipelines. Streaming: Azure Stream Analytics, Azure Event Hubs.

---

## Domain 2 — Relational Data

What is a Primary Key?::A column (or set of columns) that uniquely identifies each row in a table; cannot be NULL.
<!--SR:!2026-04-30,4,270-->

What is a Foreign Key?::A column that references the Primary Key of another table; enforces referential integrity.

What SQL clause filters aggregated results?::HAVING (filters after GROUP BY). WHERE filters before aggregation.

What does INNER JOIN return?::Only rows that have matching values in both tables.

What does LEFT JOIN return?::All rows from the left table plus matching rows from the right; NULLs where no match exists on the right.

What is the difference between Azure SQL Database and Azure SQL Managed Instance?::SQL Database = PaaS, cloud-native, missing some SQL Server features (SQL Agent, linked servers). SQL Managed Instance = PaaS, near-100% SQL Server compatibility, VNet-native; use for lift-and-shift.
<!--SR:!2026-04-23,1,230-->

What is the difference between DTU and vCore pricing in Azure SQL?::DTU = bundled CPU+memory+I/O (simpler). vCore = choose cores and memory independently (flexible, required for Hyperscale).
<!--SR:!2026-04-23,1,230-->

What SQL Server features does Azure SQL Database NOT support?::SQL Server Agent, CLR assemblies, linked servers, cross-database queries — use SQL Managed Instance instead.

What is 3NF (Third Normal Form)?::A table is in 3NF if it's in 2NF AND there are no transitive dependencies (non-key column depends on another non-key column).

What is an elastic pool in Azure SQL?::Multiple databases that share a common pool of resources (DTUs or vCores), reducing cost for databases with variable/unpredictable workloads.

---

## Domain 3 — Non-Relational Data

What are the four NoSQL data models?::Key-Value, Document, Column-family, Graph.

Which Cosmos DB API would you use for a social network with friend relationships?::Gremlin API (graph model).

Which Cosmos DB API would you use to migrate a MongoDB application?::Cosmos DB MongoDB API.

What is the default Cosmos DB consistency level?::Session consistency — consistent within a single client session.

What Cosmos DB consistency level guarantees the latest write is always returned?::Strong consistency (but cannot be used with multi-region writes).

What are the three Azure Blob types and their use cases?::Block blob (large files, most common), Append blob (log files, append-only), Page blob (VM disks, random read/write).

What is the Azure Blob access tier with the lowest storage cost?::Archive — but requires rehydration (hours of latency) before access.

What is the key difference between Azure Blob Storage and ADLS Gen2?::ADLS Gen2 adds a hierarchical namespace (true directories, O(1) rename), POSIX ACLs at file/folder level, and is optimised for big data analytics engines.

What does PartitionKey determine in Azure Table Storage?::The physical partition where the entity is stored; queries filtering on PartitionKey are fast, cross-partition scans are slow.

What is a Request Unit (RU) in Cosmos DB?::The currency for Cosmos DB throughput. 1 RU ≈ cost to read a 1 KB item by key. Writes and complex queries cost more RU/s.

---

## Domain 4 — Analytics

What is the difference between a Dedicated SQL Pool and a Serverless SQL Pool in Synapse?::Dedicated = provisioned MPP data warehouse, pay for DWU. Serverless = query ADLS files on-demand with T-SQL, pay per TB scanned.

What are the three distribution types for Dedicated SQL Pool tables?::Hash (large fact tables), Round-robin (staging tables), Replicated (small dimension tables).

What is Azure Data Factory's primary purpose?::Orchestrating ETL/ELT pipelines — it moves and triggers data processing but does not process data itself.

What Integration Runtime type does ADF need to connect to on-premises data sources?::Self-Hosted Integration Runtime (installed on a machine inside the on-prem network or private VNet).

What is a Tumbling Window in Stream Analytics?::A fixed-size, non-overlapping time window — each event belongs to exactly one window.

What is the difference between a Tumbling Window and a Hopping Window?::Tumbling = non-overlapping (no event counted twice). Hopping = overlapping windows (events can appear in multiple windows).

What is Azure Databricks best suited for?::Large-scale Spark processing, ML model training, Delta Lake ELT pipelines — more powerful than ADF for complex data transformations.

What is Delta Lake?::An open-source storage layer that adds ACID transactions and time-travel (data versioning) to Parquet files, used in Databricks and Synapse Spark.

When would you use Azure HDInsight instead of Databricks?::When lifting and shifting existing Hadoop, HBase, Kafka, or Hive/LLAP workloads to Azure.
<!--SR:!2026-04-24,1,230-->

What is Microsoft Purview used for?::Data governance — automated scanning, cataloguing, data lineage, classification of sensitive data, and access policy management.

What is the difference between Azure Event Hubs and Azure IoT Hub?::Event Hubs = general-purpose, high-throughput event streaming (ingest only). IoT Hub = IoT devices; adds bidirectional communication, device registry, device twins.

What is a Power BI Gateway?::A bridge that allows Power BI Service to connect to on-premises or private data sources for live queries or scheduled refresh.

What is the difference between Power BI Import and DirectQuery modes?::Import = data copied into Power BI (fast, scheduled refresh). DirectQuery = queries run against source in real-time (latest data, but slower).

What does Azure Stream Analytics use as its query language?::A SQL-like language with streaming-specific extensions (windowing functions like TumblingWindow, HoppingWindow, SessionWindow).

What Azure service would you use to catalogue data across Azure SQL, ADLS, and on-prem SQL Server?::Microsoft Purview (unified data governance and catalog).
