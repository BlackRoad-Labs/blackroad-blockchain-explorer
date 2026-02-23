#!/usr/bin/env python3
"""BlackRoad Blockchain Explorer — lightweight Bitcoin block explorer."""
import json, urllib.request, datetime

BTC_API = "https://blockstream.info/api"

def get_latest_block() -> dict:
    with urllib.request.urlopen(f"{BTC_API}/blocks/tip/height", timeout=10) as r:
        height = int(r.read())
    with urllib.request.urlopen(f"{BTC_API}/blocks/{height}", timeout=10) as r:
        blocks = json.loads(r.read())
    return blocks[0] if blocks else {}

def get_block(hash_or_height) -> dict:
    url = f"{BTC_API}/block/{hash_or_height}"
    with urllib.request.urlopen(url, timeout=10) as r:
        return json.loads(r.read())

def format_block(b: dict) -> str:
    ts = datetime.datetime.fromtimestamp(b.get("timestamp",0)).strftime("%Y-%m-%d %H:%M UTC")
    return (f"  Block #{b.get(\"height\",\"?\")}\\n"
            f"  Hash:  {b.get(\"id\",\"?\")[:32]}...\\n"
            f"  Time:  {ts}\\n"
            f"  Txs:   {b.get(\"tx_count\",0)}\\n"
            f"  Size:  {b.get(\"size\",0)/1024:.1f} KB\\n"
            f"  Fee:   {b.get(\"extras\",{}).get(\"medianFee\",\"?\")} sat/vB\\n")

if __name__ == "__main__":
    import sys
    print("\\n₿ BlackRoad Bitcoin Explorer\\n")
    if len(sys.argv) > 1:
        print(format_block(get_block(sys.argv[1])))
    else:
        print(format_block(get_latest_block()))

