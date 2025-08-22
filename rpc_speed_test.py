import asyncio
import websockets
import json
import time
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RPCProvider:
    def __init__(self, name: str, ws_url: str, subscription_method: str = "eth_subscribe"):
        self.name = name
        self.ws_url = ws_url
        self.subscription_method = subscription_method
        self.websocket = None
        self.first_block_time = None
        self.block_times = []
        self.is_connected = False

    async def connect_and_subscribe(self):
        """Connect to WebSocket and subscribe to new blocks"""
        try:
            self.websocket = await websockets.connect(self.ws_url)
            self.is_connected = True
            logger.info(f"Connected to {self.name}")

            # Subscribe to new block headers
            subscription_request = {
                "id": 1,
                "method": self.subscription_method,
                "params": ["newHeads"]
            }

            await self.websocket.send(json.dumps(subscription_request))
            logger.info(f"Subscribed to new blocks on {self.name}")

        except Exception as e:
            logger.error(f"Failed to connect to {self.name}: {e}")
            self.is_connected = False

    async def listen_for_blocks(self, results: Dict):
        """Listen for new block notifications and record timing"""
        if not self.is_connected:
            return

        try:
            async for message in self.websocket:
                current_time = time.time()
                data = json.loads(message)

                # Check if this is a new block notification
                if "params" in data and "subscription" in data["params"]:
                    block_data = data["params"]["result"]
                    block_number = int(block_data.get("number", "0x0"), 16)

                    if self.first_block_time is None:
                        self.first_block_time = current_time
                        results[self.name] = {
                            "first_block_time": current_time,
                            "first_block_number": block_number,
                            "total_blocks": 0
                        }

                    self.block_times.append(current_time)
                    results[self.name]["total_blocks"] += 1

                    logger.info(f"{self.name}: Block #{block_number} received at {current_time}")

        except websockets.exceptions.ConnectionClosed:
            logger.warning(f"Connection to {self.name} closed")
        except Exception as e:
            logger.error(f"Error listening to {self.name}: {e}")

    async def close(self):
        """Close WebSocket connection"""
        if self.websocket:
            await self.websocket.close()

# RPC Provider configurations
# Note: You'll need to add your API keys for providers that require them
RPC_PROVIDERS = [
    RPCProvider(
        name="Alchemy",
        ws_url="wss://eth-mainnet.g.alchemy.com/v2/<API_KEY>"  # Replace with your API key
    ),
    RPCProvider(
        name="QuickNode",
        ws_url="wss://lingering-floral-dream.quiknode.pro/<API_KEY>/"  # Replace with your endpoint
    ),
    RPCProvider(
        name="Ankr",
        ws_url="wss://rpc.ankr.com/eth/ws/<API_KEY>"  # Replace with your API key
    ),
    RPCProvider(
        name="Moralis",
        ws_url="wss://speedy-nodes-nyc.moralis.io/<API_KEY>/eth/mainnet/ws"  # Replace with your API key
    ),
]

async def test_rpc_speed(duration_minutes: int = 5):
    """Test multiple RPC providers and compare their block notification speed"""
    results = {}
    tasks = []

    logger.info(f"Starting RPC speed test for {duration_minutes} minutes...")

    # Connect to all providers
    for provider in RPC_PROVIDERS:
        await provider.connect_and_subscribe()
        if provider.is_connected:
            # Start listening task
            task = asyncio.create_task(provider.listen_for_blocks(results))
            tasks.append(task)

    # Run for specified duration
    await asyncio.sleep(duration_minutes * 60)

    # Cancel all tasks and close connections
    for task in tasks:
        task.cancel()

    for provider in RPC_PROVIDERS:
        await provider.close()

    return results

def analyze_results(results: Dict):
    """Analyze and display the results"""
    print("\n" + "="*50)
    print("RPC PROVIDER SPEED TEST RESULTS")
    print("="*50)

    if not results:
        print("No results collected. Check your API keys and connections.")
        return

    # Sort by first block time (fastest first)
    sorted_results = sorted(
        results.items(),
        key=lambda x: x[1]["first_block_time"]
    )

    print(f"\n🏆 RANKING BY FIRST BLOCK NOTIFICATION:")
    print("-" * 40)

    fastest_time = sorted_results[0][1]["first_block_time"] if sorted_results else 0


    print("""

      _    _ _     _     _             _____          _
     | |  | (_)   | |   | |           / ____|        | |
     | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___
     |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \\
     | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
     |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|

                 SpeedTest by Aero25x

               Join us to get more scripts
               https://t.me/hidden_coding

    """)

    for rank, (provider, data) in enumerate(sorted_results, 1):
        delay = data["first_block_time"] - fastest_time
        print(f"{rank}. {provider}")
        print(f"   First block: #{data['first_block_number']}")
        print(f"   Total blocks received: {data['total_blocks']}")
        print(f"   Delay from fastest: {delay:.3f}s")
        print()

    print(f"📊 SUMMARY:")
    print(f"Fastest provider: {sorted_results[0][0]}")
    print(f"Total providers tested: {len(results)}")

    # Calculate average blocks per provider
    avg_blocks = sum(data["total_blocks"] for data in results.values()) / len(results)
    print(f"Average blocks received: {avg_blocks:.1f}")

async def main():
    """Main function to run the RPC speed test"""
    print("🚀 Ethereum RPC Provider Speed Test")
    print("This will test multiple RPC providers to see which sends new block notifications fastest.")
    print("\n⚠️  Important: Make sure to replace API keys in the RPC_PROVIDERS list!")
    print("Some providers require authentication and won't work without valid API keys.\n")

    # Ask user for test duration
    try:
        duration = int(input("Enter test duration in minutes (default 5): ") or "5")
    except ValueError:
        duration = 5

    print(f"\n🔄 Starting {duration}-minute speed test...")

    try:
        results = await test_rpc_speed(duration)
        analyze_results(results)
    except KeyboardInterrupt:
        print("\n⏹️  Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during test: {e}")


print("""



  _    _ _     _     _             _____          _
 | |  | (_)   | |   | |           / ____|        | |
 | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___
 |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \\
 | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
 |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|

              SpeedTest by Aero25x

            Join us to get more scripts
            https://t.me/hidden_coding


    """)

if __name__ == "__main__":
    asyncio.run(main())
