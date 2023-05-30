# Django Monorepo Microservice

Simple payment application utilizing [Monorepo](https://monorepo.tools/) codebase architecture and [Microservice](https://microservices.io/) deployment architecture.

The Monorepo codebase architecture was achieved **without** using any of the traditional build tools (_e.g._ [Bazel](https://bazel.build/), [Pants](https://www.pantsbuild.org/)).

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

## Glossary

| Service    | Admin                                             | Swagger                                               |
| ---------- | ------------------------------------------------- | ----------------------------------------------------- |
| `rabbitmq` | [0.0.0.0:15672](http://0.0.0.0:15672/)            | -                                                     |
| `ledger`   | [0.0.0.0:8201/admin/](http://0.0.0.0:8201/admin/) | -                                                     |
| `wallet`   | [0.0.0.0:8200/admin/](http://0.0.0.0:8200/admin/) | [0.0.0.0:8200/swagger/](http://0.0.0.0:8200/swagger/) |

---

## Usage

Before anything, generate a JWT `RS256` key-pair:

```sh
./scripts/keygen.sh
```

---

## Deployment

> Make sure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed.

Build and start the services with:

```sh
docker compose up
```

---

## Development

> Make sure you have [Python 3.11.2](https://www.python.org/downloads/release/python-3112/) installed.

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

> To also additionally install the development requirements, use the `--develop` or `-D` flag.

> To install the requirements of only one service, run `./scripts/install.sh <SERVICE NAME>`

Generate gRPC codes:

```sh
./scripts/codegen.sh
```

Run migrations for all services:

```sh
./scripts/manage.sh --all migrate
```

> This will perform migrations for the `wallet` and `ledger` services.

> To run migrations for only one service, run `./scripts/manage.sh <SERVICE NAME> migrate`

---

## Testing

### - Wallet Creation

Get a valid UUID  for `userID` from [uuidgenerator.net](https://www.uuidgenerator.net/version4).

Either run the following command:

```sh
./scripts/manage.sh wallet createwallet <userID>
```

or go to [0.0.0.0:8200/admin/wallet/wallet/add/](http://0.0.0.0:8200/admin/wallet/wallet/add/) and manually create a `wallet` record.

> In deployment, you need to inspect into the `dmm-wallet` container for running the command.

### - Token Generation

With the `userID` of an existing `Wallet`, run the following command:

```sh
./scripts/manage.sh wallet generatetoken <userID>
```

> You also need to inspect into the `dmm-wallet` container for running this command in deployment.

### API

Import the collection at `docs/dmm.postman_collection.json` into [Postman](https://www.postman.com/).

Providing the success of [Wallet Creation](#wallet-creation) and using the token obtained from [Token Generation](#token-generation), test the APIs.
