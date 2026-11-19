from skill_to_graph import init_db, seed_sample_world

def test_graph_seed_structure():
    conn = init_db(":memory:")
    seed_sample_world(conn)
    npc_count = conn.execute("SELECT COUNT(*) FROM npcs").fetchone()[0]
    edge_count = conn.execute("SELECT COUNT(*) FROM relationships").fetchone()[0]
    assert npc_count == 4
    assert edge_count == 2
