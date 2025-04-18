from models import Device, DataEntry

def get_max_energy():
    # Query all voltages (joining Device if necessary)
    voltages = [entry.voltage for entry in DataEntry.select(DataEntry.voltage).join(Device)]

    total_entries = len(voltages)
    if total_entries < 6:
        return 0  # Not enough data to simulate 6 days

    # Divide into 6 roughly equal chunks
    chunk_size = total_entries // 6
    max_per_chunk = []

    for i in range(6):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < 5 else total_entries  # Last chunk takes the rest
        chunk = voltages[start:end]
        if chunk:
            max_per_chunk.append(max(chunk))

    # Now average the 6 max values
    avg_max_energy = sum(max_per_chunk) / 6
    result = avg_max_energy / 50000

    return result