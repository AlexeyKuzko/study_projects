# Conversion factors in bytes
unit_factors = {
    "B": 1,
    "KB": 1024,
    "MB": 1024**2,
    "GB": 1024**3,
}


def convert_bytes(total_bytes):
    # Determine the largest unit possible (at least 1)
    if total_bytes >= unit_factors["GB"]:
        value = total_bytes / unit_factors["GB"]
        unit = "GB"
    elif total_bytes >= unit_factors["MB"]:
        value = total_bytes / unit_factors["MB"]
        unit = "MB"
    elif total_bytes >= unit_factors["KB"]:
        value = total_bytes / unit_factors["KB"]
        unit = "KB"
    else:
        return f"{total_bytes} B"
    # Round to nearest integer
    value = int(round(value))
    return f"{value} {unit}"


def main():
    groups = {}
    with open("files.txt", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 3:
                continue
            filename, size_str, unit = parts
            # Get the extension
            ext = filename.split(".")[-1]
            # Calculate bytes for current file
            size = int(size_str)
            bytes_count = size * unit_factors[unit]
            # Add file to its group
            if ext not in groups:
                groups[ext] = {"files": [], "total": 0}
            groups[ext]["files"].append(filename)
            groups[ext]["total"] += bytes_count

    # Process groups sorted by extension lexicographically
    first = True
    for ext in sorted(groups):
        if not first:
            print()
        first = False
        group = groups[ext]
        for filename in sorted(group["files"]):
            print(filename)
        print("----------")
        print("Summary: " + convert_bytes(group["total"]))


if __name__ == "__main__":
    main()
