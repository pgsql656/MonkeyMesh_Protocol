import json
import time
import random
from monkeymesh_agent import config

# --- MOCK EAR ---
class MockNostrChannel:
    """
    Simulates listening to a Nostr Relay by reading messages from a local JSON file.
    """
    def __init__(self, job_file_path=config.TEST_JOBS_FILE):
        self.job_file_path = job_file_path
        print(f"[Ear] Initialized Mock Ear. Listening for jobs from {self.job_file_path}...")

    def listen(self):
        """
        Yields job offers one by one with a slight delay to simulate real-time events.
        """
        try:
            with open(self.job_file_path, "r") as f:
                jobs = json.load(f)
            
            for index, job in enumerate(jobs):
                print(f"\n[Ear] Requesting relay for new events... Found event {index+1}/{len(jobs)}")
                time.sleep(1.5) # Simulate network latency
                yield job
        
        except FileNotFoundError:
            print(f"[Ear] Error: Test file not found at {self.job_file_path}")
            return []

# --- REAL EAR (Placeholder/Future Use) ---
class NostrChannel:
    """
    Real implementation using python-nostr or nostr-sdk.
    Connects to wss://relay.damus.io etc.
    """
    def __init__(self, relay_url="wss://relay.damus.io"):
        self.relay_url = relay_url
        # TODO: Implement real connection logic here
        pass

    def listen(self):
        # TODO: Implement real subscription logic here
        pass
