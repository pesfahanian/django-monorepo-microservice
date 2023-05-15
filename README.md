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

## Usage

Make all the `.sh` files executable.

```sh
find . -type f -iname "*.sh" -exec chmod +x {} \;
```

Generate JWT RS256 key-pair:

```sh
./scripts/keygen.sh
```

Generate gRPC codes:

```sh
./scripts/codegen.sh
```

With a UUID Version 4 `User ID` value obtained from [uuidgenerator.net](https://www.uuidgenerator.net/version4) (or during the `seed` step of development), go to [jwt.io](https://jwt.io/), select the `RS256` algorithm, and use the public and private keys from the JWT RS256 key-pair generated earlier and the following payload to generate a new JWT token.

```json
{
    "user_id": "<User ID>",
    "type": "access"
}
```

---

## Development

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

> To install the requirements of only one service, run `./scripts/install.sh <SERVICE NAME>`.

Run migrations for all services:

```sh
./scripts/manage.sh --all migrate
```

> This will perform migrations for the `wallet` and `ledger` services.

Seed the starter data:

```sh
./scripts/manage.sh --all seed
```

> This will create a sample `Wallet` record in the `wallet` service database. A prompt will appear requeuing conformation and displaying the `User ID`.



drop database "dmm-wallet";
drop database "dmm-ledger";
