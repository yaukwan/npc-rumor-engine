PRAGMA journal_mode=WAL;

CREATE TABLE IF NOT EXISTS npcs (
    npc_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    faction TEXT NOT NULL,
    price_multiplier REAL DEFAULT 1.0
);

CREATE TABLE IF NOT EXISTS relationships (
    source_npc_id TEXT NOT NULL,
    target_npc_id TEXT NOT NULL,
    trust_weight REAL NOT NULL,
    decay_rate REAL DEFAULT 0.15,
    PRIMARY KEY (source_npc_id, target_npc_id)
);

CREATE TABLE IF NOT EXISTS rumor_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin_npc_id TEXT NOT NULL,
    rumor_type TEXT NOT NULL,
    credibility_score REAL DEFAULT 1.0,
    ttl_hops INTEGER DEFAULT 3,
    processed INTEGER DEFAULT 0
);
