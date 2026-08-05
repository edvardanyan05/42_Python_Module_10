#!/usr/bin/env python3

def artifact_sorter(
    artifacts: list[dict[str, str | int]]
) -> list[dict[str, str | int]]:
    return sorted(artifacts, key=lambda a: int(a["power"]), reverse=True)


def power_filter(
    mages: list[dict[str, str | int]],
    min_power: int
) -> list[dict[str, str | int]]:
    return list(filter(lambda m: int(m["power"]) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(
    mages: list[dict[str, str | int]]
) -> dict[str, int | float]:
    powers: list[int] = list(map(lambda m: int(m["power"]), mages))

    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


if __name__ == "__main__":
    artifacts: list[dict[str, str | int]] = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
    ]

    spells: list[str] = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) "
        f"comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("Testing spell transformer...")
    print(*spell_transformer(spells))
