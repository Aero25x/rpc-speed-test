[![Join our Telegram RU](https://img.shields.io/badge/Telegram-RU-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aero25x)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aero25x)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@flaming_chameleon)
[![Reddit](https://img.shields.io/badge/Reddit-FF3A00?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/HiddenCode/)
[![Join our Telegram ENG](https://img.shields.io/badge/Telegram-EN-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding_en)


<img width="994" height="831" alt="image" src="https://github.com/user-attachments/assets/34fe29c1-e94e-4d90-b3af-71b6c4be5329" />




# 🚀 Ethereum RPC's Speed Test

Measure and compare the performance of different Ethereum WebSocket (WS) RPC providers by monitoring how quickly they broadcast new block events.

Developed by **[Aero25x](https://t.me/hidden_coding)**.

---

## 📌 Features

* Connects to multiple Ethereum RPC WebSocket endpoints
* Subscribes to new block headers (`eth_subscribe`)
* Logs the time each provider receives a new block
* Ranks providers based on first notification time
* Provides block count statistics over a customizable duration
* CLI interface for test duration

---

## 🛠️ Installation

### Requirements

* Python 3.7+
* Dependencies:

  ```bash
  pip install websockets
  ```

> Optional: Use a virtual environment for isolation:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

## ⚙️ Configuration

Open the script and edit the `RPC_PROVIDERS` list. Replace `<API_KEY>` placeholders with your actual keys:

```python
RPC_PROVIDERS = [
    RPCProvider(
        name="Alchemy",
        ws_url="wss://eth-mainnet.g.alchemy.com/v2/<API_KEY>"
    ),
    ...
]
```

> ❗ Some providers require an API key or project ID. Make sure it's active and has WS access.

---

## ▶️ Usage

Run the script:

```bash
python rpc_speed_test.py
```

You’ll be prompted to enter a test duration in minutes (default is 5). The script will then connect to each provider, listen for new blocks, and display the results.

---

## 🧪 Sample Output

```
🏆 RANKING BY FIRST BLOCK NOTIFICATION:
1. Alchemy
   First block: #17945231
   Total blocks received: 23
   Delay from fastest: 0.000s

2. QuickNode
   First block: #17945231
   Total blocks received: 22
   Delay from fastest: 0.224s

...

📊 SUMMARY:
Fastest provider: Alchemy
Total providers tested: 4
Average blocks received: 21.5
```

---

## 🧠 How It Works

* Uses WebSocket connections to subscribe to `newHeads`
* Measures time of first block notification per provider
* Accumulates total block notifications over the duration
* Ranks and compares performance

---

## 📎 Notes

* This tool is designed for educational and diagnostic purposes.
* Provider speeds may vary due to region, load, and network latency.
* Add or remove providers by modifying the `RPC_PROVIDERS` list.

---

## 🙋‍♂️ Author

**Aero25x**

📬 Telegram: [@hidden\_coding](https://t.me/hidden_coding)

---

## 📄 License

This project is released under the [MIT License](LICENSE). Feel free to use and modify it for your own benchmarking needs.







```
🏆 RANKING BY FIRST BLOCK NOTIFICATION:
----------------------------------------


      _    _ _     _     _             _____          _
     | |  | (_)   | |   | |           / ____|        | |
     | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___
     |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \
     | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
     |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|

                 SpeedTest by Aero25x

               Join us to get more scripts
               https://t.me/hidden_coding


1. QuickNode
   First block: #23195245
   Total blocks received: 5
   Delay from fastest: 0.000s

2. Alchemy
   First block: #23195245
   Total blocks received: 5
   Delay from fastest: 0.089s

📊 SUMMARY:
Fastest provider: QuickNode
Total providers tested: 2
Average blocks received: 5.0
```






[![Join our Telegram RU](https://img.shields.io/badge/Telegram-RU-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aero25x)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aero25x)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@flaming_chameleon)
[![Reddit](https://img.shields.io/badge/Reddit-FF3A00?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/HiddenCode/)
[![Join our Telegram ENG](https://img.shields.io/badge/Telegram-EN-03A500?style=for-the-badge&logo=telegram&logoColor=white&labelColor=blue&color=red)](https://t.me/hidden_coding_en)
