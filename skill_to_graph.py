import sqlite3
from pathlib import Path

def init_db(db_path: str = "rumor_world.db") -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    schema = Path(__file__).with_name("schema.sql").read_text(encoding="utf-8")
    conn.executescript(schema)
    return conn

def seed_sample_world(conn: sqlite3.Connection) -> None:
    conn.executemany(
        "INSERT OR REPLACE INTO npcs VALUES (?, ?, ?, ?)",
        [
            ("dock_merchant", "Dockyard Merchant", "HarborGuild", 1.0),
            ("guard_captain", "Harbor Guard", "CityWatch", 1.0),
            ("weapon_dealer", "Uptown Weapon Dealer", "MerchantGuild", 1.0),
            ("forest_hermit", "Forest Hermit", "Outcasts", 1.0),
        ],
    )
    conn.executemany(
        "INSERT OR REPLACE INTO relationships VALUES (?, ?, ?, ?)",
        [
            ("dock_merchant", "guard_captain", 0.85, 0.1),
            ("guard_captain", "weapon_dealer", 0.75, 0.15),
        ],
    )
    conn.commit()

if __name__ == "__main__":
    db = init_db()
    seed_sample_world(db)
    print("Seeded SQLite rumor graph successfully.")
