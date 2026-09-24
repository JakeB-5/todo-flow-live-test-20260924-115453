def join_labels(labels, separator=", "):
    """Join labels into a single string.

    Each label is stripped of surrounding whitespace. Labels that are empty
    after stripping are dropped. The remaining labels are joined with
    ``separator`` (default ``", "``), preserving original casing, order and
    duplicates.
    """
    stripped = (label.strip() for label in labels)
    return separator.join(label for label in stripped if label)
