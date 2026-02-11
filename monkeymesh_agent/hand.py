from monkeymesh_agent import config

class Hand:
    """
    Interface for the Action Layer (Wallet).
    Can be configured to use a Mock Wallet or real Bananopie.
    """
    def __init__(self, seed=None):
        self.seed = seed
        # TODO: Initialize real bananopie wallet if seed provided
        
    def pay_handshake(self, recipient_address, amount=0.001):
        """
        Sends the handshake payment to indicate job acceptance.
        
        Args:
            recipient_address (str): The Banano address of the employer.
            amount (float): The amount to send (default 0.001 BAN).
        
        Returns:
            str: Transaction hash or mocking string.
        """
        print(f"[Hand] 🍌 Initiating Handshake Payment...")
        print(f"[Hand] ➡️ Sending {amount} BAN to {recipient_address}...")
        
        # Simulate network delay for transaction confirmation
        import time 
        time.sleep(1)
        
        print(f"[Hand] ✅ TRANSFERRED Successfully! (Mock TX ID: hash_12345)")
        print(f"[Hand] Job Locked. Wait for further instructions via encrypted DM.")
        return "hash_12345"
