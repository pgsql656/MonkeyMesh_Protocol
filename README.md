# **MonkeyMesh: The Agent Internet Protocol**



## **1\. Abstract**

The current internet is broken. Users are farmed for data, algorithms dictate culture, and economic value is trapped in centralized silos. **MonkeyMesh** is a proposal for a new "Overlay Internet"—a decentralized, agent-first economy where users regain sovereignty. By combining local AI agents, a block-lattice ledger (Banano), and peer-to-peer transport (Nostr/IPFS), we create a "Jungle camp" where users are protected, services finds them, and content is owned, not rented.

## **2\. The Manifesto**

We believe in three core truths:

1. **Inversion of Control:** The user should not visit the web; the web should come to the user, filtered by their own AI.  
2. **Sovereign Identity:** Your reputation, work history, and social graph belong to you, not a corporation.  
3. **Frictionless Value:** Sending money should be as easy, free, and fast as sending a text message.

## **3\. The Architecture: "The Jungle Stack"**

MonkeyMesh is not a single website; it is a protocol stack that runs locally on user devices.

### **Layer 1: The Brain (Local Intelligence)**

* **Tech:** Ollama / Llama-3 (8B) / TinyLlama.  
* **Function:** Runs locally on the user's hardware. Filters incoming feeds, detects scams, and negotiates contracts. No data leaves the device without explicit permission.

### **Layer 2: The Transport (The Vines)**

* **Tech:** Nostr (Notes and Other Stuff Transmitted by Relays) \+ WebRTC.  
* **Function:** A censorship-resistant relay network. Agents broadcast "Signals" (encrypted JSON blobs) regarding job availability or content.

### **Layer 3: The Ledger (The Bananas)**

* **Tech:** Banano (Block Lattice) \+ Tezos (Smart Contracts).  
* **Function:**  
  * **Banano:** Used for micro-signals, spam prevention (PoW), and instant streaming payments.  
  * **Tezos:** Used for complex logic (Royalties, NFTs, DID Registries).

### **Layer 4: The Storage (The Trunk)**

* **Tech:** IPFS (InterPlanetary File System).  
* **Function:** Decentralized hosting for media (music, images) and social graphs.

## **4\. Core Modules**

### **A. Work: The Gig Hunter**

* **Problem:** Job hunting is manual, repetitive, and centralized (LinkedIn).  
* **Solution:** Users define a "Skill Profile." Their Agent passively scans the Mesh for matching "Job Signals."  
* **Mechanism:**  
  1. Company Agent broadcasts: `WANTED: CSS_WIZARD {Rate: 500 BAN}`.  
  2. User Agent analyzes match locally.  
  3. If match \> 90%, Agent auto-replies with verified credentials.  
  4. Gig is booked; payment is streamed per milestone.

### **B. Social: The Mirror & Bodyguard**

* **Problem:** Social media is curated by algorithms designed to maximize engagement (rage/addiction).  
* **Solution:** The "Social Mirror."  
* **Mechanism:**  
  1. **Ingest:** Agent clones user posts from Web2 (X/Instagram) to IPFS.  
  2. **Curate:** Agent downloads raw feeds from friends.  
  3. **Filter:** Local LLM scrubs ads, rage-bait, and scams based on user's "Taste Profile."  
  4. **Result:** A clean, sovereign feed.

### **C. Media: The SoundSystem**

* **Problem:** Artists earn fractions of pennies; platforms own the distribution.  
* **Solution:** Direct-to-Fan streaming.  
* **Mechanism:**  
  1. Artist Agent uploads track to IPFS.  
  2. Fan Agent streams file.  
  3. **Payment:** A Banano payment stream opens (e.g., 0.01 BAN/sec). Money flows directly to the Artist Agent wallet. No middleman.

## **5\. Implementation Strategy (The Roadmap)**

### **Phase 1: "The Sprout" (MVP)**

* **Goal:** Build the "Headhunter" module (Command Line Interface).  
* **Deliverable:** A Python script that connects two local agents via Nostr and exchanges a Banano transaction upon a keyword match.  
* **Target Audience:** Developers, Crypto-Natives.

### **Phase 2: "The Canopy" (GUI)**

* **Goal:** User-friendly Desktop App (Electron/Tauri).  
* **Deliverable:** The "MonkeyMesh" Dashboard. Visualizes the agent, manages keys, and provides the "Social Mirror" feed view.  
* **Target Audience:** Early Adopters, Tech Privacy enthusiasts.

### **Phase 3: "The Ecosystem" (Mobile)**

* **Goal:** Mobile App \+ Browser Extension.  
* **Deliverable:** An extension that scrapes Twitter/LinkedIn context for the Agent. A mobile app for managing the wallet.  
* **Target Audience:** General Public.

## **6\. Request for Comment (RFC)**

MonkeyMesh is an open protocol. We invite developers, cryptographers, and designers to join the mesh.

* **Code:** https://github.com/pgsql656/MonkeyMesh_v1
* **telegram:** t.me/monkeymesh

# **MonkeyMesh Prototype: Developer Guide (Nanobot Edition)**

**Phase 1: "The Sprout" (MVP)**

*Objective: Fork and extend HKUDS/Nanobot to create a CLI-based Autonomous Agent that finds work via Nostr and gets paid in Banano.*

## **1\. System Requirements**

The prototype runs locally (no cloud servers).

* **Hardware:** Mac M1/M2/M3 or PC with NVIDIA GPU (8GB+ VRAM recommended).  
* **OS:** Linux (Ubuntu 22.04) or macOS.  
* **Language:** Python 3.10+.  
* **Base Framework:** [HKUDS/Nanobot](https://github.com/HKUDS/nanobot) (Clone this repo).  
* **Local LLM:** [Ollama](https://ollama.com/) running llama3.  
* **Network:** Access to public Nostr relays and a Banano Node (e.g., Kalium API).

## **2\. Architecture Overview**

We utilize **Nanobot** as the agent kernel to handle memory, context windowing, and tool execution. We extend it with two custom modules:

1. **The Ear (Custom Channel):** A new nostr\_channel.py that listens to relays instead of Telegram/WhatsApp.  
2. **The Brain (Nanobot Kernel):** Configured to use local Ollama (http://localhost:11434) instead of OpenAI.  
3. **The Hand (Custom Skill):** A new wallet\_skill.py that wraps bananopie to sign transactions.

## **3\. The Protocol (Data Structures)**

Agents communicate via **Signed JSON objects** embedded in Nostr events.

### **A. The "Job Signal" (Broadcast by Company Agent)**

*Nostr Filter: \#mm\_job*

{  
  "type": "JOB\_OFFER",  
  "id": "uuid-v4",  
  "role": "Python Backend Dev",  
  "budget": "500 BAN",  
  "skills\_required": \["python", "nostr", "asyncio"\],  
  "description": "Need a script to listen to relay wss://relay.damus.io and filter for kind 1."  
}

## **4\. Implementation Steps**

### **Step 1: The Environment & Fork**

1. Clone the base repository:  
   git clone \[https://github.com/HKUDS/nanobot.git\](https://github.com/HKUDS/nanobot.git) monkeymesh\_agent  
   cd monkeymesh\_agent

2. Install MonkeyMesh specific dependencies:  
   pip install nostr-sdk bananopie

3. **Configure LLM:** Edit config.yaml (or equivalent env setup) to point the base\_url to http://localhost:11434/v1 and model to llama3.

### **Step 2: "The Hand" (Wallet Skill)**

Create a new file: src/nanobot/skills/monkey\_wallet.py.

**Logic:**

* Import bananopie.  
* Define a class BananoWallet decorated as a Tool.  
* Expose function pay\_address(address: str, amount: float) \-\> str.  
* *Security:* Load private seed from environment variable MONKEY\_SEED.

**System Prompt Injection:**

Add this to the agent's core instructions:

"You have access to a Banano Wallet. If you decide to accept a job, you MUST use the pay\_address tool to send 0.001 BAN to the employer as a handshake."

### **Step 3: "The Ear" (Nostr Channel)**

Create a new file: src/nanobot/channels/nostr.py.

**Logic:**

* Inherit from the base Channel class.  
* Implement start():  
  1. Initialize nostr\_sdk.Client.  
  2. Subscribe to filter {"\#t": \["mm\_job"\]}.  
* Implement on\_event():  
  1. Parse the JSON content.  
  2. **Crucial:** Wrap the event content in a prompt wrapper:"SYSTEM EVENT: Incoming Job Signal detected.  
     Payload: {event.content}  
     Task: Evaluate if this matches my skills. If yes, execute handshake."  
  3. Push this text into the Nanobot agent.handle\_message() queue.

### **Step 4: "The Worker Profile" (Configuration)**

Modify the system\_prompt in config.yaml to define the agent's persona.

system\_prompt: |  
  You are CodeMonkey\_v1.  
  Your Goal: Find high-paying Python jobs.  
  Your Skills: \[Python, Rust, Nostr\].  
  Min Rate: 400 BAN.  
  If a job matches your skills and rate, accept it immediately using the Wallet tool.  
  If it does not match, ignore it.

## **5\. Running the Prototype**

Instead of writing a custom loop, use the Nanobot CLI with our new channel.

\# Export keys  
export MONKEY\_SEED="your\_banano\_seed\_hex"  
export NOSTR\_KEY="your\_nostr\_private\_key"

\# Run the agent listening on Nostr  
python \-m nanobot run \--channel nostr

## **6\. Testing Strategy**

1. **Start the Agent:** Run the command above. It should log "Connected to Relays...".  
2. **Simulate a Job:** Use a separate script (or a web Nostr client like Coracle) to post a note with tag \#mm\_job containing the Job JSON.  
3. **Watch the Logs:**  
   * Nanobot should receive the message.  
   * Ollama (The Brain) should "think".  
   * It should output: "Calling tool: pay\_address...".  
4. **Verify Payment:** Check the target Banano address on a block explorer (YellowSpyglass) to see if the 0.001 BAN arrived.

## **7\. Security Notices for Nanobot Integration**

* **Tool Permission:** By default, ensure the Agent asks for confirmation before executing pay\_address during testing (Human-in-the-loop).  
* **Context Limit:** Nanobot manages history, but Nostr feeds are infinite. Ensure the nostr.py channel only pushes relevant events (filter aggressively) to avoid overflowing the context window.
