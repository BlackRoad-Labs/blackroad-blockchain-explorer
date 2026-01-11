# BlackRoad Blockchain Explorer

Multi-chain blockchain explorer with real-time analytics. Self-hosted, sovereign, and privacy-preserving.

## Features

- **Multi-Chain** - Ethereum, Bitcoin, Solana, and more
- **Real-Time** - Live transaction streaming
- **Analytics** - Wallet tracking and flow analysis
- **Self-Hosted** - Run your own explorer
- **API Access** - Full REST and WebSocket APIs
- **Privacy** - No third-party tracking

## Supported Chains

- Ethereum (mainnet, testnets, L2s)
- Bitcoin (mainnet, testnet)
- Solana
- Polygon, Arbitrum, Optimism
- Custom EVM chains

## Quick Start

```bash
./blackroad-blockchain-explorer.sh init
./blackroad-blockchain-explorer.sh index --chain ethereum
./blackroad-blockchain-explorer.sh serve --port 3000
```

## API Examples

```bash
# Get transaction
curl localhost:3000/api/tx/0x123...

# Get wallet balance
curl localhost:3000/api/address/0xabc.../balance

# Stream new blocks
wscat -c ws://localhost:3000/ws/blocks
```

## License

Copyright (c) 2026 BlackRoad OS, Inc. All rights reserved.
Proprietary software. For licensing: blackroad.systems@gmail.com
