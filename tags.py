def normalize_tags(tags):
    """Return normalized tags.

    Each tag is stripped of surrounding whitespace and lowercased. Tags that
    are empty after stripping are omitted. Duplicates (after normalization)
    are removed, preserving the order of first occurrence.
    """
    result = []
    seen = set()
    for tag in tags:
        normalized = tag.strip().lower()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        result.append(normalized)
    return result
