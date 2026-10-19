<p align="center"><img src="https://vulpurr.com/logo.svg" width="96" alt="Vulpurr"></p>

<h1 align="center">Vulpurr (VUP)</h1>

<p align="center">A private, CPU-mineable cryptocurrency built on Monero.<br>
<a href="https://vulpurr.com">Website</a> · <a href="https://vulpurr.com/explorer/">Explorer</a> · <a href="https://vulpurr.com/pool/">Pool</a> · <a href="https://t.me/vulpurr">Telegram</a></p>

**English** · [Русский](#русский)

This repository is the Vulpurr node (`vulpurrd`), the command-line wallet and the wallet RPC. It is a fork of [Monero](https://github.com/monero-project/monero) v0.18.5.3; the upstream history is kept intact and all Vulpurr changes sit on top of it. The original Monero README is in [README.monero.md](README.monero.md).

> ⚠️ The network is in test mode. Before the official launch the chain will be restarted and all balances reset. The launch date will be announced in advance; there is no premine.

## What is different from Monero

| | |
|---|---|
| Ticker | VUP |
| Addresses | start with `Vu` (subaddresses with `Vs`) |
| Block time | 120 s |
| Difficulty | LWMA-1 (N = 72, per-block adjustment) with a 600 s future time limit |
| Reorg limit | the node rejects chain reorganizations deeper than 10 blocks |
| Checkpoints | signed checkpoints fetched over HTTPS every 5 minutes, replacing MoneroPulse DNS |
| Emission | ~18.1 M VUP over ~8 years, then a 0.6 VUP/block tail forever |
| Privacy | everything Monero has: ring signatures (ring size 16), stealth addresses, RingCT / Bulletproofs+ |
| Mining | RandomX on CPU |

## Network

| | |
|---|---|
| P2P | 27080 |
| RPC | 27081 (restricted public RPC: 27089) |
| ZMQ | RPC 27082, pub 27083 (`--zmq-pub`, used by P2Pool) |
| Public node | `node.vulpurr.com:27089` |
| Seed nodes | `seed.vulpurr.com:27080`, `seed2.vulpurr.com:27080` |

## Building

Same dependencies and steps as Monero, see [README.monero.md](README.monero.md#compiling-monero-from-source).

```bash
git clone --recursive https://github.com/vulpurr-network/vulpurr.git
cd vulpurr
make -j$(nproc) release
./build/Linux/master/release/bin/vulpurrd --detach
```

The daemon binary is called `vulpurrd`; the wallet tools keep their Monero names (`monero-wallet-cli`, `monero-wallet-rpc`).

## Related repositories

- [vulpurr-gui](https://github.com/vulpurr-network/vulpurr-gui) — desktop wallet with a built-in node, P2Pool mining and signed auto-updates
- [vulpurr-p2pool](https://github.com/vulpurr-network/vulpurr-p2pool) — decentralized pool, 0% fee
- [vulpurr-pool](https://github.com/vulpurr-network/vulpurr-pool) — the classic pool behind `pool.vulpurr.com`

## Credits and license

Vulpurr exists thanks to the Monero Project and everyone who has contributed to it. Licensed under the same BSD 3-Clause license as Monero, see [LICENSE](LICENSE); all original copyright notices are kept.

---

## Русский

Этот репозиторий — нода Vulpurr (`vulpurrd`), консольный кошелёк и wallet RPC. Это форк [Monero](https://github.com/monero-project/monero) v0.18.5.3: история Monero сохранена, все изменения Vulpurr лежат поверх неё. Оригинальный README Monero — в [README.monero.md](README.monero.md).

> ⚠️ Сеть работает в тестовом режиме. Перед официальным запуском цепочку перезапустят, и все балансы обнулятся. Дату объявим заранее, скрытого премайна нет.

**Чем отличается от Monero**

- Тикер VUP, адреса начинаются на `Vu` (подадреса на `Vs`), блок раз в 120 секунд.
- Сложность по LWMA-1 (N = 72, пересчёт каждый блок), блок не может быть «из будущего» больше чем на 600 секунд.
- Нода не принимает перестройку цепочки глубже 10 блоков: подтверждённый платёж не откатить даже большой мощностью.
- Подписанные контрольные точки скачиваются по HTTPS каждые 5 минут вместо DNS-чекпоинтов MoneroPulse.
- Эмиссия ~18,1 млн VUP примерно за 8 лет, дальше вечная награда 0,6 VUP за блок.
- Вся приватность Monero: кольцевые подписи (кольцо 16), скрытые адреса, RingCT / Bulletproofs+. Майнинг на процессоре (RandomX).

**Сеть:** P2P 27080, RPC 27081 (публичный ограниченный 27089), ZMQ RPC 27082, ZMQ pub 27083. Публичная нода `node.vulpurr.com:27089`, сид-ноды `seed.vulpurr.com:27080` и `seed2.vulpurr.com:27080`.

**Сборка** такая же, как у Monero (зависимости в [README.monero.md](README.monero.md#compiling-monero-from-source)):

```bash
git clone --recursive https://github.com/vulpurr-network/vulpurr.git
cd vulpurr && make -j$(nproc) release
```

Спасибо проекту Monero и всем, кто его делает. Лицензия та же, BSD 3-Clause ([LICENSE](LICENSE)), все оригинальные копирайты сохранены.
