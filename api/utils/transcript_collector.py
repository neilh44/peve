class TranscriptCollector:
    def __init__(self):
        self.transcript_parts = []

    def add_part(self, part):
        self.transcript_parts.append(part)

    def get_full_transcript(self):
        return " ".join(self.transcript_parts)

    def reset(self):
        self.transcript_parts = []