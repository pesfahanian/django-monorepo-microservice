# Django Monorepo Microservice

Simple payment application utilizing [Monorepo](https://monorepo.tools/) codebase architecture and [Microservice](https://microservices.io/) deployment architecture.

---

## Services

### Wallet:

-   Simple CRUD operations
-   Deposit and withdraw features
-   Functionalities:
    -   Database
    -   REST API
    -   Admin panel
    -   Async events
    -   gRPC communication

### Ledger:

-   Double-entry ledger
-   Simple transaction journal
-   Functionalities:
    -   Database
    -   Admin panel
    -   Async events

### PG:

-   Bank API proxy middleman.
-   Functionalities:
    -   Ephemeral
    -   gRPC communication

---

## Usage

Make all the `.sh` files executable.

```sh
find . -type f -iname "*.sh" -exec chmod +x {} \;
```

Create and activate a virtual environment:

```sh
python -m venv .venv
source .venv/bin/activate
```

Install all the requirements:

```sh
./scripts/install.sh --all
```

> To install the development requirements, use the `--develop` or `-D` flag.

> To install the requirements of only one service, run `./scripts/install.sh <SERVICE NAME>`.

Generate JWT RS256 key-pair:

```sh
./scripts/keygen.sh
```

Generate gRPC codes:

```sh
./scripts/codegen.sh
```

create database "dmm-wallet";
grant all privileges on database "dmm-wallet" to postgres;

create database "dmm-ledger";
grant all privileges on database "dmm-ledger" to postgres;
